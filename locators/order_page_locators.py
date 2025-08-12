from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Шаг 1: Персональная информация
    FIELD_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    FIELD_LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    FIELD_ADDRESS = (By.XPATH, "//*[contains(@placeholder, 'Адрес')]")
    FIELD_METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    FIELD_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")
    

    # Шаг 2: Детали заказа
    FIELD_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    FIELD_RENT = (By.CLASS_NAME, "Dropdown-control")
    RENT_OPTION = (By.CLASS_NAME, "Dropdown-option")
    FIELD_COLOR_BLACK = (By.ID, "black")
    FIELD_COLOR_GREY = (By.ID, "grey")
    FIELD_COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    BUTTON_ORDER = (By.XPATH, "(//button[text()='Заказать'])[2]")
    BUTTON_CONFIRM = (By.XPATH, "//button[contains(text(), 'Да')]")

    # Модальное окно
    MODAL_SUCCESS = (By.XPATH, "//*[contains(text(), 'Заказ')]")