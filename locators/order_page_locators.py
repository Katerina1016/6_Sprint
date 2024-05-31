from selenium.webdriver.common.by import By


class OrderPageLocators:
    name_input_field = (By.XPATH, "//input[@placeholder = '* Имя']")  # Поле для ввода имени
    last_name_input_field = (By.XPATH, "//input[@placeholder = '* Фамилия']")  # Поле для ввода фамилии
    address_input_field = (By.XPATH,  "//input[@placeholder = '* Адрес: куда привезти заказ']")  # Поле для ввода адреса доставки
    metro_station_input_field = (By.XPATH, "//input[@placeholder = '* Станция метро']")  # Поле для ввода станции метро
    selected_metro_station = (By.XPATH, ".//div[text() = 'Водный стадион']")  # Локатор с выбранной станцией
    phone_number_input_field = (By.XPATH, "//input[@placeholder = '* Телефон: на него позвонит курьер']")  # Поле ввода номера телефона
    proceed_button = (By.XPATH, "//button[text() = 'Далее']")  # Кнопка "Далее" формы заказа
    time_of_deliver_field = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")  # Поле ввода даты доставки самоката
    rent_time_field = (By.XPATH, ".//span[@class='Dropdown-arrow']")  # Выпадающий список срока аренды
    rent_time_after_choose = (By.XPATH, ".//div[text() = 'сутки']")  # Локатор с выбранным временем срока аренды
    scooter_colour_check_black = (By.ID, 'black')  # Чек-бокс выбора цвета "черный"
    comment_for_courier_field = (By.XPATH, ".//input[@placeholder= 'Комментарий для курьера']")  # Поле ввода комментария
    order_button = (By.XPATH, ".//button[text()='Назад']/parent::div/button[text()='Заказать']")  # Кнопка "Заказать" формы заказа
    yes_button = (By.XPATH, ".//button[text() = 'Да']")  # Кнопка "Да" всплывающего окна подтверждения оформления заказа
    order_completed_popup = (By.XPATH, ".//div[text() = 'Заказ оформлен']")  # Текст "Заказ оформлен" всплывающего окна