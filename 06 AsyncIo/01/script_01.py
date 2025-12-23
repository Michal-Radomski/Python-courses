# Example 1: Defining a Simple Function
def greet():
    print("Hello, Python learners!")


# Example 2: Function with Parameters
def greet_person(name):
    print(f"Hello, {name}!")


# Example 3: Function with Default Parameter Values
def greet_with_default(name="learner"):
    print(f"Hello, {name}!")


# Example 4: Function Returning a Value
def add_two_numbers(a, b):
    return a + b


# Example 5: Function with Arbitrary Number of Arguments
def greet_multiple_people(*names):
    for name in names:
        print(f"Hello, {name}!")


# Example 6: Function with Keyword Arguments
def display_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")


# Example 7: Using a Function as a Variable (First-Class Citizens)
def square(number):
    return number * number


my_function = square
result = my_function(5)  # Calling the function stored in 'my_function'

# Calling the examples
greet()
greet_person("Alice")
greet_with_default()
greet_with_default("Bob")
result = add_two_numbers(3, 5)
print(f"The sum is: {result}")
greet_multiple_people("Alice", "Bob", "Charlie")
display_info(name="Alice", age=30, city="New York")
print(f"The square of 5 is: {result}")
