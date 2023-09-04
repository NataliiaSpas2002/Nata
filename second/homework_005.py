def plus(a,b):
    return a+b

if __name__ == '__main__':
    print(plus(2,2))


# Topic 6
# Task 1
import random
year_list = []
largest = []
maximum = -1
while len(year_list) < 10:
    years = random.randrange(1, 2023)
    year_list.append(years)
if len(year_list) == 10:
    print(year_list)
    for num in year_list:
        if num > maximum:
            maximum = num
            largest.append(num)
    print(max(largest))

# Task 2

import random
lis1 = []
lis2 = []
lis3 = []
for x in range(10):
    lis1.append(random.randint(1,10))
    lis2.append(random.randint(1,10))
for x in lis1:
    if (x in lis2) and not (x in lis3):
        lis3.append(x)
print(lis1)
print(lis2)
print(lis3)

# Task 3

my_list=[]
for x in range(1, 100):
    if (x%7==0) and not (x%5==0):
        my_list.append(x)
print (my_list)





