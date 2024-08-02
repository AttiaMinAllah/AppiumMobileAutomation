import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from pages.home_page import HomePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class InvalidIdentTest(unittest.TestCase):

    def setUp(self):
        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.device_name = 'emulator-5554'
        options.app = '/Users/attiaminallah/Documents/IDnow/coding-challenge/app-release-signed-534.apk'
        options.automation_name = 'UiAutomator2'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)
        self.home_page = HomePage(self.driver)

    def test_invalid_ident(self):
        self.assertTrue(self.home_page.is_displayed())
        invalid_ident_id = 'TS2-XXXX'
        self.home_page.enter_ident_id(invalid_ident_id)

        error_message = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, 'android:id/message'))
        )
        self.assertTrue(error_message.is_displayed())
        ok_button = self.driver.find_element(By.ID, 'android:id/button1')
        self.assertTrue(ok_button.is_displayed())
        ok_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
