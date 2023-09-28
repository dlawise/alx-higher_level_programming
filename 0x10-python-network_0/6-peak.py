#!/usr/bin/python3
def find_peak(list_of_integers):
    # Check if the list is empty
    if not list_of_integers:
        return None

    # Binary search-like approach
    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        # Check if mid is a peak
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    # left will point to a peak element
    return list_of_integers[left]
