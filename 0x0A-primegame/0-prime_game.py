#!/usr/bin/python3
"""The Prime Game Module
"""


def is_prime(num: int) -> bool:
    """check for prime number validity

    Args:
        num (int): number to validate

    Returns:
        bool: true or false
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """Finds Winner of x rounds

    Args:
        x (int): the number of rounds
        nums (list): list of numbers

    Returns:
        str: Maria or Ben depending on who wins
    """
    if not nums or x < 1:
        return None

    maria, ben = 0, 0

    for n in nums:
        primes = [i for i in range(2, n + 1) if is_prime(i)]

        if len(primes) % 2 == 0:
            ben += 1
        else:
            maria += 1

    return "Maria" if maria > ben else "Ben"
