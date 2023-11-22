# Topic 28
# Task 3

import random


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def quicksort(arr, partition_limit=10):
    if len(arr) <= partition_limit:
        insertion_sort(arr)
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        quicksort(left)
        quicksort(right)
        arr[:] = left + middle + right


random_list = random.sample(range(1, 1000), 25)
print("Original list:", random_list)

quicksort(random_list)
print("Sorted list:", random_list)