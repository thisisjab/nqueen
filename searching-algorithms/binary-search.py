"""Binary Search"""


def binary_search(array, x, low, high):
    while low <= high:
        mid = low + (high - low) // 2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


test_value = [1, 3, 5, 8, 9, 13, 17]

print(binary_search(test_value, 8, 0, len(test_value) - 1))
