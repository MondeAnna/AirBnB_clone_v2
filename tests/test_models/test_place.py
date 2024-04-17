#!/usr/bin/python3
"""place holder"""
from unittest import TestCase
from models.place import Place


class test_Place(TestCase):
    """place holder"""

    def setUp(self):
        """place holder"""
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """place holder"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """place holder"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """place holder"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """place holder"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """place holder"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """place holder"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """place holder"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """place holder"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """place holder"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """place holder"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """place holder"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
