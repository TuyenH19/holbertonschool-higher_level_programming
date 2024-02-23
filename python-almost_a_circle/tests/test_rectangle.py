#!/usr/bin/python3
"""Test Rectangle class."""


import unittest
from models.base import Base
from models.rectangle import Rectangle

class Test_Rectangle_class(unittest.TestCase):
    """Test cases for Rectangle class."""

    def test_constructor_without_id(self):
        """Test constructor initializes id attrinute when id is NOT provided."""
        rect = Rectangle(2, 10)
        self.assertTrue(hasattr(rect, 'id'))  # check if id attribute is created
        self.assertIsInstance(rect.id, int)  # Check if id attribute is an integer
        self.assertIsInstance(rect.width, int)  # Check if width attribute is an integer
        self.assertIsInstance(rect.height, int)  # Check if height attribute is an integer
        self.assertNotEqual(rect.id, None)  # Check if id attribute is not None
        self.assertNotEqual(rect.width, None)  # Check if width attribute is not None
        self.assertNotEqual(rect.height, None)  # Check if height attribute is not None
        self.assertEqual(rect.id, Base._Base__nb_objects)  # Check if id is equal to __nb_object

    def test_unique_id_generation(self):
        """Test constructor generate unique id for each instance."""
        rect1 = Rectangle(2, 10)
        rect2 = Rectangle(3, 11)
        self.assertNotEqual(rect1, rect2)  # Check if id of rect1 is equal with id of rect2

    def test_width_error(self):
        """Test if width attribute raise a TypeError and ValueError."""
        with self.assertRaises(TypeError):
            rect = Rectangle('Text', 1)  # Check if width raise TypeError when set it a string
        with self.assertRaises(TypeError):
            rect = Rectangle((1,), 1)  # Check if width raise TypeError when set it a tuple
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 1)  # Check if width attribute raise an error

    def test_height_error(self):
        """Test if height attribute raise a TypeError and ValueError."""
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 'Text')  # Check if height raise TypeError when set it a string
        with self.assertRaises(TypeError):
            rect = Rectangle(1, (1,))  # Check if width raise TypeError when set it a tuple
        with self.assertRaises(ValueError):
            rect = Rectangle(1, 0)  # Check if height attribute raise an error

    def test_negative_x(self):
        """Test if x attribute raise a ValueError when set to negative."""
        with self.assertRaises(ValueError):
            rect = Rectangle(2, 1, -1, 1)  # Check if x attribute raise an error

    def test_negative_y(self):
        """Test if y attribute raise a ValueError when set to negative."""
        with self.assertRaises(ValueError):
            rect = Rectangle(2, 1, 1, -1)  # Check if y attribute raise an error

    def test_update_method_with_args(self):
        """Test update method with args."""
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(6, 7, 8, 9, 10)
        self.assertEqual(rect.id, 6)
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 8)
        self.assertEqual(rect.x, 9)
        self.assertEqual(rect.y, 10)

    def test_update_method_with_kwargs(self):
        """Test update method with kwargs."""
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(id=6, width=7, height=8, x=9, y=10)
        self.assertEqual(rect.id, 6)
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 8)
        self.assertEqual(rect.x, 9)
        self.assertEqual(rect.y, 10)

    def test_update_method_with_both_args_and_kwargs(self):
        """Test update method with both args and kwargs."""
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(6, width=7, height=8, x=9, y=10)
        self.assertEqual(rect.id, 6)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)


if __name__ == '__main__':
    unittest.main()
