import pytest
from selenium.webdriver.common.by import By
from android.pages.terms_conditions_page import TermsConditionsPage
from android.pages.quit_session_page import QuitSessionPage

def test_ident_process(driver, home_page, ident_ids):
    terms_conditions_page = TermsConditionsPage(driver)
    quit_session_page = QuitSessionPage(driver)
    
    # Validate that the home screen is displayed with an edit box for ident id and a button labeled 'start ident'
    assert home_page.is_ident_box_displayed()
    
    # Enter any one of the given ident IDs in the text box and click the 'start ident' button
    home_page.enter_ident_id(ident_ids[0])
    
    # Validate that the terms and conditions screen is displayed
    assert terms_conditions_page.is_displayed()
    terms_conditions_page.close_terms_conditions()
    
    # Validate that the options with the reasons are displayed
    assert quit_session_page.is_displayed()
    quit_session_page.select_reason_and_quit()
    
    # Validate that there is an intermediate screen displayed before the app redirects to the home screen
    intermediate_screen = home_page.wait_for_element(By.ID, 'checkScreenDocumentHeader')
    assert intermediate_screen.is_displayed()
    
    # Wait and validate redirection back to the home screen
    home_screen_logo = home_page.wait_for_element(By.ID, 'homescreen_idnow_logo')
    assert home_screen_logo.is_displayed()
