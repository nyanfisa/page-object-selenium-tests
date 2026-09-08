from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#global_action_menu > a.global_action_link")

class LoginPageLocators():
    REGISTER_BUTTON = (By.CSS_SELECTOR, "a.login_create_btn")

class RegisterPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "div.join_form") 
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='email']")
    REENTER_EMIAIL_FIELD = (By.CSS_SELECTOR, "input[name='reenter_email']")
    COUNTRY_DROPDOWN = (By.CSS_SELECTOR, "select[name='country']")
    IFRAME = (By.CSS_SELECTOR, "iframe[src*='captcha']")
    CAPTCHA_ENTRY_CHECK = (By.CSS_SELECTOR, "div#captcha_entry > div#checkbox")
    CREATE_ACCOUNT_BUTTON = (By.ID, "createAccountButton")   
    