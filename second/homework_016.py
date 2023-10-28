# Topic 16
# Task 1
class Person:
    def __init__(self, name, subject, num_teach_hours, num_cl_room, *args, **kwargs):
        self.name = name
        self.subject = subject
        self.num_teach_hours = num_teach_hours
        self.num_cl_room = num_cl_room

class Teacher(Person):
    def __init__(self, salary, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.salary = salary

    def salary_growth(self, salary_sum = 1, *args, **kwargs):
        self.salary += salary_sum

our_teacher = Teacher(10000, 'Alfred Nobel','English', 150, 12)
our_teacher.salary_growth(2000)
print(our_teacher.salary)

class Student(Person):
    def __init__(self, homework, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.homework = homework

    def homework_num(self, homework_num = 1, *args, **kwargs):
        self.homework += homework_num

our_student = Student(14,'Alex Malcovich', 'English', 150, 12)
our_student.homework_num(1)
print(our_student.homework)

# Task 2
class Mathematician:
    @staticmethod
    def square_nums(nums):
        return [num ** 2 for num in nums]

    @staticmethod
    def remove_positives(nums):
        return [num for num in nums if num <= 0]

    @staticmethod
    def filter_leaps(year):
        return [i for i in year if i % 4 == 0]


m = Mathematician()

my_square = ([7, 11, 5, 4])
square_result = m.square_nums(my_square)
print(square_result)

my_remove = ([26, -11, -8, 13, -90])
remove_result = m.remove_positives(my_remove)
print(remove_result)

my_filter_leaps = ([2001, 1884, 1995, 2003, 2020])
filter_leaps_result = m.filter_leaps(my_filter_leaps)
print(filter_leaps_result)

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]



# Task 3

class Product:
    def __init__(self, product_type, name, price):
        self.type = product_type
        self.name = name
        self.price = price

class ProductStore:
    def __init__(self):
        self.products = {}
        self.income = 0
        self.default_price_multiplier = 1.3
        self.discounts = {}

    def add(self, product, amount):
        if not isinstance(product, Product):
            raise ValueError("Invalid product ")

        if product.name in self.products:
            self.products[product.name]['amount'] += amount
        else:
            price_multiplier = self.discounts.get(product.name, self.default_price_multiplier)
            self.products[product.name] = {
                'type': product.type,
                'price': product.price * price_multiplier,
                'amount': amount
            }

    def set_discount(self, identifier, percent, identifier_type='name'):
        if identifier_type == 'name':
            self.discounts[identifier] = (100 - percent) / 100
        elif identifier_type == 'type':
            for product_name, product_info in self.products.items():
                if product_info['type'] == identifier:
                    self.discounts[product_name] = (100 - percent) / 100

    def sell_product(self, product_name, amount):
        if product_name not in self.products:
            raise ValueError(f"Product {product_name} not found")

        if self.products[product_name]['amount'] < amount:
            raise ValueError(f"Insufficient stock of {product_name}")

        self.products[product_name]['amount'] -= amount
        self.income += round(self.products[product_name]['price'] * amount)

    def get_income(self):
        return self.income

    def get_all_products(self):
        return self.products

    def get_product_info(self, product_name):
        if product_name in self.products:
            return product_name, self.products[product_name]['amount']
        else:
            raise ValueError(f"Product {product_name} not found")


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)
s.add(p2, 300)

s.set_discount('Ramen', 10, 'name')

s.sell_product('Ramen', 10)

print(s.get_product_info('Ramen'))  # Output: ('Ramen', 290)
assert s.get_product_info('Ramen') == ('Ramen', 290)


# Task 4
class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

        with open('logs.txt', 'a') as log_file:
            log_file.write(f"Error: {msg}\n")

try:
    raise CustomException("This is a custom exception.")
except CustomException as e:
    print(f"Caught an exception: {e}")

