from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class QuitSessionPage:
    def __init__(self, driver):
        self.driver = driver
        self.reasons_option_5 = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("I will complete the identification later")')
        self.quit_button = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Quit session")')

    def select_reason_and_quit(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(self.reasons_option_5)
        ).click()
        self.driver.find_element(*self.quit_button).click()

    def is_displayed(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(self.reasons_option_5)).is_displayed()
