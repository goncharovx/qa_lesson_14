import allure
from selene import be, have, query
from selene.support.shared import browser


def text_containing(expected: str):
    return lambda el: expected in el.get(query.text)


class TjNeuronetQuestPage:
    url = "https://t-j.ru/neuronet-quest/"

    article_title_locator = "h1._articleTitle_1rqip_128"
    article_subtitle_locator = "div._articleSubtitle_1rqip_146"
    step_label_locator = "div.root--MLwdb span.label--gwdO6"
    heading_locator = "div.heading--dqW4Y[data-level='3']"
    heading_test_locator = "div.heading--dqW4Y[data-level='3'][data-test-element='ui-kit_heading']"
    next_button_locator = "button.button--c0AcD"
    next_button_container_locator = "div.root--ZMvYB button.button--c0AcD"
    result_label_locator = "span.label--gwdO6"
    result_heading_locator = "div.heading--dqW4Y[data-level='2'][data-test-element='ui-kit_heading']"
    result_paragraph_locator = "div.paragraph--qfchi[data-testid='paragraph']"
    result_link_locator = "a.link--AUgoy[data-testid='link']"

    def open(self):
        with allure.step("Открыть страницу калькулятора"):
            browser.open(self.url)
        return self

    def verify_article_title(self, expected_title):
        with allure.step("Проверить заголовок статьи"):
            browser.element(self.article_title_locator) \
                .should(be.visible) \
                .should(text_containing("Узнайте, какую нейро"))
        return self

    def verify_article_subtitle(self, expected_subtitle):
        with allure.step("Проверить подзаголовок статьи"):
            browser.element(self.article_subtitle_locator) \
                .should(be.visible) \
                .should(have.text(expected_subtitle))
        return self

    def verify_step_label(self, expected_label):
        with allure.step(f"Проверить метку шага '{expected_label}'"):
            browser.element(self.step_label_locator) \
                .should(be.visible) \
                .should(have.text(expected_label))
        return self

    def verify_heading(self, expected_heading):
        with allure.step(f"Проверить заголовок '{expected_heading}'"):
            browser.element(self.heading_locator) \
                .should(be.visible) \
                .should(have.text(expected_heading))
        return self

    def verify_heading_with_test(self, expected_heading):
        with allure.step(f"Проверить заголовок с тестовым атрибутом '{expected_heading}'"):
            browser.element(self.heading_test_locator) \
                .should(be.visible) \
                .should(have.text(expected_heading))
        return self

    def click_option(self, option_text):
        with allure.step(f"Выбрать вариант '{option_text}'"):
            browser.all("label.control--fKq8_") \
                .element_by(have.text(option_text)) \
                .should(be.visible) \
                .click()
        return self

    def click_next(self):
        with allure.step("Нажать кнопку 'Далее'"):
            browser.element(self.next_button_locator) \
                .should(be.visible) \
                .should(have.text("Далее")) \
                .click()
        return self

    def click_next_in_container(self):
        with allure.step("Нажать кнопку 'Далее' в контейнере"):
            browser.element(self.next_button_container_locator) \
                .should(be.visible) \
                .should(have.text("Далее")) \
                .click()
        return self

    def verify_result(self, expected_label, expected_heading, expected_paragraph, expected_link_url,
                      expected_link_text):
        with allure.step("Проверить метку результата"):
            browser.element(self.result_label_locator) \
                .should(be.visible) \
                .should(have.text(expected_label))
        with allure.step("Проверить заголовок результата"):
            browser.element(self.result_heading_locator) \
                .should(be.visible) \
                .should(have.text(expected_heading))
        with allure.step("Проверить описание результата"):
            browser.element(self.result_paragraph_locator) \
                .should(be.visible) \
                .should(have.text(expected_paragraph))
        with allure.step("Проверить ссылку результата"):
            browser.element(self.result_link_locator) \
                .should(be.visible) \
                .should(have.attribute("href", expected_link_url)) \
                .should(have.text(expected_link_text))
        return self
