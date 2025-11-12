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
    return max(evens)


print(highest_even([10, 2, 3, 4, 8, 11]))  # 10

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
