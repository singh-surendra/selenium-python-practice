from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")


# generic function

def select_values(element, text):
    select = Select(element)
    select.select_by_visible_text(text)


def select_values_from_dropdown(dropdownOptionsList, value):
    print(len(dropdownOptionsList))
    for ele in dropdownOptionsList:
        print(ele.text)
        if ele.text == value:
            ele.click()
            break


ele_indus = driver.find_element(By.ID, 'Form_submitForm_Industry')
# select = Select(ele_indus)

# select.select_by_visible_text("Education")
# select.select_by_index(4)
# select.select_by_value("health")
# print(select.is_multiple)

ele_country = driver.find_element(By.ID, 'Form_submitForm_Country')
# select_con = Select(ele_country)
# select_con.select_by_visible_text('India')

select_values(ele_indus, "Education")
select_values(ele_country, 'India')

# to print out all dropdown options
select = Select(ele_indus)
indus_list = select.options
for item in indus_list:
    print(item.text)
    if item.text == 'Automotive':
        item.click()
        break

# select dropdown without Select tag

indus_options = driver.find_elements(By.XPATH, '//select[@id="Form_submitForm_Industry"]//option')
select_values_from_dropdown(indus_options, 'Travel')

time.sleep(2)

driver.close()
driver.quit()
