#!/usr/bin/python3

"""place holder"""
from unittest import TestCase
from models.review import Review


class test_review(TestCase):
    """place holder"""

    def __init__(self, *args, **kwargs):
        """place holder"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """place holder"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """place holder"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """place holder"""
        new = self.value()
        self.assertEqual(type(new.text), str)
