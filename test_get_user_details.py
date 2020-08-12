import requests


def test_get_user_details():
    base_url = "http://localhost:9090"
    api_path = "/api/getUserDetails"

    res = requests.get(url=base_url + api_path)
    response = res.json()
    status_code = res.status_code

    assert status_code == 200
    assert response["name"] == "qycai"
    assert response["age"] == 18
