#!/usr/bin/python3
""" Module for testing file storage"""
from unittest.mock import Mock
from unittest import TestCase
from copy import deepcopy
import unittest
import os


from models.base_model import BaseModel
from models import storage


class test_fileStorage(TestCase):
    """Class to test the file storage method"""

    def setUp(self):
        """ Set up test environment """

        kwargs = {
            "id": "c9b82080-fe21-4851-a044-0965293161a0",
            "created_at": "2024-04-17T12:25:47.964490",
            "updated_at": "2024-04-17T12:25:47.964490",
            "__class__": "BaseModel",
        }

        self.model_01 = Mock()

        self.model_01.to_dict.return_value = kwargs
        self.model_01.id = kwargs.get("id")

        self.model_02 = deepcopy(self.model_01)
        self.model_02.id = "".join(reversed(self.model_01.id))

        self.identifier_01 = f"{kwargs.get('__class__')}.{self.model_01.id}"
        self.identifier_02 = f"{kwargs.get('__class__')}.{self.model_02.id}"

    '''

    def tearDown(self):
        """ Remove storage file at end of tests """

        try:
            os.remove('file.json')
        except:
            pass
    '''

    def test_storage_is_initially_empty(self):
        """assert that storage is initially empty"""
        self.assertEqual(storage.all(), {})

    def test_adding_and_deleting_unique_id_object_to_storage(self):
        """assert addition and deletion of uniquely id'ed object to storage"""

        storage.new(self.model_01)
        self.assertEqual(storage.all(), {self.identifier_01: self.model_01})

        storage.delete(self.model_01)
        self.assertEqual(storage.all(), {})

    @unittest.skip
    def test_all(self):
        """__objects is properly returned"""
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    @unittest.skip
    def test_base_model_instantiation(self):
        """File is not created on BaseModel save"""
        new = BaseModel()
        self.assertFalse(os.path.exists("file.json"))

    @unittest.skip
    def test_empty(self):
        """Data is saved to file"""
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize("file.json"), 0)

    @unittest.skip
    def test_save(self):
        """FileStorage save method"""
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists("file.json"))

    @unittest.skip
    def test_reload(self):
        """Storage file is successfully loaded to __objects"""
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()["id"], loaded.to_dict()["id"])

    @unittest.skip
    def test_reload_empty(self):
        """Load from an empty file"""
        with open("file.json", "w") as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    @unittest.skip
    def test_reload_from_nonexistent(self):
        """Nothing happens if file does not exist"""
        self.assertEqual(storage.reload(), None)

    @unittest.skip
    def test_base_model_save(self):
        """BaseModel save method calls storage save"""
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists("file.json"))

    @unittest.skip
    def test_type_path(self):
        """Confirm __file_path is string"""
        self.assertEqual(type(storage._FileStorage__file_path), str)

    @unittest.skip
    def test_type_objects(self):
        """Confirm __objects is a dict"""
        self.assertEqual(type(storage.all()), dict)

    @unittest.skip
    def test_key_format(self):
        """Key is properly formatted"""
        new = BaseModel()
        _id = new.to_dict()["id"]
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, "BaseModel" + "." + _id)

    @unittest.skip
    def test_storage_var_created(self):
        """FileStorage object storage created"""
        from models.engine.file_storage import FileStorage

        print(type(storage))
        self.assertEqual(type(storage), FileStorage)
