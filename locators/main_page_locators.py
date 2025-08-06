from selenium.webdriver.common.by import By


class MainPageLocators:
    URL = "https://qa-scooter.praktikum-services.ru/"

    # FAQ
    @staticmethod
    def get_faq_question_locator(index):
        return (By.ID, f"accordion__heading-{index}")

    @staticmethod
    def get_faq_answer_locator(index):
        return (By.ID, f"accordion__panel-{index}")

    # Кнопки "Заказать"
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']//button[text()='Заказать']")

    # Логотипы
    LOGO_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter__3ls6h")
    LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")