from selenium import webdriver
from options import options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time





service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        })
    """
})

driver.get("https://google.com")

time.sleep(2)

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.send_keys("SQLAlchemy Documentation" + Keys.ENTER)

time.sleep(10)

driver.quit()
