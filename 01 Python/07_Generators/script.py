# Generators


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
