import pytest
from selenium.webdriver.common.by import By
from android.pages.terms_conditions_page import TermsConditionsPage
from android.pages.quit_session_page import QuitSessionPage

def test_quit_ident_process(driver, home_page, ident_ids):
    #Validate that user is able to see the terms and conditions page to quit the ident process.
    terms_conditions_page = TermsConditionsPage(driver)
    quit_session_page = QuitSessionPage(driver)
    
    assert home_page.is_ident_box_displayed()
    home_page.enter_ident_id(ident_ids[0])
    assert terms_conditions_page.is_displayed()
    terms_conditions_page.close_terms_conditions()
    assert quit_session_page.is_displayed()
    quit_session_page.select_reason_and_quit()
    intermediate_screen = home_page.wait_for_element(By.ID, 'checkScreenDocumentHeader')
    assert intermediate_screen.is_displayed()
    home_screen_logo = home_page.wait_for_element(By.ID, 'homescreen_idnow_logo')
    assert home_screen_logo.is_displayed()
