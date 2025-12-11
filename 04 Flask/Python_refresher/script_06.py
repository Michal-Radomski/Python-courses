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
