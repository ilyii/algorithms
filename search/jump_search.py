#!/usr/bin/env python3

"""
Author: ilyi
Date: August 03, 2023
"""

from typing import List, Any
from search.utils import is_sorted


def jump_search(a:List, l:int, r:int, t, n):
    assert r >= l >= 0
    assert r < len(a)
    assert is_sorted(a)

    step = int(n ** 0.5)
    previous = 0  

    # Find block 
    while a[min(step, n)-1] < t:
        previous = step
        step += int(n ** 0.5)
        if previous >= n:
            return -1
     
    # Linear search in block
    while a[previous] < t:
        previous += 1

        # Not found
        if previous == min(step, n):
            return -1
     
    # Found
    if a[int(previous)] == t:
        return previous
     
    return -1
    

