#!/usr/bin/python3


"""Test suite for the city module"""


from importlib import import_module
from unittest.mock import Mock
from unittest import TestCase


from models.base_model import Base, BaseModel
from models.city import City


class TestCityFileStorage(TestCase):
    """Collective testing of city model attributes for file storage"""

    def setUp(self):
        """Provide a factory for test instances"""

        self.city = City()

    def test_initialisation_has_empty_attr(self):
        """Provide a factory for test instances"""

        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")

    def test_inheritance(self):
        """Assert is subclass of BaseModel"""

        self.assertTrue(issubclass(City, BaseModel))
        self.assertTrue(issubclass(City, Base))
