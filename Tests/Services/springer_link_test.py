import pytest
from Pages.LoginUtbPage import LoginPage
from playwright.sync_api import Page
from Tests.test_base import TestBase


# source_id = "UTB00001"
class SpringerLink(TestBase):

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(SpringerLink, self).setup(page, "UTB00001")

    def test_wayfless(self):
        super(SpringerLink, self).wayfless()
        self.assert_access()

    def test_proxy_shibboleth(self):
        super(SpringerLink, self).proxy_shibboleth()
        self.assert_access()

    def test_proxy_ldap(self):
        super(SpringerLink, self).proxy_ldap()
        self.assert_access()

    def test_wayf(self):
        super(SpringerLink, self).wayf()
        self.page.goto(self.e_source.link_native_home)
        self.page.click("text=» Sign up / Log in")
        self.page.click("text=Access via your institution")
        self.page.fill("input[name=\"search\"]", "bata")
        self.page.press("input[name=\"search\"]", "Enter")
        with self.page.expect_navigation():
            self.page.click("text=Tomas Bata University in Zlín")
        login_page = LoginPage(self.page, self.data)
        login_page.login_and_accept_gdpr()
        self.assert_access()

    @pytest.mark.vpn
    def test_vpn(self):
        super(SpringerLink, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        self.asserts.check_inner_text("//*[@id=\"diagnostic-info\"]", "the Library of Tomas Bata University in Zlin")
