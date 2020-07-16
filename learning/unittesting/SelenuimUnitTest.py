import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time



class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()

    def test_search_1(self):
        self.driver.get("https://www.google.com/")
        self.driver.find_element_by_name("q").send_keys("Automation step by step")
        self.driver.find_element_by_name("btnK").click()
        time.sleep(2)
        title = self.driver.title
        print(title)
        self.assertEquals(title, 'Automation step by step - Google Search')



    def test_search_2(self):
        self.driver.get("https://www.google.com/")
        self.driver.find_element_by_name("q").send_keys("Surendra Singh")
        self.driver.find_element_by_name("btnK").click()
        time.sleep(2)
        title = self.driver.title
        print(title)
        self.assertEquals(title, 'Surendra Singh - Google Search')

if __name__ == '__main__':
    unittest.main(verbosity=2)

# verbosity can be added directly from CLI as well : python -v <filename>