# Topic 14
# Task 1
def logger(func):
    def wrapper(*args):
        print(*args)
        return func(*args)
    return wrapper

@logger
def add(x, y):
    return x + y
print(add(2, 3))

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

print(square_all(10, 3, 2))
#
# Task 2
#
# def stop_words(words: list):
#     def ops(func):
#         def wrapper(*args):
#             x = func(*args)
#             for item in words:
#                 x = x.replace(item, "*")
#             return x
#         return wrapper
#     return ops
#
# @stop_words(['pepsi', 'BMW'])
# def create_slogan(name: str) -> str:
#     return f"{name} drinks pepsi in his brand new BMW!"
#
# print(create_slogan("Steve"))
#
# assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

# Task 3

def arg_rules(type_: type, max_length: int, contains: list):
    def decoraror(func):
        def wrapper(*args):
            my_string = func(*args)
            # print(my_string)
            for item in args:
                if isinstance(item, type_) and len(*args) <= max_length and not contains in args:
                    return my_string
                else:
                    return False

        return wrapper
    return decoraror

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan1(name: str) -> str:

    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan1('johndoe05@gmail.com') is False

assert create_slogan1('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
print(create_slogan1('johndoe05@gmail.com'))
print(create_slogan1('S@SH05'))




