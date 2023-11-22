# Topic 28
# Task 1

def bidirectional_bubble_sort(arr):
    n = len(arr)
    swapped = True

    while swapped:
        # Forward pass (upward)
        swapped = False
        for i in range(n -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # Bacward pass (downward)
        for i in range(n - 1, 0, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

    return arr


my_list = [101, 64, 34, 25, 12, 22, 11, 90, 10]
sorted_list = bidirectional_bubble_sort(my_list)
print("Bubble sorted list:", sorted_list)

# The bidirectional bubble sort має часову складність O(n^2),
# що робить його не дуже ефективним і зазвичай використовується там,
# де простота важливіша за ефективність.

# Task 2


def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2

        left_half = array[:mid]
        # left_half = [array[i] for i in range(0, mid)]
        right_half = array[mid:]
        #right_half = [array[i] for i in range(mid, len(array))]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1


merge_sort(my_list)
print("Merge sorted list:", my_list)