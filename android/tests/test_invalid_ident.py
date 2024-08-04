import pytest
from selenium.webdriver.common.by import By

def test_invalid_ident(driver, home_page):
    # Validate that the home screen is displayed with an edit box for ident id and a button labeled 'start ident'
    assert home_page.is_ident_box_displayed()

    # Enter an invalid ident ID in the text box and click the 'start ident' button
    home_page.enter_ident_id('TS2-XXXX')

    # Validate that the error message is displayed
    error_message = home_page.wait_for_element(By.ID, 'android:id/message')
    assert error_message.is_displayed()
    ok_button = driver.find_element(By.ID, 'android:id/button1')
    assert ok_button.is_displayed()
    ok_button.click()
