#!/usr/bin/python3
"""Module that returns the key with the biggest integer value."""


def best_score(a_dictionary):
    """Return the key with the highest value."""
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    best_key = None
    highest_score = 0

    for key in a_dictionary:
        if best_key is None or a_dictionary[key] > highest_score:
            highest_score = a_dictionary[key]
            best_key = key

    return best_key
