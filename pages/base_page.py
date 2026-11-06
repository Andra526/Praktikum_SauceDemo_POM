from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """Kelas induk berisi aksi umum yang dipakai semua Page Object."""

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def is_visible(self, locator):
        try:
            return self.find(locator).is_displayed()
        except Exception:
            return False

    def current_url(self):
        return self.driver.current_url
    #
