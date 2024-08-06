#IDnowMobileAutomation

## Framework Overview

The IDNow Mobile Automation framework is designed to automate the testing of IDNow's mobile applications on both Android and iOS platforms. It uses the Appium framework to interact with mobile devices and runs test cases written in Python using the pytest framework. The framework is structured to promote maintainability and scalability, with clear separation between different components.

### Key Components

1. **Page Object Model (POM)**: 
   - The framework follows the Page Object Model design pattern. This pattern helps in maintaining the test code by separating the UI elements and interactions from the test scripts.
   - Each screen of the mobile application is represented as a class in the `pages` directory. For example, `home_page.py` represents the home page of the application.

2. **Test Cases**:
   - Test cases are written in Python and are located in the `tests` directory. These test cases use the page objects to interact with the application and verify its behavior.
   - Example test cases include `test_invalid_ident_id.py` and `test_quit_ident_process.py` for Android, and `test_invalid_ident_id_error.py` for iOS.

3. **Configuration and Fixtures**:
   - The `conftest.py` file is used to configure the pytest framework and define common fixtures that are used across test cases.
   - Fixtures include setting up the Appium driver, loading test data, and initializing page objects.

4. **Platform-Specific Setup**:
   - The framework supports running tests on both Android and iOS platforms. The platform to be tested can be specified using command-line options.
   - Different capabilities and settings are defined for Android and iOS in the `driver` fixture within `conftest.py`.

5. **Environment Variables**:
   - Environment-specific variables, such as BrowserStack credentials, are stored in a `.env` file to keep them separate from the codebase.

## Getting Started

### Prerequisites

To see the output of the project tests, you need to have the following on your local machine:

- Python 3.8+
- pip
- Virtual environment tool (e.g., `virtualenv`, `venv`)
- Java Development Kit (JDK)
- Node.js and npm
- Appium
- Android SDK
- iOS environment (for Mac users): Xcode and related tools
- BrowserStack credentials (if using BrowserStack for iOS testing)

### Setup Instructions

1. **Install Java Development Kit (JDK)**

    - Download and install the JDK from the (https://www.oracle.com/java/technologies/javase-jdk11-downloads.html).
    - Ensure `JAVA_HOME` environment variable is set and added to the system's PATH.

2. **Install Node.js and npm**

    - Download and install Node.js from the (https://nodejs.org/).

3. **Install Appium**

    ```bash
    npm install -g appium
    ```

4. **Install Android SDK**

    - Download and install Android Studio from the (https://developer.android.com/studio).
    - Ensure `ANDROID_HOME` environment variable is set and added to the system's PATH.
    - Install necessary SDK packages and create an Android virtual device (AVD).

5. **iOS Setup (Mac users)**

    - Install Xcode from the (https://apps.apple.com/us/app/xcode/id497799835).
    - Ensure command line tools are installed:

      ```bash
      xcode-select --install
      ```

    - Create an iOS simulator via Xcode.

6. **Install Python Dependencies**

    - Clone the repository and navigate to the project directory:

      ```bash
      git clone https://github.com/yourusername/IDNowMobileAutomation.git
      cd IDNowMobileAutomation
      ```

    - Set up a virtual environment:

      ```bash
      python -m venv venv
      ```

    - Install the required Python packages:

      ```bash
      pip install -r requirements.txt
      ```

7. **Running the Appium Server**

    - Start the Appium server:

      ```bash
      appium
      ```

## BrowserStack Configuration

For BrowserStack to run tests on iOS devices, ensure you have the following setup:

1. **BrowserStack Account**: Signin with your account (https://www.browserstack.com/).

2. **Set BrowserStack Credentials**:
    - I added the browserstack credentials directly in the conftest file because those credentials are expired now 
    - But Ideally we should add them in .env file and use as export 

3. **iOS App Setup on BrowserStack**:
    - Upload your iOS app to BrowserStack and get the app URL (e.g., `bs://<app-hash>`).
    - Update the `conftest.py` file to include this URL in the iOS capabilities.

## Running Tests

To run the tests, use the following command:

```bash
pytest --platform= android
