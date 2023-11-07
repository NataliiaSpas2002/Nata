# Topik 36
# Task 1

import asyncio
from multiprocessing import Process


async def to_fibonacci(n: int):
    print(f"{to_fibonacci.__name__}")
    start = 1
    res = []

    while start <= n:
        if n <= 1:
            return n
        start += 1
        a, b = 0, 1
        for item in range(2, n):
            a, b = b, a + b

            res.append(a)
        return res


async def to_factorial(number):
    res = []
    start = 1

    while start <= number:
        fact = 1

        start += 1
        for item in range(2, number + 1):
            fact *= item

            res.append(fact)
        return res


async def to_square(n: int):
    print(f"{to_square.__name__}")
    return [item ** 2 for item in list(range(1, n))]


async def to_cube(n: int):
    print(f"{to_cube.__name__}")
    return [item ** 3 for item in list(range(1, n))]


async def main():
    res = await asyncio.gather(
        to_fibonacci(10),
        to_factorial(10),
        to_square(10),
        to_cube(10)
    )
    print(res)


asyncio.run(main())


def fibonacci(n: int):
    print(f"{fibonacci.__name__} Process")
    start = 1
    res = []

    while start <= n:
        if n <= 1:
            return n
        start += 1
        a, b = 0, 1
        for item in range(2, n):
            a, b = b, a + b

            res.append(a)
        return res


def factorial(number):
    print(f"{factorial.__name__} Process")
    res = []
    start = 1

    while start <= number:
        fact = 1

        start += 1
        for item in range(2, number + 1):
            fact *= item

            res.append(fact)
        return res


def square(n):
    print(f"{square.__name__} Process")
    return [item ** 2 for item in list(range(1, n))]


def cube(n):
    print(f"{cube.__name__} Process")
    return [item ** 3 for item in list(range(1, n))]


if __name__ == '__main__':
    p1 = Process(target=square, args=(10,))
    p2 = Process(target=cube, args=(10,))
    p3 = Process(target=factorial, args=(10,))
    p4 = Process(target=fibonacci, args=(10,))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    print("Well done!")