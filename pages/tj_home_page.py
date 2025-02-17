import allure
from selene import be, have
from selene.support.shared import browser

class TjHomePage:
    base_url = "https://t-j.ru/"

    def open(self):
        with allure.step("Открыть главную страницу t-j.ru"):
            browser.open(self.base_url)
        return self

    def verify_title(self, expected_title):
        with allure.step("Проверить title страницы"):
            browser.should(lambda _: browser.driver.title == expected_title)
        return self

    def click_search_icon(self):
        with allure.step("Кликнуть по иконке поиска (лупа)"):
            browser.element("button._loupe_wvz82_55")\
                .should(be.visible)\
                .should(be.clickable)\
                .click()
        return self