"""Merge Sort - split in halves, sort each half, then merge them."""
from algorithms.base import COMPARE, WRITE


def merge_sort(arr):
    # `yield from` lets us pass on the steps of the recursive calls
    yield from _merge_sort(arr, 0, len(arr) - 1)


def _merge_sort(arr, low, high):
    if low >= high:                      # 0 or 1 element is already sorted
        return
    mid = (low + high) // 2
    yield from _merge_sort(arr, low, mid)
    yield from _merge_sort(arr, mid + 1, high)
    yield from _merge(arr, low, mid, high)


def _merge(arr, low, mid, high):
    left = arr[low:mid + 1]              # temporary copy of left half
    right = arr[mid + 1:high + 1]        # temporary copy of right half
    i = j = 0
    k = low
    while i < len(left) and j < len(right):
        yield COMPARE, (low + i, mid + 1 + j)
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        yield WRITE, (k,)
        k += 1
    while i < len(left):                 # copy what is left of left half
        arr[k] = left[i]
        yield WRITE, (k,)
        i += 1
        k += 1
    while j < len(right):                # copy what is left of right half
        arr[k] = right[j]
        yield WRITE, (k,)
        j += 1
        k += 1
