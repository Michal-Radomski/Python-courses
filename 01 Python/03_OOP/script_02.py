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
class User:
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

print(isinstance(wizard1, Wizard))  # True
print(isinstance(wizard1, User))  # True
print(isinstance(wizard1, object))  # True
