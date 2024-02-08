#!/usr/bin/python3
"""Unittest for max integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    A class to test a max integer function
    """
    
    def test_max_integer(self):
        """
        Test the max integer in a list of integers when the integers
        are positive of negative numbers
        """
        self.assertIsNone(max_integer([]))
        self.assertAlmostEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertAlmostEqual(max_integer([-2, -1, 0]), 0)
        self.assertAlmostEqual(max_integer([-10, -120, -15, -18]), -10)
        self.assertAlmostEqual(max_integer([1.0, 1.2, 1.3, 2.8, 2.3]), 2.8)
        self.assertAlmostEqual(max_integer([8.8]), 8.8)

    def test_wrong_types(self):
        """
        Test the max integer with wrong parameters types
        """
        with self.assertRaises(TypeError):
            max_integer(None)
    
        with self.assertRaises(TypeError):
            max_integer(['Text1', 1, 2, 'Text2'])
       