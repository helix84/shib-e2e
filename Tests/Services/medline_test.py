import pytest
from Pages.LoginUtbPage import LoginPage
from playwright.sync_api import Page

from Pages.WebOfSciencePage import WebOfSciencePage
from Tests.test_base import TestBase


# source_id = "UTB00185"
class Medline(TestBase):

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(Medline, self).setup(page, "UTB00185")

    @pytest.mark.skip(reason="no wayfless access")
    def test_wayfless(self):
        super(Medline, self).wayfless()
        self.assert_access()

    def test_proxy_shibboleth(self):
        super(Medline, self).proxy_shibboleth()
        self.assert_access()

    def test_proxy_ldap(self):
        super(Medline, self).proxy_ldap()
        self.assert_access()

    def test_wayf(self):
        super(Medline, self).wayf()
        self.page.goto(self.e_source.link_native_home)
        web_of_science = WebOfSciencePage(self.page, self)
        web_of_science.login_via_web_of_science()
        login_page = LoginPage(self.page, self.data)
        login_page.login_and_accept_gdpr()
        self.assert_access()

    @pytest.mark.vpn
    def test_vpn(self):
        super(Medline, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        web_of_science = WebOfSciencePage(self.page, self)
        web_of_science.assert_login()
