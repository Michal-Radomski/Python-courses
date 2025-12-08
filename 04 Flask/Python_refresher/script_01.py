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
l = ["Bob", "Rolf", "Anne"]  # * List
t = ("Bob", "Rolf", "Anne")  # * Tuple -> immutable!
s = {"Bob", "Rolf", "Anne"}  # * Set -> can't duplicate elems!

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

# * Operations on Sets
# -- Difference between two sets --
friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

# local_friends = ...
# If there are 3 friends, and 2 are abroad, that means that 1 friend is local.
# We can easily calculate which names are in `friends` but not in `abroad` by using `.difference`

local = friends.difference(abroad)
print(local)  # {'Rolf'}

print(abroad.difference(friends))  # This returns an empty set -> set()

# -- Union of two sets --
local = {"Rolf"}
abroad = {"Bob", "Anne"}

# friends = ...
# If we have 1 local friend and 2 abroad friends, we could calculate the total friends by using `.union`

friends = local.union(abroad)
print(friends)  # {'Rolf', 'Bob', 'Anne'}

# -- Intersection of two sets --
art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

# Given these two sets of students, we can calculate those who do both art and science by using `.intersection`
both = art.intersection(science)
print(both)  # {'Jen', 'Bob'}

s1 = {1, 3, 4, 5, 7, 8}
s2 = {2, 3, 4, 6, 8, 9}

s3 = s1.symmetric_difference(s2)
s4 = s1.difference(s2) | s2.difference(s1)

print(s3)  # {1, 2, 5, 6, 7, 9}
print(s4)  # {1, 2, 5, 6, 7, 9}

# * Booleans
print(5 == 5)  # True
print(5 > 5)  # False
print(10 != 10)  # False
# Comparisons: ==, !=, >, <, >=, <=

# -- is --
# Python also has the `is` keyword. It's a confusing keyword for now, so I don't recommend using it.
friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]

print(friends == abroad)  # True
print(friends is abroad)  # False -> checks the memory!

# * If
day_of_week = input("What day of the week is it today? ")

if day_of_week == "Monday":
    print("Have a great start to your week!")
elif day_of_week == "Friday":
    print("It's ok to finish a bit early!")
else:
    print("Full speed ahead!")

# -- Problem: user not entering what we expect --
day_of_week = input("What day of the week is it today? ").lower()

if day_of_week == "monday":
    print("Have a great start to your week!")
elif day_of_week == "friday":
    print("It's ok to finish a bit early!")
else:
    print("Full speed ahead!")

# * In keyword
friends = ["Rolf", "Bob", "Jen"]
print("Jen" in friends)  # True
# * The `in` keyword works in most sequences like lists, tuples, and sets.

movies_watched = {"The Matrix", "Green Book", "Her"}
user_movie = input("Enter something you've watched recently: ")

if user_movie in movies_watched:
    print(f"I've watched {user_movie} too!")
else:
    print("I haven't watched that yet.")

# --
number = 7
user_input = input("Enter 'y' if you would like to play: ")

if user_input in ("y", "Y"):
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif number - user_number in (1, -1):
        print("You were off by 1.")
    else:
        print("Sorry, it's wrong!")
