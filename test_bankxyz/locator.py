from selenium.webdriver.common.by import By

"""other"""
locator_button_home = (By.CSS_SELECTOR, 'button.btn.home[ng-click="home()"]')
"""login"""
locator_button_login_customer = (By.CSS_SELECTOR, 'div.center:nth-child(1) > button:nth-child(1)')
locator_button_login_manager = (By.CSS_SELECTOR, 'div.center:nth-child(3) > button:nth-child(1)')
"""customer"""
locator_select_user_name = (By.XPATH, '//*[@id="userSelect"]')
locator_select_hermoine = (By.XPATH, '//*[@id="userSelect"]/option[2]')
locator_select_harry = (By.XPATH, '//*[@id="userSelect"]/option[3]')
locator_select_ron = (By.XPATH, '//*[@id="userSelect"]/option[4]')
locator_select_albus = (By.XPATH, '//*[@id="userSelect"]/option[5]')
locator_select_neville = (By.XPATH, '//*[@id="userSelect"]/option[6]]')
locator_select_login_button = (By.CSS_SELECTOR, 'button.btn:nth-child(2)')
"""account"""
locator_button_transactions = (By.CSS_SELECTOR, 'button.tab[ng-click="transactions()"]')
locator_button_deposit = (By.CSS_SELECTOR, 'button.tab[ng-click="deposit()"]')
locator_button_withdrawal = (By.CSS_SELECTOR, 'button.tab[ng-click="withdrawl()"]')
locator_input_amount = (By.CSS_SELECTOR, 'input.form-control[ng-model="amount"]')
locator_input_deposit = (By.CSS_SELECTOR, 'button.btn.btn-default[value="Deposit"]')
locator_input_withdraw = (By.CSS_SELECTOR, 'button.btn.btn-default[value="Withdraw"]')
locator_select_account_currency = (By.XPATH, '//select[@id="accountSelect"]')
locator_select_account_currency_option_dollar = (By.XPATH, '//option[@label="1004"]')
locator_select_account_currency_option_pound = (By.XPATH, '//option[@label="1005"]')
locator_select_account_currency_option_rupee = (By.XPATH, '//option[@label="1006"]')

locator_error_message = (By.XPATH, '//span[@class="error ng-binding" and @ng-show="message" and not(text())]')
locator_success_message = (By.XPATH, '//span[@class="error ng-binding"]')

locator_assert_td_ng_binding_1 = (By.CSS_SELECTOR, 'td.ng-binding')
locator_assert_td_ng = selenium_action.action_check_element_presence(locator_assert_td_ng_binding_1)
containt_in_assert_td_ng = False
for element in locator_assert_td_ng:
    if "ыы" in element.text:
        containt_in_assert_td_ng = True
        break
assert containt_in_assert_td_ng, "Элемент ЫЫ тосибоси"

locator_assert_td_ng_binding_2 = (By.XPATH, "//td[contains(text(), 'ыы')]")
locator_assert_td_ng = selenium_action.action_check_element_presence(locator_assert_td_ng_binding_2)
assert locator_assert_td_ng is not None, "Элемент не найден"

def assert_check_element_in_elements(self, locator, text):
    elements = self.driver.find_elements(*locator)
    for element in elements:
        if text in element.text:
            return True
    return False

locator_assert_td_ng_binding_1 = (By.CSS_SELECTOR, 'td.ng-binding')
contains_ыы = selenium_action.assert_check_element_in_elements(driver, locator_assert_td_ng_binding_1, "ыы")
print("Строка 'ыы' найдена:", contains_ыы)
assert contains_ыы == True, "Строка найдена"
