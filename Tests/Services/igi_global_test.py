import pytest
from Pages.LoginUtbPage import LoginPage
from playwright.sync_api import Page
from Tests.test_base import TestBase


# source_id = "UTB00234"
class IgiGlobal(TestBase):

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(IgiGlobal, self).setup(page, "UTB00234")

    @pytest.mark.skip(reason="no wayfless access")
    def test_wayfless(self):
        super(IgiGlobal, self).wayfless()
        self.assert_access()

    def test_proxy_shibboleth(self):
        super(IgiGlobal, self).proxy_shibboleth()
        self.assert_access()

    def test_proxy_ldap(self):
        super(IgiGlobal, self).proxy_ldap()
        self.assert_access()

    @pytest.mark.skip(reason="nefunguje prihlaseni")
    def test_wayf(self):
        super(IgiGlobal, self).wayf()
        self.page.goto(self.e_source.link_native_home)
        self.page.click("text=Institution Login Log in using your institution credentials. Log In >> span")
        self.page.fill("[placeholder=\"Institution name or email...\"]", "zlin")
        self.page.press("[placeholder=\"Institution name or email...\"]", "Enter")
        self.page.click("[aria-label=\"Univerzita Tomáše Bati ve Zlíně\"]")
        login_page = LoginPage(self.page, self.data)
        login_page.login_and_accept_gdpr()
        self.assert_access()

    @pytest.mark.vpn
    def test_vpn(self):
        super(IgiGlobal, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        self.asserts.check_inner_text("//*[@id=\"collapse-menu\"]", "Tomas Bata University in Zlín")
