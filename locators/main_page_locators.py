from selenium.webdriver.common.by import By


class MainPageLocators:
    logo_yandex = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')  # логотип "Яндекс"
    logo_scooter = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')  # Логотип "Самокат"
    scooter_logo_text = (By.CLASS_NAME, 'Header_Disclaimer__3VEni')  # Текст "Учебный тренажер"
    accept_cookie_button = (By.ID, 'rcc-confirm-button')  # Кнопка "Принять куки"
    order_button_from_header = (By.XPATH, ".//div[starts-with(@class, 'Header')]/button[text()='Заказать']")  # Кнопка "Заказать" в шапке
    order_button_from_page = (By.XPATH, ".//div[starts-with(@class, 'Home')]/button[text()='Заказать']")  # Кнопка "Заказать" внизу страницы
    drop_down_lists = (By.CSS_SELECTOR, '.accordion')  # выпадающие списки с вопросами

    drop_down_lists_buttons = [  # Локаторы кнопок выпадающих списков "Вопросы о важном"
        (By.ID, "accordion__heading-0"),
        (By.ID, "accordion__heading-1"),
        (By.ID, "accordion__heading-2"),
        (By.ID, "accordion__heading-3"),
        (By.ID, "accordion__heading-4"),
        (By.ID, "accordion__heading-5"),
        (By.ID, "accordion__heading-6"),
        (By.ID, "accordion__heading-7")
    ]

    drop_down_lists_texts = [  # Локаторы ответов на вопросы
        (By.ID, "accordion__panel-0"),
        (By.ID, "accordion__panel-1"),
        (By.ID, "accordion__panel-2"),
        (By.ID, "accordion__panel-3"),
        (By.ID, "accordion__panel-4"),
        (By.ID, "accordion__panel-5"),
        (By.ID, "accordion__panel-6"),
        (By.ID, "accordion__panel-7")
    ]