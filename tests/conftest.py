import pytest
import allure
from selenium import webdriver
from data import Urls

@allure.step('Открытие браузера / переход на страницу сервиса Яндекс.Самокат / закрытие браузера')
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.fullscreen_window()
    driver.get(Urls.BASE_PAGE)
    yield driver
    driver.quit()
