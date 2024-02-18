    wait = WebDriverWait(browser, 10) # ожидание 1 секунда
    element = wait.until(EC.visibility_of_element_located((By.XPATH, 'xpath'))) # ожидание видимости XPATH
    driver.quit() # закрытие окон после тестов

    def fin():
        driver.quit()
    request.addfinalizer(fin)
    return driver

def logout(browser):
    """Выход"""
    selenium_helper = SeleniumAction(browser)
    selenium_helper.action_click_element(logout_but)

def test_logout_successful(browser, login):
    """Проверка выхода"""
    logout(browser)
    assert "https://www.saucedemo.com/" in browser.current_url.lower()

@pytest.fixture(autouse=True)
def setup(browser, selenium_action, login, logout, sort_products, get_product):
    pass

def test_open_in_new_tab(self, browser):
    # Открываем новую вкладку
    browser.execute_script("window.open('');")
    # Переключаемся на новую вкладку
    browser.switch_to.window(browser.window_handles[1])
    # Проверяем, что новая вкладка открыта
    assert len(browser.window_handles) == 2
    print("Открыли новую вкладку")

"""РАБОТЫ С ФИКСТУРАМИ"""

@pytest.fixture(scope="module") # область видимости фикстуры,
def setup_module_fixture():
    print("\n--- Setup Module Fixture ---")
    yield
    print("\n--- Teardown Module Fixture ---")
    # "function" фикстура будет создана один раз для каждой тестовой функции (по умолчанию)
    # "class" фикстура будет создана один раз для каждого класса тестов
    # "module" фикстура будет создана один раз для каждого модуля тестов
    # "session" фикстура будет создана один раз для всей сессии тестирования

@pytest.fixture(params=[1, 2, 3]) # позволяет задать набор параметров, которые будут переданы в тестовую функцию
def param_fixture(request):
    param_value = request.param
    print(f"\n--- Setup Param Fixture with param value: {param_value} ---")
    yield param_value
    print("\n--- Teardown Param Fixture ---")

@pytest.fixture(autouse=True) # указывает, будет ли фикстура вызвана автоматически или только при явном запросе в тесте
def autouse_fixture():
    print("\n--- Setup Autouse Fixture ---")
    yield
    print("\n--- Teardown Autouse Fixture ---")

@pytest.fixture(ids=["test_case_1", "test_case_2", "test_case_3"]) # устанавливает пользовательские идентификаторы для фикстуры, которые будут отображаться в отчете о тестировании
def id_fixture():
    print("\n--- Setup ID Fixture ---")
    yield
    print("\n--- Teardown ID Fixture ---")

def test_example(setup_module_fixture, param_fixture, id_fixture):
    print("\n--- Running Test Example ---")
    assert True

@pytest.fixture(name="name_fixture") # устанавливает имя для фикстуры, которое будет отображаться в отчете о тестировании
def name_fixture():
    print("\n--- Name Fixture ---")

"""ПЕРЕХОДЫ ПО ДИРЕКТОРИЯМ"""

import os
# Получаем путь к текущему скрипту
current_script_path = os.path.abspath(__file__)
# Преобразуем относительный путь в абсолютный
absolute_path = os.path.realpath(current_script_path)
# Получаем родительский каталог
parent_directory = os.path.dirname(absolute_path)

from pathlib import Path
current_dir = Path(__file__).resolve().parent
project_root = current_dir.parent.parent
file_path = project_root / "folder" / "file.exe"
# __file__ - магическая переменная содержит путь к текущему исполняемому файлу(скрипту)
# Path(__file__) - создает объект Path из пути,gолученного из __file__
# resolve() - преобразует путь к абсолютному виду, разрешая все символические ссылки и относительные пути.
# parent - возвращает родительский каталог указанного пути