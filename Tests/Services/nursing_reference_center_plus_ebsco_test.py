import pytest
from Pages.LoginUtbPage import LoginPage
from playwright.sync_api import Page
from Tests.test_base import TestBase


# source_id = "UTB00218"
class NursingReferenceCenterPlus(TestBase):

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(NursingReferenceCenterPlus, self).setup(page, "UTB00218")

    def test_wayfless(self):
        super(NursingReferenceCenterPlus, self).wayfless()
        self.assert_access()

    def test_proxy_shibboleth(self):
        super(NursingReferenceCenterPlus, self).proxy_shibboleth()
        self.assert_access()

    def test_proxy_ldap(self):
        super(NursingReferenceCenterPlus, self).proxy_ldap()
        self.assert_access()

    def test_wayf(self):
        super(NursingReferenceCenterPlus, self).wayf()
        self.page.goto(self.e_source.link_native_home)
        login_page = LoginPage(self.page, self.data)
        login_page.login_and_accept_gdpr()
        self.assert_access()

    @pytest.mark.vpn
    def test_vpn(self):
        super(NursingReferenceCenterPlus, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        self.asserts.check_inner_text("//*[@id=\"main\"]", "UNIVERZITA TOMASE BATI VE ZLINE")
