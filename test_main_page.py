import pytest
from selenium.webdriver.common.by import By
import time
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


def test_open_steam(browser):
    url = "https://store.steampowered.com/"
    
    # 1. Главная страница
    main_page = MainPage(browser, url)
    main_page.open()
    main_page.should_be_login_link()
    main_page.go_to_login_page()

    # 2. Страница логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    login_page.go_to_register_page()
    
    # 3. Страница регистрации
    register_page = RegisterPage(browser, browser.current_url)
    register_page.should_be_register_page()

  