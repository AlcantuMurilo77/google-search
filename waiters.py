from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


def wait_for_element(driver: WebDriver, by: By , locator:str, timeout: int) -> WebDriverWait:
    return WebDriverWait(driver, timeout).until(
    expected_conditions.presence_of_element_located((by, locator))
)
