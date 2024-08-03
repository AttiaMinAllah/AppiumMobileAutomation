import pytest
import json
import os
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from common.utils import wait_for_element  # Update import path

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

def test_invalid_ident(driver):
    # Validate that the home screen is displayed with an edit box for ident id and a button labeled 'start ident'
    ident_box = wait_for_element(driver, By.ID, 'editTextCode')
    start_button = driver.find_element(By.ID, 'start_ident')
    assert ident_box.is_displayed()
    assert start_button.is_displayed()

    # Enter an invalid ident ID in the text box and click the 'start ident' button
    invalid_ident_id = 'TS2-XXXX'
    ident_box.send_keys(invalid_ident_id)
    start_button.click()

    # Validate that the error message is displayed
    error_message = wait_for_element(driver, By.ID, 'android:id/message')
    assert error_message.is_displayed()
    ok_button = driver.find_element(By.ID, 'android:id/button1')
    assert ok_button.is_displayed()
    ok_button.click()
