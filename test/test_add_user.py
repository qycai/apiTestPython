import requests

base_url = "http://localhost:9090"


class TestAddUser:
    # body体存放在json文件，读取文件内容
    @staticmethod
    def get_request_body_file():
        with open("../resources/body/addUserDetails.json") as add_user_body:
            request_body = add_user_body.read()
        print("-----request body is-----", request_body)
        return request_body

    def test_add_user(self):
        api_path = "/api/addUserDetails"
        res = requests.post(base_url + api_path, data=self.get_request_body_file())
        status_code = res.status_code
        assert status_code == 200
