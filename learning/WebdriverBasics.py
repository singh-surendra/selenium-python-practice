import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome("../drivers/chromedriver")
# or
driver = webdriver.Chrome(executable_path="../drivers/chromedriver")
driver.set_page_load_timeout(10)
driver.implicitly_wait(10)
driver.get("https://www.google.com/")
driver.find_element(By.NAME,'q').send_keys("Hello Suri")
time.sleep(2)
driver.find_element(By.NAME,'q').clear()
driver.find_element_by_name("q").send_keys("Automation step by step")
driver.find_element_by_name("btnK").click()
time.sleep(2)
driver.close()
driver.quit()

print("test is complete")
