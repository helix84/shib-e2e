import pytest
from Pages.LoginUtbPage import LoginPage
from playwright.sync_api import Page
from Tests.test_base import TestBase


# source_id = "UTB00270"
class OxfordScholarshipOnlineLinguistics(TestBase):

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(OxfordScholarshipOnlineLinguistics, self).setup(page, "UTB00270")

    @pytest.mark.skip(reason="no wayfless access")
    def test_wayfless(self):
        super(OxfordScholarshipOnlineLinguistics, self).wayfless()
        self.assert_access()

    def test_proxy_shibboleth(self):
        super(OxfordScholarshipOnlineLinguistics, self).proxy_shibboleth()
        self.assert_access()

    def test_proxy_ldap(self):
        super(OxfordScholarshipOnlineLinguistics, self).proxy_ldap()
        self.assert_access()

    @pytest.mark.skip(reason="no wayf access")
    def test_wayf(self):
        super(OxfordScholarshipOnlineLinguistics, self).wayf()
        self.page.goto(self.e_source.link_native_home)
        login_page = LoginPage(self.page, self.data)
        login_page.login_and_accept_gdpr()
        self.assert_access()

    @pytest.mark.vpn
    def test_vpn(self):
        super(OxfordScholarshipOnlineLinguistics, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        self.asserts.check_inner_text("html", "Oxford Scholarship Online")
