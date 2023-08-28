import pytest
from Pages.LoginUtbPage import LoginPage
from playwright.sync_api import Page

from Pages.WebOfSciencePage import WebOfSciencePage
from Tests.test_base import TestBase


# source_id = "UTB00121"
class JournalCitationReports(TestBase):

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(JournalCitationReports, self).setup(page, "UTB00121")

    def test_wayfless(self):
        super(JournalCitationReports, self).wayfless()
        self.assert_access()

    def test_proxy_shibboleth(self):
        super(JournalCitationReports, self).proxy_shibboleth()
        self.assert_access()

    def test_proxy_ldap(self):
        super(JournalCitationReports, self).proxy_ldap()
        self.assert_access()

    def test_wayf(self):
        super(JournalCitationReports, self).wayf()
        self.page.goto(self.e_source.link_native_home)
        web_of_science = WebOfSciencePage(self.page, self)
        web_of_science.login_via_web_of_science()
        login_page = LoginPage(self.page, self.data)
        login_page.login_and_accept_gdpr()

    @pytest.mark.vpn
    def test_vpn(self):
        super(JournalCitationReports, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        web_of_science = WebOfSciencePage(self.page, self)
        web_of_science.assert_login()
