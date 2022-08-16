# First we import all the dependecies.
import time
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import unittest

class SeleniumTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def testGoogle(self):
        # We open the Google home page in Chrome.
        driver = self.driver
        driver.get('https://www.google.com/?client=chrome')

        # We access the search bar, pass in a query and search it.
        searchbar = driver.find_element(By.CLASS_NAME, 'gLFyf')
        searchbar.send_keys("Apple")
        searchbar.submit()

        # We put the programm to sleep temporarily so that the subsequent code isn't
        # executed before the search is complete.
        time.sleep(1)

        # Here, we access the first heading on the search page and get its child-links
        topResults = driver.find_elements(By.XPATH, ".//*[@id='rso']//div//h3/a")
        assert topResults != None, "Page not rendered fully"

    def testApi(self):
        driver = self.driver

        # We reopen  Google to perform an API test.
        driver.get("https://www.google.com")

        for request in driver.requests:
            if request.response:
                print("Request Method: {0}\nRequest Host: {1}\nResquest Status Code: {2}\nRequest Response Date: {3}\n"
                .format(request.method, request.host, request.response.status_code, request.response.date))

    # We then terminate the instance of the driver.
    def destroy(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
