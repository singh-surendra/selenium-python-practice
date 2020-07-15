from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
print(driver.title)

username_url = driver.find_element(By.ID, 'Form_submitForm_subdomain')
first_name = driver.find_element(By.ID, 'Form_submitForm_FirstName')
last_name = driver.find_element(By.ID, 'Form_submitForm_LastName')
email = driver.find_element(By.ID, 'Form_submitForm_Email')
feature_link = driver.find_element(By.LINK_TEXT,"Features")

username_url.send_keys("suri singh")
first_name.send_keys("Suri")
last_name.send_keys("Singh")
email.send_keys("suriAuto@gmail.com")
feature_link.click()

time.sleep(3)

driver.close()
driver.quit()
