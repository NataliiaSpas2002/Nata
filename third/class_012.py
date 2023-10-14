# def plus(a,b):
#     return a+b
#
# if __name__ == '__main__':
#     print(plus(2,2))


# your function runs
# time.sleep(3)
# end = time.time()
#
# print(f"duration: {end - start}")
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функція {func.__name__} виконалася за {execution_time} секунд")
        return result
    return wrapper

@timer_decorator
def our_func():
    time.sleep(5)
    return "Done"

print(our_func())

