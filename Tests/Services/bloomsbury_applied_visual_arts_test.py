import pytest
from Pages.LoginUtbPage import LoginPage
from Tests.test_base import TestBase
from playwright.sync_api import Page


# source_id = "UTB00235"
class BloomsburyAppliedVisualArts(TestBase):
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(BloomsburyAppliedVisualArts, self).setup(page, "UTB00235")

    @pytest.mark.skip(reason="wayf not working")
    def test_wayf(self):
        super(BloomsburyAppliedVisualArts, self).wayf()
        self.page.goto(self.e_source.link_native_home)
        self.page.click("text=Log In")
        self.page.click("text=Shibboleth Login Page")
        with self.page.expect_navigation():
            self.page.click("#results-list >> text=Tomas Bata University in Zlín")
        login_page = LoginPage(self.page, self.data)
        login_page.login_and_accept_gdpr()
        self.assert_access()

    @pytest.mark.skip(reason="no wayfless access")
    def test_wayfless(self):
        super(BloomsburyAppliedVisualArts, self).wayfless()
        self.assert_access()

    def test_proxy_shibboleth(self):
        super(BloomsburyAppliedVisualArts, self).proxy_shibboleth()
        self.assert_access()

    def test_proxy_ldap(self):
        super(BloomsburyAppliedVisualArts, self).proxy_ldap()
        self.assert_access()

    @pytest.mark.vpn
    def test_vpn(self):
        super(BloomsburyAppliedVisualArts, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        self.assertEqual(" Access Provided by Tomas Bata University in Zlin ",
                         self.page.inner_text("//*[@id=\"checkForLogin\"]"))
