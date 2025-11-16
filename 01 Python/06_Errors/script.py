#  Error Handling
while True:
    try:
        age = int(input("Enter your age: "))
        age_in_dogs_year = 10 / age

    except ZeroDivisionError:  # If there is an error
        print("enter age greater than 0")
        continue

    except ValueError:  # If there is an error
        print("Please enter a no.")
        break

    except ValueError:  # If there is an error
        print("!!!!")

    else:
        print(f"thank you, and your age is {age}")
        break

    finally:
        print("I will always get printed no matter what :)")

    print("can you hear me??????")
# thank you, and your age is 100
# I will always get printed no matter what :)


def division_fn(num1, num2):
    try:
        return num1 / num2
    except (ZeroDivisionError, TypeError) as err:
        print(f"error: {err}")


print(division_fn(1, "0"))  # error: unsupported operand type(s) for /: 'int' and 'str'
print(division_fn(1, 0))  # error: division by zero
print(division_fn(1, 4))  # 0.25

# * Raise Error -> raise() is a function that interrupts the normal execution process of a program.
print("Hello!!!!")
# raise TypeError("yo")
# raise Exception("Any message ")
# print("bye")

# try:
#     age = int(input("age: "))
#     age = 10 / age
#     raise ValueError("Ending the program")  # Ends a program
#     # raise Exception("quit")

# except ValueError:
#     print("Please enter a no.")

try:
    x = 1 / 0  # this raises ZeroDivisionError automatically
except ZeroDivisionError:
    print("Caught division by zero!")
    raise  # re-raises the same exception to propagate upward
