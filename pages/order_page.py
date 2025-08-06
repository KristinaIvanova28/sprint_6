import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    def wait_for_metro_suggestion_and_click(self, station_name):
        suggestion_locator = (
            By.XPATH,
            f"//div[contains(@class, 'select-search__option') and contains(., '{station_name}')]"
        )
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(suggestion_locator),
            message=f"Подсказка для '{station_name}' не появилась"
        )
        self.driver.execute_script("arguments[0].click();", element)

    def fill_first_page(self, name, last_name, address, metro, phone):
        self.input_text(OrderPageLocators.FIELD_NAME, name)
        self.input_text(OrderPageLocators.FIELD_LAST_NAME, last_name)
        self.input_text(OrderPageLocators.FIELD_ADDRESS, address)

        metro_input = self.wait_for_visible(OrderPageLocators.FIELD_METRO)
        metro_input.clear()
        metro_input.send_keys(metro)

        metro_input.send_keys(Keys.ARROW_DOWN)
        metro_input.send_keys(Keys.ENTER)

        self.input_text(OrderPageLocators.FIELD_PHONE, phone)
        self.click(OrderPageLocators.BUTTON_NEXT)

    def fill_second_page(self, date, rent_days_index, color_black, color_grey, comment):
        self.input_text(OrderPageLocators.FIELD_DATE, date)
        self.select_date(date)

        self.click(OrderPageLocators.FIELD_RENT)
        self.wait_for_all_visible(OrderPageLocators.RENT_OPTION)[rent_days_index].click()

        if color_black:
            self.click(OrderPageLocators.FIELD_COLOR_BLACK)
        if color_grey:
            self.click(OrderPageLocators.FIELD_COLOR_GREY)

        self.input_text(OrderPageLocators.FIELD_COMMENT, comment)
        self.click(OrderPageLocators.BUTTON_ORDER)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.MODAL_SUCCESS),
            message="Модальное окно не появилось"
        )

        self.click_confirm_button()

    def is_success_modal_displayed(self):
        return self.wait_for_visible(OrderPageLocators.MODAL_SUCCESS).is_displayed()
    
    def select_date(self, date_str):
        day = date_str.split('.')[0].lstrip('0')
        day_locator = (
            By.XPATH,
            f"//div[contains(@class, 'react-datepicker__day') and text()='{day}']"
        )
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(day_locator),
            message=f"День '{day}' не кликабельн"
        )
        element.click()
    
    def click_confirm_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'оформить заказ')]")),
            message="Модальное окно не появилось"
        )
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.BUTTON_CONFIRM),
            message="Кнопка 'Да' не кликабельна"
        )
        self.driver.execute_script("arguments[0].click();", button)