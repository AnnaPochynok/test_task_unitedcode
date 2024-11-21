Description
---
Automated API tests as tech tasks

    .
    ├── data                    # Various data files that are used for tests
    │   ├── constants           # Test data that are used in tests
    ├── src                     # Test framework source files with tests implementation
    │   ├── api                 # API tests source files
    ├── tests                   # test files
    │   ├── api                 # API tests
    ├── .env                    # Environment variables for local run 
    ├── .gitignore              # List files and dirs ignored by git
    ├── conftest.py             # Fixture files related to all test types
    ├── README.md               # Project description
    └── requirements.txt        # Project related packages

Preconditions (local)
---
Make sure you have `git`, `python3` and `pip3` installed. Note: Python 3.9.16 is recommended.

Prepare local environment
---
* Clone the project to your local machine and navigate to the project directory:
```shell
git clone https://github.com/AnnaPochynok/test_task_unitedcode.git
cd test_task_unitedcode
```
* Install and setup virtualenv for the project:
```shell
pip install virtualenv
virtualenv --python python3 venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```
* Install all packages required for the tests run:
```shell
pip install -r requirements.txt
```
----

## Setting the API Key
This project uses The Cat API for testing. To simplify usage, a default API key is already included in the code and does not require additional setup.
The default API key is:
```shell
live_ysU1HpwSOWxYSYNUkBUHQdzOYYFl5WAdlir4M8Y1ubWG357wPzG4BmdZHiQDRwGT
```
If you have your own API key and wish to use it, you can override it in the .env file in the root of project: `API_KEY=<your_api_key>`

If you don't have your own API_KEY, follow these steps to obtain your key and set it up in the project:

Step 1: Register on The Cat API
* Visit The Cat API. https://thecatapi.com/
* Click on Get Your API KEY.
* Click on Get Free Access.
* Complete the process by providing your email and app description.
* Get you own API KEY from the received email letter.

Step 2: Add Your API Key to the .env file:
* Open the .env file and override the line: `API_KEY=<your_api_key>`

Running tests locally
---

## Run all tests

Once the environment is ready the tests can be executed. Run the following command to do so:
```shell
pytest tests
```

## Run tests with HTML reporting

To run tests with HTML reporting add the argument `--html=reports/test_report.html` to the command.
```shell
pytest --html=reports/test_report.html
```

To open generated report you can open the file directly from the terminal
```shell
open reports/test_report.html
```
