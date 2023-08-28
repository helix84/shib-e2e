import pytest
from Pages.LoginUtbPage import LoginPage
from playwright.sync_api import Page
from Tests.test_base import TestBase


# source_id = "UTB00228"
class TaylorAndFrancisOnlineScienceTechnologyLibrary(TestBase):

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(TaylorAndFrancisOnlineScienceTechnologyLibrary, self).setup(page, "UTB00228")

    def test_wayfless(self):
        super(TaylorAndFrancisOnlineScienceTechnologyLibrary, self).wayfless()
        self.assert_access()

    def test_proxy_shibboleth(self):
        super(TaylorAndFrancisOnlineScienceTechnologyLibrary, self).proxy_shibboleth()
        self.assert_access()

    def test_proxy_ldap(self):
        super(TaylorAndFrancisOnlineScienceTechnologyLibrary, self).proxy_ldap()
        self.assert_access()

    def test_wayf(self):
        super(TaylorAndFrancisOnlineScienceTechnologyLibrary, self).wayf()
        self.page.goto(self.e_source.link_native_home)
        self.page.click("text=Log in")
        self.page.click("text=Access through your institution")
        self.page.wait_for_timeout(5000)
        self.page.select_option("select", "Czech academic identity federation eduID.cz")
        with self.page.expect_navigation():
            self.page.click("text=Tomas Bata University in Zlín")
        login_page = LoginPage(self.page, self.data)
        login_page.login_and_accept_gdpr()
        self.assert_access()

    @pytest.mark.vpn
    def test_vpn(self):
        super(TaylorAndFrancisOnlineScienceTechnologyLibrary, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        self.asserts.check_inner_text("html", "Access provided by Univerzita Tomase Bati")
