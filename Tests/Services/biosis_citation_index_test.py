import pytest
from Pages.LoginUtbPage import LoginPage
from Pages.WebOfSciencePage import WebOfSciencePage
from Tests.test_base import TestBase
from playwright.sync_api import Page


# source_id = "UTB00183"
class BIOSISCitationIndex(TestBase):
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(BIOSISCitationIndex, self).setup(page, "UTB00183")

    def test_wayf(self):
        super(BIOSISCitationIndex, self).wayf()
        self.page.goto(self.e_source.link_native_home)
        web_of_science = WebOfSciencePage(self.page, self)
        web_of_science.login_via_web_of_science()
        login_page = LoginPage(self.page, self.data)
        login_page.login_and_accept_gdpr()
        self.assert_access()

    @pytest.mark.skip(reason="no wayfless access")
    def test_wayfless(self):
        super(BIOSISCitationIndex, self).wayfless()
        self.assert_access()

    def test_proxy_shibboleth(self):
        super(BIOSISCitationIndex, self).proxy_shibboleth()
        self.assert_access()

    def test_proxy_ldap(self):
        super(BIOSISCitationIndex, self).proxy_ldap()
        self.assert_access()

    @pytest.mark.vpn
    def test_vpn(self):
        super(BIOSISCitationIndex, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        web_of_science = WebOfSciencePage(self.page, self)
        web_of_science.assert_login()
