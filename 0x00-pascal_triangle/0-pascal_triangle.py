#!/usr/bin/python3
def pascal_triangle(pas_len=0):
    """
    Function that implements Pascal Triangle to any Base
    """
    base_list = [[1], [1, 1]]

    if pas_len == 0:
        return []
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
