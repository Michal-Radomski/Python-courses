import random
from random import shuffle
import sys


print(random)  # <module 'random' from '/usr/lib/python3.12/random.py'>
# print(dir(random))
# print(help(random))

print(random.random())  # eg 0.09664545653920054
print(random.randint(1, 100))  # eg 25
print(
    random.choice("saurabh")
)  # We can pass any iterator, like a list for example -> eg r
print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # eg 4

my_list = [1, 2, 3, 4, 5]
shuffle(my_list)
# print(my_list)  # eg [3, 2, 5, 4, 1]

print(sys)  # <module 'sys' (built-in)>
print(sys.argv)  # ['script_01.py']
