class Headers:

    @staticmethod
    def common_headers_json():
        header = {"Content-Type": "application/json"}
        return header

    @staticmethod
    def common_headers_xml(self):
        header = {"Content-Type": "application/xml"}
        return header

    @staticmethod
    def common_header_put_patch_delete(generated_token):
        header = {
            "Content-Type": "application/json",
            "Cookie": "token="+str(generated_token),
            # "Cookie": f"token={generated_token}"
                   }
        return header
