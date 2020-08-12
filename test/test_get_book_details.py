import requests
import pytest

base_url = "http://localhost:9090"
test_data = ["sanguo", "hongloumeng", "shuihu", "xiyouji"]


class TestGetBookDetails:
    @pytest.mark.parametrize("book_name", test_data)
    def test_get_book_details_by_path_para(self, book_name):
        api_path = f"/api/getBook/{book_name}"

        res = requests.get(url=base_url + api_path)
        status_code = res.status_code
        response_body = res.text

        assert status_code == 200
        assert response_body == "get book with url pattern successfully"
