#!/usr/bin/python3
"""Determine the fewest number of coins
to meet total
"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """Function to carry out ops

    Args:
        coins (List[int]): a list of coins to use
        total (int): coin to meet

    Returns:
        int: -1 if not available, fewest number of coin
    """
    if total <= 0:
        return 0
    tracker = [float('inf')] * (total + 1)
    tracker[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                tracker[i] = min(tracker[i], tracker[i - coin] + 1)
    return tracker[total] if tracker[total] != float('inf') else -1
