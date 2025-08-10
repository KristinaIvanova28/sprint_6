import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from typing import List, Tuple
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Ожидание, когда элемент станет кликабельным")
    def wait_for_clickable(self, locator: Tuple[By, str]):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Ожидание, когда элемент станет видимым")
    def wait_for_visible(self, locator: Tuple[By, str]):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание, когда все элементы локатора станут видимыми")
    def wait_for_all_visible(self, locator: Tuple[By, str]) -> List:
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    @allure.step("Клик по элементу")
    def click(self, locator: Tuple[By, str]):
        element = self.wait_for_clickable(locator)
        element.click()

    @allure.step("Ввод текста в поле: {text}")
    def input_text(self, locator: Tuple[By, str], text: str):
        field = self.wait_for_visible(locator)
        field.clear()
        field.send_keys(text)

    @allure.step("Получение текста элемента")
    def get_text(self, locator: Tuple[By, str]) -> str:
        return self.wait_for_visible(locator).text

    @allure.step("Получение текущего URL")
    def get_current_url(self) -> str:
        return self.driver.current_url

    @allure.step("Прокрутка к элементу")
    def scroll_to_element(self, locator: Tuple[By, str]):
        element = self.wait_for_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Безопасный клик (с прокруткой в центр экрана)")
    def click_safely(self, locator: Tuple[By, str]):
        element = self.wait_for_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.click(locator)

    @allure.step("Переключение на последнюю вкладку")
    def switch_to_last_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Закрытие текущей вкладки")
    def close_current_tab(self):
        self.driver.close()

    @allure.step("Переключение на вкладку по индексу: {index}")
    def switch_to_window_by_index(self, index: int):
        handles = self.driver.window_handles
        if 0 <= index < len(handles):
            self.driver.switch_to.window(handles[index])
        else:
            raise IndexError(f"Нет вкладки с индексом {index}. Доступно вкладок: {len(handles)}")
    
    @allure.step("Клик по элементу, если он виден (без падения при отсутствии)")
    def click_if_visible(self, locator: Tuple[By, str]):
        try:
            element = self.wait_for_visible(locator)
            element.click()
        except:
            pass