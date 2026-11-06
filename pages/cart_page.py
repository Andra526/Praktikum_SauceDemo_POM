from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    # Relative XPath
    PAGE_TITLE = (By.XPATH, "//span[@data-test='title']")
    CART_ITEM_NAMES = (By.XPATH, "//div[@data-test='inventory-item-name']")
    CHECKOUT_BUTTON = (By.XPATH, "//button[@data-test='checkout']")

    def get_title(self):
        return self.get_text(self.PAGE_TITLE)

    def get_item_names(self):
        self.find(self.PAGE_TITLE)
        return [e.text for e in self.driver.find_elements(*self.CART_ITEM_NAMES)]

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
