# Topic 18
# Task 1

import re

class MyClass:
    def __init__(self, email):
        self.validate(email)

    @classmethod
    def validate(cls, email):
        regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if(re.fullmatch(regex, email)):
            print("Email is valid")
        else:
            print("Invalid email format")


my_email = MyClass("nataliyaspasenko@gmail.com")
my_email2 = MyClass("nataliya55-gmail.com")
my_email3 = MyClass("nataliya55@gmail.com")

# Task 2

# created a descriptor class WorkerBossDescriptor
# to handle the behavior of the boss property in the Worker class.
class WorkerBossDescriptor:
    # get to access the boss property of a Worker instance. It returns the value of _boss.
    def __get__(self, instance, owner):
        return instance.boss
    #  assign a value to the boss property of a Worker instance.
    def __set__(self, instance, value):
        if isinstance(value, Boss) or value is None:
            if instance._boss:
                instance._boss.remove_worker(instance)
            instance._boss = value
            if value:
                value.add_worker(instance)
        else:
            raise ValueError("Invalid boss instance")

class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self._id = id_
        self._name = name
        self._company = company
        self._workers = []

    def id(self):
        return self._id

    def name(self):
        return self._name

    def company(self):
        return self._company

    def workers(self):
        return self._workers

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self._workers.append(worker)
        else:
            raise ValueError("Invalid worker instance")

    def remove_worker(self, worker):
        if worker in self._workers:
            self._workers.remove(worker)

    def __str__(self):
        return f"Boss(id={self._id}, name={self._name}, company={self._company})"

class Worker:
    boss = WorkerBossDescriptor()

    def __init__(self, id_: int, name: str, company: str, boss=None):
        self._id = id_
        self._name = name
        self._company = company
        self._boss = None
        # Use the descriptor for boss to ensure proper validation
        self.boss = boss

    def id(self):
        return self._id

    def name(self):
        return self._name

    def company(self):
        return self.company

    def __str__(self):
        return f"Worker(id={self._id}, name={self._name}, company={self._company}"


boss1 = Boss(1, "Andriy Verevsky", "Kernel")
boss2 = Boss(2, "Andreas Flodström", "Beetroot academy")

worker1 = Worker(101, "Maria Dutton", "Kernel", boss1)
worker2 = Worker(102, "Steven Reynolds", "Beetroot academy")

print(boss1.workers)  # Output: [<__main__.Worker object at ...>]
print(boss2.workers)  # Output: [<__main__.Worker object at ...>]

print(boss1.id())
print(boss2.id())
print(worker1)
print(worker2)
print(boss1)
print(boss2)


# Task 3
from functools import wraps
class TypeDecorators:
    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return int(result)
            except (ValueError, TypeError):
                return result
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return str(result)
            except (ValueError, TypeError):
                return result
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return bool(result)
            except (ValueError, TypeError):
                return result
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return float(result)
            except(ValueError, TypeError):
                return result
        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('25') == 25

assert do_something('True') is True






