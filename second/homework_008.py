# Topic 8
# Task 1

def favourite_movie(movie):
    print('My favourite movie is ' + movie)
favourite_movie('Inception.')

# Task 2
def my_function(country, capital):
    result = {country: capital}
    return result

print(my_function('Denmark', 'Copenhagen'))

# Task 3
import math

def make_operation(operator, *args):
    if operator == "+":
        return sum(args)
    elif operator == "-":
        return args[0] - sum(args[1:])
    elif operator == '*':
        return math.prod(args[:])
    else:
        return 'Your number is wrong'

print(make_operation( '+',3,4))
print(make_operation('-', 3,4))
print(make_operation('a', 3,4,5))