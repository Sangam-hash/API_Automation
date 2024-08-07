import pytest
from src.utils.api_calls_wrapper import ApiWrapperCalls
from src.payload.payloads import Payloads
from src.helpers.api_headers import Headers
from src.constants.api_constants import URLS


@pytest.fixture(scope="class")
def create_token():
    response = ApiWrapperCalls.post_request(url=URLS.url_create_token(),
                                            headers=Headers.common_headers_json(),
                                            payload=Payloads.payload_create_token())
    return response.json()["token"]
