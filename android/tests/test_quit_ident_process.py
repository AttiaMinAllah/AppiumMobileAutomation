import pytest
import json
from android.pages.home_page import HomePage
from android.pages.terms_conditions_page import TermsConditionsPage
from android.pages.quit_session_page import QuitSessionPage

def load_test_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

test_data = load_test_data('common/test_data.json')

@pytest.mark.usefixtures("driver")
class TestIdentProcess:

    def test_ident_process(self, driver):
        home_page = HomePage(driver)
        terms_conditions_page = TermsConditionsPage(driver)
        quit_session_page = QuitSessionPage(driver)

        # Validate that the home screen is displayed with an edit box for ident id and a button labeled 'start ident'
        assert home_page.is_ident_field_displayed()

        # Enter any one of the given ident IDs in the text box and click the 'start ident' button
        ident_ids = test_data['ident_ids']
        home_page.enter_ident_id(ident_ids[0])

        # Validate that the terms and conditions screen is displayed
        assert terms_conditions_page.is_terms_conditions_displayed()

        # Click on the close icon on the top left corner
        terms_conditions_page.close_terms_conditions()

        # Validate that the options with the reasons are displayed
        assert quit_session_page.are_reasons_displayed()

        # Choose the last option and click 'Quit session'
        quit_session_page.select_reason_and_quit('option_5')

        # Validate that there is an intermediate screen displayed before the app redirects to the home screen
        assert quit_session_page.is_intermediate_screen_displayed()

        # Optionally wait and validate redirection back to the home screen
        assert quit_session_page.is_home_screen_logo_displayed()
