import pytest
from selenium.webdriver.common.by import By
import time
from pages.base_page import BasePage
from pages.main_page import MainPage


def test_open_steam(browser):
    url = "https://store.steampowered.com/"
    page = MainPage(browser, url)

    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
  