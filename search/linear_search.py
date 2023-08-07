#!/usr/bin/env python3

"""
Author: ilyi
Date: August 03, 2023
"""

from typing import List, Any


def linear_search(a:List, l:int, r:int, t):
    assert r >= l >= 0 
    assert r < len(a) 

    for i in range(l, r+1):
        if a[i] == t:
            return i
    return -1


