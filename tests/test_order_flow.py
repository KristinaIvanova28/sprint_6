
import pytest
import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import UserData


@allure.severity(allure.severity_level.CRITICAL)
class TestOrderFlow:

    @allure.title("Оформление заказа через верхнюю кнопку")
    @allure.description("Проверка полного цикла заказа самоката через кнопку 'Заказать' в шапке")
    def test_order_via_top_button_user1(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        with allure.step("Открытие главной страницы"):
            main_page.open()

        with allure.step("Принятие куки-баннера (если отображается)"):
            main_page.accept_cookies()

        with allure.step("Клик по верхней кнопке 'Заказать'"):
            main_page.click_order_button_top()

        with allure.step("Ожидание загрузки первой страницы заказа"):
            order_page.wait_for_first_page_loaded()

        with allure.step("Заполнение первой страницы заказа"):
            order_page.fill_first_page(
                UserData.USER_1["name"],
                UserData.USER_1["last_name"],
                UserData.USER_1["address"],
                UserData.USER_1["metro"],
                UserData.USER_1["phone"]
            )

        with allure.step("Ожидание загрузки второй страницы заказа"):
            order_page.wait_for_second_page_loaded()

        with allure.step("Заполнение второй страницы заказа"):
            order_page.fill_second_page(
                UserData.USER_1["date"],
                UserData.USER_1["rent_days_index"],
                UserData.USER_1["color_black"],
                UserData.USER_1["color_grey"],
                UserData.USER_1["comment"]
            )

        with allure.step("Проверка: заказ успешно оформлен"):
            assert order_page.is_success_modal_displayed(), "Модальное окно успеха не отображается"

    @allure.title("Оформление заказа через нижнюю кнопку")
    @allure.description("Проверка полного цикла заказа самоката через кнопку 'Заказать' внизу страницы")
    def test_order_via_bottom_button_user2(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        with allure.step("Открытие главной страницы"):
            main_page.open()

        with allure.step("Принятие куки-баннера (если отображается)"):
            main_page.accept_cookies()

        with allure.step("Клик по нижней кнопке 'Заказать'"):
            main_page.click_order_button_bottom()

        with allure.step("Ожидание загрузки первой страницы заказа"):
            order_page.wait_for_first_page_loaded()

        with allure.step("Заполнение первой страницы заказа"):
            order_page.fill_first_page(
                UserData.USER_2["name"],
                UserData.USER_2["last_name"],
                UserData.USER_2["address"],
                UserData.USER_2["metro"],
                UserData.USER_2["phone"]
            )

        with allure.step("Ожидание загрузки второй страницы заказа"):
            order_page.wait_for_second_page_loaded()

        with allure.step("Заполнение второй страницы заказа"):
            order_page.fill_second_page(
                UserData.USER_2["date"],
                UserData.USER_2["rent_days_index"],
                UserData.USER_2["color_black"],
                UserData.USER_2["color_grey"],
                UserData.USER_2["comment"]
            )

        with allure.step("Проверка: заказ успешно оформлен"):
            assert order_page.is_success_modal_displayed(), "Модальное окно успеха не отображается"