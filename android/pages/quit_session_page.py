from selenium.webdriver.common.by import By
from android.pages.base_page import BasePage

class QuitSessionPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.reasons_option_5 = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("I will complete the identification later")')
        self.quit_button = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Quit session")')

    def select_reason_and_quit(self):
        self.wait_for_element(*self.reasons_option_5).click()
        self.driver.find_element(*self.quit_button).click()

    def is_displayed(self):
        return self.wait_for_element(*self.reasons_option_5).is_displayed()
