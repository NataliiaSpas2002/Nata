# Topic 28
# Task 1

def bidirectional_bubble_sort(arr):
    n = len(arr)
    swapped = True

    while swapped:
        swapped = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break
        swapped = False

        n -= 1
        for i in range(n - 1, 0, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

    return arr


my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bidirectional_bubble_sort(my_list)
print("Bubble sorted list:", sorted_list)


# Task 2


def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2

        left_half = [array[i] for i in range(0, mid)]

        right_half = [array[i] for i in range(mid, len(array))]

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


my_second_list = [101, 64, 34, 25, 12, 22, 11, 90, 10]
merge_sort(my_second_list)
print("Merge sorted list:", my_second_list)