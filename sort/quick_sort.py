#!/usr/bin/env python3

"""
Author: ilyi
Date: August 03, 2023
"""

from typing import List

"""
Quick sort algorithm. "Divide and conquer."
Time complexity: Average-Case: O(nlogn), Worst-Case: O(n^2)
"""
def quick_sort(a: List) -> List:
    if len(a) <= 1:
        return a
    pivot = a.pop()
    left = []
    right = []
    for i in a:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)
    return quick_sort(left) + [pivot] + quick_sort(right)
