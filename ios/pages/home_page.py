from selenium.webdriver.common.by import By
from common.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.ident_box = (By.ID, 'ios_ident_box_id')  # Update this with actual iOS locator
        self.start_button = (By.ID, 'ios_start_button_id')  # Update this with actual iOS locator

    def enter_ident_id(self, ident_id):
        self.wait_for_element(*self.ident_box).send_keys(ident_id)
        self.driver.find_element(*self.start_button).click()

    def is_ident_box_displayed(self):
        return self.wait_for_element(*self.ident_box).is_displayed()
