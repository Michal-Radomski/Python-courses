# Decorators
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
