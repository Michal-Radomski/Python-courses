# # Variables
# # -- Numbers and Floats --
# x = 15
# price = 9.99
# discount = 0.2
# result = price * (1 - discount)
# print(result)  # 7.992000000000001

# # -- Strings --
# name = "Rolf"
# name = "Rolf"
# print(name)  # Rolf
# print(name * 2)  # RolfRolf

# # -- Changing variables --
# # Variables are names for values.
# a = 25
# b = a

# # Here we've given the value '25' the names 'a' and 'b'.
# print(a)  # 25
# print(b)  # 25
# b = 17
# # Here we've given the value '17' the name 'b'. The name 'a' is still a name for '25'!
# print(a)  # 25
# print(b)  # 17

# # * String formatting
# name = "Rolf"
# greeting = f"Hello, {name}"
# print(greeting)  # Hello, Rolf

# name = "Anne"
# print(
#     greeting
# )  # This still prints "Hello, Rolf" because `greeting` was calculated earlier.
# print(
#     f"Hello, {name}"  # Hello, Anne
# )  # This is correct, since it uses `name` at the current point in time.

# # -- Using .format() --
# # We can define template strings and then replace parts of it with another value, instead of doing it directly in the string.
# greeting = "Hello, {}"
# with_name = greeting.format("Rolf")
# print(with_name)  # Hello, Rolf

# longer_phrase = "Hello, {}. Today is {}."
# formatted = longer_phrase.format("Rolf", "Monday")
# print(formatted)  # Hello, Rolf. Today is Monday.

# # * User Input
# name = input("Enter your name: ")
# print(name)

# # -- Mathematics on user input --
# size_input = input("How big is your house (in square feet): ")
# square_feet = int(size_input)
# square_metres = square_feet / 10.8  # Make sure this is correct
# print(f"{square_feet} square feet is {square_metres} square metres.")

# user_age = input("Enter your age: ")
# age_number = int(user_age)

# months = age_number * 12
# print(f"{age_number} is equal to {months} months.")

# * Lists, tuples, and sets
l = ["Bob", "Rolf", "Anne"]  # List
t = ("Bob", "Rolf", "Anne")  # Tuple
s = {"Bob", "Rolf", "Anne"}  # Set

# Access individual items in lists and tuples using the index.
print(l[0])  # Bob
print(t[0])  # Bob
# print(s[0])  #* This gives an error because sets are unordered, so accessing element 0 of something without order doesn't make sense.

# Modify individual items in lists using the index.
l[0] = "Smith"
# t[0] = "Smith"  #* This gives an error because tuples are "immutable".

print(l)  # ['Smith', 'Rolf', 'Anne']
print(t)  # ('Bob', 'Rolf', 'Anne')

# Add to a list by using `.append`
l.append("Jen")
print(l)  # ['Smith', 'Rolf', 'Anne', 'Jen']
# * Tuples cannot be appended to because they are immutable.

# Add to sets by using `.add`
s.add("Jen")
print(s)  # {'Jen', 'Anne', 'Bob', 'Rolf'}

# Sets can't have the same element twice.
s.add("Bob")
print(s)  # {'Jen', 'Anne', 'Bob', 'Rolf'}
