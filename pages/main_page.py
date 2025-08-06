# pages/main_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def open(self):
        self.driver.get(MainPageLocators.URL.strip())

    def click_faq_question(self, index):
        locator = MainPageLocators.get_faq_question_locator(index)
        element = self.wait_for_visible(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def get_faq_answer_text(self, index):
        locator = MainPageLocators.get_faq_answer_locator(index)
        return self.get_text(locator)

    def click_order_button_top(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON_TOP)
        )
        button.click()

    def click_order_button_bottom(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON_BOTTOM)
        )
        button.click()

    def click_scooter_logo(self):
        self.click(MainPageLocators.LOGO_SCOOTER)

    def click_yandex_logo(self):
        self.click(MainPageLocators.LOGO_YANDEX)

    def is_on_main_page(self):
        return self.get_current_url() == MainPageLocators.URL.strip()