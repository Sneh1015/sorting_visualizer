"""
Package that collects all algorithms in one dictionary.
The dictionary order is also the order of the buttons on screen.
"""
from algorithms.bubble_sort import bubble_sort
from algorithms.selection_sort import selection_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort
from algorithms.radix_sort import radix_sort
from algorithms.shell_sort import shell_sort

ALGORITHMS = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Radix Sort": radix_sort,
    "Shell Sort": shell_sort,
}
