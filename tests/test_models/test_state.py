#!/usr/bin/python3
"""This is a Module for test State class"""
import unittest
import json
import pep8
import datetime

from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Tests State class implementation"""
    def test_doc_module(self):
        """This is a Module documentation"""
        my_doc = State.__doc__
        self.assertGreater(len(my_doc), 1)

    def test_pep8_conformance_state(self):
        """Test that models/state.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Code style errors Found and warnings")

    def test_pep8_conformance_test_state(self):
        """Test that tests/test_models/test_state.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result_2 = pep8style.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result_2.total_errors, 0,
                         "Code style errors Found and warnings")

    def test_doc_constructor(self):
        """This is Constructor documentation"""
        my_doc = State.__init__.__doc__
        self.assertGreater(len(my_doc), 1)

    def test_class(self):
        """It Validates the types of the attributes in a class"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(State, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(State.name, str)


if __name__ == '__main__':
    unittest.main()
