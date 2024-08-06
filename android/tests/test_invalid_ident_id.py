# import pytest
from selenium.webdriver.common.by import By

def test_invalid_ident_ID(driver, home_page):
    # Validate that entering and invalid intendID shows an error
    assert home_page.is_ident_field_displayed()
    home_page.enter_ident_id('TS2-XXXX')
    error_message = home_page.wait_for_element(By.ID, 'android:id/message')
    assert error_message.is_displayed()
    ok_button = driver.find_element(By.ID, 'android:id/button1')
    assert ok_button.is_displayed()
    ok_button.click()
