from test_saucedemo.test_step import *

# pytest test_check_pytest.py \ pytest -m smoke test_check_pytest.py \ pytest --markers smoke_market

@pytest.mark.smoke_market # pytest -k test_login_successful test_check_pytest.py
def test_login_successful(browser, selenium_action, login, logout):
    """Проверка входа"""
    login()
    selenium_action.action_wait_on_page(1000)
    assert "https://www.saucedemo.com/inventory.html" in browser.current_url.lower()
    print('Вход успешный')
    logout()
    selenium_action.action_close_current_window()

@pytest.mark.smoke_market # pytest -k test_logout_successful test_check_pytest.py
def test_logout_successful(browser, selenium_action, login, logout):
    """Проверка выхода"""
    login()
    logout()
    selenium_action.action_wait_on_page(1000)
    assert "https://www.saucedemo.com/" in browser.current_url.lower()
    print('Выход успешный')
    selenium_action.action_close_current_window()

@pytest.mark.smoke_market # pytest -k test_sort_products_successful test_check_pytest.py
def test_sort_products_successful(browser, selenium_action, login, logout, sort_products):
    """Проверка сортировки"""
    login()
    sort_products()
    first_product_id = selenium_action.action_get_attribute(locator_sort_first_prod, "id")
    selenium_action.action_wait_on_page(1000)
    assert first_product_id == "item_2_img_link"
    print('Сортировка успешна')
    logout()
    selenium_action.action_close_current_window()

@pytest.mark.smoke_market # pytest -k test_get_product_successful test_check_pytest.py
def test_get_product_successful(browser, selenium_action, login, logout, get_product):
    """Проверка покупки"""
    login()
    get_product()
    selenium_action.action_wait_on_page(1000)
    assert "https://www.saucedemo.com/checkout-complete.html" in browser.current_url.lower()
    print('Покупка успешна')
    logout()
    selenium_action.action_close_current_window()