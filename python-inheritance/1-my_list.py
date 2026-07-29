#!/usr/bin/python3
"""
Module that defines a MyList class.
"""


class MyList(list):
    """
    A class that inherits from list and adds sorting functionality.
    """

    def print_sorted(self):
        """
        Prints the list sorted in ascending order.
        """
        print(sorted(self))
