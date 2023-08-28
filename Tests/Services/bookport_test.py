import pytest
from Pages.LoginUtbPage import LoginPage
from Tests.test_base import TestBase
from playwright.sync_api import Page


# source_id = "UTB00244"
class Bookport(TestBase):
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(Bookport, self).setup(page, "UTB00244")

    def test_wayf(self):
        super(Bookport, self).wayf()
        self.page.goto(self.e_source.link_native_home)
        login_page = LoginPage(self.page, self.data)
        login_page.login_and_accept_gdpr()
        self.assert_access()

    def test_wayfless(self):
        super(Bookport, self).wayfless()
        self.assert_access()

    @pytest.mark.skip(reason="not active in proxy")
    def test_proxy_shibboleth(self):
        super(Bookport, self).proxy_shibboleth()
        self.assert_access()

    @pytest.mark.skip(reason="not active in proxy")
    def test_proxy_ldap(self):
        super(Bookport, self).proxy_ldap()
        self.assert_access()

    @pytest.mark.vpn
    def test_vpn(self):
        super(Bookport, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        self.asserts.is_exists("//*[@id=\"userMenuLabel\"]", "User menu label is not visible - Not log in!")
