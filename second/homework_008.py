
# Topic 7
# Task 1
def Convert(string):
    list1 = list(string.split(" "))
    return list1
str1 = "There is nothing more dangerous than"
my_dict = {i + 1: Convert(str1)[i] for i in range(len(Convert(str1)))}
print(my_dict)

# Task 2
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
total = sum(prices[v] * stock[v] for v in prices)
print(total)

# Task 3

j = [(j ** 2) for j in range(1,11)]
my_list = list(enumerate(j, start = 1))
print(my_list)

# Task 4

day = ['Monday', 'Tusday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weeks_day = {day[i]: i + 1 for i in range(len(day))}
print(weeks_day)
number_weeks_day = {i + 1: day[i] for i in range(len(day))}
print(number_weeks_day)






