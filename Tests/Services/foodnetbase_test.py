import pytest
from Pages.LoginUtbPage import LoginPage
from playwright.sync_api import Page
from Tests.test_base import TestBase


# source_id = "UTB00175"
class FoodNetBase(TestBase):

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(FoodNetBase, self).setup(page, "UTB00175")

    def test_wayfless(self):
        super(FoodNetBase, self).wayfless()
        self.assert_access()

    def test_proxy_shibboleth(self):
        super(FoodNetBase, self).proxy_shibboleth()
        self.assert_access() #nefunguje proxy prihlaseni vubec

    def test_proxy_ldap(self):
        super(FoodNetBase, self).proxy_ldap()
        self.assert_access() #nefunguje proxy prihlaseni vubec

    def test_wayf(self):
        super(FoodNetBase, self).wayf()
        self.page.goto(self.e_source.link_native_home)
        with self.page.expect_navigation():
            self.page.click("text=Login")
        self.page.click("text=With Shibboleth or OpenAthens")
        self.page.fill("[placeholder=\"Search for your institution\"]", "zlin")
        self.page.click("text=Tomas Bata University in Zlin")
        with self.page.expect_navigation():
            self.page.click("text=continue")
        login_page = LoginPage(self.page, self.data)
        login_page.login_and_accept_gdpr()
        self.assert_access()

    @pytest.mark.vpn
    def test_vpn(self):
        super(FoodNetBase, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        self.asserts.check_inner_text("//*[@id=\"menubutton1\"]", "Hi, User")
