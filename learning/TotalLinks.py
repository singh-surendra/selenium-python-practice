from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("https://www.amazon.in/")

linksList = driver.find_elements(By.TAG_NAME, 'a')
print(len(linksList))

for element in linksList:
    link_text = element.text
    print(link_text)
    print(element.get_attribute('href'))

imageList = driver.find_elements(By.TAG_NAME, 'img')
print(len(imageList))
for element in imageList:
    print(element.get_attribute('src'))








time.sleep(2)

driver.close()
driver.quit()