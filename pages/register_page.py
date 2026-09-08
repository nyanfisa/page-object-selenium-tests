from .base_page import BasePage
from .locators import RegisterPageLocators


class RegisterPage(BasePage):
    def should_be_register_page(self):
            self.should_be_register_url()
            self.should_be_register_form()

    def should_be_register_url(self):
            #проверка на корректный url адрес
            self.should_be_on_page("/join")     

    def should_be_register_form(self):
            # реализуйте проверку, что есть форма регистрации на странице
            assert self.is_element_present(*RegisterPageLocators.REGISTER_FORM), "Register form is not presented"
            assert self.is_element_present(*RegisterPageLocators.EMAIL_FIELD), "First email field is not presented"
            assert self.is_element_present(*RegisterPageLocators.REENTER_EMIAIL_FIELD), "Second(reenter) email field is not presented"
            assert self.is_element_present(*RegisterPageLocators.COUNTRY_DROPDOWN), "Country dropdown link is not presented"
            assert self.is_element_present(*RegisterPageLocators.CAPTCHA_ENTRY_CHECK), "Captcha is not presented"
            assert self.is_element_present(*RegisterPageLocators.CREATE_ACCOUNT_BUTTON), "Register button link is not presented"