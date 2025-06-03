from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
import time
from options import options
from waiters import wait_for_element

service: Service = Service(executable_path="chromedriver.exe")
driver: WebDriver = webdriver.Chrome(service=service, options=options)

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        })
    """
})

driver.get("https://google.com")

wait_for_element(driver, By.CLASS_NAME, "gLFyf", 5)

input_element: WebElement = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys("SQLAlchemy Documentation" + Keys.ENTER)

wait_for_element(driver, By.PARTIAL_LINK_TEXT, "SQLAlchemy Documentation — SQLAlchemy 2.0 Documentation", 5)

link:WebElement = driver.find_element(By.PARTIAL_LINK_TEXT, "SQLAlchemy Documentation — SQLAlchemy 2.0 Documentation")
link.click()
driver.save_screenshot('prints/sql_alc.png')

time.sleep(10)

driver.quit()
