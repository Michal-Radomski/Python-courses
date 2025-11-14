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


# Creating Our Own Objects
class PlayerCharacter:
    def __init__(self, name, age):  # Construction method
        self.name = name
        self.age = age

    def run(self):
        print("Run")

    def printSelf(self):
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
player1.printSelf()  # <__main__.PlayerCharacter object at 0x741eae193860>
print(player1)  # <__main__.PlayerCharacter object at 0x703d7ed93a10>
