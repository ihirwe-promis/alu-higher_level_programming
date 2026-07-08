#!/usr/bin/python3
"""Module that updates or adds a key/value pair in a dictionary."""


def update_dictionary(a_dictionary, key, value):
    """Replace or add a key/value pair and return the dictionary."""
    a_dictionary[key] = value
    return a_dictionary
