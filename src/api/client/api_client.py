import os

import requests


class ApiClient:
    """A client for interacting with an API, providing methods to send HTTP requests
    (GET, POST, DELETE, PUT) and manage session data."""

    def __init__(self):
        self.session = requests.session()
        self.api_url = os.environ.get("BASE_URL")
        self.json_headers = {"x-api-key": f"{os.environ.get('API_KEY')}"}
        self.response = None

    def get(self, url, endpoint, body=None, params=None):
        self.response = self.session.get(
            url=url + endpoint,
            data=body,
            params=params,
            headers=self.json_headers,
        )

    def clean_session_cookies(self):
        self.session.cookies.clear()
