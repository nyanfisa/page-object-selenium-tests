import pytest
from selenium.webdriver.common.by import By
import time
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage

url = "https://store.steampowered.com/"

def test_open_steam_profile(browser):
    main_page = MainPage(browser, url)
    main_page.open()
    main_page.should_be_login_link()

    login_page = main_page.go_to_login_page()
    login_page.should_be_login_page()
    login_page.login_to_profile()

@pytest.mark.parametrize("email_field, reenter, agreement_check, expected_result", [
    pytest.param(
        "test_user@gmail.com", "test_user@gmail.com", True, "success",
        marks=pytest.mark.xfail(reason="Steam требует капчу — успешная регистрация не автоматизируется")
    ),
    ("test_user@gmail.com", "new_user@gmail.com", False, "error"), 
    ("test_user@gmail.com", "", True, "error"),
    ("test_user@@gmail.com", "test_user@@gmail.com", False, "error"),
    (".testuser@gmail.com", ".newuser@gmail.com", True, "error"),
    ("test_user@gmailcom", "", False, "error"),
    ("", "test_user@gmail.com", False, "error"),
    ("", "", True, "error")
])


def test_registration_form(browser, email_field, reenter, agreement_check, expected_result):
    main_page = MainPage(browser, url)
    main_page.open()
    main_page.should_be_login_link()

    login_page = main_page.go_to_login_page()
    login_page.should_be_login_page()

    register_page = login_page.go_to_register_page()
    register_page.should_be_register_page()
    register_page.fill_the_register_form(email_field, reenter, agreement_check)

    if expected_result == "success":
        assert not register_page.is_error_visible(), "Registration form error appeared, but was not expected"
    else:
        assert register_page.is_error_visible(), "Registration form error did not appear"    




