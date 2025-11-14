# OOP
class BigObject:  # Class
    # code
    pass


obj1 = BigObject()  # instantiate
obj2 = BigObject()  # instantiate
obj3 = BigObject()  # instantiate

print(type(None))  # <class 'NoneType'>
print(type(True))  # <class 'bool'>
print(type(5))  # <class 'int'>
print(type(5.5))  # <class 'float'>
print(type("hi"))  # <class 'str'>
print(type([]))  # <class 'list'>
print(type(()))  # <class 'tuple'>
print(type({}))  # <class 'dict'>
print(type(BigObject))  # <class 'type'>
print(type(obj1))  # <class '__main__.BigObject'>


# * Creating Our Own Objects
class PlayerCharacter:
    def __init__(self, name, age):  # Construction method
        self.name = name
        self.age = age

    def run(self):
        print("Run")

    def print_self(self):
        print(self)


player1 = PlayerCharacter("Cindy", 44)
player2 = PlayerCharacter("Tom", 21)
player2.attack = 50

print(player1.name)
print(player2.name)
print(player1.age)
print(player2.age)
player1.run()
print(player2.attack)
# print(player1.attack) #* Error
player1.print_self()  # <__main__.PlayerCharacter object at 0x741eae193860>
print(player1)  # <__main__.PlayerCharacter object at 0x703d7ed93a10>


# * Attributes and Methods
class PlayerCharacter:
    membership = True  # Class object attribute, its an attribute of PlayerCharacter. It is a static attribute

    def __init__(self, name, age):
        if self.membership:  # or we can write: 'if PlayerCharacter.membership :'
            self.name = name  # these are dynamic attribute
            self.age = age

    def run(self):
        print(f"run {self.name}")
        # print(f"run {PlayerCharacter.name})   # we cannot do this

    def shout(self):
        print(f"My name is {self.name}")


player1 = PlayerCharacter("Rohan", 22)
player2 = PlayerCharacter("Mohan", 98)

print(player1.name)
print(
    player1.membership
)  # each of the class instance can assess the class object attribute -> True
print(player1.run())
# run Rohan
# None
player1.run()  # run Rohan
player1.shout()  # My name is Rohan

# help(list)

# * __init__


class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name="anonymous", age=0):
        if age > 18:
            self.name = name
            self.age = age

    def shout(self):
        print(f"My name is {self.name}")


player1 = PlayerCharacter("Tom", 20)
player2 = PlayerCharacter(age=20)
print(player1.shout())
# My name is Tom
# None
print(player2.name)  # anonymous


# * Exercise
class Cat:
    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Answers:
# 1 Instantiate the Cat object with 3 cats.
cat1 = Cat("cat1", 5)
cat2 = Cat("Cat2", 7)
cat3 = Cat("Cat3", 3)


# 2 Create a function that finds the oldest cat.
def oldest_cat(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.".
print(
    f"Oldest Cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old."
)  # Oldest Cat is 7 years old.


# * @classmethod and @staticmethod
class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        if self.membership:
            self.name = name
            self.age = age

    def run(self):
        print(f"run {self.name}")

    # Not often used!
    @classmethod  # we can use this method without instantiating the class
    def add_things(cls, n1, n2):  # cls -> class, instead of self
        return cls("Jojo", n1 + n2)

    # Not often used!
    @staticmethod  # same as @classmethod, only thing is we don't pass the class as argument, and hence can't use its attribute
    def add_things2(n1, n2):
        return n1 + n2


player1 = PlayerCharacter.add_things(4, 5)
# Jojo
# 9
print(player1.name)  # ---
print(player1.age)  # ---
print(player1.membership)  # True

print(PlayerCharacter.add_things2(45, 5))  # 50
# print(player2.membership)     # gives error
