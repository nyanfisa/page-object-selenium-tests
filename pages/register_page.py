from .base_page import BasePage
from .locators import RegisterPageLocators

class RegisterPage(BasePage):
    def should_be_register_page(self):
        self.should_be_register_url()
        self.should_be_register_form()

    def should_be_register_url(self):
        self.should_be_on_page("/join")     

    def should_be_register_form(self):
        assert self.is_element_present(*RegisterPageLocators.REGISTER_FORM), "Register form is not presented"
        assert self.is_element_present(*RegisterPageLocators.EMAIL_FIELD), "First email field is not presented"
        assert self.is_element_present(*RegisterPageLocators.REENTER_EMAIL_FIELD), "Second(reenter) email field is not presented"
        assert self.is_element_present(*RegisterPageLocators.COUNTRY_DROPDOWN), "Country dropdown link is not presented"
        assert self.is_element_present(*RegisterPageLocators.CAPTCHA_IFRAME), "Captcha is not presented"
        assert self.is_element_present(*RegisterPageLocators.AGREEMENT_CHECKBOX), "Agreement checkbox is not presented"
        assert self.is_element_present(*RegisterPageLocators.CREATE_ACCOUNT_BUTTON), "Register button link is not presented"


    def fill_the_register_form(self, email_field, reenter, captcha_check, agreement_check):
        email = self.browser.find_element(*RegisterPageLocators.EMAIL_FIELD)
        email.send_keys(email_field)
        reenter_email = self.browser.find_element(*RegisterPageLocators.REENTER_EMAIL_FIELD)
        reenter_email.send_keys(reenter)
        country = self.browser.find_element(*RegisterPageLocators.COUNTRY_DROPDOWN)
        country.click()
        self.browser.find_element(*RegisterPageLocators.COUNTRY_CHOICE).click()
        captcha = self.browser.find_element(*RegisterPageLocators.CAPTCHA_IFRAME)
        if captcha_check:
            captcha.click()
        agreement = self.browser.find_element(*RegisterPageLocators.AGREEMENT_CHECKBOX)
        if agreement_check:
            agreement.click()






