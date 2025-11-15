# Functional Programming
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
from functools import reduce


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
