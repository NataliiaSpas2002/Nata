# Topik 19
# Task 1

def with_index(iterable, start=0):
    for item in iterable:
        yield start, item
        start += 1


my_list = ['physics', 'mathematics', 'chemistry']


# for index, value in with_index(my_list, start=1):
#     result = list(with_index(my_list, 1))
# print(result)

names = ['physics', 'mathematics', 'chemistry']
enumNames = enumerate(names, 1)

print(list(enumNames))

# Task 2

def in_range(start, end, step=1):
    current = start
    while (step > 0 and current < end) or (step < 0 and current > end):
        yield current
        current += step


# result = list(in_range(0,100,10))
# print(result)

print(list(range(0, 100, 10)))

# Task 3


class MyIterable:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0 and self.current >= self.end:
            raise StopIteration
        elif self.step < 0 and self.current <= self.end:
            raise StopIteration

        result = self.current
        self.current += self.step
        return result

    def __getitem__(self, index):
        if self.step > 0 and self.start + index * self.step >= self.end:
            raise IndexError("Index out of range")
        elif self.step < 0:
            if self.start + index * self.step <= self.end:
                raise IndexError("Index out of range")

        return self.start + index * self.step


my_iterable = MyIterable(0, 10, 1)


print(my_iterable[0])
print(my_iterable[1])
print(my_iterable[2])

