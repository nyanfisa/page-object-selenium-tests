from .base_page import BasePage
from .locators import LoginPageLocators
from .register_page import RegisterPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv

load_dotenv()

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        
    def should_be_login_url(self):
        #проверка на корректный url адрес
        self.should_be_on_page("/login")

    def should_be_register_button(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), "Register button is not presented"    

    def go_to_register_page(self): 
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
        return RegisterPage(browser=self.browser, url=self.browser.current_url) 

    def login_to_profile(self):
        username_field = WebDriverWait(self.browser, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.USERNAME_FIELD)
        )
        username_field.send_keys(os.getenv("STEAM_LOGIN"))  

        password_field = WebDriverWait(self.browser, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.PASSWORD_FIELD)
        )
        password_field.send_keys(os.getenv("STEAM_PASS"))

        button = WebDriverWait(self.browser, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.SUBMIT_BUTTON)
        ) 
        button.click()

        