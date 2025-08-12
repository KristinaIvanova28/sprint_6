
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import os


@pytest.fixture
def driver():
    options = Options()

    options.binary_location = "/Applications/Firefox.app/Contents/MacOS/firefox"
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")

    driver_path = os.path.join(os.getcwd(), "drivers", "geckodriver")
    service = Service(driver_path)

    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()

    yield driver
    driver.quit()