# Python -Almost a circle

# Learning Objectives

* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

# Step by step
Write the first class Base
Write the class Rectangle that inherits from Base
Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded)
Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance
Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here
Update the class Rectangle by overriding the str method so that it returns [Rectangle] instance
Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y
Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute
Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, kwargs) that assigns a key/value argument to attributes
Write the class Square that inherits from Rectangle
Update the class Square by adding the public getter and setter size
Update the class Square by adding the public method def update(self, *args, kwargs) that assigns attributes
Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle
Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square
Update the class Base by adding the class method def savetofile(cls, listobjs): that writes the JSON string representation of listobjs to a file
Update the class Base by adding the static method def fromjsonstring(jsonstring): that returns the list of the JSON string representation jsonstring
Update the class Base by adding the class method def create(cls, dictionary): that returns an instance with all attributes already set
Update the class Base by adding the class method def loadfromfile(cls): that returns a list of instances

## Base class
* Requirement: 
Write the first class Base:

Create a folder named models with an empty file __init__.py inside - with this file, the folder will become a Python package

Create a file named models/base.py:

Class Base:
private class attribute __nb_objects = 0
class constructor: def __init__(self, id=None)::
if id is not None, assign the public instance attribute id with this argument value - you can assume id is an integer and you don’t need to test the type of it
otherwise, increment __nb_objects and assign the new value to the public instance attribute id
This class will be the “base” of all other classes in this project. The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)
* Main file:
#!/usr/bin/python3
""" 0-main """
from models.base import Base

if __name__ == "__main__":

    b1 = Base('test')
    print(b1.id)
    >>> test

    b2 = Base()
    print(b2.id)
    >>> 1

    b3 = Base()
    print(b3.id)
    >>> 2

    b4 = Base(12)
    print(b4.id)
    >>> 12

    b5 = Base()
    print(b5.id)
    >>> 3
    
    Base._Base__nb_objects = 0 # 
    b6 = Base()
    print(b6.id)
    >>> 1

* Test file
    ** Initialize the attribute
        *** With id: Compare value of id input and the object after initializing with that id - assertEqual()
        *** Without id:
            + Check if attribute is created before attempting to access its - self.assertTrue(hasattr(obj, 'id'))
            (if the id attribute is not created properly, attempting to access obj.id directly would raise an AttributeError.)
            + Check if attribute is an integer -  self.assertIsInstance(obj.id, int)
            + Check if attribute is not none - self.assertNotEqual(obj.id, None) 
            + Check if id is equal to __nb_object - self.assertEqual(obj.id, Base._Base__nb_objects)
    ** Test unique id initialize
    ** Other tests (negative, positive, zero)


