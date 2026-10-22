"""Selection Sort - find the smallest element and put it at the front."""
from algorithms.base import COMPARE, SWAP, SORTED


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            yield COMPARE, (j, min_index)
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            yield SWAP, (i, min_index)
        yield SORTED, (i,)
