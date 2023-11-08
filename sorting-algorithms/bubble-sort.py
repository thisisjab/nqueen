"""Bubble Sort"""


def bubble_sort(value: list):
    """Sort a list using bubble sort algorithm.

    This is a very basic implementation.
    """

    n = len(value)

    for i in range(n):
        for j in range(0, n - i - 1):
            if value[j] > value[j + 1]:
                value[j], value[j + 1] = value[j + 1], value[j]


test_value = [5, 54, 3, 6, 2, 64]

bubble_sort(test_value)

print(test_value)
