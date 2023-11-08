"""Bubble Sort"""


from termcolor import colored


def bubble_sort(value: list):
    """Sort a list using bubble sort algorithm.

    This is a very basic implementation.
    """

    n = len(value)

    for i in range(n):
        for j in range(0, n - i - 1):
            print(colored(f'Current array: {value}', 'yellow'))
            print(f'Comparing value[{j}]={value[j]} with value[{j+1}]={value[j+1]}', end='\n')
            if value[j] > value[j + 1]:
                print(colored(f' -- Changing value[{j}]={value[j]} with value[{j+1}]={value[j+1]}', 'green'))
                value[j], value[j + 1] = value[j + 1], value[j]
            print()

test_value = [5, 54, 3, 6, 2, 64]

bubble_sort(test_value)

print(test_value)