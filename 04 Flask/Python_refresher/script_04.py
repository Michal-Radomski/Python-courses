# Object Oriented Programming
student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}


def average(sequence):
    return sum(sequence) / len(sequence)


print(average(student["grades"]))  # 88.0

# But wouldn't it be nice if we could...
# print(student.average()) ?


class Student:
    def __init__(self):
        self.name = "Rolf"
        self.grades = (89, 90, 93, 78, 90)

    def average(self):
        return sum(self.grades) / len(self.grades)


student = Student()
print(student.average())  # 88.0
# Identical to Student.average(student)


# -- Parameters in __init__ --
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student = Student("Bob", (36, 67, 90, 100, 100))
print(student.average())  # 78.6


# -- Remember *args ? --
class Student:
    def __init__(self, name, *grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student = Student("Bob", 36, 67, 90, 100, 100)
print(student.average())  # 78.6


# * Magic methods: __str__ and __repr__
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


bob = Person("Bob", 35)
print(
    bob
)  # Not the nicest thing to read! -> <__main__.Person object at 0x7fd3609bd340>


# -- __str__ --
# The goal of __str__ is to return a nice, easy to read string for end users.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person {self.name}, {self.age} years old"


bob = Person("Bob", 35)
print(bob)  # Much nicer -> Person Bob, 35 years old


# -- __repr__ --
# The goal of __repr__ is to be unambiguous, and if possible what it outputs should allow us to re-create an identical object.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        # I'm adding the < > just so it's clear that this is an object we're printing out!
        return f"<Person({self.name!r}, {self.age})>"  # !r calls the __repr__ method of the thing.


bob = Person("Bob", 35)
print(
    bob
)  # Not as nice, but we could re-create "Bob" very easily. -> <Person('Bob', 35)>


class Store:
    def __init__(
        self,
        name,
    ):
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
        self.name = name
        self.items = []

    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        item = {"name": name, "price": price}
        self.items.append(item)

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        total = 0
        for item in self.items:
            total += item["price"]
        return total


# * @classmethod and @staticmethod
