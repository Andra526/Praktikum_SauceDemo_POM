import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1366,768")
    options.add_argument("--disable-notifications")
    # Matikan popup "change password" milik Chrome
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    })
    if os.getenv("HEADLESS", "0") == "1":
        options.add_argument("--headless=new")
    drv = webdriver.Chrome(options=options)
    yield drv
    drv.quit()


@pytest.fixture
def login_page(driver):
    return LoginPage(driver).load()


@pytest.fixture
def inventory_page(driver):
    return InventoryPage(driver)


@pytest.fixture
def cart_page(driver):
    return CartPage(driver)


@pytest.fixture
def checkout_page(driver):
    return CheckoutPage(driver)


@pytest.fixture
def logged_in(login_page):
    """Login sebagai standard_user sebelum test dijalankan."""
    login_page.login("standard_user", "secret_sauce")
    return login_page
