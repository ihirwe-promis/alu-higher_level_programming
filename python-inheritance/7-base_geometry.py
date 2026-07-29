#!/usr/bin/python3
"""
Module that defines the BaseGeometry class.
"""


class BaseGeometry:
    """
    A base geometry class.
    """

    def area(self):
        """
        Raises an exception because area is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        Args:
            name: name of the value being validated.
            value: value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
