from selenium import webdriver

options = webdriver.FirefoxOptions()
# options.headless = True   or
options.add_argument("--headless")


driver = webdriver.Firefox(executable_path="../drivers/geckodriver", options=options)
driver.get("https://google.com")
print(driver.title)
driver.find_element_by_name("q").send_keys("Autom0tion step by step")
print(driver.title)
driver.close()
driver.quit()
print("Completed")