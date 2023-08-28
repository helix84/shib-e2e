import pytest
from Pages.LoginUtbPage import LoginPage
from playwright.sync_api import Page
from Tests.test_base import TestBase


# source_id = "UTB00130"
class EmeraldJournalsAndBooks(TestBase):

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(EmeraldJournalsAndBooks, self).setup(page, "UTB00130")

    def test_wayfless(self):
        super(EmeraldJournalsAndBooks, self).wayfless()
        self.assert_access()

    def test_proxy_shibboleth(self):
        super(EmeraldJournalsAndBooks, self).proxy_shibboleth()
        self.assert_access()

    def test_proxy_ldap(self):
        super(EmeraldJournalsAndBooks, self).proxy_ldap()
        self.assert_access()

    def test_wayf(self):
        super(EmeraldJournalsAndBooks, self).wayf()
        self.page.goto(self.e_source.link_native_home)
        self.page.click("text=Login")
        self.page.click("#idpbutton div div:has-text(\"Access through your institution\")")
        self.page.fill("[aria-label=\"Search institutions\"]", "zlin")
        self.page.press("[aria-label=\"Search institutions\"]", "Enter")
        with self.page.expect_navigation():
            self.page.click("text=UNIVERZITA TOMASE BATI VE ZLINE")
        login_page = LoginPage(self.page, self.data)
        login_page.login_and_accept_gdpr()
        self.assert_access()

    @pytest.mark.vpn
    def test_vpn(self):
        super(EmeraldJournalsAndBooks, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        self.asserts.check_inner_text("//*[@id=\"login-header\"]", "Welcome UNIVERZITA TOMASE BATI VE ZLINE")
