#!/usr/bin/python3
""" place holders """
from models.base_model import BaseModel
import unittest
from datetime import datetime
import string
import json
import os


class test_basemodel(unittest.TestCase):
    """place holders"""

    ALLOWED_ID_CHARS = string.hexdigits.lower() + "-"

    DISALLOWED_ID_CHARS = (
        string.whitespace + string.ascii_uppercase + string.punctuation
    ).replace("-", "")

    def __init__(self, *args, **kwargs):
        """place holders"""

        super().__init__(*args, **kwargs)

    def setUp(self):
        """create non-persistant and unique instance per test"""

        self.name = "BaseModel"
        self.model = BaseModel()

    # patch open at some point
    def tearDown(self):
        try:
            os.remove("file.json")
        except:
            pass

    def test_model_without_kwargs(self):
        """focus on `id`, `created_at` and `updated_at`"""

        id_type = type(self.model.id)
        created_type = type(self.model.created_at)
        updated_type = type(self.model.updated_at)

        self.assertEqual(id_type, str)
        self.assertEqual(created_type, datetime)
        self.assertEqual(updated_type, datetime)

        for char in self.model.id:
            self.assertTrue(char in self.ALLOWED_ID_CHARS)
            self.assertTrue(char not in self.DISALLOWED_ID_CHARS)

        self.assertEqual(self.model.created_at, self.model.updated_at)

    def test_model_with_kwargs(self):
        """focus on `id`, `created_at`,  `updated_at` and `__class__`"""

        kwargs = self.model.to_dict()
        new_model = BaseModel(**kwargs)

        attrs_actual = list(new_model.__dict__.keys())
        attrs_expected = ["id", "created_at", "updated_at"]

        self.assertTrue("__class__" not in new_model.__dict__)
        self.assertEqual(attrs_actual, attrs_expected)

    def test_two_models_are_the_same_when_fundamental_align(self):
        kwargs = self.model.to_dict()
        new_model = BaseModel(**kwargs)
        self.assertEqual(self.model, new_model)

    def test_kwargs_int(self):
        """assert that only strings can be used as kwarg keys"""

        kwargs = self.model.to_dict()
        kwargs.update({1: 2})

        with self.assertRaises(TypeError) as exception:
            BaseModel(**kwargs)

        expected_error = "keywords must be strings"
        actual_error, *_ = exception.exception.args

        self.assertEqual(actual_error, expected_error)

    def test_str(self):
        """assert standardised str formatting"""

        expected = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        actual = str(self.model)
        self.assertEqual(actual, expected)

    @unittest.skip
    def test_todict(self):
        """place holders"""

        n = self.model.to_dict()
        self.assertEqual(self.model.to_dict(), n)

    @unittest.skip
    def test_kwargs_none(self):
        """place holders"""

        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    @unittest.skip
    def test_kwargs_one(self):
        """place holders"""

        n = {"Name": "test"}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    @unittest.skip
    def test_id(self):
        """place holders"""

        id_type = type(self.model.id)
        self.assertEqual(id_type, str)

    @unittest.skip
    def test_created_at(self):
        """place holders"""

        self.assertEqual(type(self.model.created_at), datetime.datetime)

    @unittest.skip
    def test_updated_at(self):
        """place holders"""

        self.assertEqual(type(self.model.updated_at), datetime.datetime)
        n = self.model.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == self.model.updated_at)

    @unittest.skip
    def test_save(self):
        """Testing save"""

        self.model.save()
        key = self.name + "." + self.model.id
        with open("file.json", "r") as f:
            j = json.load(f)
            self.assertEqual(j[key], self.model.to_dict())
