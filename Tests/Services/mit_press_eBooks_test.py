import pytest
from Pages.LoginUtbPage import LoginPage
from playwright.sync_api import Page

from Tests.test_base import TestBase


# source_id = "UTB00326"
class MITPressEBooks(TestBase):

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(MITPressEBooks, self).setup(page, "UTB00326")

    def test_wayfless(self):
        super(MITPressEBooks, self).wayfless()
        self.assert_access()

    def test_proxy_shibboleth(self):
        super(MITPressEBooks, self).proxy_shibboleth()
        self.assert_access()

    def test_proxy_ldap(self):
        super(MITPressEBooks, self).proxy_ldap()
        self.assert_access()

    def test_wayf(self):
        super(MITPressEBooks, self).wayf()
        self.page.goto(self.e_source.link_native_home)
        self.page.click("text=Sign In")
        with self.page.expect_navigation():
            self.page.click("a:has-text(\"Sign in via your Institution\")")
        self.page.select_option("select[name=\"FederationDropdown\"]", "11")
        self.page.select_option("select[name=\"InstitutionDropdown\"]", "https://shibboleth.utb.cz/idp/shibboleth")
        with self.page.expect_navigation():
            self.page.click("a:has-text(\"Select\")")
        login_page = LoginPage(self.page, self.data)
        login_page.login_and_accept_gdpr()
        self.assert_access()

    @pytest.mark.vpn
    def test_vpn(self):
        super(MITPressEBooks, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        self.asserts.check_inner_text("//*[@id=\"tablet-user-dropdown\"]", "Bata")
