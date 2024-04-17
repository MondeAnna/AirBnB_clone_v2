#!/usr/bin/python3
""" place holders """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ place holders """

    def __init__(self, *args, **kwargs):
        """ place holders """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ place holders """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    @unittest.skip
    def test_default(self):
        """ place holders """
        i = self.value()
        self.assertEqual(type(i), self.value)

    @unittest.skip
    def test_kwargs(self):
        """ place holders """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)
        self.assertEqual(new, i)

    @unittest.skip
    def test_kwargs_int(self):
        """ place holders """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    @unittest.skip
    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    @unittest.skip
    def test_str(self):
        """ place holders """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    @unittest.skip
    def test_todict(self):
        """ place holders """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    @unittest.skip
    def test_kwargs_none(self):
        """ place holders """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    @unittest.skip
    def test_kwargs_one(self):
        """ place holders """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    @unittest.skip
    def test_id(self):
        """ place holders """
        new = self.value()
        self.assertEqual(type(new.id), str)

    @unittest.skip
    def test_created_at(self):
        """ place holders """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    @unittest.skip
    def test_updated_at(self):
        """ place holders """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
