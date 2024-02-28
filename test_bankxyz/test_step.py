from config.setting_bank import *
from test_bankxyz.locator import *
from test_bankxyz.data import *

@pytest.fixture
def login_bank_customer(browser, selenium_action): # pytest -k login test_step.py
    def login_bank_customer_function():
        selenium_action.action_click_element(locator_button_login_customer)
    yield login_bank_customer_function

@pytest.fixture
def login_bank_customer_harry(browser, selenium_action): # pytest -k login test_step.py
    def login_bank_customer_harry_function():
        selenium_action.action_click_element(locator_select_harry)
        selenium_action.action_wait_on_page(1000)
        selenium_action.action_click_element(locator_select_login_button)
    yield login_bank_customer_harry_function

@pytest.fixture
def login_bank_customer_hermoine(browser, selenium_action): # pytest -k login test_step.py
    def login_bank_customer_hermoine_function():
        selenium_action.action_click_element(locator_select_hermoine)
        selenium_action.action_wait_on_page(1000)
        selenium_action.action_click_element(locator_select_login_button)
    yield login_bank_customer_hermoine_function