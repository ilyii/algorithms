#!/usr/bin/env python3

"""
Author: ilyi
Date: September 09, 2023
"""

def euclids_algorithm(n,m):
    while m:
        n, m = m, n % m
    return abs(n)