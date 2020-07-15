from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

browserName = "chrome"

if browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "firefox":
    driver = webdriver.Firefox(executable_path= GeckoDriverManager().install())
elif browserName == "safari":
    driver = webdriver.Safari()
else:
    print("plaese pass the correct browser name :" + browserName)
    raise Exception('driver is not found')

driver.implicitly_wait(5)
driver.get("https://app.hubspot.com/login")
driver.find_element(By.ID,'username').send_keys("surendra0123@gmailcom")
driver.find_element(By.ID,'password').send_keys("Test@12345")
driver.find_element(By.ID,'loginBtn').click()
print(driver.title)
time.sleep(4)
driver.close()
driver.quit()




