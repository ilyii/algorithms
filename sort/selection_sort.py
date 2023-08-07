#!/usr/bin/env python3

"""
Author: ilyi
Date: August 03, 2023
"""

from typing import List

"""
Selection sort algorithm. 
Time complexity: O(n^2)
"""
def selection_sort(a: List) -> List:
    for i in range(len(a)):
        min_idx = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a