from playwright.sync_api import TimeoutError


class Utils:
    def __init__(self, page):
        self.page = page

    def is_exist(self, selector, timeout=10000):
        try:
            self.page.wait_for_selector(selector, timeout=timeout)
            return True
        except TimeoutError:
            return False

    def string_to_bool(self, value):
        if value == 'True':
            return True
        elif value == 'False':
            return False
