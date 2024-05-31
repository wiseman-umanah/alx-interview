#!/usr/bin/python3
"""
Module that contains function that returns
a list of lists of integers representing the
Pascal’s triangle of n
"""


def pascal_triangle(pas_len=0):
    """
    Function that implements Pascal Triangle to any Base

    Parameters
    ----------
    pas_len: int, optional
        The power of the Pascal Triangle

    Return
    ------
        [[]] - for power 0 and below
        [[1]] - for power 1
        [[1, 1]] - for power 2
        [...[...],[...]...] - dynamically created based on the power
    """
    base_list = [[1], [1, 1]]

    if pas_len <= 0:
        return [[]]
    if pas_len == 1:
        return [[1]]
    if pas_len == 2:
        return base_list

    for p_i in range(1, pas_len):
        p_list = [1]
        for p_ii in range(len(base_list[p_i]) - 1):
            p_list.append(base_list[p_i][p_ii] + base_list[p_i][p_ii + 1])
        p_list.append(1)
        base_list.append(p_list)

    return base_list
