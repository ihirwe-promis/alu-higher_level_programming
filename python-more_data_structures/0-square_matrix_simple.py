#!/usr/bin/python3
"""Module that returns a matrix with squared values."""


def square_matrix_simple(matrix=[]):
    """Return a new matrix with each value squared."""
    new_matrix = []

    for row in matrix:
        new_row = []

        for number in row:
            new_row.append(number ** 2)

        new_matrix.append(new_row)

    return new_matrix
