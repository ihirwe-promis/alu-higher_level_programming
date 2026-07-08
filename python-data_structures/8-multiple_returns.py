#!/usr/bin/python3
"""Module that returns the length of a string and its first character."""


def multiple_returns(sentence):
    """Return a tuple containing the length and first character."""
    if len(sentence) == 0:
        return (0, None)

    return (len(sentence), sentence[0])
