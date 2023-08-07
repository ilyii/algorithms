#!/usr/bin/env python3

"""
Author: ilyi
Date: August 03, 2023
"""

from typing import List

"""
Merge sort algorithm. "Divide and conquer."
Time complexity: O(nlogn)
"""
def merge_sort(a: List) -> List:
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left, right)

"""
Merge two sorted lists into one sorted list.
"""
def merge(left: List, right: List) -> List:
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res

