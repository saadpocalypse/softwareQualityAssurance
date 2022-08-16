# First we download all the dependecies.
from selenium import webdriver
import os 
from selenium.webdriver.common.by import By
import time

# This is so we can get the current working directory for chromedriver.
cwdVariable = os.getcwd() + "/chromedriver"
driver = webdriver.Chrome(cwdVariable)

# We open the Google home page in Chrome.
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
for childLink in topResults:
    print(childLink.get_attribute("href"))

# We wait for the code to execute and then quit the driver.
time.sleep(1)
driver.quit()