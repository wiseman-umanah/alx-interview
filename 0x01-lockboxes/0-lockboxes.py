#!/usr/bin/python3
"""Module on lockboxes
and opening them"""


def canUnlockAll(boxes):
    """Function that opens lockboxes"""
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = boxes[0]

    while keys:
        key = keys.pop(0)
        if key < n and not unlocked[key]:
            unlocked[key] = True
            keys.extend(boxes[key])

    return all(unlocked)
