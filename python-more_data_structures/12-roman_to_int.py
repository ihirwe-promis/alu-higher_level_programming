#!/usr/bin/python3
"""Module that converts Roman numerals to integers."""


def roman_to_int(roman_string):
    """Convert a Roman numeral to an integer."""
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    result = 0

    for i in range(len(roman_string)):
        current = roman_values[roman_string[i]]

        if i + 1 < len(roman_string):
            next_value = roman_values[roman_string[i + 1]]

            if current < next_value:
                result -= current
            else:
                result += current
        else:
            result += current

    return result
