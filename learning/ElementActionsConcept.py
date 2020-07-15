from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://classic.crmpro.com/")
time.sleep(2)

username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')
login_button = driver.find_element(By.XPATH, "//input[@value='Login']")

act_chains = ActionChains(driver)

act_chains.send_keys_to_element(username, "HelloSuri")
act_chains.send_keys_to_element(password, "Test@12")
act_chains.click(login_button).perform()

time.sleep(2)
driver.close()
driver.quit()
