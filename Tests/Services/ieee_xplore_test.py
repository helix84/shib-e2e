import pytest
from Pages.LoginUtbPage import LoginPage
from playwright.sync_api import Page
from Tests.test_base import TestBase


# source_id = "UTB00012"
class IEEEXplore(TestBase):

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(IEEEXplore, self).setup(page, "UTB00012")

    def test_wayfless(self):
        super(IEEEXplore, self).wayfless()
        self.assert_access()

    def test_proxy_shibboleth(self):
        super(IEEEXplore, self).proxy_shibboleth()
        self.assert_access()

    def test_proxy_ldap(self):
        super(IEEEXplore, self).proxy_ldap()
        self.assert_access()

    def test_wayf(self):
        super(IEEEXplore, self).wayf()
        self.page.goto(self.e_source.link_native_home)
        self.page.click("text=Institutional Sign In")
        element = self.page.wait_for_selector('ngb-modal-window')
        element.wait_for_selector('input').click()
        self.page.wait_for_timeout(2000)
        element.wait_for_selector('input').fill("bata")
        element.wait_for_selector('input').press("Enter")
        with self.page.expect_navigation():
            self.page.click("text=Tomas Bata University in Zlin")
        login_page = LoginPage(self.page, self.data)
        login_page.login_and_accept_gdpr()
        self.assert_access()

    @pytest.mark.vpn
    def test_vpn(self):
        super(IEEEXplore, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        self.asserts.check_inner_text("html", "Tomas Bata University in Zlin")
