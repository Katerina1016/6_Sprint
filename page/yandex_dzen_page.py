import allure
from page.main_scooter_page import MainPage
from locators.main_dzen_page import YandexDzenLocators


class DzenPage(MainPage):
    @allure.step
    def check_element_main_button(self):
        self.wait_about_element_located(YandexDzenLocators.dzen_main_page_button)
        self.check_element_displayed(YandexDzenLocators.dzen_main_page_button)
