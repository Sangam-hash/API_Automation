import requests


class ApiWrapperCalls:

    @staticmethod
    def get_request(url, auth=None):
        response = requests.get(url, auth)
        return response

    @staticmethod
    def post_request(url, headers, payload, auth=None):
        response = requests.post(url=url, auth=auth, headers=headers, json=payload)
        return response

    @staticmethod
    def put_request(url, headers, payload, auth=None, in_json=False):
        response = requests.put(url=url, auth=auth, headers=headers, json=payload)
        if in_json is True:
            return response.json()
        return response

    @staticmethod
    def patch_request(url, headers, payload, auth=None, in_json=False):
        response = requests.patch(url=url, auth=auth, headers=headers, json=payload)
        if in_json is True:
            return response.json()
        return response

    @staticmethod
    def delete_request(url, headers, auth=None):
        response = requests.delete(url=url, auth=auth, headers=headers)
        return response

