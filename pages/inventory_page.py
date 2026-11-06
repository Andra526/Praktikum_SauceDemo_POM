from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class InventoryPage(BasePage):
    # Relative XPath
    PAGE_TITLE = (By.XPATH, "//span[@data-test='title']")
    SORT_DROPDOWN = (By.XPATH, "//select[@data-test='product-sort-container']")
    ITEM_NAMES = (By.XPATH, "//div[@data-test='inventory-item-name']")
    ITEM_PRICES = (By.XPATH, "//div[@data-test='inventory-item-price']")
    ADD_BACKPACK_BUTTON = (By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']")
    REMOVE_BACKPACK_BUTTON = (By.XPATH, "//button[@data-test='remove-sauce-labs-backpack']")
    ADD_BIKE_LIGHT_BUTTON = (By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-bike-light']")
    CART_LINK = (By.XPATH, "//a[@data-test='shopping-cart-link']")
    CART_BADGE = (By.XPATH, "//span[@data-test='shopping-cart-badge']")
    MENU_BUTTON = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    LOGOUT_LINK = (By.XPATH, "//a[@data-test='logout-sidebar-link']")

    def get_title(self):
        return self.get_text(self.PAGE_TITLE)

    def add_backpack(self):
        self.click(self.ADD_BACKPACK_BUTTON)

    def remove_backpack(self):
        self.click(self.REMOVE_BACKPACK_BUTTON)

    def add_bike_light(self):
        self.click(self.ADD_BIKE_LIGHT_BUTTON)

    def get_cart_count(self):
        if not self.driver.find_elements(*self.CART_BADGE):
            return 0
        return int(self.get_text(self.CART_BADGE))

    def open_cart(self):
        self.click(self.CART_LINK)

    def sort_by(self, visible_text):
        Select(self.find(self.SORT_DROPDOWN)).select_by_visible_text(visible_text)

    def get_item_names(self):
        self.find(self.ITEM_NAMES)
        return [e.text for e in self.driver.find_elements(*self.ITEM_NAMES)]

    def get_item_prices(self):
        self.find(self.ITEM_PRICES)
        return [float(e.text.replace("$", "")) for e in self.driver.find_elements(*self.ITEM_PRICES)]

    def logout(self):
        self.click(self.MENU_BUTTON)
        self.click(self.LOGOUT_LINK)
