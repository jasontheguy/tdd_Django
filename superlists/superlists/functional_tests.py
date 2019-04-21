from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_list_and_retrieve_later(self):
        #Functional tests follow user Stories like so: Susie Q heard about a new to-do app.
        #She goes to check out it's homepage. 
        self.browser.get('http://localhost:8000') #Test mimics user
        
        #She noticess page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test')

if __name__ == '__main__':
    unittest.main(warnings='ignore')

    