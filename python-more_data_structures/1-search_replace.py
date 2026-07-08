#!/usr/bin/python3
"""Module that replaces all occurrences of an element in a new list."""


def search_replace(my_list, search, replace):
    """Return a new list with all matching elements replaced."""
    new_list = []

    for item in my_list:
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)

    return new_list
