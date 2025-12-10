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


# # * Function arguments and parameters
# def add(x, y):  # * Parameters!!!
#     result = x + y
#     print(result)


# add(2, 3)  # * 5 -> arguments!!!


# # -- If a function doesn't have parameter, you can't give it arguments --
# def say_hello():
#     print("Hello!")


# # say_hello("Bob")  # Error


# # -- But if you add a parameter, then you must give it an argument --
# def say_hello(name):
#     print(f"Hello, {name}!")


# say_hello("Bob")
# # say_hello()  # Error, needs an argument


# # -- Keyword arguments --
# # To make things clearer, in Python you can give keyword arguments.
# def say_hello(name):
#     print(f"Hello, {name}!")


# # * Named arguments/ keyword arguments
# say_hello(name="Bob")  # Obvious that this is someone's name


# def divide(dividend, divisor):
#     if divisor != 0:
#         print(dividend / divisor)
#     else:
#         print("You fool!")


# divide(dividend=15, divisor=3)
# divide(15, 0)
# divide(15, divisor=0)  # That's OK
# # divide(dividend=15, 0)  # Not OK, named arguments must go after positional arguments


# # * Default params
# def add(x, y=3):
#     print(x + y)


# add(5)  # 8
# add(5, 8)  # 13
# # add(y=3)  # Error, missing x

# # -- Order of default parameters --

# # def add(x=5, y):  # Not OK, default parameters must go after non-default
# #     print(x + y)

# # -- Usually don't use variables as default value --
# # default_y = 3
# # def add(x, y=default_y):
# #     sum = x + y
# #     print(sum)
# # add(2)  # 5

# # default_y = 4
# # print(default_y)  # 4

# # add(2)  # 5, even though we re-defined default_y


# # * Functions returning values
# def add(x, y):
#     print(x + y)


# add(5, 8)
# result = add(5, 8)
# print(result)  # None

# # If we want to get something back from the function, it must return a value.
# # All functions return _something_. By default, it's None.


# # -- Returning values --
# def add(x, y):
#     return x + y


# add(1, 2)  # Nothing printed out anymore.
# result = add(2, 3)
# print(result)  # 5


# # -- Returning terminates the function --
# def add(x, y):
#     return
#     print(x + y)
#     return x + y


# result = add(5, 8)  # Nothing printed out
# print(result)  # None, as is the first return


# # -- Returning with conditionals --
# def divide(dividend, divisor):
#     if divisor != 0:
#         return dividend / divisor
#     else:
#         return "You fool!"


# result = divide(15, 3)
# print(result)  # 5

# another = divide(15, 0)
# print(another)  # You fool!


# # * Lambda functions in Python
# def add(x, y):
#     return x + y


# print(add(5, 7))  # 12

# # -- Written as a lambda --
# add = lambda x, y: x + y
# print(add(5, 7))  # 12


# def double(x):
#     return x * 2


# sequence = [1, 3, 5, 9]

# doubled = [
#     double(x) for x in sequence
# ]  # Put the result of double(x) in a new list, for each of the values in `sequence`
# doubled = map(double, sequence)
# print(list(doubled))  # [2, 6, 10, 18]

# # -- Written as a lambda --
# sequence = [1, 3, 5, 9]
# doubled = map(lambda x: x * 2, sequence)
# print(list(doubled))  # [2, 6, 10, 18]

# # -- Important to remember --
# # Lambdas are just functions without a name.
# # They are used to return a value calculated from its parameters.
# # Almost always single-line, so don't do anything complicated in them.
# # Very often better to just define a function and give it a proper name.

# # * Dictionary comprehensions
# users = [
#     (0, "Bob", "password"),
#     (1, "Rolf", "bob123"),
#     (2, "Jose", "longp4assword"),
#     (3, "username", "1234"),
# ]

# username_mapping = {user[1]: user for user in users}
# userid_mapping = {user[0]: user for user in users}
# print(
#     username_mapping
# )  # {'Bob': (0, 'Bob', 'password'), 'Rolf': (1, 'Rolf', 'bob123'), 'Jose': (2, 'Jose', 'longp4assword'), 'username': (3, 'username', '1234')}
# print(username_mapping["Bob"])  # (0, "Bob", "password")

# # -- Can be useful to log in for example --
# username_input = input("Enter your username: ")
# password_input = input("Enter your password: ")

# _, username, password = username_mapping[username_input]

# if password_input == password:
#     print("Your details are correct!")
# else:
#     print("Your details are incorrect.")

# # If we didn't use the mapping, the code would require us to loop over all users.
# # Shown on the side, pause the video if you want to read it thoroughly.

# # The dictionary must contain three keys: 'name', 'school', and 'grades'.
# # The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.
# student = {"name": "Jose", "school": "Computing", "grades": (66, 77, 88)}


# # Assume the argument, data, is a dictionary.
# # Modify the grades variable so it accesses the 'grades' key of the data dictionary.
# def average_grade(data):
#     grades = data["grades"]
#     return sum(grades) / len(grades)


# # Implement the function below
# # Given a list of students (a list of dictionaries), calculate the average grade received on an exam, for the entire class
# # You must add all the grades of all the students together
# # You must also count how many grades there are in total in the entire list
# def average_grade_all_students(student_list):
#     total = 0
#     count = 0
#     for student in student_list:
#         total = total + sum(student["grades"])
#         count = count + len(student["grades"])

#     return total / count


# * Unpacking arguments
def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total


print(multiply(3, 5))  # * (3,5)    15
print(multiply(-1))  # * (-1,)   -1

# The asterisk takes all the arguments and packs them into a tuple.
# The asterisk can be used to unpack sequences into arguments too!


def add(x, y):
    return x + y


nums = [3, 5]
print(add(*nums))  # instead of add(nums[0], nums[1]) -> 8


# -- Uses with keyword arguments --
# Double asterisk packs or unpacks keyword arguments
def add(x, y):
    return x + y


nums = {"x": 15, "y": 25}
print(add(**nums))  # 40


# -- Forced named parameter --
def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg
    return total


def apply(*args, operator):
    if operator == "*":
        return multiply(args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."


print(apply(1, 3, 6, 7, operator="+"))  # 17
# print(apply(1, 3, 5, "+"))  # Error


# * Unpacking keyword arguments
# -- Unpacking kwargs --
def named(**kwargs):
    print(kwargs)


named(name="Bob", age=25)  # {'name': 'Bob', 'age': 25}
# named({"name": "Bob", "age": 25})  # Error, the dictionary is actually a positional argument.

# Unpack dict into arguments. This is OK, but slightly more confusing. Good when working with variables though.
named(**{"name": "Bob", "age": 25})


# -- Unpacking and repacking --
def named(**kwargs):
    print(kwargs)


def print_nicely(**kwargs):
    named(**kwargs)  # Unpack the dictionary into keyword arguments.
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")


print_nicely(name="Bob", age=25)


# -- Both args and kwargs --
def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 3, 5, name="Bob", age=25)
# (1, 3, 5)
# {'name': 'Bob', 'age': 25}
# This is normally used to accept an unlimited number of arguments and keyword arguments, such that some of them can be passed onto other functions.
# You'll frequently see things like these in Python code:
