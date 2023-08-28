import pytest
from playwright.sync_api import Page

from Tests.test_base import TestBase


# source_id = "UTB00056"
class Knovel(TestBase):

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(Knovel, self).setup(page, "UTB00056")

    def test_wayfless(self):
        super(Knovel, self).wayfless()
        self.assert_access()

    def test_proxy_shibboleth(self):
        super(Knovel, self).proxy_shibboleth()
        self.assert_access()

    def test_proxy_ldap(self):
        super(Knovel, self).proxy_ldap()
        self.assert_access()

    def test_wayf(self):
        super(Knovel, self).wayf()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access() #nelze nalezt instituci

    @pytest.mark.vpn
    def test_vpn(self):
        super(Knovel, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        self.asserts.check_inner_text("//*[@id=\"header-menu_dropdown_menu_label\"]", "Welcome Tomas Bata Uni...")
