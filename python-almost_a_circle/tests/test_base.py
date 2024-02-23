#!/usr/bin/python3
"""Test base.py"""
import unittest
from models.base import Base


class Test_Base_Class(unittest.TestCase):
    """Test cases for the constructor of Base class."""

    def test_constructor_initialization(self):
        """Test constructor initializes id attrinute when id is provided."""
        test_id = 100
        obj = Base(id=test_id)
        # Check if id attribute is initialized correctly
        self.assertEqual(obj.id, test_id)

    def test_constructor_without_id(self):
        """Test constructor initializes id if it is NOT provided."""
        obj = Base()
        # check if id attribute is created
        self.assertTrue(hasattr(obj, 'id'))
        # Check if id attribute is an integer
        self.assertIsInstance(obj.id, int)
        # Check if id attribute is not None
        self.assertNotEqual(obj.id, None)
        # Check if id is equal to __nb_object
        self.assertEqual(obj.id, Base._Base__nb_objects)

    def test_unique_id_generation(self):
        """Test constructor generate unique id for each instance."""
        obj1 = Base()
        obj2 = Base()
        # Check if id of obj1 is equal with id of obj2
        self.assertNotEqual(obj1.id, obj2.id)

    def test_positive_id(self):
        """Test if id is positive."""
        test_id = 19
        obj = Base(id=test_id)
        # Check if id attribute is initialized correctly
        self.assertEqual(obj.id, test_id)

    def test_negative_id(self):
        """Test if id is negative."""
        test_id = -19
        obj = Base(id=test_id)
        # Check if id attribute is initialized correctly
        self.assertEqual(obj.id, test_id)

    def test_zero_id(self):
        """Test if id is negative."""
        test_id = 0
        obj = Base(id=test_id)
        # Check if id attribute is initialized correctly
        self.assertEqual(obj.id, test_id)
