"""Insertion Sort"""


from termcolor import colored


def insertion_sort(value: list):
    """Sort a list using insertion sort algorithm."""

    n = len(value)

    for i in range(n):
        for j in range(i, n):
            if value[i] > value[j]:
                value[i], value[j] = value[j], value[i]


test_value = [5, 54, 3, 6, 2, 64]

insertion_sort(test_value)

print(test_value)
