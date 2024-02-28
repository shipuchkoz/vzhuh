from config.config_saucedemo import *
from test_saucedemo.locator import *
from test_saucedemo.test_data import *

@pytest.fixture
def login(browser, selenium_action): # pytest -k login test_step.py
    def login_function():
        selenium_action.action_fill_input(locator_field_user_name, data_standard_user)
        selenium_action.action_fill_input(locator_field_user_pass, data_password)
        selenium_action.action_click_element(locator_button_login)
    yield login_function

@pytest.fixture
def logout(browser, selenium_action): # pytest -k logout test_step.py
    def logout_function():
        selenium_action.action_click_element(locator_button_menu)
        selenium_action.action_click_element(locator_button_logout)
    yield logout_function

@pytest.fixture
def sort_products(browser, selenium_action): # pytest -k sort_products test_step.py
    def sort_products_function():
        selenium_action.action_click_element(locator_sort)
        selenium_action.action_select_dropdown_option(locator_sort, data_sort_option_low)
    yield sort_products_function

@pytest.fixture
def get_product(browser, selenium_action): # pytest -k get_product test_step.py
    def get_product_function():
        selenium_action.action_click_element(locator_add_cart_product_1)
        selenium_action.action_click_element(locator_add_cart_product_2)
        selenium_action.action_click_element(locator_shopping_cart)
        selenium_action.action_click_element(locator_button_checkout)
        selenium_action.action_fill_input(locator_field_first_name, data_first_name)
        selenium_action.action_fill_input(locator_field_last_name, data_last_name)
        selenium_action.action_fill_input(locator_field_postal_code, data_zip_code)
        selenium_action.action_click_element(locator_button_submit)
        selenium_action.action_click_element(locator_button_finish)
    yield get_product_function
