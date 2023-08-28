import pytest
from Pages.LoginUtbPage import LoginPage
from playwright.sync_api import Page
from Tests.test_base import TestBase


# source_id = "UTB00097"
class WileyOnlineLibrary(TestBase):

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(WileyOnlineLibrary, self).setup(page, "UTB00097")

    def test_wayfless(self):
        super(WileyOnlineLibrary, self).wayfless()
        self.assert_access()

    def test_proxy_shibboleth(self):
        super(WileyOnlineLibrary, self).proxy_shibboleth()
        self.assert_access()

    def test_proxy_ldap(self):
        super(WileyOnlineLibrary, self).proxy_ldap()
        self.assert_access()

    def test_wayf(self):
        super(WileyOnlineLibrary, self).wayf()
        self.page.goto(self.e_source.link_native_home)
        self.page.click("[aria-label=\"Log in or Register\"]")
        self.page.click("text=INSTITUTIONAL LOGIN >")
        self.page.select_option("select", "Czech academic identity federation eduID.cz")
        with self.page.expect_navigation():
            self.page.click("text=Tomas Bata University in Zlín")
        login_page = LoginPage(self.page, self.data)
        login_page.login_and_accept_gdpr()
        self.assert_access()

    @pytest.mark.vpn
    def test_vpn(self):
        super(WileyOnlineLibrary, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        self.asserts.check_inner_text("html", "Tomas Bata University in Zlin")
