The `is` operator in Python is an identity operator that checks if two variables refer to the exact same object in memory,
returning `True` if they point to the same location and `False` otherwise.[4][6][8]

## Usage Examples

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)  # True (same object)
print(a is c)  # False (different objects, same value)
print(a == c)  # True (equal values)
```

Use `is` for checking singletons like `None` (`if x is None:`) rather than `==`, as it verifies object identity.[5][7][10][4]

## vs `==` Operator

Unlike `==`, which compares values for equality, `is` tests memory addresses via object IDs (`id()`). Small integers (-5
to 256) and some strings are interned, so `is` may return `True` unexpectedly for equal values.[1][6][10]

[1](https://realpython.com/python-operators-expressions/) [2](https://www.w3schools.com/python/python_operators.asp)
[3](https://docs.python.org/3/library/operator.html)
[4](https://stackoverflow.com/questions/13650293/understanding-the-is-operator)
[5](https://www.reddit.com/r/learnpython/comments/uvtr8i/how_does_comparison_using_is_operator_works_in/)
[6](https://www.geeksforgeeks.org/python/difference-between-and-is-operator-in-python/)
[7](https://saurus.ai/python-course/python-is-operator/) [8](https://www.w3schools.com/python/ref_keyword_is.asp)
[9](https://www.youtube.com/watch?v=qtTs03rI7W0) [10](https://realpython.com/python-is-identity-vs-equality/)
