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

# * String formatting
name = "Rolf"
greeting = f"Hello, {name}"
print(greeting)  # Hello, Rolf

name = "Anne"
print(
    greeting
)  # This still prints "Hello, Rolf" because `greeting` was calculated earlier.
print(
    f"Hello, {name}"  # Hello, Anne
)  # This is correct, since it uses `name` at the current point in time.

# -- Using .format() --
# We can define template strings and then replace parts of it with another value, instead of doing it directly in the string.
greeting = "Hello, {}"
with_name = greeting.format("Rolf")
print(with_name)  # Hello, Rolf

longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format("Rolf", "Monday")
print(formatted)  # Hello, Rolf. Today is Monday.
