import allure
import pytest
from selene import be, have
from selene.support.shared import browser
from pages.tj_home_page import TjHomePage

@allure.tag('search', 'ui')
@allure.epic('Страница "t-j.ru"')
@allure.story('Поиск инструментов')
@pytest.mark.ui_test
class TestSearchInstrument:
    def setup_method(self):
        self.home_page = TjHomePage().open()

    @allure.title("Поиск по слову 'ликвидные облигации'")
    @pytest.mark.parametrize("search_query, expected_heading", [
        ("ликвидные облигации", "Как искать ликвидные облигации"),
    ])
    def test_search(self, search_query, expected_heading):
        self.home_page.click_search_icon()
        with allure.step("Проверить появление поля поиска"):
            search_input = browser.element("input[name='q']")
            search_input.should(be.visible)
            search_input.should(have.attribute("placeholder", "Поиск"))
        with allure.step("Ввести запрос и выполнить поиск"):
            search_input.type(search_query).press_enter()
        with allure.step("Проверить, что первый результат содержит ожидаемый заголовок"):
            browser.all("div._card_1m6jv_7").first.element("h4._heading_nm8q3_1")\
                .should(have.text(expected_heading))