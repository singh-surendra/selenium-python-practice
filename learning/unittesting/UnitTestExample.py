import unittest
from Examples import Example
# https://stackoverflow.com/questions/1322575/what-numbers-can-you-pass-as-verbosity-in-running-python-unit-test-suites
# https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("this will run before all methods")

    @classmethod
    def tearDownClass(cls):
        print("this will run after all methods")

    def setUp(self):
        print("this will run before each method")

    def tearDown(self) -> None:
        print("this will run after each method")

    def test_add(self):
        result = Example.add(self, 10, 20)
        self.assertEqual(result, 30)

    def test_add(self):
        result = Example.sub(self, 20, 10)
        self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()
