# Topik 19
# Task 1

def with_index(iterable, start=0):
    for item in iterable:
        yield start, item
        start += 1


my_list = ['physics', 'mathematics', 'chemistry']


my_numeration = enumerate(my_list, 1)

print(list(my_numeration))

# Task 2


def in_range(*args):
    if len(args) == 2:
        start, end = args
        step = 1
    elif len(args) == 3:
        start, end, step = args
    else:
        raise ValueError

    current = start
    while (step > 0 and current < end) or (step < 0 and current > end):
        yield current
        current += step


print(list(range(20)))

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

