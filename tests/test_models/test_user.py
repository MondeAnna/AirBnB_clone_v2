#!/usr/bin/python3
"""place holder"""
from unittest import TestCase
from models.user import User


class test_User(TestCase):
    """place holder"""

    def setUp(self):
        """place holder"""
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """place holder"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """place holder"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """place holder"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """place holder"""
        new = self.value()
        self.assertEqual(type(new.password), str)
