#!/usr/bin/python3
"""Module that prints integers of a list in reverse order."""


def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order."""
    if my_list is None:
        return

    for number in my_list[::-1]:
        print("{:d}".format(number))
