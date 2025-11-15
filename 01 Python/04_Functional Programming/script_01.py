# Functional Programming
from functools import reduce
import functools


# * Pure Functions
def multiply_by2(li):
    new_li = []
    for item in li:
        new_li.append(item * 2)
    return new_li


print(multiply_by2([5, 6, 8]))  # [10, 12, 16]
"""
If we define 'new_li' outside the function, or print something inside the function, then it is no longer a pure function.
"""


# * Map()
def multiply_by2(item):
    return item * 2


my_list = [5, 8, 9]

# it returns a map object, which then we can convert to a list/tuple/set
print(map(multiply_by2, my_list))  # <map object at 0x7789e8f92cb0

# notice that we just write the function name without the curly braces
print(list(map(multiply_by2, my_list)))  # [10, 16, 18]
print(my_list)  # [5, 8, 9]

"""
notice that map is not modifying anything, and creating a new list.
it is also using separate data and function to work upon them.
it's a nice concept of Functional programming and pure function.
"""


# * Filter()
def only_even(item):
    return item % 2 == 0


my_list = [5, 8, 9, 2, 5, 6, 98, 56, 62]

print(filter(only_even, my_list))  # <filter object at 0x7a1c8378f130>
print(list(filter(only_even, my_list)))  # [8, 2, 6, 98, 56, 62]
print(
    list(map(only_even, my_list))
)  # [False, True, False, True, False, True, True, True, True]
print(my_list)  # [5, 8, 9, 2, 5, 6, 98, 56, 62]

# * Zip()
li1 = [1, 2, 3]
set1 = {4, 5, 6}
tuple1 = (7, 8, 9)

print(zip(li1, set1, tuple1))  # <zip object at 0x71e34d64b780>
print(
    list(zip(li1, set1, tuple1))
)  # combines the items sequence wise into a sequence of tuples -> [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
print(li1, set1, tuple1)  # [1, 2, 3] {4, 5, 6} (7, 8, 9)

# * Reduce()


def accumulator(acc, item):
    print(f"acc: {acc}, item: {item}")
    return acc + item


my_list = [1, 2, 3, 4, 5]
print(reduce(accumulator, my_list))  # by default takes '0' as the 3rd argument -> 15
print(reduce(accumulator, my_list), 0)  # by default takes '0' as the 3rd argument -> 15
print(reduce(accumulator, my_list, 10))  # 25
print(my_list)  # [1, 2, 3, 4, 5]

"""
acc is nothing but the return of the last iteration.
"""

# * Exercise
# 1 Capitalize all of the pet names and print the list
my_pets = ["sisi", "bibi", "titi", "carla"]


def capitalize(string):
    return string.upper()


print(list(map(capitalize, my_pets)))  # ['SISI', 'BIBI', 'TITI', 'CARLA']


# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ["a", "b", "c", "d", "e"]
my_numbers = [5, 4, 3, 2, 1]

print(
    list(zip(my_strings, sorted(my_numbers)))
)  # [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]


# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def is_smart_student(score):
    return score > 50


print(list(filter(is_smart_student, scores)))  # [73, 65, 76, 100, 88]


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, (my_numbers + scores)))  # 456

# * Lambda Expressions
my_list = [1, 2, 3, 4, 5]

print(list(map(lambda item: item * 2, my_list)))  # [2, 4, 6, 8, 10]

print(list(filter(lambda item: item % 2 != 0, my_list)))  # [1, 3, 5]

print(functools.reduce(lambda acc, item: item + acc, my_list))  # 15

"""
syntax:
lambda param: action(param)
it automatically returns the action taken,
it do not have any name, doesn't get stored in the memory.
and so used only once.
and behaves exactly like a function.
"""

a = [(0, 2), (4, 4), (10, -1), (5, 3)]

a.sort(key=lambda x: x[1], reverse=False)
print(a)  # [(10, -1), (0, 2), (5, 3), (4, 4)]

# * Exercise
my_list = [5, 4, 3]

print(list(map(lambda item: item * item, my_list)))  # [25, 16, 9]
print(list(map(lambda item: item**2, my_list)))  # [25, 16, 9]

# List Sorting
a = [(0, 2), (4, 3), (9, 9), (10, -2)]

a.sort(key=lambda x: x[1])
print(a)  # [(10, -2), (0, 2), (4, 3), (9, 9)]

# * List Comprehensions
my_list = []

for item in "hello":
    my_list.append(item)

print(my_list)  # ['h', 'e', 'l', 'l', 'o']

my_list1 = [item for item in "Saurabh"]
print(my_list1)  # ['S', 'a', 'u', 'r', 'a', 'b', 'h']

my_list2 = [num**2 for num in range(1, 11)]
print(my_list2)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# * Set and Dictionary Comprehension
# only even squares
my_set = {num**2 for num in range(1, 11) if num**2 % 2 == 0}
print(my_set)  # {64, 100, 4, 36, 16}
# remember that set don't contain duplicate values

my_dict = {num: num**2 for num in range(1, 11)}
print(my_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}


random_dict = {"a": 1, "b": 2, "c": 3, "d": 4}

my_new_dict = {k: v**2 for k, v in random_dict.items()}
print(my_new_dict)  # {'a': 1, 'b': 4, 'c': 9, 'd': 16}

my_new_dict2 = {k: v**2 for k, v in random_dict.items() if v % 2 == 0}
print(my_new_dict2)  # {'b': 4, 'd': 16}

# * Exercise
some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)  # ['b', 'n']


# Solution:
some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]
duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))
print(duplicates)  # ['b', 'n']
