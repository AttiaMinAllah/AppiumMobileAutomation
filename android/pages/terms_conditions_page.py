from selenium.webdriver.common.by import By
from common.base_page import BasePage

class TermsConditionsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.terms_conditions = (By.ID, 'privacy_item_body_checkbox')
        self.close_icon = (By.ID, 'btn_close')

    def close_terms_conditions(self):
        self.wait_for_element(*self.close_icon).click()

    def is_displayed(self):
        return self.wait_for_element(*self.terms_conditions).is_displayed()
