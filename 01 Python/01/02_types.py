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
basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]]
print(basket)
print(basket[1][1][0])  # Oranges
