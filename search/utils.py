from typing import List


def is_sorted(a: List) -> bool:
    """
    Check if a list is sorted
    """
    for i in range(1, len(a)):
        if a[i] < a[i-1]:
            return False
    return True