#!/usr/bin/env python3

"""
Author: ilyi
Date: August 03, 2023
"""

from typing import List

"""
Bubble sort algorithm. "bubbling the largest elements to the end of the array in each pass."
Time complexity: Average-Case: O(n^2), Best-Case: O(n)
"""
def bubble_sort(a: List, plot:bool) -> List:
    for i in range(len(a)):
        for j in range(1, len(a)-i):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]           
    return a


