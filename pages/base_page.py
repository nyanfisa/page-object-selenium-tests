from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from urllib.parse import urlparse

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def is_element_present(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except NoSuchElementException:
            return False
        return True 

    def should_be_on_page(self, expected_path):
        current_url = self.browser.current_url
        parsed_url = urlparse(current_url)

        assert parsed_url.path.startswith(expected_path), f"Expected path to start with {expected_path}, got {parsed_url.path}"       


    def open(self):
        self.browser.get(self.url)