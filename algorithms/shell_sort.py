"""Shell Sort - insertion sort on elements that are `gap` places apart."""
from algorithms.base import COMPARE, WRITE


def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap:
                yield COMPARE, (j - gap, i)
                if arr[j - gap] <= temp:
                    break
                arr[j] = arr[j - gap]
                yield WRITE, (j,)
                j -= gap
            arr[j] = temp
            yield WRITE, (j,)
        gap //= 2                        # shrink the gap each round
