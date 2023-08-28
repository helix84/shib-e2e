class LoginPage:
    def __init__(self, page, data):
        self.page = page
        self.data = data

    @property
    def login_username_input(self):
        return self.page.wait_for_selector("input[name=\"j_username\"]")

    @property
    def login_password_input(self):
        return self.page.wait_for_selector("input[name=\"j_password\"]")

    @property
    def login_button(self):
        return self.page.wait_for_selector("text=Přihlásit se:")

    @property
    def gdpr_confirm_button(self):
        return self.page.wait_for_selector("text=Přijmout")

    def login_and_accept_gdpr(self):
        self.login_username_input.fill(self.data.user.get_name())
        self.login_password_input.fill(self.data.user.get_password())
        self.login_button.click()
        with self.page.expect_navigation():
            self.gdpr_confirm_button.click()
