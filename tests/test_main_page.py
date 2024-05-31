import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
from data import DropDownListsTexts, Urls
from locators.main_page_locators import MainPageLocators
from page.home_scooter_page import HomePage
from page.yandex_dzen_page import DzenPage


class TestMainPage:
    @allure.title('Тест проверяющий, при клике на слово "Самокат" в шапке сайта, переход на страницу Самокат')
    @allure.description('''1. Клик на кнопку Заказать
                           2. Клик на слово Самокат в шапке
                           3. Сравнение ожидаемого и текущего URL; Проверка отображения текста "Тренировочный тренажер"''')
    def test_click_on_scooter_logo(self, driver):
        main_page = HomePage(driver)
        main_page.order_button_click()
        main_page.scooter_logo_click()
        current_url = main_page.get_current_url()
        title_displayed = main_page.check_main_title()
        assert current_url == Urls.MAIN_PAGE and title_displayed

    @allure.title('Тест проверяющий, при клике на слово "Яндекс" в шапке сайта, переход на страницу Яндекс.Дзен')
    @allure.description('''1. Клик на слово "Яндекс"
                           2. Переход на новую вкладку
                           3. Сравнение ожидаемого и текущего URL; Проверка, что появилась кнопка "Главная"''')
    def test_click_on_yandex_logo(self, driver):
        main_page = HomePage(driver)
        dzen_page = DzenPage(driver)
        main_page.yandex_logo_click()
        main_page.switch_to_the_new_tab()
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(Urls.YA_DZEN_URL))
        assert dzen_page.check_element_main_button

    @allure.title('Тест сравнение текста в выпадающих списках вопросов')
    @allure.description('''1. Скролл до вопросов;
                           2. Клик на вопрос;
                           3. Получение текстов;
                           4. Сравнение ожидаемого и фактического текста''')
    @pytest.mark.parametrize('questions_buts_locators, questions_text_locators, expected_question_text', zip(MainPageLocators.drop_down_lists_buttons, MainPageLocators.drop_down_lists_texts, DropDownListsTexts.expected_texts))
    def test_questions_accordeon(self, driver, questions_buts_locators, questions_text_locators, expected_question_text):
        home_page = HomePage(driver)
        home_page.accept_cookie()
        home_page.scroll_to_questions()
        text = home_page.get_text_of_questions(questions_buts_locators, questions_text_locators)
        assert text == expected_question_text
