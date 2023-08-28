import pytest
from Pages.LoginUtbPage import LoginPage
from Tests.test_base import TestBase
from playwright.sync_api import Page


# source_id = "UTB00250"
class CoronavirusResearchDatabase(TestBase):
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(CoronavirusResearchDatabase, self).setup(page, "UTB00250")

    @pytest.mark.skip(reason="nefunkcni login na ProQuest strankach")
    def test_wayf(self):
        super(CoronavirusResearchDatabase, self).wayf()
        self.page.goto(self.e_source.link_native_home)
        self.page.click("text=Použijte přihlášení přes vaši instituci")
        self.page.click("text=Tomas Bata University in Zlín")
        login_page = LoginPage(self.page, self.data)
        login_page.login_and_accept_gdpr()
        self.assert_access()

    def test_wayfless(self):
        super(CoronavirusResearchDatabase, self).wayfless()
        self.assert_access()

    def test_proxy_shibboleth(self):
        super(CoronavirusResearchDatabase, self).proxy_shibboleth()
        self.assert_access()

    def test_proxy_ldap(self):
        super(CoronavirusResearchDatabase, self).proxy_ldap()
        self.assert_access()

    @pytest.mark.vpn
    def test_vpn(self):
        super(CoronavirusResearchDatabase, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        html = self.page.wait_for_selector("//*[@id=\"content\"]")
        self.assertIn("<img title=\"TBU Library in Zlin\" alt=\"TBU Library in Zlin\"", html.inner_html())
