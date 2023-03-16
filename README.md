# Rostelecom-testing
Final project for SkillFactory QA course

Files
-----

[conftest.py](conftest.py) contains all the required code to catch failed test cases and make screenshot
of the page in case any test case will fail.

[pages/base.py](pages/base.py) contains PageObject pattern implementation for Python.

[pages/elements.py](pages/elements.py) contains helper class to define web elements on web pages.

[registration.txt](registration.txt) contains the sets of invalid (incorrect) data used for negative testing of registration page. The sets are created with the help of pairwiseTool.

[fields.py](fields.py) contains the sets of invalid (incorrect) data taken from 'registration.txt' and turned into variables. There're also lists of incorrect data used in other negative testings.


DotEnv file
-----------

I used .env file to store my email (valid_email), phone (valid_phone), login (valid_login), personal account number (valid_ls) and password (valid_password) for my Rostelecom account. Note that I used the same password in all the cases, so there's only one variable for it.


How To Run Tests
----------------

1) Install all requirements:

    ```bash
    pip3 install -r requirements
    ```

2) Download Selenium WebDriver from https://chromedriver.chromium.org/downloads (choose version which is compatible with your browser)

3) Run tests:

    ```bash
    python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
    ```

   ![alt text](example.png)
