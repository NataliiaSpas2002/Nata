# Topic 4
# Task 1
my_str = 'helloworld'
print(my_str[0:2] + my_str[-2:], sep="")

my_str1 = 'my'
print(my_str1*2)

my_str2 = 'x'
print(my_str2*0)

# Task 2
user_input = input('Please type your phone number: ')
if user_input.isdigit() and len(user_input) == 10:
    print("Thank you! We’ll contact you.")
else:
    print("Your phone number is incorrect")

# Task 3
user_espr = input('Please solve the mathematical expression, how much is 82+1 = ')
user_espr = int(user_espr)
if user_espr == 83:
    print('Correct!')
else:
    print('Think a little more.')

# Task 4
first_name = input('Please enter your first name: ')
if first_name == 'nataliia' or first_name == first_name.title():
    print('Thank you!')
else:
    print('Is it your first name?')




























