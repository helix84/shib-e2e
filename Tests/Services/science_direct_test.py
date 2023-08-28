import pytest
from Pages.LoginUtbPage import LoginPage
from playwright.sync_api import Page
from Tests.test_base import TestBase


# source_id = "UTB00003"
class ScienceDirect(TestBase):

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(ScienceDirect, self).setup(page, "UTB00003")

    def test_wayfless(self):
        super(ScienceDirect, self).wayfless()
        self.assert_access()

    def test_proxy_shibboleth(self):
        super(ScienceDirect, self).proxy_shibboleth()
        self.assert_access()

    def test_proxy_ldap(self):
        super(ScienceDirect, self).proxy_ldap()
        self.assert_access()

    def test_wayf(self):
        super(ScienceDirect, self).wayf()
        self.page.goto(self.e_source.link_native_home)
        self.page.click("a[role=\"button\"]:has-text(\"Sign in\")")
        with self.page.expect_navigation():
            self.page.click("text=Sign in via your institution")
        self.page.fill("input[role=\"combobox\"]", "bata")
        self.page.click("text=Tomas Bata University in Zlín (Tomas Bata University in Zlin)")
        with self.page.expect_navigation():
            self.page.click(
                "button:has-text(\"Access through Tomas Bata University in Zlín (Tomas Bata University in Zlin)\")")
        login_page = LoginPage(self.page, self.data)
        login_page.login_and_accept_gdpr()
        with self.page.expect_navigation():
            self.page.click("text=Continue anonymously")
        self.assert_access()

    @pytest.mark.vpn
    def test_vpn(self):
        super(ScienceDirect, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        self.asserts.is_exists("//*[@id=\"institution-popover\"]", "Logon is not visible - Not log in!")
