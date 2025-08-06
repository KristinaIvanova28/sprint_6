
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_all_visible(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def click(self, locator):
        self.wait_for_clickable(locator).click()

    def input_text(self, locator, text):
        field = self.wait_for_visible(locator)
        field.clear()
        field.send_keys(text)

    def get_text(self, locator):
        return self.wait_for_visible(locator).text

    def get_current_url(self):
        return self.driver.current_url

    def scroll_to_element(self, locator):
        element = self.wait_for_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_safely(self, locator):
        element = self.wait_for_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.click(locator)

    def switch_to_last_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def close_current_tab(self):
        self.driver.close()

    def switch_to_window_by_index(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])