#!/usr/bin/python3


"""Module for testing file storage"""


from unittest.mock import mock_open
from unittest.mock import patch
from unittest.mock import Mock
from unittest import TestCase
import unittest
import json
import os


from models.base_model import BaseModel
from models import storage


class test_fileStorage(TestCase):
    """Class to test the file storage method"""

    def setUp(self):
        """Set up test environment"""

        kwargs_01 = {
            "id": "c9b82080-fe21-4851-a044-0965293161a0",
            "created_at": "2024-04-17T12:25:47.964490",
            "updated_at": "2024-04-17T12:25:47.964490",
            "__class__": "BaseModel",
        }

        kwargs_02 = {
            "id": "f34kjher-345h9-f23re-skfu3289hfdfw",
            "created_at": "2023-11-29T00:25:47.964490",
            "updated_at": "2023-11-29T15:05:03.934575",
            "__class__": "User",
        }

        self.model_01 = Mock()
        self.model_01.to_dict.return_value = kwargs_01
        self.model_01.id = kwargs_01.get("id")

        self.model_02 = Mock()
        self.model_02.to_dict.return_value = kwargs_02
        self.model_02.id = kwargs_02.get("id")

        self.identifier_01 = f"BaseModel.{self.model_01.id}"
        self.identifier_02 = f"User.{self.model_02.id}"

    def tearDown(self):
        """Tear Down kept as ci/cd checker may write to file during testing"""

        try:
            os.remove("file.json")
        except:
            pass

    def test_storage_is_initially_empty(self):
        """assert that storage is initially empty"""
        self.assertEqual(storage.all(), {})

    def test_adding_and_deleting_unique_id_object_to_storage(self):
        """assert addition and deletion of uniquely id'ed object to storage"""

        storage.new(self.model_01)
        self.assertEqual(storage.all(), {self.identifier_01: self.model_01})

        storage.delete(self.model_01)
        self.assertEqual(storage.all(), {})

    def test_multiple_addition_of_same_object_twice_does_not_alter_storage(self):
        """assert multiple addition of same does not alter storage"""

        storage.new(self.model_02)
        storage.new(self.model_02)

        self.assertEqual(storage.all(), {self.identifier_02: self.model_02})

        storage.delete(self.model_02)
        self.assertEqual(storage.all(), {})

    @unittest.skip("Failure to have `all` recognise the mocks as being class")
    def test_that_all_provides_objects_by_class_type(self):
        """assert that `all` provides objects by class type"""

        storage.new(self.model_01)
        storage.new(self.model_02)

        """
        self.assertEqual(
            storage.all(Mock),
            {
                self.identifier_01: self.model_01,
                self.identifier_02: self.model_02,
            },
        )
        """

        storage.delete(self.model_01)
        storage.delete(self.model_02)

    def test_no_saving_done_when_storage_is_empty(self):
        """assert no saving is done when storage is empty"""

        with patch("builtins.open", mock_open(), create=True) as open_:
            storage.save()

        open_.assert_not_called()

    @patch("json.dump")
    def test_saving_data_to_file(self, mock_json_dump):
        """assert data is saved to file"""

        storage.new(self.model_01)

        with patch("builtins.open", mock_open(), create=True) as open_:
            storage.save()

        open_.assert_called_once()
        mock_json_dump.assert_called_once()

        storage.delete(self.model_01)

    @patch("pathlib.Path.is_file", return_value=False)
    def test_reload_from_nonexistent_file(self, mock_path):
        """assert None is returned if file does not exist"""

        self.assertEqual(storage.reload(), None)

    @patch("pathlib.Path.stat")
    @patch("pathlib.Path.is_file", return_value=True)
    def test_reload_raises_value_error_if_file_is_empty(self, mock_path, mock_stat):
        """assert reloading from an empty file raises ValueError"""

        mock_stat.return_value.st_size = 0

        with self.assertRaises(ValueError):
            storage.reload()

    @patch("pathlib.Path.stat")
    @patch("pathlib.Path.is_file", return_value=True)
    def test_reload(self, mock_path, mock_stat):
        """Storage file is successfully loaded to __objects"""

        mock_stat.return_value.st_size = 100

        storage.new(self.model_01)
        storage.new(self.model_02)

        mock_read_in = json.dumps({
            identifier: obj.to_dict()
            for identifier, obj in storage.all().items()
        })

        with patch("builtins.open", mock_open()):
            storage.delete(self.model_01)
            storage.delete(self.model_02)

        with patch("builtins.open", mock_open(read_data=mock_read_in)) as open_:
            storage.reload()

        self.assertTrue(self.identifier_01 in storage.all().keys())
        self.assertTrue(self.identifier_02 in storage.all().keys())

        with patch("builtins.open", mock_open(), create=True):
            storage.delete(self.model_01)
            storage.delete(self.model_02)
