import requests
import pytest

base_url = "http://localhost:9090"


class TestGetUserDetails:

    def test_get_user_details(self):
        api_path = "/api/getUserDetails"
        res = requests.get(url=base_url + api_path)
        response = res.json()
        status_code = res.status_code

        assert status_code == 200
        assert response["name"] == "qycai"
        assert response["age"] == 18


name_age = [("connie", 11), ("qycai", 18)]


@pytest.mark.parametrize("username, age", name_age)
def test_get_user_details_by_name_and_age(username, age):
    api_path = "/api/getUserByNameAndAge"
    # params参数指定query parameters
    res = requests.get(url=base_url + api_path, params={"name": username, "age": age})
    print(res.text)
    response_body = res.text
    status_code = res.status_code

    assert status_code == 200
    assert response_body == "get user by name and age successfully"
