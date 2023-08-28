import pytest
from Pages.LoginUtbPage import LoginPage
from Tests.test_base import TestBase
from playwright.sync_api import Page


# source_id = "UTB00223"
class DeGruyterEBooksAndEJournals(TestBase):
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(DeGruyterEBooksAndEJournals, self).setup(page, "UTB00223")

    def test_wayf(self):
        super(DeGruyterEBooksAndEJournals, self).wayf()
        self.page.goto(self.e_source.link_native_home)
        self.page.click("text=Log in")
        self.page.click("#loginButton")
        self.page.fill("[aria-label=\"Search for your institution here\"]", "bata")
        self.page.click("input:has-text(\"Find\")")
        self.page.click("text=Univerzita Tomase Bati ve Zline - Tomas Bata University in Zlin")
        with self.page.expect_navigation():
            self.page.click("a:has-text(\"Login\")")
        login_page = LoginPage(self.page, self.data)
        login_page.login_and_accept_gdpr()
        self.assert_access()

    def test_wayfless(self):
        super(DeGruyterEBooksAndEJournals, self).wayfless()
        self.assert_access()

    def test_proxy_shibboleth(self):
        super(DeGruyterEBooksAndEJournals, self).proxy_shibboleth()
        self.assert_access()

    def test_proxy_ldap(self):
        super(DeGruyterEBooksAndEJournals, self).proxy_ldap()
        self.assert_access()

    @pytest.mark.vpn
    def test_vpn(self):
        super(DeGruyterEBooksAndEJournals, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        self.asserts.is_exists("//*[@id=\"authenticatedUserDiv\"]", "Not log in!")
