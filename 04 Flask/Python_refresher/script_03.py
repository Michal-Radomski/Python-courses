# * Functions
# def hello():
#     print("Hello!")


# hello()


# # -- Defining vs. calling --
# # It's still all sequential!
# def user_age_in_seconds():
#     user_age = int(input("Enter your age: "))
#     age_seconds = user_age * 365 * 24 * 60 * 60
#     print(f"Your age in seconds is {age_seconds}.")


# print("Welcome to the age in seconds program!")
# user_age_in_seconds()
# print("Goodbye!")

# # -- Don't reuse names --
# # def print():
# #     print("Hello, world!")  # Error!


# # -- Don't reuse names, it's generally confusing! --
# # friends = ["Rolf", "Bob"]
# # def add_friend():
# #     friend_name = input("Enter your friend name: ")
# #     friends = friends + [friend_name]  # Another way of adding to a list!
# # add_friend()
# # print(friends)  # Always ['Rolf', 'Bob']


# # -- Can't call a function before defining it --
# def say_hello():
#     print("Hello!")


# say_hello()


# # -- Remember function body only runs when the function is called --
# def add_friend():
#     friends.append("Rolf")


# friends = []
# add_friend()
# print(friends)  # [Rolf]


# * Function arguments and parameters
def add(x, y):  # * Parameters!!!
    result = x + y
    print(result)


add(2, 3)  # * 5 -> arguments!!!


# -- If a function doesn't have parameter, you can't give it arguments --
def say_hello():
    print("Hello!")


# say_hello("Bob")  # Error


# -- But if you add a parameter, then you must give it an argument --
def say_hello(name):
    print(f"Hello, {name}!")


say_hello("Bob")
# say_hello()  # Error, needs an argument


# -- Keyword arguments --
# To make things clearer, in Python you can give keyword arguments.
def say_hello(name):
    print(f"Hello, {name}!")


# * Named arguments/ keyword arguments
say_hello(name="Bob")  # Obvious that this is someone's name


def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You fool!")


divide(dividend=15, divisor=3)
divide(15, 0)
divide(15, divisor=0)  # That's OK
# divide(dividend=15, 0)  # Not OK, named arguments must go after positional arguments


# * Default params
def add(x, y=3):
    print(x + y)


add(5)  # 8
add(5, 8)  # 13
# add(y=3)  # Error, missing x

# -- Order of default parameters --

# def add(x=5, y):  # Not OK, default parameters must go after non-default
#     print(x + y)

# -- Usually don't use variables as default value --
# default_y = 3
# def add(x, y=default_y):
#     sum = x + y
#     print(sum)
# add(2)  # 5

# default_y = 4
# print(default_y)  # 4

# add(2)  # 5, even though we re-defined default_y


# * Functions returning values
def add(x, y):
    print(x + y)


add(5, 8)
result = add(5, 8)
print(result)  # None

# If we want to get something back from the function, it must return a value.
# All functions return _something_. By default, it's None.


# -- Returning values --
def add(x, y):
    return x + y


add(1, 2)  # Nothing printed out anymore.
result = add(2, 3)
print(result)  # 5


# -- Returning terminates the function --
def add(x, y):
    return
    print(x + y)
    return x + y


result = add(5, 8)  # Nothing printed out
print(result)  # None, as is the first return


# -- Returning with conditionals --
def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You fool!"


result = divide(15, 3)
print(result)  # 5

another = divide(15, 0)
print(another)  # You fool!
