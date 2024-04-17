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
        """place holders"""
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
        self.assertEqual(self.model.id, new_model.id)
        self.assertNotEqual(new_model.created_at, new_model.updated_at)
        self.assertEqual(self.model.created_at, new_model.created_at)

    @unittest.skip
    def test_kwargs(self):
        """place holders"""
        copy = self.model.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is self.model)
        self.assertEqual(new, self.model)

    @unittest.skip
    def test_kwargs_int(self):
        """place holders"""
        copy = self.model.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    @unittest.skip
    def test_save(self):
        """Testing save"""
        self.model.save()
        key = self.name + "." + self.model.id
        with open("file.json", "r") as f:
            j = json.load(f)
            self.assertEqual(j[key], self.model.to_dict())

    @unittest.skip
    def test_str(self):
        """place holders"""
        self.assertEqual(
            str(self.model),
            "[{}] ({}) {}".format(self.name, self.model.id, self.model.__dict__),
        )

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
