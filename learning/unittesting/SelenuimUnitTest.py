import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

import HtmlTestRunner



class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    @classmethod
    def tearDownClass(cls):
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

    @unittest.skip("This is a skipped test.")
    def test_skip(self):
        """ This test should be skipped. """
        pass

if __name__ == '__main__':
    # unittest.main(verbosity=2)
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/surendra.singh/Documents/SuriPersonal/Pyhton/selenium-python-practice/reports',verbosity=2))

# verbosity can be added directly from CLI as well : python -v <filename>