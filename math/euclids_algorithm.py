#!/usr/bin/env python3

"""
Author: ilyi
Date: September 09, 2023
"""
from tests import test_euclids_algorithm

def euclids_algorithm(n,m):
    while m:
        n, m = m, n % m
    return abs(n)


if __name__ == "__main__":
    test_euclids_algorithm(euclids_algorithm)