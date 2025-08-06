
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import UserData
from locators.order_page_locators import OrderPageLocators
import allure


class TestOrderFlow:
    @pytest.mark.parametrize("button_method, user_data", [
        ("top", UserData.USER_1),
        ("top", UserData.USER_2),
        ("bottom", UserData.USER_1),
        ("bottom", UserData.USER_2),
    ])
    @allure.title("Полный сценарий заказа с кнопкой {button_method}")
    @allure.description("Проверка оформления заказа с разными данными и кнопками")
    def test_complete_order_flow(self, driver, button_method, user_data):
        """Полный сценарий заказа с разными кнопками и данными"""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.open()

        # Шаг 0: Закрыть баннер с куками
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            ).click()
            print("✅ Баннер с куками закрыт")
        except Exception as e:
            print(f"❌ Баннер с куками не появился: {e}")

        # Шаг 1: Клик по кнопке "Заказать"
        if button_method == "top":
            main_page.click_order_button_top()
        else:
            main_page.click_order_button_bottom()

        # Шаг 2: Ожидание появления формы (поле "Имя")
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.FIELD_NAME),
            message="Форма заказа не появилась"
        )

        # Шаг 3: Заполнение первой страницы
        order_page.fill_first_page(
            user_data["name"],
            user_data["last_name"],
            user_data["address"],
            user_data["metro"],
            user_data["phone"]
        )

        # Шаг 4: Ожидание второй страницы (поле "Когда привезти")
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.FIELD_DATE),
            message="Вторая страница не загрузилась"
        )

        # Шаг 5: Заполнение второй страницы
        order_page.fill_second_page(
            user_data["date"],
            user_data["rent_days_index"],
            user_data["color_black"],
            user_data["color_grey"],
            user_data["comment"]
        )

        # Шаг 6: Проверка успешного заказа
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.MODAL_SUCCESS),
            message="Модальное окно успеха не появилось"
        )
        assert order_page.is_success_modal_displayed(), "Модальное окно успеха не отображается"