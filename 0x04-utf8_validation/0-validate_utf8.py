#!/usr/bin/python3
"""Module that determines if a given data set
represents a valid UTF-8 encoding"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """method that determines if a given data set
    represents a valid UTF-8 encoding

    data (list): a list containing bytes

    Return:
        returns True if UTF-8
    """
    count = 0

    for byte in data:
        if count == 0:
            if byte >> 5 == 0b110:
                count = 1
            elif byte >> 4 == 0b1110:
                count = 2
            elif byte >> 3 == 0b11110:
                count = 3
            elif byte >> 7 != 0b0:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            count -= 1

    return count == 0
