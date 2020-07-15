from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
# driver = webdriver.Chrome(ChromeDriverManager("2.36").install())
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://google.com")
print(driver.title)
driver.find_element_by_name("q").send_keys("Automation step by step")
time.sleep(2)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)

print(driver.title)
driver.close()
driver.quit()
print("Completed")