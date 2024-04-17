#!/usr/bin/python3


"""Test suite for the city module"""


from unittest import TestCase


from models.base_model import Base, BaseModel
from models.state import State


class TestState(TestCase):
    """Collective testing of city model attributes"""

    def __init__(self, *args, **kwargs):
        """place"""

        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """place"""

        new = self.value()
        self.assertEqual(type(new.name), str)
