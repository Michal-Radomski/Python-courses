# Basics 2_2/2


# * Functions
# Positional *Parameters*
def say_hello(name, age):
    print(f"Hi {name}, your age is {age}")


# Default *Parameters*
def say_hello2(name="jojo", age=25):
    print(f"Hi {name}, your age is {age}")


# Positional *Arguments*
say_hello("Michal", 27)  # Hi Michal, your age is 27

# Default *Arguments*
say_hello2()  # Hi jojo, your age is 25
say_hello2("Michal")  # Hi Michal, your age is 25

# Keyword *Arguments* -> Bas Practice!
say_hello(age=89, name="YOHO")  # Hi YOHO, your age is 89


# Highest Even: Write a function to find the highest even number from the list.
def highest_even(li):
    evens = []
    for item in li:
        if not item % 2 and item not in evens:
            evens.append(item)
    return max(evens)


print(highest_even([10, 2, 3, 4, 8, 11]))  # 10

print(say_hello)  # eg <function say_hello at 0x784e269da340>
