import pytest
from Pages.LoginUtbPage import LoginPage
from playwright.sync_api import Page
from Tests.test_base import TestBase


# source_id = "UTB00212"
class Statista(TestBase):

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(Statista, self).setup(page, "UTB00212")

    @pytest.mark.skip(reason="no wayfless access")
    def test_wayfless(self):
        super(Statista, self).wayfless()
        self.assert_access()

    def test_proxy_shibboleth(self):
        super(Statista, self).proxy_shibboleth()
        self.assert_access()

    def test_proxy_ldap(self):
        super(Statista, self).proxy_ldap()
        self.assert_access()

    def test_wayf(self):
        super(Statista, self).wayf()
        self.page.goto(self.e_source.link_native_home)
        self.page.click("//*[@id=\"onetrust-accept-btn-handler\"]")
        self.page.click("text=Login")
        self.page.click("text=Campus Access")
        self.page.select_option("select[name=\"loginShibboleth[shibbolethLink]\"]", "335")
        with self.page.expect_navigation():
            self.page.click("text=Check access")
        login_page = LoginPage(self.page, self.data)
        login_page.login_and_accept_gdpr()
        self.assert_access()

    @pytest.mark.vpn
    def test_vpn(self):
        super(Statista, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        self.asserts.check_inner_text("//*[@id=\"content\"]", "Welcome Univerzita Tomáše Bati ve Zlíně!")
