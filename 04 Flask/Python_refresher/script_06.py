# First-class functions
# A first class function just means that functions can be passed as arguments to functions.


def calculate(*values, operator):
    return operator(*values)


def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You fool!"


# We pass the `divide` function as an argument
result = calculate(20, 4, operator=divide)
print(result)  # 5.0


def average(*values):
    return sum(values) / len(values)


result = calculate(10, 20, 30, 40, operator=average)
print(result)  # 25.0


# -- searching with first-class functions --
def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}")


friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]


def get_friend_name(friend):
    return friend["name"]


print(search(friends, "Anne Pun", get_friend_name))


# -- using lambdas since this can be simple enough --
def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}")


friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]

print(search(friends, "Anne Pun", lambda friend: friend["name"]))


# -- or as an extra, using built-in functions --
from operator import itemgetter


def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}")


friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]

print(search(friends, "Rolf Smith", itemgetter("name")))

# * Decorators
# user = {"username": "jose", "access_level": "guest"}


# def get_admin_password():
#     return "1234"


# print(get_admin_password())  # Can do this even though I'm a "guest"

# # Now this only runs if I'm an admin... but
# if user["access_level"] == "admin":
#     print(get_admin_password())

# print(get_admin_password())  # The function itself is still unsecured


# # -- "secure" function --
# def secure_get_admin():
#     if user["access_level"] == "admin":
#         print(get_admin_password())


# # Now secure_get_admin() is secure.
# # But get_admin_password() is still around, and I could call it:
# secure_get_admin()
# print(get_admin_password())


# # We want to get rid of get_admin_password so that only the secure function remains!
# # Maybe something like this?
# def secure_function(func):
#     if user["access_level"] == "admin":
#         return func


# user = {"username": "bob", "access_level": "admin"}

# get_admin_password = secure_function(get_admin_password)
# print(get_admin_password())  # Error!

# # When we ran `secure_function`, we checked the user's access level. Because at that point the user was not an admin, the function did not `return func`. Therefore `get_admin_password` is set to `None`.


# # We want to delay overwriting until we run the function
# def get_admin_password():
#     return "1234"


# def make_secure(func):
#     def secure_function():
#         if user["access_level"] == "admin":
#             return func()

#     return secure_function


# get_admin_password = make_secure(
#     get_admin_password
# )  # `get_admin_password` is now `secure_func` from above

# user = {"username": "jose", "access_level": "guest"}
# print(get_admin_password())  # Now we check access level

# user = {"username": "bob", "access_level": "admin"}
# print(get_admin_password())  # Now we check access level


# # -- More information or error handling --
# def get_admin_password():
#     return "1234"


# def make_secure(func):
#     def secure_function():
#         if user["access_level"] == "admin":
#             return func()
#         else:
#             return f"No admin permissions for {user['username']}."

#     return secure_function


# get_admin_password = make_secure(
#     get_admin_password
# )  # `get_admin_password` is now `secure_func` from above

# user = {"username": "jose", "access_level": "guest"}
# print(get_admin_password())  # Now we check access level

# user = {"username": "bob", "access_level": "admin"}
# print(get_admin_password())  # Now we check access level

user = {"username": "jose", "access_level": "guest"}


# * Decorators -> (at) syntax
def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function


@make_secure
def get_admin_password():
    return "1234"


# -- keeping function name and docstring --
import functools

user = {"username": "jose", "access_level": "guest"}


def make_secure(func):
    @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function


@make_secure
def get_admin_password():
    return "1234"


# * Mutability in Python
a = []
b = a
# Remember a and b are _names_ for the list. They both have the _same_ value.

a.append(35)  # Modify the value.

print(a)  # [35]
print(b)  # [35]

# We mutated (changed) the value, its names still point to the _same thing_, so it doesn't matter which name you use.

a = []
b = []

a.append(35)

print(a)  # [35]
print(b)  # []

# Here they are different lists, because [] creates a new list every time. You can check whether two things are the _same_ one by usingt the `id()` function:

print(id(a))
print(id(b))  # Different from id(a)

# -- immutable --
# Some values can't be changed because they don't have methods that modify the value itself.
# In case of the list, `.append()` mutates the list.
# For example integers don't have any such methods, so they are called _immutable_.

a = 8597
b = 8597

print(id(a))
print(id(b))  # Same one

a = 8598

print(id(a))
print(
    id(b)
)  # Different, because we didn't change 8597. We just used the name 'a' for a different value. 'b' still is a name for 8597.

# Most things are mutable in Python. If you want to keep one of your classes immutable, don't add any methods that change the objects' properties.

# Tuples and strings are the only fundamental collection in Python which is immutable.
# Lists, sets, dictionaries are all mutable.
# Integers, floats, and booleans are all immutable.

# -- += and similar --
# A lot of beginners think this:
a = "hello"
b = a

print(id(a))
print(id(b))

a += "world"

# Would cause 'b' to change
# But it doesn't, because strings are immutable. When you do str + str, a _new_ string is created.
# This means that a becomes a new string containing "helloworld", but b still is a name for "hello".

print(id(a))
print(id(b))


# * Mutable default parameters (and why they're a bad idea)
# from typing import List


# class Student:
#     def __init__(self, name: str, grades: List[int] = []):  #* This is bad!
#         self.name = name
#         self.grades = grades

#     def take_exam(self, result):
#         self.grades.append(result)


# bob = Student("Bob")
# rolf = Student("Rolf")
# bob.take_exam(90)
# print(bob.grades)
# print(rolf.grades)  # Whaaaaaat

# The function parameters evaluate when the function is defined, not when it runs.
# That means that self.grades is a name for the list that was evaluated when the function was defined.
# We're then modifying it in take_exam
# But all calls to the __init__ method have the same list (because parameters are only evaluated once!)
# So all students have the same list

# Avoid it by not having mutable parameters. Instead, do what we did in prior lectures:

from typing import List


class Student:
    def __init__(self, name: str, grades: List[int] = None):
        self.name = name
        self.grades = grades or []  # * New list created if one isn't passed

    def take_exam(self, result):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)  # Now it's empty.
