#!/usr/bin/python3
"""Module that adds all unique integers in a list."""


def uniq_add(my_list=[]):
    """Return the sum of unique integers."""
    total = 0
    unique = set(my_list)

    for number in unique:
        total += number

    return total
