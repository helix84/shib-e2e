from playwright.sync_api import Error
from Pages.LoginUtbPage import LoginPage


class ProxyPage:
    def __init__(self, page, data, test):
        self.page = page
        self.data = data
        self.test = test
        self.login_page = LoginPage(page, data)

    @property
    def shibboleth_button(self):
        return self.page.wait_for_selector("text=Univerzitní účet Single Sign-On (Shibboleth)")

    @property
    def ldap_button(self):
        return self.page.wait_for_selector("text=Účet LDAP")

    @property
    def login_ldap_button(self):
        return self.page.wait_for_selector("text=Přihásit se")

    @property
    def login_ldap_username_input(self):
        return self.page.wait_for_selector("input[name=\"user\"]")

    @property
    def login_ldap_password_input(self):
        return self.page.wait_for_selector("input[name=\"pass\"]")

    def navigate(self, link_native_home):
        try:
            self.page.goto(self.data.proxy_url + link_native_home, timeout=20000)
        except Error:
            self.test.fail("ERR_CONNECTION_TIMED_OUT - Proxy is not working!")

    def login_shibboleth(self):
        self.shibboleth_button.click()
        self.login_page.login_and_accept_gdpr()

    def login_ldap(self):
        self.ldap_button.click()
        self.login_ldap_username_input.fill(self.data.user.get_name())
        self.login_ldap_password_input.fill(self.data.user.get_password())
        self.login_ldap_button.click()
