import pytest
from playwright.sync_api import Page

from Pages.LoginUtbPage import LoginPage
from Tests.test_base import TestBase


# source_id = "UTB00123"
@pytest.mark.skip(reason="not working at all")
class LectureNotesInMathematics(TestBase):

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(LectureNotesInMathematics, self).setup(page, "UTB00123")

    def test_wayfless(self):
        super(LectureNotesInMathematics, self).wayfless()
        self.assert_access()

    def test_proxy_shibboleth(self):
        super(LectureNotesInMathematics, self).proxy_shibboleth()
        self.assert_access()

    def test_proxy_ldap(self):
        super(LectureNotesInMathematics, self).proxy_ldap()
        self.assert_access()

    def test_wayf(self):
        super(LectureNotesInMathematics, self).wayf()
        self.page.goto(self.e_source.link_native_home)
        self.page.click("[data-test=\"login-link\"]")
        self.page.click("text=Access via your institution")
        self.page.fill("input[name=\"search\"]", "zlin")
        self.page.press("input[name=\"search\"]", "Enter")
        with self.page.expect_navigation():
            self.page.click("text=Tomas Bata University in Zlín")
        login_page = LoginPage(self.page, self.data)
        login_page.login_and_accept_gdpr()
        self.assert_access()

    @pytest.mark.vpn
    def test_vpn(self):
        super(LectureNotesInMathematics, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        self.asserts.check_inner_text("//*[@id=\"header-menu_dropdown_menu_label\"]", "Welcome Tomas Bata Uni...")
