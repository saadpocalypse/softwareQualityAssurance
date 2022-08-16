# Assignment 2

# Requirements
* First and foremost, you need Selenium.
* Download pip from [here.](https://pip.pypa.io/en/stable/installation/)
* In Terminal, write the following command:

  ``` pip install Selenium```

* One Selenium is installed, we need to download the WebDriver for Chrome from [here.](https://chromedriver.chromium.org/downloads)
* Put the ChromeDriver in the same folder as your Python file running that would run the test. All the requirements have now been met.
* On MacOS, running ChromeDriver for the first time requires allowing its operations to be executed through Security & Privacy settings in System Preferences.

<br>

# Procedure
The test I wrote works in 4 essential steps.
1. The homepage for Google is accessed.
<img width="1077" alt="Screenshot 2022-08-16 at 7 54 23 PM" src="https://user-images.githubusercontent.com/64619851/184911212-68e63c55-e382-4c07-a3a1-5f5f675509dc.png">


2. A search is made for the query "Apple" (note: The prompt at the top saying "Chrome is being controlled by automated test software").
<img width="1187" alt="Screenshot 2022-08-16 at 7 18 28 PM" src="https://user-images.githubusercontent.com/64619851/184904228-b078c049-f4db-4bde-8cfa-b3f1153a2c9e.png">


3. The child-links for the first heading are accessed (iPhone, Mac, Watch, iPad).
<img width="422" alt="Screenshot 2022-08-16 at 7 53 24 PM" src="https://user-images.githubusercontent.com/64619851/184910718-95616e69-0808-4876-8467-22eb3a72beed.png">


4. The links are displayed in the Terminal.
<img width="1080" alt="Screenshot 2022-08-16 at 7 28 37 PM" src="https://user-images.githubusercontent.com/64619851/184905214-4daabef4-b49e-4d4d-b3c0-0eb38b23648a.png">

<br>

# Test Cases

| Function      | Purpose |
| ----------- | ----------- |
| ``get``    | We use this to open a URL, in this case we open Google. |
| ``sleep``    | We stall the program appropriately to ensure proper execution of tasks. |
| ``getcwd``    | We get the current working directory for ChromeDriver. |
| ``find_element``    | We access the search bar on Google's homepage and the links after the search is performed. |
| ``send_keys``    | We pass a query to the searchbox, in our case it is "Apple". |
| ``submit``    | We submit the query and perform the search. |
| ``close``    | We close the ChromeDriver instance. |
