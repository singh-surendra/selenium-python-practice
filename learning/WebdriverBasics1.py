import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome("../drivers/chromedriver")
# or
driver = webdriver.Chrome(executable_path="../drivers/chromedriver")
driver.set_page_load_timeout(10)
driver.implicitly_wait(10)
driver.get("https://www.google.com/")

# enter "naveen automationlabs" in google search and then select youtube option from the list
driver.find_element(By.NAME,'q').send_keys("Naveen Automationlabs")
time.sleep(2)
optionsList = driver.find_elements(By.CSS_SELECTOR,'ul.erkvQe li span')
print(len(optionsList))

for ele in optionsList:
    print(ele.text)
    if ele.text == 'naveen automationlabs youtube':
        ele.click()
        break

driver.close()
driver.quit()

print("test is complete")