import pytest
from Pages.LoginUtbPage import LoginPage
from playwright.sync_api import Page
from Tests.test_base import TestBase


# source_id = "UTB00055"
class IOPscience(TestBase):

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(IOPscience, self).setup(page, "UTB00055")

    @pytest.mark.skip(reason="wayfless access via wayf test method")
    def test_wayfless(self):
        super(IOPscience, self).wayfless()
        self.assert_access()

    @pytest.mark.skip(reason="proxy not working")
    def test_proxy_shibboleth(self):
        super(IOPscience, self).proxy_shibboleth()
        self.assert_access()

    @pytest.mark.skip(reason="proxy not working")
    def test_proxy_ldap(self):
        super(IOPscience, self).proxy_ldap()
        self.assert_access()

    def test_wayf(self):
        super(IOPscience, self).wayf()
        self.page.goto(self.e_source.wayfless)
        self.page.fill("[placeholder=\"Institution name or email...\"]", "zlin")
        self.page.press("[placeholder=\"Institution name or email...\"]", "Enter")
        with self.page.expect_navigation():
            self.page.click("[aria-label=\"Univerzita Tomáše Bati ve Zlíně\"]")
        login_page = LoginPage(self.page, self.data)
        login_page.login_and_accept_gdpr()
        self.assert_access()

    @pytest.mark.vpn
    def test_vpn(self):
        super(IOPscience, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        self.asserts.check_inner_text("//*[@id=\"wd-inst-name inst-name\"]", "Tomas Bata University")
