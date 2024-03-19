import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from vzhuh.config.action import SeleniumAction
import os


def pytest_add_option(parser):
    parser.add_option("--browser", action="store", default="chrome", help="Browser to run tests in (chrome, firefox, edge)")


@pytest.fixture(scope='session')
def browser(request):
    browser_name = request.config.getoption("--browser")
    current_dir = os.path.dirname(os.path.abspath(__file__))

    if browser_name == "chrome":
        chrome_path = os.path.join(current_dir, "chrome.exe")
        service = ChromeService(chrome_path)
        driver = webdriver.Chrome(service=service)
    elif browser_name == "firefox":
        gecko_path = os.path.join(current_dir, "geckodriver.exe")
        service = FirefoxService(gecko_path)
        driver = webdriver.Firefox(service=service)
    elif browser_name == "edge":
        edge_path = os.path.join(current_dir, "msedgedriver.exe")
        service = EdgeService(edge_path)
        driver = webdriver.Edge(service=service)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    yield driver
    driver.quit()


@pytest.fixture
def selenium_action(browser):
    selenium_action = SeleniumAction(browser)
    yield selenium_action