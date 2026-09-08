from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        
    def should_be_login_url(self):
        #проверка на корректный url адрес
        self.should_be_on_page("/login")

    def go_to_register_page(self): 
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()


 