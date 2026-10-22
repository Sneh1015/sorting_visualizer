"""Bubble Sort - repeatedly swap neighbours that are in the wrong order."""
from algorithms.base import COMPARE, SWAP, SORTED


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            yield COMPARE, (j, j + 1)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield SWAP, (j, j + 1)
        # after each pass the biggest remaining element is at the end
        yield SORTED, (n - i - 1,)
    yield SORTED, (0,)
