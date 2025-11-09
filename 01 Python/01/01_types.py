# Fundamental data types
# int -> 3, 5, -2
# float -> 0.5
# complex
# str
# bool
# list
# tuple
# set
# dict
# Non

# * Number and float
print(type(2 + 4))
print(type(2.5 + 4.5))
print(2 + 4)
print(type(2 - 4))
print(type(2 * 4))
print(2 / 4)
print(2.1 + 4.9)
print(2**4)
print(10 // 4)  # -> integer rounded down: 2
print(10 % 4)  # -> modulo: 2

# * Math functions
print(round(3.1))
print(round(3.5))
print(abs(0))
print(abs(-3.1))
print(abs(3.1))

# * Bin()
number = 15
binary_representation = bin(number)
print("Binary of", number, "is", binary_representation)
# Output: Binary of 15 is 0b1111

negative_number = -7
print("Binary of", negative_number, "is", bin(negative_number))
# Output: Binary of -7 is -0b111

print(int("0b101", 2))  # 5

# * Complex
# Create complex number with real part 3 and imaginary part 4
z1 = complex(3, 4)
print("z1 =", z1)
# Output: z1 = (3+4j)

# Another complex number using literal syntax
z2 = 2 + 5j
print("z2 =", z2)
# Output: z2 = (2+5j)

# Access real and imaginary parts
print("Real part of z1:", z1.real)
print("Imaginary part of z1:", z1.imag)

# * Variables
user_iq1 = 190
print(user_iq1)  # 190
user_age = user_iq1 / 4
print(user_age)  # 47.5

# * Constants
PI = 3.14  # only convention
print(PI)
a, b, c = 1, 2, 3
print(a, b, c)  # 1 2 3

# Exercise Augmented Assignment Operator
counter = 0
counter += 1
counter += 1
counter += 1
counter += 1
counter -= 1
counter *= 2
print(counter)  # 6

# * Strings
first_name = "Michal"
last_name = "R"
full_name = first_name + " " + last_name
print(full_name)

long_string = """
WOW
0 0
---
"""
print(long_string)

# String Concatenation
print("hello" + " Michal")
print("hello " + str(5))
print("\n")


# Type Conversion
print(type(int(str(100))))

a = str(100)
b = int(a)
c = type(b)
print(c)
print("\n")

# Escape Sequences
weather = '\t It\'s "kind of" sunny \n Hope you have a good day!'
print(weather)
print("\n")

# Formatted Strings
name = "Johnny"
age = 55
print("Hi" + name + ". You are" + str(age) + " years old.")
print(f"Hi {name}. You are {age} years old.")  # f -> formatted string

# Python2 Formatted Strings
print("Hi {}. Your are {} years old.".format(name, age))
print("Hi {1}. You are {0} years old.".format(age, name))
print("Hi {new_name}. You are {age} years old.".format(new_name="Sally", age=100))
print("\n")

# String Indexes
# [start:stop:stepover (default->1)]
python = "I am PYTHON"
print(python[1:4])  # " am"
print(python[1:])  # " am PYTHON"
print(python[:])  # "I am PYTHON"
print(python[1:100])  # " am PYTHON"
print(python[-1])  # "N"
print(python[-4])  # " T"
print(python[:-3])  # "I am PYT"
print(python[-3:])  # "HON"
print(python[::-1])  # "NOHTYP ma I"
print("\n")

# * Strings are Immutable!

# Built-In Functions + Methods
# https://docs.python.org/3/library/functions.html
# https://www.w3schools.com/python/python_ref_string.asp
print(len("Helllooooo"))
quote = "to be or not to be"
print(quote.upper())
print(quote.capitalize())
print(quote.find("be"))
print(quote.replace("be", "me"))
print(quote)  # "to be or not to be"

# * Boolean
is_cool = True
is_cool = False
print(bool(-0))
print(bool(0))
print(bool(1))
print(bool(0.5))
print(bool("0"))
print(bool("True"))
print(bool("False"))
print(bool(False))
print(bool("any random thing"))

# * All values are considered "truthy" except for the following, which are "falsy":
# None
# False
# 0
# 0.0
# 0j
# Decimal(0)
# Fraction(0, 1)
# [] - an empty list
# {} - an empty dict
# () - an empty tuple
# '' - an empty str
# b'' - an empty bytes
# set() - an empty set
# an empty range, like range(0)
# objects for which
#     obj.__bool__() returns False
#     obj.__len__() returns 0
