import pytest
from Pages.LoginUtbPage import LoginPage
from playwright.sync_api import Page
from Tests.test_base import TestBase


# source_id = "UTB00065"
class RSCJournals(TestBase):

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(RSCJournals, self).setup(page, "UTB00065")

    def test_wayfless(self):
        super(RSCJournals, self).wayfless()
        self.assert_access()

    def test_proxy_shibboleth(self):
        super(RSCJournals, self).proxy_shibboleth()
        self.assert_access()

    def test_proxy_ldap(self):
        super(RSCJournals, self).proxy_ldap()
        self.assert_access()

    def test_wayf(self):
        super(RSCJournals, self).wayf()
        self.page.goto(self.e_source.link_native_home)
        with self.page.expect_navigation():
            self.page.click("text=Log in / register")

        with self.page.expect_navigation():
            self.page.click("text=Find my institution")
        self.page.click("text=View all institutions")
        self.page.click("text=Tomas Bata University in Zlín")
        login_page = LoginPage(self.page, self.data)
        login_page.login_and_accept_gdpr()
        self.assert_access()

    @pytest.mark.vpn
    def test_vpn(self):
        super(RSCJournals, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        self.asserts.check_inner_text("html", "University of Tomas Bata Zlin")
