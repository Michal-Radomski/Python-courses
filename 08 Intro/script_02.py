# List
items_to_purchase = ["Banana2", "Banana32", 20, "Apple", 20]
items_to_purchase[1] = "Guava"
items_to_purchase.append("Pencil")
items_to_purchase.append("Sharper")
items_to_purchase.remove("Sharper")
print((items_to_purchase))  # ['Banana2', 'Guava', 20, 'Apple', 20, 'Pencil']


# Tuples -> A tuple is a collection which is ordered and unchangeable
objects = ("Car", "Bike", "Airplane", 20, False, "Airplane")
list_object = list(objects)
list_object[1] = "CARS"
print((list_object))  # ['Car', 'CARS', 'Airplane', 20, False, 'Airplane']

# Sets
my_dataset = {"Car", "dog", 2, False, "Airplane", "Airplane", 2}
# my_dataset[2] = 10 #* TypeError: 'set' object does not support item assignment
print(len(my_dataset))  # 5
print(my_dataset)  # {False, 2, 'Car', 'dog', 'Airplane'}

# Dictionaries
data = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(data["year"])  # 1964
print(data)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
x = data.get("model")
print(x)  # Mustang

data["year"] = 2021
print(data)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 2021}

data.update({"model": "Aston Martin", "year": 1964})
print(data)  # {'brand': 'Ford', 'model': 'Aston Martin', 'year': 1964}

# data.pop()
for x in data.values():
    print(x)
# Ford
# Aston Martin
# 1964
