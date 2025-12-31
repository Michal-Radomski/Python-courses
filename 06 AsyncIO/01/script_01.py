# Example 1: Defining a Simple Function
def greet():
    print("Hello, Python learners!")  # Hello, Python learners!


# Example 2: Function with Parameters
def greet_person(name):
    print(f"Hello, {name}!")


# Example 3: Function with Default Parameter Values
def greet_with_default(name="learner"):
    print(f"Hello, {name}!")


# Example 4: Function Returning a Value
def add_two_numbers(a, b):
    return a + b


# Example 5: Function with Arbitrary Number of Arguments
def greet_multiple_people(*names):
    for name in names:
        print(f"Hello, {name}!")


# Example 6: Function with Keyword Arguments
def display_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")


# Example 7: Using a Function as a Variable (First-Class Citizens)
def square(number):
    return number * number


my_function = square
result = my_function(5)  # Calling the function stored in 'my_function'

# Calling the examples
greet()
greet_person("Alice")  # Hello, Alice!
greet_with_default()  # Hello, learner!
greet_with_default("Bob")  # Hello, Bob!
result = add_two_numbers(3, 5)
print(f"The sum is: {result}")  # The sum is: 8
greet_multiple_people("Alice", "Bob", "Charlie")
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!
display_info(name="Alice", age=30, city="New York")
# name: Alice
# age: 30
# city: New York
print(f"The square of 5 is: {result}")  # The square of 5 is: 8

# * Imports
# # Example 1: Importing a Whole Module
# import math

# print(math.sqrt(16))  # Using the sqrt function from the math module

# # Example 2: Importing Specific Attributes
# from datetime import datetime

# print(datetime.now())  # Printing the current date and time

# # Example 3: Importing with Aliases
# import statistics as stats

# numbers = [1, 2, 3, 4, 5]
# print(stats.mean(numbers))  # Calculating the mean of numbers

# # Example 4: Creating and Importing a Custom Module
# # Assuming there's a file named mymodule.py with a function greet()
# # mymodule.py content:
# # def greet(name):
# #     return f"Hello, {name}!"

# # Importing the custom module and using its function
# import mymodule

# print(mymodule.greet("Python Learner"))

# # Example 5: Using Built-in Modules for Practical Tasks
# import os
# import sys

# # Getting the name of the operating system
# print(os.name)

# # Getting the list of command-line arguments passed to a Python script
# print(sys.argv)

# # Example 6: Handling Import Errors
# try:
#     import non_existent_module
# except ImportError:
#     print("The module doesn't exist.")

# import math
# from datetime import datetime


# def calculate_circle_area(radius):
#     return math.pi * radius * radius


# def get_current_year():
#     return datetime.now().year


# * Classes
# Example 1: Defining and Instantiating a Class
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        return f"{self.name} says {self.sound}"


# Creating an instance of Animal
dog = Animal("Dog", "Woof")
print(dog.make_sound())  # Dog says Woof


# Example 2: Inheritance
class Bird(Animal):
    def __init__(self, name, sound, can_fly):
        super().__init__(name, sound)
        self.can_fly = can_fly

    def fly(self):
        return "flies" if self.can_fly else "can't fly"


# Creating an instance of Bird
sparrow = Bird("Sparrow", "Tweet", True)
print(f"{sparrow.make_sound()} and {sparrow.fly()}.")  # Sparrow says Tweet and flies.


# Example 3: Class Method and Static Method
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    @classmethod
    def square(cls, side_length):
        return cls(side_length, side_length)

    @staticmethod
    def is_square(width, height):
        return width == height


# Creating instances of Rectangle
rectangle = Rectangle(10, 20)
square = Rectangle.square(10)

print(f"Rectangle area: {rectangle.area()}")  # Rectangle area: 200
print(f"Square area: {square.area()}")  # Square area: 100
print(
    f"Is the rectangle a square? {'Yes' if Rectangle.is_square(rectangle.width, rectangle.height) else 'No'}"  # Is the rectangle a square? No
)
