import allure
import pytest
from pages.tj_home_page import TjHomePage

@allure.tag('smoke', 'ui')
@allure.epic('Страница "t-j.ru"')
@allure.story('Проверка title')
@pytest.mark.ui_test
class TestTjTitle:
    def setup_method(self):
        self.home_page = TjHomePage().open()

    @allure.title("Проверка title страницы")
    def test_title(self):
        self.home_page.verify_title("Т—Ж: журнал про ваши деньги")