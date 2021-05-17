import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
import unittest
from src.app import app


class CreateFileTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.payload = {
            "audioFileType": 1,
            "audioFileMetadata": {"id": 113, "name": "uklele", "duration": 120},
        }
        self.headers = {}
        self.incorrect_payload = "finance"

    def tearDown(self):
        self.client.delete("/delete_file/1/113")
        print("TESTING COMPLETED: create endpoint")

    def test_200(self):
        response = self.client.post(
            "/create_file", headers=self.headers, json=self.payload
        )
        self.assertEqual(response.status_code, 200)

    def test_400(self):
        response = self.client.post(
            "/create_file", headers=self.headers, json=self.incorrect_payload
        )
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
