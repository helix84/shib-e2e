import pytest
from Pages.LoginUtbPage import LoginPage
from Tests.test_base import TestBase
from playwright.sync_api import Page


# source_id = "UTB00139"
class CsnOnline(TestBase):
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(CsnOnline, self).setup(page, "UTB00139")

    def test_wayf(self):
        super(CsnOnline, self).wayf()
        self.page.goto(self.e_source.link_native_home)
        self.page.click("text=Univerzita Tomáše Bati ve Zlíně")
        login_page = LoginPage(self.page, self.data)
        login_page.login_and_accept_gdpr()
        self.assert_access()

    @pytest.mark.skip(reason="no wayfless access")
    def test_wayfless(self):
        super(CsnOnline, self).wayfless()
        self.assert_access()

    @pytest.mark.skip(reason="not active in proxy")
    def test_proxy_shibboleth(self):
        super(CsnOnline, self).proxy_shibboleth()

    @pytest.mark.skip(reason="not active in proxy")
    def test_proxy_ldap(self):
        super(CsnOnline, self).proxy_ldap()

    @pytest.mark.vpn
    def test_vpn(self):
        super(CsnOnline, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        self.asserts.is_exists("//*[@id=\"logon\"]", "Logon is not visible - Not log in!")
