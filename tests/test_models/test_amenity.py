#!/usr/bin/python3


"""Test suite for the amenity module"""


from unittest import TestCase


from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(TestCase):

    """Collective testing of base model attributes"""

    def setUp(self):
        """Provide a factory for test instances"""

        self.amenity = Amenity()

    def test_initialisation_has_empty_attr(self):
        """Provide a factory for test instances"""

        self.assertEqual(self.amenity.name, "")

    def test_inheritance(self):
        """Assert is subclass of BaseModel"""

        self.assertTrue(issubclass(Amenity, BaseModel))
