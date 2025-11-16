import utility  # Module
import shopping.shopping_cart  # Package include a few modules

print(utility)  # <module 'utility' from '.../utility.py'>

print(utility.multiply(3, 4))  # 12
print(utility.divide(3, 4))  # 0.75

print(shopping)  # <module 'shopping' (namespace) from ['.../shopping']>
print(
    shopping.shopping_cart
)  # <module 'shopping.shopping_cart' from '.../shopping/shopping_cart.py'>
print(shopping.shopping_cart.buy("apple"))  # ['apple']

print(__name__)  # __main__
if __name__ == "__main__":
    print("this is the file being run, and not getting imported.")
# this is the file being run, and not getting imported.
