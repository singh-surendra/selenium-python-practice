from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("https://www.freshworks.com/")

header_element = driver.find_element(By.TAG_NAME, 'h1')
print(header_element.text)

# how to find out all the all  links




time.sleep(2)

driver.close()
driver.quit()