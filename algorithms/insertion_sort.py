"""Insertion Sort - pick one element and insert it into the sorted part."""
from algorithms.base import COMPARE, WRITE


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # shift bigger elements one place to the right
        while j >= 0:
            yield COMPARE, (j, i)
            if arr[j] <= key:
                break
            arr[j + 1] = arr[j]
            yield WRITE, (j + 1,)
            j -= 1
        arr[j + 1] = key
        yield WRITE, (j + 1,)
