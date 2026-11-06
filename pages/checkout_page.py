from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    # Relative XPath
    PAGE_TITLE = (By.XPATH, "//span[@data-test='title']")
    FIRST_NAME_INPUT = (By.XPATH, "//input[@data-test='firstName']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@data-test='lastName']")
    POSTAL_CODE_INPUT = (By.XPATH, "//input[@data-test='postalCode']")
    CONTINUE_BUTTON = (By.XPATH, "//input[@data-test='continue']")
    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")
    FINISH_BUTTON = (By.XPATH, "//button[@data-test='finish']")
    COMPLETE_HEADER = (By.XPATH, "//h2[@data-test='complete-header']")

    def get_title(self):
        return self.get_text(self.PAGE_TITLE)

    def fill_information(self, first_name, last_name, postal_code):
        self.type(self.FIRST_NAME_INPUT, first_name)
        self.type(self.LAST_NAME_INPUT, last_name)
        self.type(self.POSTAL_CODE_INPUT, postal_code)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def click_finish(self):
        self.click(self.FINISH_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def get_complete_message(self):
        return self.get_text(self.COMPLETE_HEADER)
