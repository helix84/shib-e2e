import pytest

from Helpers.Utils import Utils
from Pages.LoginUtbPage import LoginPage
from playwright.sync_api import Page
from Tests.test_base import TestBase


# source_id = "UTB00136"
class Ebsco(TestBase):

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(Ebsco, self).setup(page, "UTB00136")

    def test_wayfless(self):
        super(Ebsco, self).wayfless()
        self.assert_access()

    def test_proxy_shibboleth(self):
        super(Ebsco, self).proxy_shibboleth()
        with self.page.expect_navigation():
            self.page.click("text=EBSCOhost - databáze EBSCO na UTB")
        self.assert_access()

    def test_proxy_ldap(self):
        super(Ebsco, self).proxy_ldap()
        with self.page.expect_navigation():
            self.page.click("text=EBSCOhost - databáze EBSCO na UTB")
        self.assert_access()

    def test_wayf(self):
        super(Ebsco, self).wayf()
        self.page.goto(self.e_source.link_native_home)
        self.page.click("text=Institutional Login")
        self.page.fill("[placeholder=\"Search by name, postal code, or city.\"]", "zlin")
        self.page.click("button:has-text(\"Submit\")")
        with self.page.expect_popup() as popup_info:
            self.page.click(
                    "text=UNIVERZITA TOMASE BATI VE ZLINELVTNAMESTI T.G. MASARYKA 5555ZLIN, 760 01CZECH RE >> span")
        page2 = popup_info.value
        login_page = LoginPage(page2, self.data)
        login_page.login_and_accept_gdpr()
        self.assert_access_on_another_tab(page2)


    @pytest.mark.vpn
    def test_vpn(self):
        super(Ebsco, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access_on_another_tab(self, page):
        utils = Utils(page)
        self.assertTrue(utils.is_exist("//*[@id=\"SearchButton\"]"), "Couldn't reach ebsco site.")

    def assert_access(self):
        self.page.click("input:has-text(\"Pokračovat\")")
        self.asserts.is_exists("//*[@id=\"SearchButton\"]", "Couldn't reach ebsco site.")
