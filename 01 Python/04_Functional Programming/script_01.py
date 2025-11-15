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


# * map()
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
