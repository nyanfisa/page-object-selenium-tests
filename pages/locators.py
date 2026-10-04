from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#global_action_menu > a.global_action_link")

class LoginPageLocators():
    REGISTER_BUTTON = (By.CSS_SELECTOR, "a.login_create_btn")
    USERNAME_FIELD = (By.XPATH, "//section//form//input[@type='text']")
    PASSWORD_FIELD = (By.XPATH, "//section//form//input[@type='password']")
    SUBMIT_BUTTON = (By.XPATH, "//section//form//button[@type='submit']")

class RegisterPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "div.join_form") 
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='email']")
    REENTER_EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='reenter_email']")
    COUNTRY_DROPDOWN = (By.CSS_SELECTOR, "select[name='country']")
    COUNTRY_CHOICE = (By.CSS_SELECTOR, "[value='RU']")
    CAPTCHA_IFRAME = (By.CSS_SELECTOR, "iframe[src*='captcha']")
    #CAPTCHA_ENTRY_CHECK = (By.CSS_SELECTOR, "div#captcha_entry > div#checkbox")
    AGREEMENT_CHECKBOX = (By.ID, "i_agree_check")
    CREATE_ACCOUNT_BUTTON = (By.ID, "createAccountButton")   

class ProfilePageLocators():
    ACC_PULLDOWN_BUTTON = (By.ID, "account_pulldown") 
    ACCOUNT_NAME = (By.XPATH, '//div[@id="account_dropdown"]//a[href="https://store.steampowered.com/account/"]/span') 

    