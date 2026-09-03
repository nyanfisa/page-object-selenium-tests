import pytest
from selenium.webdriver.common.by import By
import time
from .pages.base_page import BasePage


def test_open_steam(browser):
    url = "https://store.steampowered.com/"
    base_page = BasePage(browser, url)
    base_page.open()
  
    assert "Steam" in browser.title