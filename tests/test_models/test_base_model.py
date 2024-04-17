#!/usr/bin/python3


"""test suite for base model"""


from unittest.mock import mock_open
from unittest.mock import patch
from unittest import TestCase
import datetime
import string
import os


from models.base_model import BaseModel


class TestBaseModel(TestCase):
    """place holders"""

    ALLOWED_ID_CHARS = string.hexdigits.lower() + "-"

    DISALLOWED_ID_CHARS = (
        string.whitespace + string.ascii_uppercase + string.punctuation
    ).replace("-", "")

    def setUp(self):
        """create non-persistant and unique instance per test"""

        self.model = BaseModel()

    def test_model_without_kwargs(self):
        """focus on `id`, `created_at` and `updated_at`"""

        id_type = type(self.model.id)
        created_type = type(self.model.created_at)
        updated_type = type(self.model.updated_at)

        self.assertEqual(id_type, str)
        self.assertEqual(created_type, datetime.datetime)
        self.assertEqual(updated_type, datetime.datetime)

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

    def test_equality_of_separate_models(self):
        """assert instance equality"""

        kwargs = self.model.to_dict()
        new_model = BaseModel(**kwargs)
        self.assertEqual(self.model, new_model)

    def test_invalid_kwargs_keywords(self):
        """assert non-string kwarg keys are erroneous"""

        expected_error = "keywords must be strings"
        kwargs = self.model.to_dict()
        kwargs.update({1: 2})

        with self.assertRaises(TypeError) as exception:
            BaseModel(**kwargs)

        actual_error, *_ = exception.exception.args
        self.assertEqual(actual_error, expected_error)

        kwargs = self.model.to_dict()
        kwargs.update({None: None})

        with self.assertRaises(TypeError) as exception:
            BaseModel(**kwargs)

        actual_error, *_ = exception.exception.args
        self.assertEqual(actual_error, expected_error)

    def test_invalid_keys_in_kwargs(self):
        """assert only lowercased strings to be kwarg keys"""

        expected_error = "__class__"
        kwargs = {"Name": "test"}

        with self.assertRaises(KeyError) as exception:
            BaseModel(**kwargs)

        actual_error, *_ = exception.exception.args
        self.assertEqual(actual_error, expected_error)

    def test_str(self):
        """assert standardised str formatting"""

        expected = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        actual = str(self.model)
        self.assertEqual(actual, expected)

    def test_updated_at(self):
        """assert instantiating with kwargs alters `updated_at`"""

        kwargs = self.model.to_dict()
        new_model = BaseModel(**kwargs)

        self.assertNotEqual(new_model.created_at, new_model.updated_at)

    def test_save_to_file(self):
        """assert saving renders instance to file storage"""

        with patch("builtins.open", mock_open(), create=True) as open_:
            self.model.save()

        open_.assert_called_once()
