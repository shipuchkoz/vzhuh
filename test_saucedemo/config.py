import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from vzhuh.config.action import SeleniumAction
import os


# Функция для получения пути к драйверу
def get_driver_path(browser_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if browser_name.lower() == 'chrome':
        return os.path.join(current_dir, "chromedriver.exe")
    elif browser_name.lower() == 'firefox':
        return os.path.join(current_dir, "geckodriver.exe")
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")


# Фикстура для создания браузера
@pytest.fixture(params=['chrome', 'firefox', 'edge'])
def browser(request):
    browser_name = request.param
    driver_path = get_driver_path(browser_name)

    if browser_name.lower() == 'chrome':
        service = ChromeService(driver_path)
        driver = webdriver.Chrome(service=service)
    elif browser_name.lower() == 'firefox':
        service = FirefoxService(driver_path)
        driver = webdriver.Firefox(service=service)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    yield driver
    driver.quit()



@pytest.fixture
def selenium_action(browser):
    selenium_action = SeleniumAction(browser)
    yield selenium_action