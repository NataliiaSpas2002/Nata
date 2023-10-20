# Topic 17
# Task 1

class Animal:
    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        print('Woof Woof')


class Cat(Animal):
    def talk(self):
        print('Meow')


def pets_talk(animal_instance):
    animal_instance.talk()


dog_talk = Dog()
cat_talk = Cat()

pets_talk(dog_talk)
pets_talk(cat_talk)

# Task 2

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name, year, author):
        book = Book(name, year, author)
        self.books.append(book)
        return book


    def library_books(self):
        return self.books

    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]

    def __repr__(self):
        return f"Library({self.name})"

    def __str__(self):
        return f"Library: {self.name}"


class Book:
    total_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        author.books.append(self)
        Book.total_books += 1

    def __repr__(self):
        return f"Book({self.name}, {self.year}, {self.author})"

    def __str__(self):
        return f"Book: {self.name} {self.year} by {self.author.name}"


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f"Author({self.name}, {self.country}, {self.birthday})"

    def __str__(self):
        return f"Author: {self.name} from {self.country}, born on {self.birthday}"


library = Library("My Library")
author1 = Author("Stephen Edwin King", "USA", "1947-09-21")
author2 = Author("Ayn Rand", "USA", "1905-02-02")
author3 = Author("Gabriel Garcia Mårquez", "Latin America", "1927-03-06 - 2014-04-17")


book1 = library.new_book("\"The Dark Tower VII: The Dark Tower\"", 2004, author1)
book2 = library.new_book("\"The Dark Tower VI: Song of Susannah\"", 2004, author1)
book3 = library.new_book("\"Atlas Shrugged\"", 1957, author2)
book4 = library.new_book("\"One hundred years of Solitude\"", 1967, author3)


books_by_author = library.group_by_author(author1)
books_by_year = library.group_by_year(1967)


print("Books by Author:")
for book in books_by_author:
    print(book)


print("\nBooks by Year:")
for book in books_by_year:
    print(book)


all_books = library.library_books()
print("All books in the Library:")
for book in all_books:
    print(book)


# Task 3
from math import gcd

class Fraction:
    def __init__(self, numerat, denominat):
        if denominat == 0:
            raise ValueError

        common = gcd(numerat, denominat)
        self.numerator = numerat // common
        self.denominator = denominat // common

    def __add__(self, other):
        my_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        my_denominator = self.denominator * other.denominator
        return Fraction(my_numerator, my_denominator)

    def __mul__(self, other):
        my_numerator = self.numerator * other.numerator
        my_denominator = self.denominator * other.denominator
        return Fraction(my_numerator, my_denominator)

    def __sub__(self, other):
        my_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        my_denominator = self.denominator * other.denominator
        return Fraction(my_numerator, my_denominator)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ValueError

        my_numerator = self.numerator * other.denominator
        my_denominator = self.denominator * other.numerator
        return Fraction(my_numerator, my_denominator)


    # Check if the numerators and denominators of the two fractions are equal
    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    # Compare fractions using cross-multiplication
    def __lt__(self, other):
        return (self.numerator * other.denominator) < (other.numerator * self.denominator)

    def __le__(self, other):
        return (self.numerator * other.denominator) <= (other.numerator * self.denominator)

    def __str__(self):
        return f"{self.numerator}/ {self.denominator}"

if __name__ == "__main__":
    x = Fraction(3, 7)
    y = Fraction(1, 5)

    result_addition = x + y
    print(result_addition)  # Output: 22/35
    print(result_addition == Fraction(22, 35))

    result_subtraction = x - y
    print(result_subtraction)  # Output: 8/35

    result_multiplication = x * y
    print(result_multiplication)  # Output: 3/35

    result_division = x / y
    print(result_division)  # Output: 15/7

    print(x == Fraction(3, 7))  # Output: True

    print(x < y) # Output: False
    print(x <= y) # Output: False


