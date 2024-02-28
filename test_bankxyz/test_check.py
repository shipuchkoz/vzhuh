from test_bankxyz.test_step import *

# pytest test_check_pytest.py \ pytest -m smoke test_check_pytest.py

@pytest.mark.smoke_bank # pytest -k test_login_successful test_check_pytest.py
def test_login_successful_bank_harry(browser, selenium_action, login_bank_customer, login_bank_customer_harry):
    """Проверка входа"""
    login_bank_customer()
    login_bank_customer_harry()
    selenium_action.action_wait_on_page(1000)
    assert "https://www.globalsqa.com/angularjs-protractor/bankingproject/#/account" in browser.current_url.lower()
    print('Вход успешный')
#    selenium_action.action_close_current_window()

@pytest.mark.smoke_bank # pytest -k test_login_successful test_check_pytest.py
def test_login_successful_bank_hermoine(browser, selenium_action, login_bank_customer, login_bank_customer_hermoine):
    """Проверка входа"""
    login_bank_customer()
    login_bank_customer_hermoine()
    selenium_action.action_wait_on_page(1000)

    sucesfule_text = selenium_action.action_get_text(locator)
    assert sucesfule_text == "Deposit Successful"

    assert "https://www.globalsqa.com/angularjs-protractor/bankingproject/#/account" in browser.current_url.lower()
    print('Вход успешный')
#    selenium_action.action_close_current_window()


