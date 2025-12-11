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
class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print(f"Called static_method. We don't get any object or class info here.")


instance = ClassTest()
instance.instance_method()  # Called instance_method of <__main__.ClassTest object at 0x77e0f89ee210>

ClassTest.class_method()  # Called class_method of <class '__main__.ClassTest'>
ClassTest.static_method()  # Called static_method. We don't get any object or class info here.


# -- What are they used for? --
# Instance methods are used for most things. When you want to produce an action that uses the data stored in an object.
# Static methods are used to just place a method inside a class because you feel it belongs there (i.e. for code organization, mostly!)
# Class methods are often used as factories.


class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


heavy = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Python 101", 600)

print(heavy)  # <Book Harry Potter, hardcover, weighing 1600g>
print(light)  # <Book Python 101, paperback, weighing 600g>


# * Class inheritance
class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.connected = False


# printer = Device("Printer", "USB")
# print(printer)


# We don't want to add printer-specific stuff to Device, so...
class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        # super(Printer, self).__init__(name, connected_by)  - Python2.7
        super().__init__(name, connected_by)  # Python3+
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            raise TypeError("Device is disconnected at this time, cannot print.")
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages


printer = Printer("Printer", "USB", 500)
printer.print(20)
print(printer)
printer.print(50)
print(printer)
printer.disconnect()
# printer.print(30)  # Error

# * Class composition
# -- Composition over inheritance here --
# Composition: "A BookShelf has many Books"


class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."


class Book:
    def __init__(self, name):
        self.name = name


book = Book("Harry Potter")
book2 = Book("Python 101")
shelf = BookShelf(book, book2)
print(shelf)  # BookShelf with 2 books.
