import pytest
from Pages.LoginUtbPage import LoginPage
from playwright.sync_api import Page
from Tests.test_base import TestBase


# source_id = "UTB00137"
class Reaxys(TestBase):

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(Reaxys, self).setup(page, "UTB00137")

    def test_wayfless(self):
        super(Reaxys, self).wayfless()
        self.assert_access()

    def test_proxy_shibboleth(self):
        super(Reaxys, self).proxy_shibboleth()
        self.assert_access()

    def test_proxy_ldap(self):
        super(Reaxys, self).proxy_ldap()
        self.assert_access()

    def test_wayf(self):
        super(Reaxys, self).wayf()
        self.page.goto(self.e_source.link_native_home)
        self.page.click("text=Sign in via your institution")
        self.page.wait_for_timeout(5000)
        self.page.fill("input", "bata")
        with self.page.expect_navigation():
            self.page.click("text=Tomas Bata University in Zlín")
        login_page = LoginPage(self.page, self.data)
        login_page.login_and_accept_gdpr()
        self.assert_access()

    @pytest.mark.vpn
    def test_vpn(self):
        super(Reaxys, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        self.asserts.is_exists("//*[@id=\"personalization-user-dropdown\"]", "Logon is not visible - Not log in!")
