from utility import multiply, divide  # Be explicit!
from shopping.shopping_cart import buy

print(__name__)  # __main__

print(multiply)  # <function multiply at 0x705ea56ad3a0>

print(multiply(2, 5))  # 10
print(divide(6, 3))  # 2.0

print(buy("apple"))  # ['apple']
