#!/usr/bin/python3
"""Module that deletes a key from a dictionary."""


def simple_delete(a_dictionary, key=""):
    """Delete a key from the dictionary if it exists."""
    if key in a_dictionary:
        del a_dictionary[key]

    return a_dictionary
