import allure
import pytest

from pages.tj_neuronet_quest_page import TjNeuronetQuestPage


@allure.tag('ai', 'calculator', 'ui')
@allure.epic('Калькулятор AI')
@allure.story('Выбор нейросети')
@pytest.mark.ui_test
class TestAiCalculatorSelection:
    def setup_method(self):
        self.page = TjNeuronetQuestPage().open()

    @allure.title("Полный сценарий выбора нейросети")
    def test_ai_calculator(self):
        with allure.step("Проверить заголовок статьи"):
            self.page.verify_article_title("Узнайте, какую нейросеть использовать для ваших задач")

        with allure.step("Проверить подзаголовок статьи"):
            self.page.verify_article_subtitle("Интерактивный навигатор по миру искусственного интеллекта")

        with allure.step("Шаг 1: Проверить метку и заголовок, выбрать 'Рабочую' и нажать 'Далее'"):
            self.page.verify_step_label("Шаг 1")
            self.page.verify_heading("Какую задачу вам нужно решить?")
            self.page.click_option("Рабочую")
            self.page.click_next()

        with allure.step("Шаг 2: Проверить метку и заголовок, выбрать 'Сгенерировать код' и нажать 'Далее'"):
            self.page.verify_step_label("Шаг 2")
            self.page.verify_heading("С чем нужна помощь?")
            self.page.click_option("Сгенерировать код")
            self.page.click_next_in_container()

        with allure.step(
                "Шаг 3: Проверить метку и заголовок, выбрать 'Необязательно, могу сменить IP⁠-⁠адрес' "
                "и нажать 'Далее'"):
            self.page.verify_step_label("Шаг 3")
            self.page.verify_heading_with_test("Нужно, чтобы сервис был доступен в России?")
            self.page.click_option("Необязательно, могу сменить IP⁠-⁠адрес")
            self.page.click_next()

        with allure.step("Шаг 4: Проверить метку и заголовок, выбрать 'Да' и нажать 'Далее'"):
            self.page.verify_step_label("Шаг 4")
            self.page.verify_heading_with_test("Сможете оплатить сервис иностранной картой?")
            self.page.click_option("Да")
            self.page.click_next()

        with allure.step("Проверить итоговый результат"):
            self.page.verify_result(
                "Результат", "Вам подойдет GitHub Copilot",
                "GitHub Copilot", "https://github.com/features/copilot",
                "GitHub Copilot")
