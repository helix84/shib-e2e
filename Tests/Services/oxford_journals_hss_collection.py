import pytest
from Pages.LoginUtbPage import LoginPage
from playwright.sync_api import Page
from Tests.test_base import TestBase


# source_id = "UTB00028"
class OxfordJournalsHSSCollection(TestBase):

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(OxfordJournalsHSSCollection, self).setup(page, "UTB00028")

    @pytest.mark.skip(reason="no wayfless access")
    def test_wayfless(self):
        super(OxfordJournalsHSSCollection, self).wayfless()
        self.assert_access()

    def test_proxy_shibboleth(self):
        super(OxfordJournalsHSSCollection, self).proxy_shibboleth()
        self.assert_access()

    def test_proxy_ldap(self):
        super(OxfordJournalsHSSCollection, self).proxy_ldap()
        self.assert_access()

    @pytest.mark.skip(reason="no wayf access")
    def test_wayf(self):
        super(OxfordJournalsHSSCollection, self).wayf()
        self.page.goto(self.e_source.link_native_home)
        self.page.click("text=Sign in through your institution")
        login_page = LoginPage(self.page, self.data)
        login_page.login_and_accept_gdpr()
        self.assert_access()

    @pytest.mark.vpn
    def test_vpn(self):
        super(OxfordJournalsHSSCollection, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        self.page.click("text=Search Menu Menu >> :nth-match(a[role=\"button\"], 2)")
        self.asserts.check_inner_text("html", "Tomas Bata University in Zlin")
