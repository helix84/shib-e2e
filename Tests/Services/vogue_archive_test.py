import pytest
from Pages.LoginUtbPage import LoginPage
from playwright.sync_api import Page
from Tests.test_base import TestBase


# source_id = "UTB00328"
class VogueArchive(TestBase):

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(VogueArchive, self).setup(page, "UTB00328")

    def test_wayfless(self):
        super(VogueArchive, self).wayfless()
        self.assert_access()

    def test_proxy_shibboleth(self):
        super(VogueArchive, self).proxy_shibboleth()
        self.assert_access()

    def test_proxy_ldap(self):
        super(VogueArchive, self).proxy_ldap()
        self.assert_access()

    def test_wayf(self):
        super(VogueArchive, self).wayf()
        self.page.goto(self.e_source.link_native_home)
        self.page.fill("//*[@id=\"institutionfinderdiv\"]/input", "utb")
        self.page.wait_for_timeout(2000)
        self.page.press("//*[@id=\"institutionfinderdiv\"]/input", "Enter")
        self.page.click("text=Univerzita Tomase Bati ve Zline")
        login_page = LoginPage(self.page, self.data)
        login_page.login_and_accept_gdpr()
        self.assert_access()

    @pytest.mark.vpn
    def test_vpn(self):
        super(VogueArchive, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        self.asserts.check_inner_html("html", "https://knihovna.utb.cz/")
