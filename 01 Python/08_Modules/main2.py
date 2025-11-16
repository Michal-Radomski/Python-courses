from utility import *
from shopping import shopping_cart

print(__name__)  # __main__

# print(utilities)    # gives error
print(multiply(4, 10))  # 40
print(divide(10, 5))  # 2.0

# print(shopping)    # gives error
print(
    shopping_cart
)  # <module 'shopping.shopping_cart' from '.../shopping/shopping_cart.py'>
print(shopping_cart.buy("banana"))  # ['banana']
