# Topic 13
# Task 1
def local_func():
    var1 = 20
    var2 = "Anna"
    var3 = [1, 2, 3]

    local_var = locals()
    num_var = len(local_var)

    print(f"Number of local variables: {num_var}")

local_func()

# Task 2
def my_func():
    def inner_func(x, y):
        return x - y
    return inner_func

print(my_func()(10, 3))

# Task 3
def choose_func(nums: list, func1, func2):
    if all(num > 0 for num in nums):
        return func1(nums)
    else:
        return func2(nums)

def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


nums1 = [1, 2, 3, 4, 5]

nums2 = [1, -2, 3, -4, 5]

result1 = choose_func(nums1, square_nums, remove_negatives)
result2 = choose_func(nums2, square_nums, remove_negatives)

print(result1)
print(result2)

assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]

assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]

