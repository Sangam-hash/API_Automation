import allure
import pytest
from allure_commons.types import AttachmentType
from assertpy import assert_that
from src.utils.api_calls_wrapper import ApiWrapperCalls
from src.payload.payloads import Payloads
from src.helpers.api_headers import Headers
from src.constants.api_constants import URLS


@pytest.mark.usefixtures("create_token")
class TestDataDrivenBooking:

    @pytest.mark.data_driven
    @allure.title("Data Driven")
    @allure.description("Creating Multiple Bookings")
    @pytest.mark.parametrize("payloads", [Payloads.payload_create_booking(), Payloads.payload_create_booking_1()])
    def test_datadriven_bookings(self, payloads, create_token):

        with allure.step(f"Creating booking with Payload {payloads} and {create_token}"):
            response = ApiWrapperCalls.post_request(url=URLS.url_create_booking(),
                                                    headers=Headers.common_headers_json(),
                                                    payload=payloads)

        with allure.step(f"Verifying that the : (Actual Status Code) : {response.status_code} "
                         f"== 200 : (Expected Status Code)"):
            assert_that(response.status_code).is_equal_to(200)

        with allure.step(f"Verifying if the booking is created: {response.json()["bookingid"]}"):
            assert_that(response.json()).contains("bookingid")

    @pytest.mark.negative
    @allure.title("Create Invalid Booking")
    @allure.description("Creating a booking with a invalid payload and verifying that the booking is not successful")
    def test_create_invalid_booking(self):

        with allure.step(f"Step-1: Making a post call to the URl : \"{URLS.url_create_booking()}\" with invalid "
                         f"payload which is empty"):
            allure.attach(str({}), name="Empty Request Payload",
                          attachment_type=AttachmentType.JSON)
            response = ApiWrapperCalls.post_request(url=URLS.url_create_booking(),
                                                    headers=Headers.common_headers_json(),
                                                    payload={})

        with allure.step(f"Step-2: Verifying that the post call should Fail: \"Actual status code:\" "
                         f"{response.status_code} == 500 \"Expected Status Code\" "):
            allure.attach(str(response.status_code), name="Response Status Code", attachment_type=AttachmentType.TEXT)
            assert_that(response.status_code).is_equal_to(500)
