import pytest
from selenium.webdriver.common.by import By
import time
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage

url = "https://store.steampowered.com/"

def test_open_steam_profile(browser):
    # 1. Главная страница
    main_page = MainPage(browser, url)
    main_page.open()
    main_page.should_be_login_link()
    #main_page.go_to_login_page()

    login_page = main_page.go_to_login_page()
    login_page.should_be_login_page()
    login_page.login_to_profile()


# @pytest.mark.parametrize("email_field, reenter, captcha, agreement_check", [
#     ("test@example.com", "test@example.com", True, True),
#     ("test_user@gmail.com", "test_user@gmail.com", True, True), 
#     ("test_user@gmail.com", "new_user@gmail.com", False, False), 
#     ("test_user@gmail.com", "", True, True),
#     ("test_user@@gmail.com", "test_user@@gmail.com", False, False),
#     (".testuser@gmail.com", ".newuser@gmail.com", True, True),
#     ("test_user@gmailcom", "", False, False),
#     ("", "test_user@gmail.com", True, False),
#     ("", "", False, True)
# ])

@pytest.mark.parametrize("email_field, reenter, agreement_check", [
    ("test@example.com", "test@example.com", True),
    ("test_user@gmail.com", "test_user@gmail.com", True), 
    ("test_user@gmail.com", "new_user@gmail.com", False), 
    ("test_user@gmail.com", "", True),
    ("test_user@@gmail.com", "test_user@@gmail.com", False),
    (".testuser@gmail.com", ".newuser@gmail.com", True),
    ("test_user@gmailcom", "", False),
    ("", "test_user@gmail.com", False),
    ("", "", True)
])
def test_registration_form(browser, email_field, reenter, agreement_check):
    main_page = MainPage(browser, url)
    main_page.open()
    main_page.should_be_login_link()

    login_page = main_page.go_to_login_page()
    login_page.should_be_login_page()

    register_page = login_page.go_to_register_page()
    register_page.should_be_register_page()
    register_page.fill_the_register_form(email_field, reenter, agreement_check)




