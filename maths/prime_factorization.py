#!/usr/bin/env python3

"""
Author: ilyi
Date: September 15, 2023
"""

def prime_factorization(x):
    results = []
    f = 2
    while x > 1:
        if x % f == 0:
            results.append(f)
            x //= f
        else:
            f += 1
    return results
