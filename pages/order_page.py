import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    @allure.step("Заполнение первой страницы заказа")
    def fill_first_page(self, name, last_name, address, metro, phone):
        self.input_text(OrderPageLocators.FIELD_NAME, name)
        self.input_text(OrderPageLocators.FIELD_LAST_NAME, last_name)
        self.input_text(OrderPageLocators.FIELD_ADDRESS, address)

        metro_input = self.wait_for_visible(OrderPageLocators.FIELD_METRO)
        metro_input.clear()
        metro_input.send_keys(metro)

        metro_input = self.wait_for_visible(OrderPageLocators.FIELD_METRO)
        metro_input.clear()
    
        metro_input.send_keys(metro)
        metro_input.send_keys(Keys.ARROW_DOWN)
        metro_input.send_keys(Keys.ENTER)

        self.input_text(OrderPageLocators.FIELD_PHONE, phone)
        self.click(OrderPageLocators.BUTTON_NEXT)

    @allure.step("Ожидание загрузки первой страницы заказа")
    def wait_for_first_page_loaded(self):
        self.wait_for_visible(OrderPageLocators.FIELD_NAME)

    @allure.step("Ожидание загрузки второй страницы заказа")
    def wait_for_second_page_loaded(self):
        self.wait_for_visible(OrderPageLocators.FIELD_DATE)

    @allure.step("Выбор даты доставки: {date_str}")
    def select_date(self, date_str):
        day = date_str.split('.')[0].lstrip('0')
        day_locator = (
            By.XPATH,
            f"//div[contains(@class, 'react-datepicker__day') and text()='{day}' "
            f"and not(contains(@class, 'react-datepicker__day--outside-month'))]"
        )
        element = self.wait_for_clickable(day_locator)
        element.click()

    @allure.step("Заполнение второй страницы заказа")
    def fill_second_page(self, date, rent_days_index, color_black, color_grey, comment):
        self.input_text(OrderPageLocators.FIELD_DATE, date)
        self.select_date(date)

        self.click(OrderPageLocators.FIELD_RENT)
        rent_options = self.wait_for_all_visible(OrderPageLocators.RENT_OPTION)
        rent_options[rent_days_index].click()

        if color_black:
            self.click(OrderPageLocators.FIELD_COLOR_BLACK)
        if color_grey:
            self.click(OrderPageLocators.FIELD_COLOR_GREY)

        self.input_text(OrderPageLocators.FIELD_COMMENT, comment)
        self.click(OrderPageLocators.BUTTON_ORDER)

    @allure.step("Подтверждение заказа кнопкой 'Да'")
    def click_confirm_button(self):
        self.click(OrderPageLocators.BUTTON_CONFIRM)

    @allure.step("Проверка: модальное окно успеха отображается")
    def is_success_modal_displayed(self):
        return self.wait_for_visible(OrderPageLocators.MODAL_SUCCESS).is_displayed()