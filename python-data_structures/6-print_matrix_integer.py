#!/usr/bin/python3
"""Module that prints a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""
    for row in matrix:
        for index in range(len(row)):
            if index == len(row) - 1:
                print("{:d}".format(row[index]))
            else:
                print("{:d}".format(row[index]), end=" ")
