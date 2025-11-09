# Types 2
# * Lists (Array in JS/TS)

li = [1, 2.5, "hello", True]
print(li)

amazon_cart = ["laptop", "book", "phone", "pen", "key"]
# start:stop:stepover
print(amazon_cart[0])  # laptop
print(amazon_cart[::-1])  # ['key', 'pen', 'phone', 'book', 'laptop']
print(amazon_cart[0:2])  # ['laptop', 'book']
print(amazon_cart)

print("\nPart-2")
new_cart = amazon_cart  # here we are actually passing the address of the old list,
# and not copying and storing the list in new location.
new_cart[0] = "PC"  # lists are mutable, unlike strings which are immutable.
print(
    amazon_cart
)  # notice that the old list is also modified. -> ['PC', 'book', 'phone', 'pen', 'key']
print(new_cart)  # ['PC', 'book', 'phone', 'pen', 'key']

print("\nPart-3")
flipkart_cart = amazon_cart[
    :
]  # - here we are actually copying the whole list to another location or we can use .copy()
flipkart_cart[0] = "headphones"
print(amazon_cart)  # ['PC', 'book', 'phone', 'pen', 'key']
print(flipkart_cart)  # ['headphones', 'book', 'phone', 'pen', 'key']

print("\nPart-4")
my_list = [1, 2, 3]
bonus = my_list + [5]
my_list[0] = "z"
print(my_list)  # ['z', 2, 3]
print(bonus)  # [1, 2, 3, 5]

new_list = ["a", "b", "c"]
print(new_list[1])  # b
print(new_list[-2])  # b
print(new_list[1:3])  # ['b', 'c']
new_list[0] = "z"
print(new_list)  # ['z', 'b', 'c']
print("\n")

# Matrix
basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]]
print(basket)
print(basket[1][1][0])  # Oranges

# * List Methods
print("\nappend")
li = [1, 2, 3, 4, 5]
new_li = li.append(100)
print(li)  # [1, 2, 3, 4, 5, 100]
print(new_li)  # None

print("\ninsert")
new_li = li.insert(2, 2000)
print(li)  # [1, 2, 2000, 3, 4, 5, 100]
print(new_li)  # None

print("\nextend")
new_li = li.extend([45, "hello"])
print(li)  # [1, 2, 2000, 3, 4, 5, 100, 45, 'hello']
print(new_li)  # None

print("\npop")
new_li = li.pop()
print(li)  # [1, 2, 2000, 3, 4, 5, 100, 45]
print(new_li)  # hello

print("\npop")
new_li = li.pop(0)
print(li)  # [2, 2000, 3, 4, 5, 100, 45]
print(new_li)  # 1

print("\nremove")
new_li = li.remove(2000)
print(li)  # [2, 3, 4, 5, 100, 45]
print(new_li)  # None

print("\nclear")
new_li = li.clear()
print(li)  # []
print(new_li)  # None


li = ["a", "b", "c", "d", "e", "d"]
print(
    li.index("d")
)  # if that value is not there in the list, then it will throw an error and program will stop running. -> 3

# lookup:start:stop
print(li.index("d", 0, 5))  # 3

print("a" in li)  # we use this to avoid the error. -> True
print("x" in li)  # False

name = "Michal"
print("b" in name)  # we can use this with strings as well -> False

print(li.count("d"))  # 2

li2 = [1, 2, 5, 6, 7, 4, 56, 38, 0]
print(li2.sort())  # None
print(li2)  # [0, 1, 2, 4, 5, 6, 7, 38, 56]

print(li2.reverse())  # None
print(li2)  # [56, 38, 7, 6, 5, 4, 2, 1, 0

print("Sorted function")
print(
    sorted(li2)
)  # its a function which sort the list, but it does not modify the list permanently. -> # [0, 1, 2, 4, 5, 6, 7, 38, 56]
print(li2)  # [56, 38, 7, 6, 5, 4, 2, 1, 0]

new_li2 = li2.copy()  # same as doing new_li = li[:]
print(new_li2)  # [56, 38, 7, 6, 5, 4, 2, 1, 0]


basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# 1. Remove the Banana from the list
basket.remove("Banana")
# 2. Remove "Blueberries" from the list.
basket.remove("Blueberries")
# 3. Put "Kiwi" at the end of the list.
basket.append("Kiwi")
print(basket)  # ['Apples', 'Oranges', 'Kiwi']
# 4. Add "Apples" at the beginning of the list
basket.insert(0, "Apples")
# 5. Count how many apples in the basket
basket.count("Apples")
# 6. empty the basket
basket.clear()
print(basket)  # []

friends = ["Simon", "Patty", "Joy", "Carrie", "Amira", "Chu"]
new_friend = ["Stanley"]
friends.extend(new_friend)
print(sorted(friends))  # ['Amira', 'Carrie', 'Chu', 'Joy', 'Patty', 'Simon', 'Stanley']

