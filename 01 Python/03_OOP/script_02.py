# OOP 2/2

# * Private vs Public Variables


class PlayerCharacter:
    def __init__(self, name, age):
        if age > 18:
            self._name = name  # * Convention: _ -> private property/method
            self._age = age  # * Convention: _ -> private property/method

    def speak(self):
        print(f"My name is {self._name} and I am {self._age} years old.")


player1 = PlayerCharacter("Tom", 20)
player1.speak()  # My name is Tom and I am 20 years old.


# * Inheritance
# Parent Class
class User:  # User accepts object as parent class class User(object)
    def sign_in(self):
        print("logged in")


# Sub Class/ Child Class/ Derived Class
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"Attacking with arrows: Arrows left- {self.num_arrows}")


wizard1 = Wizard("Merlin", 50)
archer1 = Archer("Robbin", 100)
wizard1.attack()  # Attacking with power of 50
archer1.attack()  # Attacking with arrows: Arrows left- 100

#  Isinstance(subclass, parent class)
print(isinstance(wizard1, Wizard))  # True
print(isinstance(wizard1, User))  # True
print(isinstance(wizard1, object))  # True
print(isinstance(wizard1, Archer))  # False

"""
By default every class is a subclass of 'object' class, hence when we type 'instance.' (object_name dot), we get all those
default methods suggestions from the IDE.
"""


# * Polymorphism
class User:
    def signed_in(self):
        print("User is logged in.")

    def attack(self):
        print("Do nothing.")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)  # Just a way to use parent class method.
        print(f"{self.name} is attacking with {self.power} power.")


class Archer(User):
    def __init__(self, name, arrow):
        self.name = name
        self.arrow = arrow

    def attack(self):
        print(f"{self.name} is attacking with {self.arrow} arrows.")


wizard1 = Wizard("John", 50)
archer1 = Archer("Mohan", 85)


def player_attack(char_):
    char_.attack()


player_attack(wizard1)
# Do nothing.
# John is attacking with 50 power.
player_attack(archer1)  # Mohan is attacking with 85 arrows.
# notice that these two instances are executing the child class method and not the parent class method.

for char in [wizard1, archer1]:
    char.attack()
# Do nothing.
# John is attacking with 50 power.
# Mohan is attacking with 85 arrows.

"""
This is polymorphism.
Even though we are using the same function, it is giving different output based on the object.
"""


# * Exercise
class Pets:
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"{self.name} is just walking around"


class Simon(Cat):
    def sing(self, sounds):
        return f"{sounds}"


class Sally(Cat):
    def sing(self, sounds):
        return f"{sounds}"


# 1 Add another Cat
class Chilli(Cat):
    def sing(self, sounds):
        return f"{sounds}"


# 2 Create a list of all the pets (create 3 cat instances from the above).
my_cats = [Simon("Simon", 5), Sally("Sally", 7), Chilli("Chilli", 3)]

# 3 Instantiate the Pet class with all your cats use variable my_pets.
my_pets = Pets(my_cats)
print(my_pets)

# 4 Output all the cats walking using the my_pets instance.
my_pets.walk()
# "Simon" is just walking around
# "Sally" is just walking around
# "Chilli" is just walking around


class Pets:
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"{self.name} is just walking around"


class Simon(Cat):
    def sing(self, sounds):
        return f"{sounds}"


class Sally(Cat):
    def sing(self, sounds):
        return f"{sounds}"


# 1 Add another Cat
class Chilli(Cat):
    def sing(self, sounds):
        return f"{sounds}"


# 2 Create a list of all the pets (create 3 cat instances from the above).
simon = Simon("Simon", 3)
sally = Sally("Sally", 2)
chilli = Chilli("Chilli", 4)


# 3 Instantiate the Pet class with all your cats use variable my_pets.
all_pets = [simon, sally, chilli]
print(my_pets)  # <__main__.Pets object at 0x75e08ea4b470>y

# 4 Output all the cats walking using the my_pets instance.
my_pets.walk()
# "Simon" is just walking around
# "Sally" is just walking around
# "Chilli" is just walking around


# * Super
class User:
    def __init__(self, email):
        self.email = email

    def signed_in(self):
        print("User is logged in.")

    def attack(self):
        print("Do nothing.")


class Wizard(User):
    def __init__(self, name, power, email):
        self.name = name
        self.power = power
        # same as using the below command, it does not take 'self' parameter
        super().__init__(email)
        # User.__init__(self, email)

    def attack(self):
        print(f"{self.name} is attacking with {self.power} power.")


wizard1 = Wizard("John", 50, "john@gmail.com")
print(wizard1.email)


# * Object Introspection
class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("logged in")


# Sub Class/ Child Class/ Derived Class
class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        # same as: User.__init__(self, email)
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with power of {self.power}")


wizard1 = Wizard("Merlin", 60, "merlin@gmail.com")
print(dir(wizard1))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attack', 'email', 'name', 'power', 'sign_in']


"""
It gives us all the methods and attributes that the item has access to.
But we get this functionality with IDEs build in, when we type item or instance name dot for eg. list.
And then IDE will pop a window with all the methods and attributes it has access to.
"""


# * Dunder Methods
class ActionFig:
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {"name": "Yoyo", "has_pets": "Dog"}

    def __str__(self):
        return f"{self.color}"

    def __len__(self):
        return 5

    def __call__(self):
        return "hello...??"

    def __getitem__(self, i):
        return self.my_dict[i]

    def __del__(self):
        return "deleted"


hulk = ActionFig("red", 0)

print(hulk.__str__())  # red
print(hulk)  # red
print(str(hulk))  # red
print(str("Printing an string"))  # Printing an string

print(hulk.__len__())  # 5
print(len(hulk))  # 5
print(len("0123456789"))  # 10

print(hulk.__call__())  # hello...??
# with call method, we get this special power to call a method with curly braces -> hello...??
print(hulk())

print(hulk.__getitem__("has_pets"))  # Dog
# it is same as print(hulk), it prints the memory location of the object
print(hulk.__repr__())  # <__main__.ActionFig object at 0x7d20fe40a000>

print(hulk.__del__())  # deleted
del hulk  # this deletes the variable passed, but as we have modified it, it won't delete the instance now

a = 5
del a
# print(a) # Error
"""
this will give us error, because we have deleted the variable a, 
because we haven't modified the base class __del__ method, so its performing normal
"""


# * Exercise
class SuperList(list):

    def __len__(self):
        return 1000


super_list1 = SuperList()
print(len(super_list1))  # 1000

super_list1.append(5)
print(super_list1[0])  # 5
# print(super_list1[1])  # Error
print(issubclass(SuperList, list))  # True
print(issubclass(list, object))  # True
print(issubclass(SuperList, object))  # True


# Multiple Inheritance
class User:
    def signed_in(self):
        print("User is logged in.")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"{self.name} is attacking with {self.power} power.")


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f"{self.name} is attacking with {self.arrows} arrows.")

    def check_arrows(self):
        print(f"{self.arrows} arrows left.")


# notice the order, in that order only it will give preference
class HybridAttacker(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)


hbot = HybridAttacker("Hydro", 50, 300)
hbot.attack()  # Hydro is attacking with 50 power.

print(hbot.name)  # Hydro
print(hbot.power)  # 50
print(hbot.arrows)  # 300

hbot.check_arrows()  # 300 arrows left.
hbot.signed_in()  # User is logged in.
