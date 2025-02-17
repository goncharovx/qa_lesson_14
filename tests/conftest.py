import os

import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

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
        help='Версия браузера для удалённого запуска (Selenoid)'
    )
    parser.addoption(
        '--browser_type',
        default='chrome',
        help='Тип браузера: chrome или firefox'
    )
    parser.addoption(
        '--remote',
        action='store_true',
        help='Запускать ли тесты в Selenoid (по умолчанию False - локально)'
    )


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv(env_path)


@pytest.fixture(scope='function', autouse=True)
def open_browser(request):
    """Фикстура для открытия браузера перед тестом (локально/Selenoid)"""
    browser_version = request.config.getoption('browser_version') or DEFAULT_BROWSER_VERSION
    browser_type = request.config.getoption('browser_type')
    remote = request.config.getoption('remote')

    if remote:
        """
        --- Запуск в Selenoid ---
        """
        selenoid_login = os.getenv("SELENOID_LOGIN")
        selenoid_pass = os.getenv("SELENOID_PASS")
        selenoid_url = os.getenv("SELENOID_URL")

        if not selenoid_login or not selenoid_pass or not selenoid_url:
            raise ValueError(
                "Переменные окружения SELENOID_LOGIN, SELENOID_PASS или SELENOID_URL не заданы!"
            )

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

    else:
        """
        --- Локальный запуск ---
        """
        if browser_type == 'chrome':
            options = ChromeOptions()
            # Можно добавить headless-режим, если нужно:
            # options.add_argument("--headless")

            driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=options
            )
            driver.maximize_window()

        elif browser_type == 'firefox':
            options = FirefoxOptions()
            # options.add_argument("--headless")

            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=options
            )
        else:
            raise ValueError(f"Unsupported browser type: {browser_type}")

    """ 
    --- Общие настройки для Selene ---
    """
    browser.config.driver = driver
    # browser.config.window_width = 1080
    # browser.config.window_height = 1900
    browser.config.base_url = 'https://t-j.ru'

    yield browser

    if remote:
        if browser_type == 'chrome':
            attach.add_logs(browser)
        attach.add_screenshot(browser)
        attach.add_html(browser)
        attach.add_video(browser)
    else:
        attach.add_screenshot(browser)
        attach.add_html(browser)

    browser.quit()
