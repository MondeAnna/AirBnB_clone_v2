#!/usr/bin/python3
"""Test suite for the console module"""
from unittest.mock import patch
import unittest
import cmd
from console import HBNBCommand

class test_console(unittest.TestCase):

    def setUp(self):
        """Provide a factory for test instances"""
        self.cmd = HBNBCommand()

    def test_inheritance(self):
        """Assert is subclass of BaseModel"""
        self.assertTrue(issubclass(HBNBCommand, cmd.Cmd))

    @patch("console.storage")
    def test_create(self, mock_storage):
        """
        we have to mock console printout and mock storage so we
        can see if we actually created the model instance

        does checking to see if we created the model not then
        mean that our test is coupled to the model and by extension
        the model structure?
        """
        self.assertTrue(True)
