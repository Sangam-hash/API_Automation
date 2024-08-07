class Payloads:

    @staticmethod
    def payload_create_booking():
        payload = {
            "firstname": "Python",
            "lastname": "API Testing",
            "totalprice": 111,
            "depositpaid": "true",
            "bookingdates": {
                       "checkin": "2018-01-01",
                       "checkout": "2019-01-01"},
            "additionalneeds": "Breakfast"
        }
        return payload

    @staticmethod
    def payload_create_booking_1():
        payload = {
            "firstname": "Sangam",
            "lastname": "API Testing",
            "totalprice": 100,
            "depositpaid": "true",
            "bookingdates": {
                       "checkin": "2018-01-01",
                       "checkout": "2019-01-01"},
            "additionalneeds": "Breakfast"
        }
        return payload

    @staticmethod
    def payload_create_booking_negative():
        payload = {
            "firstname": "Jim",
            "depositpaid": "true",
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"},
            "additionalneeds": "Breakfast"
        }
        return payload

    @staticmethod
    def payload_create_token():
        payload = {
            "username": "admin",
            "password": "password123"
        }
        return payload

    @staticmethod
    def payload_update_booking():
        payload = {
            "firstname": "Updated_firstname",
            "lastname": "Updated_lastname",
            "totalprice": 111,
            "depositpaid": "true",
            "bookingdates": {
                       "checkin": "2018-01-01",
                       "checkout": "2019-01-01"},
            "additionalneeds": "Breakfast"
        }
        return payload
