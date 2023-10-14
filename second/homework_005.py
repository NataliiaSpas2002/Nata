
# Topic 5
# Task 1
import random
number = random.randint(1,10)
while True:
    print("Guess number between 1 to 10: ")
    guess = input()
    i = int(guess)
    if i == number:
        print("Yes! You are right!")
        break
    elif i != number:
        print("Try again!")

# Task 2
user_name = input("Please insert name: ")
user_age = input("Please insert age: ")
convert_age = int(user_age) + 1
print("Hello " + str(user_name) + ", on your next birthday you’ll be " + str(convert_age) + " years!")

# # Task 3
import random
my_word = ['h', 'e', 'l', 'l', 'o']
count = 0
while count < 5:
    random.shuffle(my_word)
    my_string = ''
    for x in my_word:
        my_string += x
    print(my_string)
    count += 1




