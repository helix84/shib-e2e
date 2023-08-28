class Asserts:
    def __init__(self, test, page, utils):
        self.page = page
        self.utils = utils
        self.test = test

    def is_exists(self, selector, message, timeout=20000):
        self.test.assertTrue(self.utils.is_exist(selector, timeout), message)

    def check_inner_text(self, selector, text):
        self.test.assertTrue(self.utils.is_exist(selector, 20000), f"Element with {text} is not exist.")
        it = 0
        while it < 5 and text not in self.page.inner_text(selector).rstrip():
            self.page.wait_for_timeout(2000)
            it += 1
        self.test.assertIn(text, self.page.inner_text(selector))

    def check_inner_html(self, selector, html):
        self.test.failIf(self.utils.is_exist(selector, 20000) is False, f"Element with {html} is not exist.")
        it = 0
        while it < 5 and html not in self.page.inner_html(selector).rstrip():
            self.page.wait_for_timeout(2000)
            it += 1
        self.test.assertIn(html, self.page.inner_html(selector))