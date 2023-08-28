import pytest
from Tests.test_base import TestBase
from playwright.sync_api import Page
from flaky import flaky


# source_id = "UTB00331"
@flaky
class JournalOfAppliedPhysics(TestBase):
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(JournalOfAppliedPhysics, self).setup(page, "UTB00331")

    def test_wayfless(self):
        super(JournalOfAppliedPhysics, self).wayfless()
        self.assert_access()

    def test_proxy_shibboleth(self):
        super(JournalOfAppliedPhysics, self).proxy_shibboleth()
        self.assert_access()

    def test_proxy_ldap(self):
        super(JournalOfAppliedPhysics, self).proxy_ldap()
        self.assert_access()

    @pytest.mark.vpn
    def test_vpn(self):
        super(JournalOfAppliedPhysics, self).vpn()
        self.page.goto(self.e_source.link_native_home)
        self.assert_access()

    def assert_access(self):
        if self.utils.is_exist("text=Yes"):
            self.page.click("text=Yes")

        self.page.wait_for_selector("// *[ @ id = \"pb-page-content\"]")
        self.assertTrue(
            "Access provided by Tomas Bata University in Zlin" in self.page.inner_text(
                "//*[@id=\"pb-page-content\"]").rstrip())
