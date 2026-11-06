from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    # Relative XPath
    USERNAME_INPUT = (By.XPATH, "//input[@data-test='username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@data-test='password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@data-test='login-button']")
    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")

    def load(self):
        self.open(self.URL)
        return self

    def login(self, username, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
