import os

import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from utils import attach

env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")

if not os.path.exists(env_path):
    raise FileNotFoundError(f"Файл .env не найден по пути: {env_path}")

load_dotenv(env_path)

DEFAULT_BROWSER_VERSION = "126.0"


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default=DEFAULT_BROWSER_VERSION,
    )
    parser.addoption(
        '--browser_type',
        default='chrome',
    )


@pytest.fixture(scope="session", autouse=True)
def load_env():
    """Фикстура для загрузки переменных окружения"""
    load_dotenv(env_path)


@pytest.fixture(scope='function', autouse=True)
def open_browser(request):
    """Фикстура для открытия браузера перед тестом"""
    browser_version = request.config.getoption('browser_version') or DEFAULT_BROWSER_VERSION
    browser_type = request.config.getoption('browser_type')

    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    if not selenoid_login or not selenoid_pass or not selenoid_url:
        raise ValueError("Переменные окружения SELENOID_LOGIN, SELENOID_PASS или SELENOID_URL не заданы!")

    if browser_type == 'chrome':
        options = ChromeOptions()
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": browser_version,
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }
        options.capabilities.update(selenoid_capabilities)
    elif browser_type == 'firefox':
        options = FirefoxOptions()
        options.set_capability("browserName", "firefox")
        options.set_capability("browserVersion", browser_version)
        options.set_capability("selenoid:options", {
            "enableVNC": True,
            "enableVideo": True
        })
    else:
        raise ValueError(f"Unsupported browser type: {browser_type}")

    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options,
        keep_alive=True
    )

    browser.config.driver = driver

    browser.config.window_width = 1280
    browser.config.window_height = 724
    browser.config.base_url = 'https://demoqa.com'

    yield browser

    if browser_type == 'chrome':
        attach.add_logs(browser)

    attach.add_screenshot(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()