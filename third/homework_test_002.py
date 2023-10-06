def first_decorator(funk):
    def wrapper(*args, **kwargs):
        print("first decorator")
        return funk(*args, **kwargs)

    return wrapper

def second_decorator(funk):
    def wrapper(*args, **kwargs):
        print("second decorator")
        return funk(*args, **kwargs)

    return wrapper


@first_decorator
@second_decorator
def first_funk(*args, **kwargs):
    print("first funk")
    print(args, kwargs)


@second_decorator
def second_funk(*args, **kwargs):
    print("second funk")
    print(args, kwargs)


first_funk("one")
second_funk("two")
