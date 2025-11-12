# Basics 2_1/2

# * Conditional Logic
a = True
b = False

if a and b:
    print("Both a and b are true")
elif a:
    print("Only a is true")
elif b:
    print("Only b is true")
else:
    print("Both a and b are false")

is_old = True
is_licensed = True

if is_old and is_licensed:
    print("You are old enough to drive, and you have a license!")
else:
    print("You are not of age!")

print("ok ok")

# *  Truthy vs Falsy
print(bool("hello"))  # True
print(bool(5))  # True
print(bool(""))  # False
print(bool())  # False

# * All values are considered "truthy" except for the following, which are "falsy":
# None
# False
# 0
# 0.0
# 0j
# Decimal(0)
# Fraction(0, 1)
# [] - an empty list
# {} - an empty dict
# () - an empty tuple
# '' - an empty str
# b'' - an empty bytes
# set() - an empty set
# an empty range, like range(0)
# objects for which
#     obj.__bool__() returns False
#     obj.__len__() returns 0

# * Ternary Operator
is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message)  # message allowed

# * Short Circuiting
is_friend = True
is_user = True
print(is_friend and is_user)  # True
print(is_friend or is_user)  # True

# * Logical Operators
is_magician = False
is_expert = True

# Check if magician and expert: "you are a master magician"
if is_magician and is_expert:
    print("You are a master magician")  # ---

# Check if magician but not expert: "at least you're getting there"
elif is_magician and not is_expert:
    print("At least you're getting there.")  # ---

# Check if not a magician: "You need magic powers"
elif not is_magician:
    print("You need magic powers.")  # You need magic powers
else:
    print("Nothing")  # ---

print("a" > "A")  # True -> ord('a') > ord('A')
print(
    ord("a")
)  # Outputs 97 -> integer representing the Unicode code point of that character.
print(
    ord("A")
)  # Outputs 65 -> integer representing the Unicode code point of that character.

print(1 < 2 < 3 < 4)  # True
print(not (True))  # False

# * is vs ==
print(True == 1)  # True
print("" == 1)  # False
print([] == 1)  # False
print(10 == 10.0)  # True
print([] == [])  # True
print()

print(True == True)  # True
print("1" == 1)  # False
print(int("1") == 1)  # True
print([1, 2, 3] == [1, 2, 3])  # True
print()

print(True is 1)  # False
print("1" is 1)  # False
print([] is 1)  # False
print(10 is 10.0)  # False
print([1, 2, 3] is [1, 2, 3])  # False
print()

print(True is True)  # True
print("1" is "1")  # True
print([] is [])  # False

# * For Loops
for item in "Zero to Mastery":
    print(item, end=" ")
print()

for item in [1, 2, 3, 4, 5]:
    print(item, end=" ")
print()

for item in {1, 2, 3, 4, 5}:
    print(item, end=" ")
print()

for item in (1, 2, 3, 4, 5):
    print(item, end=" ")
print(item)
print()

# Nested Loops
for item in (1, 2, 3, 4, 5):
    for x in ["a", "b", "c"]:
        print(
            item, x, end="\t"
        )  # 1 a	1 b	1 c	2 a	2 b	2 c	3 a	3 b	3 c	4 a	4 b	4 c	5 a	5 b	5 c

# * Iterable -> list, dictionary, tuple, set, string

user = {"age": 45, "name": "john", "size": 10}

for i in user:
    print(i)

for i in user.keys():
    print(i)

for i in user.values():
    print(i)

for (
    i
) in user.items():  # it stores each pair as tuple, in a list (in a dict_items class).
    print(i)

print(user.items())
print(type(user.items()))
print(list(user.items()))

for key, value in user.items():
    print(key, value)
# age 45
# name john
# size 10

for item in user.items():
    key, value = item
    print(key, value)
# age 45
# name john
# size 10

# Write a program to find the sum of items in the list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

counter = 0
for item in my_list:
    counter += item

print(counter)  # 55

# * Range -> stop is omitted!
print(range(100))  # range(0, 100)
print(list(range(100)))  # [0, 1, ..., 99]

for _ in range(1, 5):
    print(_)  # 1 2 3 4

print("\n")
for _ in range(1, 10, 2):
    print(_)  # 1 3 5 7 9

print("\n")
for _ in range(10, 0, -1):
    print(_)  # 10 ... 1

# * Enumerate()
# we can pass any iterable to enumerate, and it will store them as separate tuple with index starting from 0.
# for i in enumerate("Hello World"):
#     print(i)

# for i, j in enumerate([1, 2, 3, 4]):
#     print(i, j)

# for i in enumerate((1, 2, 3, 4, 5)):
#     print(i)

# print(list(item for item in enumerate("123456789")))
# print((i * i for i in range(8)))

# print(list(enumerate("123456789")))

# print(dict(list(enumerate((i * i for i in range(1, 11)), 1))))

# Enumerate()
for i, char in enumerate("Hello"):
    print(i, char)
# 0 H
# 1 e
# 2 l
# 3 l
# 4 o

for i, char in enumerate([1, 2, 3]):
    print(i, char)

for i, char in enumerate(range(100)):
    if char == 50:
        print(f"index of 50 is: {i}")

# * While loops
# i = 0
# while i < 5:
#     print(i)
#     i += 1
#     break
# else:
#     print("done")

# while True:
#     response = input("say something: ")
#     if response == "bye":
#         break

i = 0
while i < 50:
    print(i, end="\t")
    i += 1
else:
    print("\nDone with all the work.")
print()

my_list = [1, 2, 3]
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
# 1
# 2
# 3
print()

while True:
    response = input("Say Something: ")
    if response == "bye":
        break

# * Break, Continue, Pass

my_list = [1, 2, 3]
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    continue
print()
# 1
# 2
# 3

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    break
print()
# 1

i = 0
while i < len(my_list):
    i += 1
    pass  # Does nothing!

print("No error")  # No error

# * Exercise!
# * Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

# Answer:
for row in picture:
    for pixel in row:
        if pixel:
            print("*", end="")
        else:
            print(" ", end="")
    print("")
#    *
#   ***
#  *****
# *******
#    *
#    *
#    *

# * Exercise Find Duplicates
some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]
duplicates = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)  # ['b', 'n']
