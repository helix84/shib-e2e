import pytest
from Pages.LoginUtbPage import LoginPage
from playwright.sync_api import Page
from Tests.test_base import TestBase


# source_id = "UTB00191"
class TaylorAndFrancisEBooks(TestBase):

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(TaylorAndFrancisEBooks, self).setup(page, "UTB00191")

    def test_wayfless(self):
        super(TaylorAndFrancisEBooks, self).wayfless()
        self.assert_access()

    def test_proxy_shibboleth(self):
        super(TaylorAndFrancisEBooks, self).proxy_shibboleth()
        self.assert_access()

    def test_proxy_ldap(self):
        super(TaylorAndFrancisEBooks, self).proxy_ldap()
        self.assert_access()

    def test_wayf(self):
        super(TaylorAndFrancisEBooks, self).wayf()
        self.page.goto(self.e_source.link_native_home)
        with self.page.expect_navigation():
            self.page.click("text=Login")
        self.page.click("text=With Shibboleth or OpenAthens")
        self.page.fill("[placeholder=\"Search for your institution\"]", "bata")
        self.page.click("text=Tomas Bata University in Zlin")
        self.page.click("text=continue")
        login_page = LoginPage(self.page, self.data)
        login_page.login_and_accept_gdpr()
        self.assert_access()

    @pytest.mark.vpn
    def test_vpn(self):
        super(TaylorAndFrancisEBooks, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        self.asserts.check_inner_text("html", "Hi, User")
