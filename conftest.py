import os
import pytest
from configparser import ConfigParser
from Helpers.Data import configPath
from slugify import slugify
from pathlib import Path
import yagmail
from zipfile import ZipFile
from os.path import basename
from pytest_html import plugin as html_plugin

rootDir = os.path.dirname(__file__)
screenshotDir = 'screenshots'
htmlReportsPath = os.path.join(rootDir, 'htmlReports')
screenshotsWithReportsPath = os.path.join(htmlReportsPath, screenshotDir)

htmlReportPath = os.path.join(htmlReportsPath, "results.html")
stylePath = os.path.join("assets", "style.css")
htmlReportStylePath = os.path.join(htmlReportsPath, stylePath)
outputZipReport = os.path.join(rootDir, "output_report.zip")
nameOfReportSentFile = 'report_sent.txt'
pathToReportSentFile = os.path.join(rootDir, nameOfReportSentFile)

loaded_failed_test = set()
dict_of_actual_failed_test = set()
html_report_is_done = False


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "locale": "cs"
    }


def create_zip_file_with_report(screenshots_path, output_file_name):
    with ZipFile(output_file_name, 'w') as zip_obj:
        for folderName, subfolders, filenames in os.walk(screenshots_path):
            for filename in filenames:
                file_path = os.path.join(folderName, filename)
                zip_obj.write(file_path, os.path.join(screenshots_path, basename(file_path)))
        zip_obj.write(htmlReportPath, basename(htmlReportPath))
        zip_obj.write(htmlReportStylePath, stylePath)


def send_mail(receiver, failed_tests):
    create_zip_file_with_report(screenshotDir, outputZipReport)
    yagmail.register('testreportutb@gmail.com', 'testreport123456')
    yag = yagmail.SMTP('testreportutb@gmail.com')
    yag.send(to=receiver,
             subject="Automatic Test Result Report",
             contents="Hello, this is a automatic report from E2E testing of your ezdroje services." + failed_tests,
             attachments=[outputZipReport])


def parse_notification_from_config():
    config_object = ConfigParser()
    config_object.read(configPath)
    userinfo = config_object["NOTIFICATION"]
    return userinfo["isEnabled"], userinfo["email"]


def pytest_sessionfinish():
    write_failed_test_to_report_file(sorted(dict_of_actual_failed_test.union(loaded_failed_test)))
    diff = dict_of_actual_failed_test.difference(loaded_failed_test)
    notification_data = parse_notification_from_config()
    if notification_data[0] == "True" and len(diff) > 0:
        failed_tests = "\n"
        for failed_test in diff:
            failed_tests += failed_test + "\n"
        send_mail(notification_data[1], failed_tests)


def pytest_configure(config):
    read_report_file()
    if not os.path.exists(htmlReportsPath):
        os.makedirs(htmlReportsPath)
    config.option.htmlpath = htmlReportPath


def read_report_file():
    with open(pathToReportSentFile) as f:
        for line in f:
            loaded_failed_test.add(line.rstrip())


def write_failed_test_to_report_file(set_failed_tests):
    with open(pathToReportSentFile, 'w') as file:
        for failed_test in set_failed_tests:
            file.write(failed_test + "\n")


def pytest_runtest_logreport(report):
    pytest_html = html_plugin
    extra = getattr(report, "extra", [])
    if report.when == "call" and html_report_is_done is False:
        if report.failed:
            dict_of_actual_failed_test.update([report.location[2]])
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # add the screenshots to the html report
            extra.append(pytest_html.extras.png(os.path.join(screenshotDir, f"{slugify(report.location[2])}.png")))
        report.extra = extra


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    screen_file = ''
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        if report.failed and "page" in item.funcargs:
            global html_report_is_done
            html_report_is_done = True
            dict_of_actual_failed_test.update([item.location[2]])
            page = item.funcargs["page"]
            screenshot_dir = Path(screenshotDir)
            screenshot_dir.mkdir(exist_ok=True)
            screen_file = os.path.join(screenshot_dir, f"{slugify(item.location[2])}.png")
            page.screenshot(path=screen_file)
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # add the screenshots to the html report
            extra.append(pytest_html.extras.png(screen_file))
        report.extra = extra
