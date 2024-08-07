import allure
import pytest
from allure_commons.types import AttachmentType
from assertpy import assert_that
from src.utils.api_calls_wrapper import ApiWrapperCalls
from src.payload.payloads import Payloads
from src.helpers.api_headers import Headers
from src.constants.api_constants import URLS


class TestBooking(object):

    @pytest.mark.positive
    @allure.title("Create Booking")
    @allure.description("Creating a booking with a valid payload and verifying if the booking is "
                        "successful")
    def test_valid_booking(self):

        with allure.step(f"Step-1: Making a post call to the URl : \"{URLS.url_create_booking()}\" to create a new "
                         f"booking with valid payload"):
            allure.attach(str(Payloads.payload_create_booking()), name="Request Payload",
                          attachment_type=AttachmentType.JSON)
            response = ApiWrapperCalls.post_request(url=URLS.url_create_booking(),
                                                    headers=Headers.common_headers_json(),
                                                    payload=Payloads.payload_create_booking())

        with allure.step(f"Step-2: Verifying if post call is successful: \"Actual status code:\" {response.status_code}"
                         f" == 200 \"Expected Status Code\" "):
            assert_that(response.status_code).is_equal_to(200) and assert_that(response.json()["bookingid"]).is_true()

        with allure.step(f"step-3: Test Completed. Attaching the post call response to the report for reference"):
            allure.attach(str(response.status_code), name="Response Status Code", attachment_type=AttachmentType.JSON)
            allure.attach(str(response.json()), name="Create Booking Response", attachment_type=AttachmentType.JSON)

    @pytest.mark.positive
    @allure.title("Create Token")
    @allure.description("Creating a Token with a valid Payload")
    def test_create_token(self):

        with allure.step(f"Making a Post Call to {URLS.url_create_token()} with data "
                         f"{Payloads.payload_create_token()}"):
            response = ApiWrapperCalls.post_request(url=URLS.url_create_token(),
                                                    headers=Headers.common_headers_json(),
                                                    payload=Payloads.payload_create_token())

        with allure.step(f"Response for the post call:"):
            allure.attach(str(response.json()), name="Response JSON", attachment_type=AttachmentType.JSON)
            allure.attach(str(response.status_code), name="Response Status Code", attachment_type=AttachmentType.TEXT)

        with allure.step(f"Verifying the {response.status_code} to be 200"):
            assert "token" in response.json() and response.status_code == 200, \
                "Token Not Created and Status Code MisMatch"
        assert_that(response.status_code).is_equal_to(200) and assert_that(response.json()["token"]).is_true()
