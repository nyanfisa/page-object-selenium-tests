from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

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


    def open(self):
        self.browser.get(self.url)