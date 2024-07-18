#!/usr/bin/python3
"""Module that contains function that rotates
a 2D matrix at 90deg
"""


def rotate_2d_matrix(matrix):
    """rotate a 2d matrix 90deg

    Args:
        matrix (list): matrix to rotate (n x n)
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in matrix:
        i.reverse()
