from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.spicejet.com/")
time.sleep(3)
'''this is my move to element'''

login_ele = driver.find_element(By.ID, 'ctl00_HyperLinkLogin')
act_chains = ActionChains(driver)
act_chains.move_to_element(login_ele).perform()

spiceClub_member_ele = driver.find_element(By.LINK_TEXT, 'SpiceClub Members')
act_chains.move_to_element(spiceClub_member_ele).perform()

member_login = driver.find_element(By.LINK_TEXT, 'Member Login')
member_login.click()

time.sleep(2)

driver.close()
driver.quit()