import pytest
from Pages.LoginUtbPage import LoginPage
from playwright.sync_api import Page
from Tests.test_base import TestBase


# source_id = "UTB00215"
class PeterLangEBooks(TestBase):

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(PeterLangEBooks, self).setup(page, "UTB00215")

    @pytest.mark.skip(reason="no wayfless access")
    def test_wayfless(self):
        super(PeterLangEBooks, self).wayfless()
        self.assert_access()

    def test_proxy_shibboleth(self):
        super(PeterLangEBooks, self).proxy_shibboleth()
        self.assert_access()

    def test_proxy_ldap(self):
        super(PeterLangEBooks, self).proxy_ldap()
        self.assert_access()

    @pytest.mark.skip(reason="no wayf access")
    def test_wayf(self):
        super(PeterLangEBooks, self).wayf()
        self.page.goto(self.e_source.link_native_home)
        login_page = LoginPage(self.page, self.data)
        login_page.login_and_accept_gdpr()
        self.assert_access()

    @pytest.mark.vpn
    def test_vpn(self):
        super(PeterLangEBooks, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        self.asserts.check_inner_text("html", "Contact")
