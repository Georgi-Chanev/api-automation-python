# API Automation with Python & PyTest

This is a simple API automation project using Python, PyTest and the `requests` library.  
The tests use the public API at https://reqres.in and demonstrate basic API checks such as:

- GET requests
- POST requests
- Status code validation
- JSON structure validation
- Simple reusable API client

## Project structure

api-automation-python/
│
├── tests/
│   ├── test_users.py
│   ├── test_status.py
│
├── utils/
│   └── api_client.py
│
├── requirements.txt
├── README.md
└── pytest.ini

## How to run

Install dependencies:

pip install -r requirements.txt

Run tests:

pytest -v
