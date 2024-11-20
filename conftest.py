import pytest
from dotenv import load_dotenv
from src.api.client.api_client import ApiClient

load_dotenv()


@pytest.fixture()
def api():
    api_client = ApiClient()
    yield api_client
    api_client.clean_session_cookies()
