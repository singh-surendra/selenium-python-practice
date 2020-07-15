from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("https://app.hubspot.com/login")

# username = driver.find_element(By.CSS_SELECTOR,"#username")
# username = driver.find_element(By.CLASS_NAME,"login-email")
# username.send_keys("test@test.com")
#
# username = driver.find_element(By.CLASS_NAME,"login-password")
# username.send_keys("test@test.com")

# login_button = driver.find_element(By.CLASS_NAME, 'login-submit')
# login_button.click()

driver.find_element(By.CSS_SELECTOR, 'input.form-control.private-form__control.login-email').send_keys("Hello")

driver.find_element(By.LINK_TEXT,'Sign up')




time.sleep(2)

driver.close()
driver.quit()