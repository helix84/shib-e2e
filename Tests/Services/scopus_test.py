import pytest
from Pages.LoginUtbPage import LoginPage
from playwright.sync_api import Page
from Tests.test_base import TestBase


# source_id = "UTB00011"
class Scopus(TestBase):

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(Scopus, self).setup(page, "UTB00011")

    def test_wayfless(self):
        super(Scopus, self).wayfless()
        with self.page.expect_navigation():
            self.page.click("text=Continue anonymously")
        self.assert_access()

    def test_proxy_shibboleth(self):
        super(Scopus, self).proxy_shibboleth()
        self.assert_access()

    def test_proxy_ldap(self):
        super(Scopus, self).proxy_ldap()
        self.assert_access()

    def test_wayf(self):
        super(Scopus, self).wayf()
        self.page.goto(self.e_source.link_native_home)
        self.page.click("#signin_link_move >> text=Sign in")
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
        super(Scopus, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        self.asserts.is_exists("//*[@id=\"aa-globalheader-Institutions\"]", "Logon is not visible - Not log in!")
