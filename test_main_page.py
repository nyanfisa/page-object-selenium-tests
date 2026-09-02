import pytest
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
import time
from .pages.base_page import BasePage

# link = "https://store.steampowered.com/"

# def test_guest_can_go_to_login_page(browser):
#     browser.get(link)
#     go_to_login_page(browser)

# def go_to_login_page(browser):
#     login_link = browser.find_element(By.CSS_SELECTOR, '#global_action_menu > a.global_action_link')
#     login_link.click()

def test_open_steam(browser):
    url = "https://store.steampowered.com/"
    base_page = BasePage(browser, url)
    base_page.open()
    # Здесь можно добавить проверку
    assert "Steam" in browser.title