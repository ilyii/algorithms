#!/usr/bin/env python3

"""
Author: ilyi
Date: August 03, 2023
"""

from typing import List, Any
from search.utils import is_sorted


def binary_search(a:List, l:int, r:int, t):
    assert r >= l >= 0
    assert r < len(a)
    assert is_sorted(a)

    while l <= r:
        m = (l + r) // 2
        if a[m] == t:
            return m
        elif a[m] < t:
            l = m + 1
        else:
            r = m - 1
    return -1


