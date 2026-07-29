#!/usr/bin/python3
"""
Module that provides a function to look up object attributes and methods.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    """
    return dir(obj)
