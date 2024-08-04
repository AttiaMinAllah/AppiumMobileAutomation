from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        # Initializes the BasePage with the WebDriver instance
        self.driver = driver

    def wait_for_element(self, by, value, timeout=30):
        # Waits for an element to be present in the DOM and visible on the page.
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def is_displayed(self, by, value, timeout=30):
        #Checks if an element is displayed on the page.
        return self.wait_for_element(by, value, timeout).is_displayed()
