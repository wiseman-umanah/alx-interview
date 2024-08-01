#!/usr/bin/python3
"""Calculate the perimeter of
an island in a grid
"""


def island_perimeter(grid):
    """Calculates the perimeter of an island in grid

    Args:
        grid (List[List[int]]): a 2D matrix

    Returns:
        int: perimeter
    """
    perimeter = 0

    for row in range(len(grid)):  # get rows number
        for col in range(len(grid[row])):  # get columns number
            if grid[row][col] == 1:
                perimeter += 4  # adds 4 if found
                if col + 1 < len(grid[row]) and grid[row][col + 1] == 1:
                    perimeter -= 2  # if right column is 1
                if row + 1 < len(grid) and grid[row + 1][col] == 1:
                    perimeter -= 2  # if bottom row is 1

    return perimeter
