"""Merge Sort"""


def merge_sort(value: list):
    if len(value) > 1:
        mid = len(value) // 2
        left = value[:mid]
        right = value[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                value[k] = left[i]
                i += 1
            else:
                value[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            value[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            value[k] = right[j]
            j += 1
            k += 1


test_value = [5, 54, 3, 6, 2, 64]

merge_sort(test_value)

print(test_value)
