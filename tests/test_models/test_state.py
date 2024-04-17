#!/usr/bin/python3


"""Test suite for the state module"""


from unittest import TestCase


from models.base_model import BaseModel
from models.state import State


class TestState(TestCase):

    """Collective testing of base model attributes"""

    def setUp(self):
        """Provide a factory for test instances"""

        self.state = State()

    def test_initialisation_has_empty_attr(self):
        """Provide a factory for test instances"""

        self.assertEqual(self.state.name, "")

    def test_inheritance(self):
        """Assert is subclass of BaseModel"""

        self.assertTrue(issubclass(State, BaseModel))
