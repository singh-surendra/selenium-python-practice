from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def select_values(options_list, value_list):
    if  not values_list[0] == 'all':
        for element in options_list:
            print(element.text)
            for k in range(len(value_list)):
                if element.text == value_list[k]:
                    element.click()
                    break
    else:
        try:
            for element in options_list:
                element.click()
        except Exception as e:
            print(e)



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
time.sleep(2)

driver.find_element(By.ID, 'justAnInputBox').click()
time.sleep(2)

dropdown_list = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')
# values_list = ['choice 2', 'choice 3', 'choice 6 2 1']
# values_list = ['choice 2']

# to select all options in dropdown
values_list = ['all']
select_values(dropdown_list, values_list)

# for element in dropdown_list:
#     print(element.text)
#     if element.text == 'choice 2':
#         element.click()
#         break


time.sleep(2)

driver.close()
driver.quit()
