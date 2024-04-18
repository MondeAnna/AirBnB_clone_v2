#!/usr/bin/python3


"""Module for testing database storage"""


from unittest.mock import mock_open
from unittest.mock import patch
from unittest.mock import Mock
from unittest import TestCase
from unittest import skip
import json
import os


os.environ["HBNB_TYPE_STORAGE"] = "db"
os.environ["HBNB_ENV"] = "test"


from models.engine import db_storage
from models import storage
from models import HBNB_TYPE_STORAGE


class TestDatabaseStorage(TestCase):
    """Class to test the database storage method"""

    def setUp(self):
        self.amenity = db_storage.Amenity()
        self.city = db_storage.City()
        self.place = db_storage.Place()
        self.review = db_storage.Review()
        self.user = db_storage.User()

    def test_empty_db_return_empty_list_when_using_model(self):
        for model in db_storage.MODELS.values():
            result = storage.all(model)
            self.assertEqual(result, {})
