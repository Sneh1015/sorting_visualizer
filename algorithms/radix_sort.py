"""Radix Sort - sort digit by digit (ones, tens, hundreds ...)."""
from algorithms.base import COMPARE, WRITE


def radix_sort(arr):
    if not arr:
        return
    biggest = max(arr)
    exp = 1                              # 1 = ones digit, 10 = tens digit, ...
    while biggest // exp > 0:
        yield from _counting_sort_by_digit(arr, exp)
        exp *= 10


def _counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # 1) count how many numbers have each digit (0-9)
    for i in range(n):
        count[(arr[i] // exp) % 10] += 1
        yield COMPARE, (i,)

    # 2) turn counts into final positions
    for d in range(1, 10):
        count[d] += count[d - 1]

    # 3) build the output list (go backwards to keep it stable)
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1

    # 4) copy back into the real array and show it
    for i in range(n):
        arr[i] = output[i]
        yield WRITE, (i,)
