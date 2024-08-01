#!/usr/bin/python3
"""Calculate the perimeter of
an island in a grid
"""
from typing import List


def island_perimeter(grid: List[List[int]]) -> int:
    """Calculates the perimeter of a island in grid

    Args:
        grid (List[List[int]]): a 2D matrix

    Returns:
        int: perimeter
    """
    perimeter = 0

    for rows in range(len(grid)):  # get rows number
        for cols in range(len(grid[rows])):  # get columns number
            if grid[rows][cols] == 1:
                perimeter += 4  # adds 4 if found
                if (cols + 1) < len(grid[rows]) and grid[rows][cols + 1] == 1:
                    perimeter -= 2  # if right columns is 1
                if (cols + 1) < len(grid[rows]) and grid[rows - 1][cols] == 1:
                    perimeter -= 2  # if bottom row is 1

    return perimeter
