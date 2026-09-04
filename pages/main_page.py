from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, '#global_action_menu > a.global_action_link')

    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, '#global_action_menu > a.global_action_link')
        login_link.click()