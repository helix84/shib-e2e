import pytest
from Pages.LoginUtbPage import LoginPage
from playwright.sync_api import Page
from Tests.test_base import TestBase


# source_id = "UTB00327"
class SAGEPremier(TestBase):

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(SAGEPremier, self).setup(page, "UTB00327")

    @pytest.mark.skip(reason="no wayfless access")
    def test_wayfless(self):
        super(SAGEPremier, self).wayfless()
        self.assert_access()

    def test_proxy_shibboleth(self):
        super(SAGEPremier, self).proxy_shibboleth()
        self.assert_access()

    def test_proxy_ldap(self):
        super(SAGEPremier, self).proxy_ldap()
        self.assert_access()

    def test_wayf(self):
        super(SAGEPremier, self).wayf()
        self.page.goto(self.e_source.link_native_home)
        self.page.click("text=ACCEPT ALL")
        self.page.click("text=Institution")
        with self.page.expect_navigation():
            self.page.click("div[role=\"button\"]:has-text(\"Access through your institution\")")
        self.page.select_option("select[name=\"federationSelect\"]", "Czech Republic - eduID.cz")
        with self.page.expect_navigation():
            self.page.click("text=Tomas Bata University in Zlín")
        login_page = LoginPage(self.page, self.data)
        login_page.login_and_accept_gdpr()
        self.assert_access()

    @pytest.mark.vpn
    def test_vpn(self):
        super(SAGEPremier, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        self.asserts.check_inner_text("//*[@id=\"portalLoginBar\"]", "Univerzita Tomase Bati ve Zlin")
