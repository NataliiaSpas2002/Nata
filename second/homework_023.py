# Topic 23
# Task 1

from typing import List, Tuple


def question1(first_list: List[int], second_list: List[int]) -> List[int]:
    res: List[int] = []
    for el_first_list in first_list:
        if el_first_list in second_list:
            res.append(el_first_list)
    return res


first_list = [1, 2, 3, 4, 10, 20]
second_list = [2, 4, 5, 10, 3]
result = question1(first_list, second_list)
print(result)
# The loop iterates over each element in first_list O(n)
# and checks if it's in second_list O(n)
# Answer: O(n^2)


def question2(n: int) -> int:
    for _ in range(5):
        n **= 3
    return n


result2 = question2(2)

print(result2)
# The loop runs a constant number of times (10)
# Answer: O(1)


def question3(first_list: List[int], second_list: List[int]) -> List[int]:
    temp: List[int] = first_list[:]
    for el_second_list in second_list:
        flag = False
        for check in temp:
            if second_list == check:
                flag = True
                break
        if not flag:
            temp.append(second_list)
    return temp


result3 = question3([1, 2, 3], [2, 8, 5])
print(result3)
# Iterate over each element in first_list O(n) and second_list O(n)
# Answer: O(n^2)


def question4(input_list: List[int]) -> int:
    res: int = 0
    for el in input_list:
        if el > res:
            res = el
    return res


result4 = question4([1, 5, 2])
print(result4)

# The loop iterates over each element in input_list, and the complexity is linear.
# Answer: O(n)


def question5(n: int) -> List[Tuple[int, int]]:
    res: List[Tuple[int, int]] = []
    for i in range(n):
        for j in range(n):
            res.append((i, j))
    return res


print(question5(4))
# The nested loops iterate over each value of i and j, resulting in n * n iterations
# # Answer: O(n^2)


def question6(n: int) -> int:
    while n > 1:
        n /= 2
    return n


print(question6(100))

# The loop iterates until  n becomes 1, dividing n by 2 in each iteration.
# This is a logarithmic complexity.
# Answer: O(log n)