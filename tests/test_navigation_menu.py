import allure
import pytest
from pages.tj_navigation_page import TjNavigationPage

@allure.tag('navigation', 'ui')
@allure.epic('Страница "t-j.ru"')
@allure.story('Навигационное меню')
@pytest.mark.ui_test
class TestNavigationMenu:
    def setup_method(self):
        self.nav_page = TjNavigationPage().open()

    @allure.title("Проверка пункта 'Учебник'")
    def test_menu_uchebnik(self):
        self.nav_page.verify_menu_item("Учебник", "/pro/")

    @allure.title("Проверка пункта 'Сообщество'")
    def test_menu_community(self):
        self.nav_page.verify_menu_item("Сообщество", "/community/")

    @allure.title("Проверка пункта 'Аптечка'")
    def test_menu_aptechka(self):
        self.nav_page.verify_menu_item("Аптечка", "/aptechka/")