import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from curl import Urls
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step("Открытие главной страницы")
    def open(self, url=Urls.URL):
        self.driver.get(url)

    @allure.step("Клик по вопросу в разделе FAQ (индекс: {index})")
    def click_faq_question(self, index):
        locator = MainPageLocators.get_faq_question_locator(index)
        element = self.wait_for_visible(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Получение текста ответа в разделе FAQ (индекс: {index})")
    def get_faq_answer_text(self, index):
        locator = MainPageLocators.get_faq_answer_locator(index)
        return self.get_text(locator)

    @allure.step("Клик по кнопке 'Заказать' в верхней части страницы")
    def click_order_button_top(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON_TOP)
        )
        button.click()

    @allure.step("Клик по кнопке 'Заказать' в нижней части страницы")
    def click_order_button_bottom(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON_BOTTOM)
        )
        button.click()

    @allure.step("Клик по логотипу Самокат")
    def click_scooter_logo(self):
        self.click(MainPageLocators.LOGO_SCOOTER)

    @allure.step("Клик по логотипу Яндекс")
    def click_yandex_logo(self):
        self.click(MainPageLocators.LOGO_YANDEX)

    @allure.step("Проверка: пользователь находится на главной странице")
    def is_on_main_page(self):
        return self.get_current_url() == MainPageLocators.URL.strip()
    
    @allure.step("Принять куки-баннер")
    def accept_cookies(self):
        self.click_if_visible(MainPageLocators.COOKIE_BUTTON)

    @allure.step("Клик по верхней кнопке 'Заказать'")
    def click_order_button_top(self):
        self.click(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Клик по нижней кнопке 'Заказать'")
    def click_order_button_bottom(self):
        self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)