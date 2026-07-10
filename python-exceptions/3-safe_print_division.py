#!/usr/bin/python3
"""Module that divides two integers safely."""


def safe_print_division(a, b):
    """Divide two integers and print the result in the finally block."""
    result = None

    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))

    return result
