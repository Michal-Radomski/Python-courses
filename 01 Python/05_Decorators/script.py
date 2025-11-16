# Decorators
from time import time


# * Higher Order Function
# Higher Order Function (HOC) is a function which returns another function, or accepts another function
def greet(func):
    func()


def greet2():
    def hello():
        print("hello!")

    return hello()


print(greet(greet2))
# hello!
# None


# * Decorators (decorator is Higher Order Function)
def my_decorator(func):
    def wrap_func():
        print("***********")
        func()
        print("***********")

    return wrap_func


@my_decorator
def hello():
    print("Hello!")


hello()
# ***********
# Hello!
# ***********

greet = hello()
print(greet)
# ***********
# Hello!
# ***********
# None

greet = hello
print(greet)  # <function my_decorator.<locals>.wrap_func at 0x773ff7591080>


def bye():
    print("See you later")


a = my_decorator(bye)
a()
# ***********
# See you later
# ***********


my_decorator(bye)()
# ***********
# See you later
# ***********


# * Decorators2
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        func(*args, **kwargs)

    return wrap_func


@my_decorator
def hello(name, age):
    print(f"Hello {name}, your age is {age}.")


@my_decorator
def logged_in(username):
    print(f"{username} is logged in.")


hello("Mich", 21)  # Hello Mich, your age is 21
logged_in("Mich")  # Mich is logged in.


# * Exercise
def performance(fn):
    def wrap_fn(*args, **kwargs):
        t1 = time()
        fn(*args, **kwargs)
        t2 = time()
        print(f"It took {t2-t1} sec")

    return wrap_fn


@performance
def long_fn():
    for i in range(10000000):
        i * 5


long_fn()  # It took 0.3145303726196289 sec
