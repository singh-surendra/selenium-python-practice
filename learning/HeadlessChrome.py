from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
options = webdriver.ChromeOptions()
# options.headless = True   or
options.add_argument("--headless")


driver = webdriver.Chrome(executable_path="../drivers/chromedriver", options=options)
driver.get("https://google.com")
print(driver.title)
driver.find_element_by_name("q").send_keys("Automation step by step")
time.sleep(2)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)

print(driver.title)
driver.close()
driver.quit()
print("Completed")