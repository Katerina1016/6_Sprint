import allure
from locators.main_page_locators import MainPageLocators
from page.main_scooter_page import MainPage


class HomePage(MainPage):

    @allure.step('Клик на логотип Яндекс')
    def yandex_logo_click(self):
        self.click_on_button(MainPageLocators.logo_yandex)

    @allure.step('Клик на слово Самокат')
    def scooter_logo_click(self):
        self.click_on_button(MainPageLocators.logo_scooter)

    @allure.step('Клик на кнопку Заказать в шапке')
    def order_button_click(self):
        self.click_on_button(MainPageLocators.order_button_from_header)

    @allure.step('Проверка текста в шапке')
    def check_main_title(self):
        return self.wait_about_element_located(MainPageLocators.scooter_logo_text).is_displayed()

    @allure.step('Клик на кнопку Принять куки')
    def accept_cookie(self):
        self.wait_about_element_located(MainPageLocators.accept_cookie_button)
        self.click_on_button(MainPageLocators.accept_cookie_button)

    @allure.step('Клик на кнопку заказать внизу страницы')
    def order_from_button_bottom_page(self):
        self.scroll_to_locator(MainPageLocators.order_button_from_page)
        self.check_element_displayed(MainPageLocators.order_button_from_page)
        self.click_on_button(MainPageLocators.order_button_from_page)

    @allure.step('Скролл до вопросов')
    def scroll_to_questions(self):
        self.scroll_to_locator(MainPageLocators.drop_down_lists)

    @allure.step('Клик на выпадающий список')
    def click_on_questions(self, drop_down_lists_buttons):
        self.wait_about_element_located(drop_down_lists_buttons)
        self.click_on_button(drop_down_lists_buttons)

    @allure.step('Текст выпадающего списка')
    def get_text_of_questions(self, drop_down_lists_buttons, drop_down_lists_texts):
        self.click_on_questions(drop_down_lists_buttons)
        self.check_element_displayed(drop_down_lists_texts)
        text_of_questions = self.get_text_from_locator(drop_down_lists_texts)
        return text_of_questions
