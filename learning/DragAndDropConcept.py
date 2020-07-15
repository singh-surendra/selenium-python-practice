from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://jqueryui.com/resources/demos/droppable/default.html")
time.sleep(3)

source = driver.find_element(By.ID, 'draggable')
target = driver.find_element(By.ID, 'droppable')

# single action
act_chains = ActionChains(driver)
# act_chains.drag_and_drop(source,target).perform()

# multi- action
act_chains.click_and_hold(source).move_to_element(target).release().perform()

time.sleep(2)

driver.close()
driver.quit()