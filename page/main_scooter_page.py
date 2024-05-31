from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):  # Получение текущего URL
        return self.driver.current_url

    def wait_about_element_located(self, locator):  # Ожидание отображения элемента
        return WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located(locator))

    def get_text_from_locator(self, locator):  # Получить текст
        return self.wait_about_element_located(locator).text

    def check_element_displayed(self, locator):  # Проверка отображения
        return self.wait_about_element_located(locator).is_displayed()

    def check_element_clickable(self, locator):  # Проверка кликабельности элемента
        return WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable(locator))

    def click_on_button(self, locator):  # Клик на элемент
        self.check_element_clickable(locator)
        self.wait_about_element_located(locator).click()

    def send_keys_to_fields(self, locator, text):  # Отправка значения в поле
        self.wait_about_element_located(locator).send_keys(text)

    def scroll_to_locator(self, locator):  # Скролл страницы до элемента
        element = self.wait_about_element_located(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def switch_to_the_new_tab(self):  # Переключить на новую вкладку
        self.driver.switch_to.window(self.driver.window_handles[1])
