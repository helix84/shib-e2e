import pytest
from Pages.LoginUtbPage import LoginPage
from playwright.sync_api import Page
from Tests.test_base import TestBase


# source_id = "UTB00138"
class SciFindernScholar(TestBase):

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(SciFindernScholar, self).setup(page, "UTB00138")

    @pytest.mark.skip(reason="no wayfless access")
    def test_wayfless(self):
        super(SciFindernScholar, self).wayfless()
        self.assert_access()

    def test_proxy_shibboleth(self):
        super(SciFindernScholar, self).proxy_shibboleth()
        self.assert_access()

    def test_proxy_ldap(self):
        super(SciFindernScholar, self).proxy_ldap()
        self.assert_access()

    @pytest.mark.skip(reason="no wayf access")
    def test_wayf(self):
        super(SciFindernScholar, self).wayf()
        self.page.goto(self.e_source.link_native_home)
        login_page = LoginPage(self.page, self.data)
        login_page.login_and_accept_gdpr()
        self.assert_access()

    @pytest.mark.vpn
    def test_vpn(self):
        super(SciFindernScholar, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        self.asserts.check_inner_text("html", "Contact")
