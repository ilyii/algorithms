#!/usr/bin/env python3

"""
Author: ilyi
Date: August 03, 2023
"""

from typing import List

"""
Insertion sort algorithm. 
Time complexity: Average-Case: O(n^2), Best-Case: O(n)
"""
def insertion_sort(a: List) -> List:
    for i in range(1, len(a)):
        k = i
        while k > 0 and a[k-1] > a[k]:
            a[k-1], a[k] = a[k], a[k-1]
            k -= 1
    return a