import allure
from locators.order_page_locators import OrderPageLocators
from page.main_scooter_page import MainPage


class OrderPage(MainPage):
    @allure.step('ввод имени поля ввода имени')
    def send_name_to_name_input(self, text):
        self.send_keys_to_fields(OrderPageLocators.name_input_field, text)

    @allure.step('ввод фамилии поля ввода фамилии')
    def send_last_name_to_last_name_input(self, text):
        self.send_keys_to_fields(OrderPageLocators.last_name_input_field, text)

    @allure.step('ввод адреса доставки поля адрес доставки')
    def send_address_to_address_input(self, text):
        self.send_keys_to_fields(OrderPageLocators.address_input_field, text)

    @allure.step('ввод станции метро поля ввода "Станция метро"')
    def send_subway_to_subway_input(self, text):
        self.click_on_button(OrderPageLocators.metro_station_input_field)
        self.send_keys_to_fields(OrderPageLocators.metro_station_input_field, text)
        self.click_on_button(OrderPageLocators.selected_metro_station)

    @allure.step('ввод номера телефона поля ввода телефона')
    def send_phone_number_to_number_input_field(self, text):
        self.send_keys_to_fields(OrderPageLocators.phone_number_input_field, text)

    @allure.step('Клик на кнопку "Продолжить" в форме заказа')
    def click_on_next_button(self):
        self.click_on_button(OrderPageLocators.proceed_button)

    @allure.step('Полностью заполнить первую часть формы заказа')
    def fill_order_form_for_who(self, user_one):
        self.send_name_to_name_input(user_one[1])
        self.send_last_name_to_last_name_input(user_one[2])
        self.send_address_to_address_input(user_one[3])
        self.send_subway_to_subway_input(user_one[4])
        self.send_phone_number_to_number_input_field(user_one[5])
        self.click_on_next_button()

    @allure.step('Введите дату доставки самоката')
    def send_deliver_date_to_delivery_input(self, text):
        self.click_on_button(OrderPageLocators.time_of_deliver_field)
        self.send_keys_to_fields(OrderPageLocators.time_of_deliver_field, text)

    @allure.step('Выберите время аренды')
    def rent_time_choose(self):
        self.click_on_button(OrderPageLocators.rent_time_field)
        self.click_on_button(OrderPageLocators.rent_time_after_choose)

    @allure.step('Выберите черный цвет скутера')
    def scooter_colour_choose(self):
        self.click_on_button(OrderPageLocators.scooter_colour_check_black)

    @allure.step('Отправить комментарий в поле ввода комментариев')
    def send_comment_to_comment_input(self, text):
        self.send_keys_to_fields(OrderPageLocators.comment_for_courier_field, text)

    @allure.step('Нажмите на кнопку "Заказать"')
    def finish_order(self):
        self.click_on_button(OrderPageLocators.order_button)

    @allure.step('Полностью заполните вторую часть формы заказа')
    def complete_filling_of_order_form(self, text):
        self.send_deliver_date_to_delivery_input(text[6])
        self.rent_time_choose()
        self.scooter_colour_choose()
        self.send_comment_to_comment_input(text[7])
        self.finish_order()

    @allure.step('Подтверждение заказа')
    def confirm_order(self):
        self.click_on_button(OrderPageLocators.yes_button)

    @allure.step('Полный рабочий процесс выполнения заказа')
    def full_flow_to_order(self, user_one):
        self.fill_order_form_for_who(user_one)
        self.complete_filling_of_order_form(user_one)
        self.confirm_order()

    @allure.step('Всплывающее окно оформления заказа')
    def order_completed_popup(self):
        return self.wait_about_element_located(OrderPageLocators.order_completed_popup).is_displayed()
