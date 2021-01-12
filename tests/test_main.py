import unittest

from fastapi.testclient import TestClient

from main import app


class MainTests(unittest.TestCase):

    def setUp(self):
        self.test_client = TestClient(app)
        self.expected_response = {
            "pub_id": "123ABC",
            "clean_abstract": ["one", "two", "three"]
        }

    def test_good_post_response(self):
        response = self.test_client.post(
            "/clean/",
            json={"pub_id": "123ABC", "abstract": "One,two and three."},
        )
        assert response.status_code == 200
        assert response.json() == self.expected_response