print(list(range(1, 100)))

words = ["Hello", "world", "from", "Python"]
result = " ".join(words)
print(result)  # Hello world from Python

result = "-".join(words)
print(result)  # Hello-world-from-Python

# List Unpacking
a, b, c, *other, d = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    0,
]  # this will work with set, tuple and normal (as in 1,2,3,4,5) also. and it always store the variables as list, if more than one item, otherwise as int.

print(type(a))
print(b)  # 2
print(c)  # 3
print(other)  # [4, 5, 6, 7, 8, 9]
print(type(other))
print(d)  # 0

# * None
weapons = None
print(weapons)  # None -> null in JS/TS

# Dictionaries
my_dict = {"a": [1, 2, 3], "b": "hello", "c": True}
print(type(my_dict))  # <class 'dict'>

my_list = [
    {"a": [1, 2, 3], "b": "hello", "c": True},
    {"a": [4, 5, 6], "b": "bye", "c": False},
]

print(my_dict["a"])  # [1, 2, 3]
print(my_dict["a"][1])  # 2
print(my_list[1]["a"][2])  # 6

# Ordered Dictionary
from collections import OrderedDict

od = OrderedDict()
od["apple"] = 1
od["banana"] = 2
od["cherry"] = 3

print(list(od.items()))  # [('apple', 1), ('banana', 2), ('cherry', 3)]


# * Optional chaining equivalent
def optional_chain(root, *keys):
    result = root
    for key in keys:
        if isinstance(result, dict):
            result = result.get(key, None)
        else:
            result = getattr(result, key, None)
        if result is None:
            break
    return result


obj = {"a": {"b": {"c": 1}}}
print(optional_chain(obj, "a", "b", "c"))  # outputs 1
print(optional_chain(obj, "a", "x", "c"))  # outputs None

# * Dictionary Methods
user = {"name": "john", "sex": "M", "age": 20}
# * print(user["height"]) # this will give us error, as height doesn't exit in the dictionary.

print(user.get("height"))  # None

print(
    user.get("height", 6)
)  # if the key value pair doesn't exit, then it will write the default value.
print(user)  # 6

# new way to create a dictionary
user2 = dict(name="saurabh", age=25)
print(user2)  # {'name': 'saurabh', 'age': 25}
print(user2["name"])  # saurabh


user = {"name": "john", "sex": "M", "age": 20}

print("john" in user.items())  # False
print("sex" in user)  # True

print("john" in user.values())  # True
print("sex" in user.keys())  # True

print(
    user.items()
)  # returns a list containing a tuple for each key value pair -> dict_items([('name', 'john'), ('sex', 'M'), ('age', 20)])

print(user.clear())  # None
print(user)  # {}


user2 = {"name": "pepy", "sex": "F", "age": 45}

print(user2.pop("age"))  # 45
print(user2)  # {'name': 'pepy', 'sex': 'F'}

print(user2.update({"sex": "M"}))  # None
print(user2)  # {'name': 'pepy', 'sex': 'M'}

print(user2.update({"size": 32}))  # None
print(user2)  # {'name': 'pepy', 'sex': 'M', 'size': 32}

print(
    user2.popitem()
)  # it randomly pops an item -> ('size', 32), #* Python 3.7 remove the last item!
print(user2)  # {'name': 'pepy', 'sex': 'M'}

print(user2.keys())  # {'name': 'pepy', 'sex': 'M'}
print(user2.values())  # {'name': 'pepy', 'sex': 'M'}


user3 = {
    "age": 45,
    "username": "john",
    "weapons": ["gun"],
    "is_active": True,
    "clan": "army",
}

user3["weapons"].append("shield")
user3["weapons"] = user3["weapons"] + ["pistol"]
print(
    user3
)  # {'age': 45, 'username': 'john', 'weapons': ['gun', 'shield', 'pistol'], 'is_active': True, 'clan': 'army'}

# * Dictionary Exercise
# 1 Create a user profile for your new game.
# This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'
user_profile = {
    "age": 0,
    "username": " ",
    "weapons": None,
    "is_active": False,
    "clan": None,
}

# 2 iterate and print all the keys in the above user.
print(user_profile.keys())

# 3 Add a new weapon to your user
user_profile["weapons"] = "Katana"

# 4 Add a new key to include 'is_banned'. Set it to false
user_profile.update({"is_banned": False})

# 5 Ban the user by setting the previous key to True
user_profile["is_banned"] = True

# 6 create a new user2 my copying the previous user and update the age value and username value.
user2 = user_profile.copy()
user2.update({"age": 50, "username": "User2"})
print(
    user_profile
)  # {'age': 0, 'username': ' ', 'weapons': 'Katana', 'is_active': False, 'clan': None, 'is_banned': True}
print(
    user2
)  # {'age': 50, 'username': 'User2', 'weapons': 'Katana', 'is_active': False, 'clan': None, 'is_banned': True}
