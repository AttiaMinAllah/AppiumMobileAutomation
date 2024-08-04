# android/tests/conftest.py
import sys
import os
import pytest
import json
from appium import webdriver
from appium.options.android import UiAutomator2Options

print("sys.path:", sys.path)  # For debugging

def pytest_addoption(parser):
    # Add custom command line option for platform
    parser.addoption(
        "--platform", action="store", default="android", help="platform to run tests on: android or ios"
    )

@pytest.fixture(scope="module")
def ident_ids():
    # Load test data from JSON file
    test_data_path = os.path.join(os.path.dirname(__file__), '../../common', 'test_data.json')
    with open(test_data_path) as f:
        test_data = json.load(f)
    return test_data["ident_ids"]

@pytest.fixture(scope="module")
def driver(pytestconfig):
    # Initialize the WebDriver based on the platform option
    platform = pytestconfig.getoption("platform")
    print(f"Running tests on platform: {platform}")  # Debugging platform option

    if platform == 'android':
        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.device_name = 'emulator-5554'
        options.app = '/Users/attiaminallah/Documents/IDnowMobileAutomation/app-release-signed-534.apk'
        options.automation_name = 'UiAutomator2'

        driver = webdriver.Remote('http://localhost:4723', options=options)
    elif platform == 'ios':
        # Add your iOS WebDriver options here when needed
        pass
    else:
        raise ValueError("Unsupported platform: {}".format(platform))

    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def home_page(driver):
    # Initialize HomePage with the WebDriver
    from android.pages.home_page import HomePage
    return HomePage(driver)
