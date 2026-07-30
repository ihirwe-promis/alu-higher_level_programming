#!/usr/bin/python3
"""Defines a function that creates Pascal's triangle."""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle."""
    if n <= 0:
        return []

    triangle = []

    for row_num in range(n):
        row = [1]

        if triangle:
            previous = triangle[-1]

            for i in range(len(previous) - 1):
                row.append(previous[i] + previous[i + 1])

            row.append(1)

        triangle.append(row)

    return triangle
