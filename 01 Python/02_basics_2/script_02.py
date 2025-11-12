# Basics 2_2/2


# * Functions
# Function should do one thing
# Function should return something


# Positional *Parameters*
def say_hello(name, age):
    print(f"Hi {name}, your age is {age}")


# Default *Parameters*
def say_hello2(name="jojo", age=25):
    print(f"Hi {name}, your age is {age}")


# Positional *Arguments*
say_hello("Michal", 27)  # Hi Michal, your age is 27

# Default *Arguments*
say_hello2()  # Hi jojo, your age is 25
say_hello2("Michal")  # Hi Michal, your age is 25

# Keyword *Arguments* -> Bas Practice!
say_hello(age=89, name="YOHO")  # Hi YOHO, your age is 89


# Highest Even: Write a function to find the highest even number from the list.
def highest_even(li):
    evens = []
    for item in li:
        if not item % 2 and item not in evens:
            evens.append(item)
    return max(evens)  # max() build-in function!


print(highest_even([2, 10, 2, 3, 4, 8, 11]))  # 10

print(say_hello)  # eg <function say_hello at 0x784e269da340>


# * Keyword: Return
def sum1(num1, num2):
    return num1 + num2


total = sum1(10, 5)
print(sum1(10, total))  # 25
print()


def sum2(num1, num2):
    def another_func(n1, n2):
        return n1 + n2

    return another_func(num1, num2)


total = sum2(10, 20)
print(total)  # 30


# * Exercise
def checkDriverAge():
    age = input("What is your age?: ")
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")


checkDriverAge()


def checkDriverAge2(age=0):
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")


checkDriverAge2(99)


# * Docstrings
def test(a):
    """
    info: This is test function which print the argument passed
    """
    print(a)


help(test)
print(test.__doc__)  # info: This is test function which print the argument passed


# * Clean Code
def is_even(num):
    return num % 2 == 0


print(is_even(50))  # True


def is_odd(num):
    return num % 2 == 1


print(is_odd(5))  # True
print(is_odd(10))  # False


# * *args and **kwargs
def super_func(
    *args, **kwargs
):  # we can actually name these parameters anything we want, but its a good practice to give the same name only.
    print(args)  # (1, 2, 3, 4, 5)
    print(type(args))  # <class 'tuple'>
    print(*args)  # 1 2 3 4 5
    # print(type(*args)) 	# gives error

    print(kwargs)  # {'num1': 5, 'num2': 10}
    # print(**kwargs) 	# gives error
    print(kwargs.keys())  # dict_keys(['num1', 'num2'])
    print(kwargs.values())  # dict_values([5, 10])
    print(type(kwargs))  # <class 'dict'>

    total = 0
    for items in kwargs.values():
        total += items

    return sum(args) + total  # sum() is build-in function!


print(super_func(1, 2, 3, 4, 5, num1=5, num2=10))  # 30

# Rules for the order of parameters
# positional parameters, *args, default parameters, **kwargs


def super_func(name, *args, i="hi", **kwargs):
    total = 0
    for item in kwargs.values():
        total += item
    print(i, name)
    return sum(args) + total


print(super_func("Mich", 1, 2, 3, 4, 5, i="hello", num1=5, num2=10))
# hello Mich
# 30

# * Walrus Operator -> :=
a = "helloooooooooo"

if (n := len(a)) > 10:
    print(f"too long {n} elements")  # too long 14 elements

while (n := len(a)) > 1:
    print(n)
    a = a[:-1]
# 14
# 13
# 12
# 11
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# h

print(a)


# * Scope
test_var = 100  # Global scope


b = 1


def parent_func():
    # b = 10
    # total = 0
    def local_func():
        return b

    return local_func()


print(parent_func())  # 1
print(b)  # 1

# print(total)    # this will produce an error, as 'total' is undefined.
# scope of a function remains inside the function only.

# 1 - start with local
# 2 - parent local
# 3 - global
# 4 - built in python functionsI

# * Global keyword - Not good practice!
total = 0


def count():
    global total  # Use the global variable total
    total += 1  # here we are referenced total before assignment, hence we have declare 'global total' first
    return total


count()
count()
count()

print(total)  # 3


# * Nonlocal keyword - it is used to access parent variables - Not good practice!
def outer():
    x = "outer"

    def inner():
        nonlocal x  # this won't create a new variable 'x', and will modify the parent 'x' only.
        x = "inner"
        print("inner x: " + x)  # inner x: inner

    inner()
    print("outer x: " + x)  # outer x: inner


outer()


def outer2():
    x = "outer"

    def inner2():
        x = "inner"
        print("inner2 x: " + x)  # inner2 x: inner

    inner2()
    print("outer2 x: " + x)  # outer2 x: outer


outer2()
