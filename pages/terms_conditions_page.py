from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TermsConditionsPage:
    def __init__(self, driver):
        self.driver = driver
        self.terms_conditions = (By.ID, 'privacy_item_body_checkbox')
        self.close_icon = (By.ID, 'btn_close')

    def close_terms_conditions(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(self.close_icon)
        ).click()

    def is_displayed(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(self.terms_conditions)
        ).is_displayed()
