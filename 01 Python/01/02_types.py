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
print(li)
print(new_li)

print("\ninsert")
new_li = li.insert(2, 2000)
print(li)
print(new_li)

print("\nextend")
new_li = li.extend([45, "hello"])
print(li)
print(new_li)

print("\npop")
new_li = li.pop()
print(li)
print(new_li)

print("\npop")
new_li = li.pop(0)
print(li)
print(new_li)

print("\nremove")
new_li = li.remove(2000)
print(li)
print(new_li)

print("\nclear")
new_li = li.clear()
print(li)
print(new_li)


# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# # 1. Remove the Banana from the list
# basket.remove("Banana")
# # 2. Remove "Blueberries" from the list.
# basket.remove("Blueberries")
# # 3. Put "Kiwi" at the end of the list.
# basket.append("Kiwi")
# # 4. Add "Apples" at the beginning of the list
# basket.insert(0, "Apples")
# # 5. Count how many apples in the basket
# basket.count("Apples")
# # 6. empty the basket
# basket.clear()
# print(basket)
