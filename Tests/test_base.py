import pytest

import unittest
from Helpers.Data import Data
from Helpers.Asserts import Asserts
from Helpers.Utils import Utils
from Pages.ProxyPage import ProxyPage
from Pages.LoginUtbPage import LoginPage


class TestBase(unittest.TestCase):

    def setup(self, page, source_id):
        self.page = page
        self.data = Data()
        self.utils = Utils(self.page)
        self.asserts = Asserts(self, self.page, self.utils)
        self.e_source = self.get_e_source(source_id)
        self.is_vpn_enabled = self.utils.string_to_bool(self.data.is_vpn_enabled)

    def get_e_source(self, source_id):
        return next((e_source for e_source in self.data.e_source_list if e_source.source_id == source_id), None)

    def wayfless(self):
        if self.is_vpn_enabled:
            pytest.skip("VPN is running")
        self.page.goto(self.e_source.wayfless)
        login_page = LoginPage(self.page, self.data)
        login_page.login_and_accept_gdpr()

    def proxy_shibboleth(self):
        if self.is_vpn_enabled:
            pytest.skip("VPN is running")
        proxy_page = ProxyPage(self.page, self.data, self)
        proxy_page.navigate(self.e_source.link_native_home)
        proxy_page.login_shibboleth()

    def proxy_ldap(self):
        if self.is_vpn_enabled:
            pytest.skip("VPN is running")
        proxy_page = ProxyPage(self.page, self.data, self)
        proxy_page.navigate(self.e_source.link_native_home)
        proxy_page.login_ldap()

    def wayf(self):
        if self.is_vpn_enabled:
            pytest.skip("VPN is running")

    def vpn(self):
        if not self.is_vpn_enabled:
            pytest.skip("VPN is not running")

