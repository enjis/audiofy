import os
import sys
import time

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
import unittest
from src import database
from src.app import app


class TestInsert(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        print("\nRunning Test for adding document to the database")

        self.content = {
            "audioFileType": 1,
            "audioFileMetadata": {"id": 117, "name": "our days", "duration": 410},
        }
        self.expected_result = {"Data Successfully Ingested"}

    def tearDown(self):
        self.client.delete("/delete_file/1/117")
        print("TESTING COMPLETED: db_insert\n")

    def test_db_insert(self):
        result = database.db_insert(self.content)
        self.assertEqual(result, self.expected_result)


class TestSearch(unittest.TestCase):
    def setUp(self):
        print("\nRunning Test for text search")
        self.audioFileType = 3
        self.audioFileID = 107
        self.doc_keys = ["_id", "audioFileMetadata", "audioFileType"]

    def tearDown(self):
        print("TESTING COMPLETED: db_search\n")

    def test_db_search(self):
        timer_start = time.time()
        related_documents = database.db_search(self.audioFileType, self.audioFileID)
        timer_stop = time.time()
        self.assertIsInstance(related_documents, list)
        for document in related_documents:
            self.assertTrue(all([key in self.doc_keys for key in document.keys()]))

        print(
            f"Time taken to retreive search results:{(timer_stop - timer_start) : .2f}sec"
        )


if __name__ == "__main__":
    unittest.main()
