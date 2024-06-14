#!/usr/bin/python3
"""
Given a number n, write a method that calculates the
fewest number of operations needed to result
in exactly n H characters in the file.
"""


def minOperations(n):
    """Function to execute the code

    Args:
        n (int): the number of n characters

    Return:
        The number of steps it will take to eexecute
    """
    if n <= 1:
        return 0  # return 0 means no operation done

    operations = 0
    factor = 2

    # Get factors of n and subsequently add to get ops
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
