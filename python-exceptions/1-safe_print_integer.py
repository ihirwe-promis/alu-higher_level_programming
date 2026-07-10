#!/usr/bin/python3
"""Module that prints an integer safely."""


def safe_print_integer(value):
    """Print an integer and return True if successful, otherwise False."""
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
