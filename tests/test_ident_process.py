import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from pages.home_page import HomePage
from pages.terms_conditions_page import TermsConditionsPage
from pages.quit_session_page import QuitSessionPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class IdentProcessTest(unittest.TestCase):

    def setUp(self):
        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.device_name = 'emulator-5554'
        options.app = '/Users/attiaminallah/Documents/IDnow/coding-challenge/app-release-signed-534.apk'
        options.automation_name = 'UiAutomator2'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)
        self.home_page = HomePage(self.driver)
        self.terms_conditions_page = TermsConditionsPage(self.driver)
        self.quit_session_page = QuitSessionPage(self.driver)

    def test_ident_process(self):
        self.assertTrue(self.home_page.is_displayed())
        ident_ids = [
            'TS2-LJGCD', 'TS2-QTTUF', 'TS2-XKPSF', 'TS2-TUHYJ', 'TS2-FGAKW', 
            'TS2-AGJGU', 'TS2-JRSQV', 'TS2-WEKGG', 'TS2-RWQBS', 'TS2-DWUMM'
        ]
        self.home_page.enter_ident_id(ident_ids[0])

        self.assertTrue(self.terms_conditions_page.is_displayed())
        self.terms_conditions_page.close_terms_conditions()

        self.assertTrue(self.quit_session_page.is_displayed())
        self.quit_session_page.select_reason_and_quit()

        intermediate_screen = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, 'checkScreenDocumentHeader'))
        )
        self.assertTrue(intermediate_screen.is_displayed())

        home_screen_logo = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, 'homescreen_idnow_logo'))
        )
        self.assertTrue(home_screen_logo.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
