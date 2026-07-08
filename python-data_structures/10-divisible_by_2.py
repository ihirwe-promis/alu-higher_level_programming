#!/usr/bin/python3
"""Module that checks if integers are divisible by 2."""


def divisible_by_2(my_list=[]):
    """Return a list of True/False values for divisibility by 2."""
    new_list = []

    for number in my_list:
        if number % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)

    return new_list
