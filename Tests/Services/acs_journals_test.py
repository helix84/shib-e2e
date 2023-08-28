import pytest
from Pages.LoginUtbPage import LoginPage
from playwright.sync_api import Page
from Tests.test_base import TestBase


# source_id = "UTB00033"
class AcsJournals(TestBase):
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(AcsJournals, self).setup(page, "UTB00329")

    def test_wayf(self):
        super(AcsJournals, self).wayf()
        self.page.goto(self.e_source.link_native_home)
        self.page.click("text=Find my institution")
        self.page.click("text=Czech academic identity federation eduID.cz")
        with self.page.expect_navigation():
            self.page.click("a:has-text(\"Tomas Bata University in Zlín\")")
        login_page = LoginPage(self.page, self.data)
        login_page.login_and_accept_gdpr()
        self.assert_access()

    def test_wayfless(self):
        super(AcsJournals, self).wayfless()
        self.assert_access()

    def test_proxy_shibboleth(self):
        super(AcsJournals, self).proxy_shibboleth()
        self.assert_access()

    def test_proxy_ldap(self):
        super(AcsJournals, self).proxy_ldap()
        self.assert_access()

    @pytest.mark.vpn
    def test_vpn(self):
        super(AcsJournals, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        self.page.wait_for_selector("// *[ @ id = \"pb-page-content\"]")
        self.assertTrue(
            "Access provided byUNIV TOMASE BATI VE ZLINE" in self.page.inner_text(
                "// *[ @ id = \"pb-page-content\"]").rstrip())
