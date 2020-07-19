from selenium import webdriver
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

# Implicit Waits
# driver.implicitly_wait(10)
driver.get("https://google.com")
driver.find_element_by_name("q").send_keys("Automation")
wait = WebDriverWait(driver, 10)

try:
   element = wait.until(EC.element_to_be_clickable((By.NAME,"btnK1")))
   print("element is clickable")
except TimeoutException:
    print("element is not clickable")
    exit(1)

element.click()
# driver.find_element_by_n%me("btnK").click()
print("Test Completed")
driver.close()
driver.quit()