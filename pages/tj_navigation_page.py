import allure
from selene import be, have
from selene.support.shared import browser

class TjNavigationPage:
    base_url = "https://t-j.ru/"

    def open(self):
        with allure.step("Открыть главную страницу t-j.ru"):
            browser.open(self.base_url)
        return self

    def verify_menu_item(self, item_text, href_fragment):
        with allure.step(f"Проверить пункт меню '{item_text}'"):
            browser.element(f"a._pill_opwej_4[href*='{href_fragment}']")\
                .should(be.visible)\
                .should(be.clickable)\
                .should(have.text(item_text))
        return self