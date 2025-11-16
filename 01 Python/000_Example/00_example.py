print("Hello World!")

age = input("How old are you?")
print("You are: " + age + " years old!")


def greet_user(name):
    print(f"Hello, {name}! Welcome to the Python script example.")


def check_number(num):
    if num > 0:
        print("The number is positive.")
    elif num == 0:
        print("The number is zero.")
    else:
        print("The number is negative.")


def main():
    name = input("What is your name?\n")
    greet_user(name)

    try:
        number = float(
            input("Enter a number to check if it is positive, zero, or negative:\n")
        )
        check_number(number)
    except ValueError:
        print("That's not a valid number.")

    print("Let's print numbers from 1 to 5:")
    for i in range(1, 6):
        print(i)


if __name__ == "__main__":
    main()


# * Higher-order function -> function that takes another function as argument
def apply_function(func, value):
    return func(value)


# A simple function to be passed to the higher-order function
def square(x):
    return x * x


result = apply_function(square, 5)  # Pass 'square' function as argument
print(result)  # * Output: 25


# * Compound function -> function that combines two functions into one
def compose(f, g):
    return lambda x: f(g(x))


# Functions to be composed
def add2(x):
    return x + 2


def multiply3(x):
    return x * 3


# Composing add2 and multiply3 (add2 after multiply3)
result = compose(add2, multiply3)(5)  # First multiply by 3, then add 2
print(result)  # * Output: 17 (5 * 3 = 15, 15 + 2 = 17)
