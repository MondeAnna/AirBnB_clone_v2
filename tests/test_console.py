#!/usr/bin/python3
"""Test suite for the console module"""
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
