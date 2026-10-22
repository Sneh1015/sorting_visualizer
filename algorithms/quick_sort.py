"""Quick Sort - choose a pivot, put smaller items left and bigger right."""
from algorithms.base import COMPARE, SWAP, PIVOT, SORTED


def quick_sort(arr):
    yield from _quick_sort(arr, 0, len(arr) - 1)


def _quick_sort(arr, low, high):
    if low > high:
        return
    if low == high:                      # single element is in its place
        yield SORTED, (low,)
        return
    p = yield from _partition(arr, low, high)
    yield SORTED, (p,)                   # pivot is now in its final place
    yield from _quick_sort(arr, low, p - 1)
    yield from _quick_sort(arr, p + 1, high)


def _partition(arr, low, high):
    """Lomuto partition (same as the original project). Last item = pivot."""
    pivot = arr[high]
    yield PIVOT, (high,)
    i = low - 1
    for j in range(low, high):
        yield COMPARE, (j, high)
        if arr[j] < pivot:
            i += 1
            if i != j:
                arr[i], arr[j] = arr[j], arr[i]
                yield SWAP, (i, j)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    yield SWAP, (i + 1, high)
    return i + 1                         # position where the pivot ended up
