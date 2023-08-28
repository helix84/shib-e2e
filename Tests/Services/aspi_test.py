import pytest
from Tests.test_base import TestBase
from playwright.sync_api import Page


# source_id = "UTB00332"
class Aspi(TestBase):
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(Aspi, self).setup(page, "UTB00332")

    @pytest.mark.skip(reason="access only with VPN")
    def test_wayfless(self):
        super(Aspi, self).wayfless()

    @pytest.mark.skip(reason="access only with VPN")
    def test_proxy_shibboleth(self):
        super(Aspi, self).proxy_shibboleth()

    @pytest.mark.skip(reason="access only with VPN")
    def test_proxy_ldap(self):
        super(Aspi, self).proxy_ldap()

    @pytest.mark.vpn
    @pytest.mark.skip(reason="Neni mozne se na stranku dostat")
    def test_vpn(self):
        super(Aspi, self).vpn()
        self.page.goto(self.e_source.link_native_home)
