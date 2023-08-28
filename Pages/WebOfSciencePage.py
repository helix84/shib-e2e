class WebOfSciencePage:
    def __init__(self, page, test):
        self.page = page
        self.test = test

    @property
    def select_institution_combobox(self):
        return self.page.wait_for_selector("text=Select institutionSelect institution")

    @property
    def czech_academic_value(self):
        return self.page.wait_for_selector("text=Czech academic identity federation eduID.cz")

    @property
    def go_to_institution_button(self):
        return self.page.wait_for_selector("button:has-text(\"Go to institution\")")

    @property
    def bata_input(self):
        return self.page.wait_for_selector("input")

    def login_via_web_of_science(self):
        self.select_institution_combobox.click()
        self.czech_academic_value.click()
        self.go_to_institution_button.click()
        with self.page.expect_navigation():
            self.page.click("text=Univerzita Tomáše Bati ve Zlíně")

    def assert_login(self):
        self.test.assertEqual(self.page.get_attribute("//*[@id=\"InstLogoTa-0\"]", "title"),
                              "Access provided by Tomas Bata University Library. Click for more info about science and "
                              "research at TBU")
