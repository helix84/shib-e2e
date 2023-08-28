import pytest
from Tests.test_base import TestBase
from playwright.sync_api import Page


# source_id = "UTB00323"
class Anopress(TestBase):
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(Anopress, self).setup(page, "UTB00323")

    @pytest.mark.skip(reason="no wayfless access")
    def test_wayfless(self):
        super(Anopress, self).wayfless()

    def test_proxy_shibboleth(self):
        super(Anopress, self).proxy_shibboleth()
        self.assert_access()

    def test_proxy_ldap(self):
        super(Anopress, self).proxy_ldap()
        self.assert_access()

    @pytest.mark.vpn
    def test_vpn(self):
        super(Anopress, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        self.assertTrue(self.utils.is_exist("//*[@id=\"btnSearch\"]"))
