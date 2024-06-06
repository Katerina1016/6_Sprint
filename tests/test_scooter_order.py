from data import Users
from page.home_scooter_page import HomePage
from page.order_scooter_page import OrderPage
import allure


class TestOrderPage:
    @allure.title('Тест заказ самоката через кнопку "Заказать" в шапке')
    @allure.description('''1. Нажатие на кнопку "Заказать" в шапке
                           2. Заполнение первой части формы заказа
                           3. Заполнение второй части формы заказа
                           4. Подтверждение заказа
                           5. Ожидание появления всплывающего окна с подтверждением заказа''')
    def test_order_by_header_button(self, driver):
        main_page = HomePage(driver)
        order_page = OrderPage(driver)
        main_page.accept_cookie()
        main_page.order_button_click()
        order_page.full_flow_to_order(Users.user_one)
        assert order_page.order_completed_popup()

    @allure.title('Тест заказ самоката через кнопку "Заказать" внизу страницы')
    @allure.description('''1. Нажатие на кнопку "Заказать"
                           2. Заполнение первой части формы заказа
                           3. Заполнение второй части формы заказа
                           4. Подтверждение заказа
                           5. Ожидание появления всплывающего окна с подтверждением заказа''')
    def test_order_by_page_button(self, driver):
        main_page = HomePage(driver)
        order_page = OrderPage(driver)
        main_page.accept_cookie()
        main_page.order_from_button_bottom_page()
        order_page.full_flow_to_order(Users.user_two)
        assert order_page.order_completed_popup()
