# Topic 26
# Task 1

def binary_search_recurs(arr, low, high, target):
    if low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_recurs(arr, mid + 1, high, target)
        else:
            return binary_search_recurs(arr, low, mid - 1, target)
    else:
        return -1


sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
target_element = 5


result = binary_search_recurs(sorted_array, 0, len(sorted_array) - 1, target_element)

if result != -1:
    print(f"Target element {target_element} found in {result} position")
else:
    print(f"Target element {target_element} don’t find")


