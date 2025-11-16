# Generators
from time import time


def generator_fn(num):
    print("check")
    # yield
    for i in range(num):  # Range is a generator
        print("****")
        yield i * 2
        print("####")


g = generator_fn(3)
print(g)  # <generator object generator_fn at 0x78d3efd85080>
print(next(g))
print(next(g))
print(next(g))
# print(next(g))  # StopIteration error
print(g)  # <generator object generator_fn at 0x7f6201385080>

for item in generator_fn(5):
    print(item)
# check
# ****
# 0
# ####
# ****
# 2
# ####
# ****
# 4
# ####
# ****
# 6
# ####
# ****
# 8
# ####

# here it goes to the generator_fn(), gets the 'i' value, pauses the function, until called for the 2nd time,
# and so on, it doesn't store all the no.s in the memory (just the most recent one).

"""
'yield' pauses the function and comes back to it when we do something to it, which is called 'next'.

if there is the keyword 'yield' written inside the function, then python recognizes that its a 
generator function, and won't run the function until the function is being iterated.
"""


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, *kwargs)
        t2 = time()
        print(f"took {t2-t1} s")
        return result

    return wrapper


@performance
def long_time():
    print("1")
    for i in range(1000000):  # it finishes after. -> took 0.03168940544128418 s
        i * 5


long_time()
print()


@performance
def long_time2():
    print("2")
    for i in list(range(1000000)):  # it took longer. -> took 0.054784297943115234 s
        i * 5


long_time2()
print()


# * Under the hood of generators
def my_own_forloop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break


my_own_forloop([1, 2, 3, 4, 5])
# <list_iterator object at 0x78beddc58520>
# 1
# <list_iterator object at 0x78beddc58520>
# 2
# <list_iterator object at 0x78beddc58520>
# 3
# <list_iterator object at 0x78beddc58520>
# 4
# <list_iterator object at 0x78beddc58520>
# 5
# <list_iterator object at 0x78beddc58520>


class OurOwnRange:
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        print("hehe")
        if self.current < self.last:
            num = OurOwnRange.current
            OurOwnRange.current += 1
            return num
        raise StopIteration


gen = OurOwnRange(0, 10)
print(gen)

for i in gen:
    print(i)

"""
loops by default deal with StopIteration error. they have build in functionality to handle them.
"""
