import pytest
import json
import os
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from common.utils import wait_for_element  # Update import path
from pages.home_page import HomePage

# Load test data from JSON file
test_data_path = os.path.join(os.path.dirname(__file__), '../common/test_data.json')
with open(test_data_path) as f:
    test_data = json.load(f)

@pytest.fixture(scope="module")
def driver():
    options = UiAutomator2Options()
    options.platform_name = 'Android'
    options.device_name = 'emulator-5554'
    options.app = '/Users/attiaminallah/Documents/IDnow/coding-challenge/app-release-signed-534.apk'
    options.automation_name = 'UiAutomator2'

    driver = webdriver.Remote('http://localhost:4723', options=options)
    yield driver
    driver.quit()

def test_ident_process(driver):
    home_page = HomePage(driver)

    # Validate that the home screen is displayed with an edit box for ident id and a button labeled 'start ident'
    assert home_page.is_displayed()

    # Enter any one of the given ident IDs in the text box and click the 'start ident' button
    ident_ids = test_data["ident_ids"]
    home_page.enter_ident_id(ident_ids[0])

    # Validate that the terms and conditions screen is displayed
    terms_conditions = wait_for_element(driver, By.ID, 'privacy_item_body_checkbox')
    assert terms_conditions.is_displayed()

    # Click on the close icon on the top left corner
    close_icon = driver.find_element(By.ID, 'btn_close')
    close_icon.click()

    # Validate that the options with the reasons are displayed
    reasons_option_1 = wait_for_element(driver, By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("I don’t have my document with me")')
    reasons_option_2 = driver.find_element(By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("I have privacy concerns")')
    reasons_option_3 = driver.find_element(By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("The app is not responding and I cannot go further")')
    reasons_option_4 = driver.find_element(By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Not interested in the service for which this identification is required")')
    reasons_option_5 = driver.find_element(By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("I will complete the identification later")')

    assert reasons_option_1.is_displayed()
    assert reasons_option_2.is_displayed()
    assert reasons_option_3.is_displayed()
    assert reasons_option_4.is_displayed()
    assert reasons_option_5.is_displayed()

    # Choose the last option and click 'Quit session'
    reasons_option_5.click()
    quit_button = driver.find_element(By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Quit session")')
    quit_button.click()

    # Validate that there is an intermediate screen displayed before the app redirects to the home screen
    intermediate_screen = wait_for_element(driver, By.ID, 'checkScreenDocumentHeader')
    assert intermediate_screen.is_displayed()

    # Wait and validate redirection back to the home screen
    home_screen_logo = wait_for_element(driver, By.ID, 'homescreen_idnow_logo')
    assert home_screen_logo.is_displayed()
