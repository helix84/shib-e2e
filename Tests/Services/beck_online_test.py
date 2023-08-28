import pytest
from Tests.test_base import TestBase
from playwright.sync_api import Page


# source_id = "UTB00113"
class BeckOnline(TestBase):
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(BeckOnline, self).setup(page, "UTB00113")

    @pytest.mark.skip(reason="no wayfless access")
    def test_wayfless(self):
        super(BeckOnline, self).wayfless()

    def test_proxy_shibboleth(self):
        super(BeckOnline, self).proxy_shibboleth()
        self.assert_access()

    def test_proxy_ldap(self):
        super(BeckOnline, self).proxy_ldap()
        self.assert_access()

    @pytest.mark.vpn
    def test_vpn(self):
        super(BeckOnline, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        self.assertTrue(self.utils.is_exist("//*[@id=\"main-form:submit\"]"))
