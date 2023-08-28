import pytest
from Pages.LoginUtbPage import LoginPage
from playwright.sync_api import Page
from Tests.test_base import TestBase


# source_id = "UTB00071"
class TeacherReferenceCenter(TestBase):

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(TeacherReferenceCenter, self).setup(page, "UTB00071")

    def test_wayfless(self):
        super(TeacherReferenceCenter, self).wayfless()
        self.assert_access()

    @pytest.mark.skip(reason="no proxy access")
    def test_proxy_shibboleth(self):
        super(TeacherReferenceCenter, self).proxy_shibboleth()
        self.assert_access()

    @pytest.mark.skip(reason="no proxy access")
    def test_proxy_ldap(self):
        super(TeacherReferenceCenter, self).proxy_ldap()
        self.assert_access()

    def test_wayf(self):
        super(TeacherReferenceCenter, self).wayf()
        self.page.goto(self.e_source.link_native_home)
        login_page = LoginPage(self.page, self.data)
        login_page.login_and_accept_gdpr()
        self.assert_access()

    @pytest.mark.vpn
    def test_vpn(self):
        super(TeacherReferenceCenter, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        self.asserts.is_exists("//*[@id=\"SearchButton\"]", "Couldn't reach ebsco site.")
