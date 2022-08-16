# Assignment 2

# Requirements
* First and foremost, you need Selenium.
* Download pip from [here.](https://pip.pypa.io/en/stable/installation/)
* In Terminal, write the following commands:

  ``` pip install Selenium```<br>
  ```pip install selenium-wire``` <br>
  ```pip install webdriver-manager```

* One Selenium is installed, we need to download the WebDriver for Chrome from [here.](https://chromedriver.chromium.org/downloads)
* Put the ChromeDriver in the same folder as your Python file running that would run the test. All the requirements have now been met.
* On MacOS, running ChromeDriver for the first time requires allowing its operations to be executed through Security & Privacy settings in System Preferences.
* WebDriver Manager makes separately downloading the WebDriver redundant, as it downloads it at runtime.
* Selenium Wire is used to catch API requests.


<br>

# Procedure
I wrote 2 tests. 

## Test 1
In Test 1, I am checking to see if the WebScraping I am doing is working correctly.

<br>

1. The homepage for Google is accessed (note: The prompt at the top saying "Chrome is being controlled by automated test software" is a telltale sign of a test being run in Selenium).
<img width="1077" alt="Screenshot 2022-08-16 at 7 54 23 PM" src="https://user-images.githubusercontent.com/64619851/184911212-68e63c55-e382-4c07-a3a1-5f5f675509dc.png">

<br>

2. A search is made for the query "Apple".
<img width="1187" alt="Screenshot 2022-08-16 at 7 18 28 PM" src="https://user-images.githubusercontent.com/64619851/184904228-b078c049-f4db-4bde-8cfa-b3f1153a2c9e.png">

<br>

3. The child-links for the first heading are accessed (iPhone, Mac, Watch, iPad, etc).
<img width="422" alt="Screenshot 2022-08-16 at 7 53 24 PM" src="https://user-images.githubusercontent.com/64619851/184910718-95616e69-0808-4876-8467-22eb3a72beed.png">

<br>

4. I check to see if the page has loaded. This is one of the tests being performed. The screenshot below shows that the results are being accessed and printed.
<img width="224" alt="Screenshot 2022-08-16 at 11 22 56 PM" src="https://user-images.githubusercontent.com/64619851/184951498-3ad86769-f67c-4886-8e0a-2a080729c340.png">

## Test 2
Test 2 deals with API testing. The initial procedure is the same as before but here I print the network requests made in the process. <br>
<img width="395" alt="Screenshot 2022-08-16 at 11 27 20 PM" src="https://user-images.githubusercontent.com/64619851/184952258-5e33b482-3bee-48d5-9fc5-76d7ba432740.png">

## Conclusion
Both tests are running smoothly and successfully. <br>
<img width="556" alt="Screenshot 2022-08-16 at 11 28 28 PM" src="https://user-images.githubusercontent.com/64619851/184952374-1aaba67b-a209-4d8d-b287-4824188bda8f.png">




# Functions

| Function      | Purpose |
| ----------- | ----------- |
| ``get``    | We use this to open a URL, in this case we open Google. |
| ``sleep``    | We stall the program appropriately to ensure proper execution of tasks. |
| ``find_element``    | We access the search bar on Google's homepage and the links after the search is performed. |
| ``send_keys``    | We pass a query to the searchbox, in our case it is "Apple". |
| ``submit``    | We submit the query and perform the search. |
| ``close``    | We close the ChromeDriver instance. |
