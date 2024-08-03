from selenium.webdriver.common.by import By
from common.utils import wait_for_element  # Update import path

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.ident_box = (By.ID, 'editTextCode')
        self.start_button = (By.ID, 'start_ident')

    def enter_ident_id(self, ident_id):
        wait_for_element(self.driver, *self.ident_box).send_keys(ident_id)
        self.driver.find_element(*self.start_button).click()

    def is_displayed(self):
        return wait_for_element(self.driver, *self.ident_box).is_displayed()
