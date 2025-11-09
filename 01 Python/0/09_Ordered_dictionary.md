An ordered dictionary in Python can be created using the `OrderedDict` class from the `collections` module. This class
remembers the order in which keys are inserted, maintaining insertion order when iterating over the dictionary.

### Example:

```python
from collections import OrderedDict

od = OrderedDict()
od['apple'] = 1
od['banana'] = 2
od['cherry'] = 3

print(list(od.items()))
```

Output:

```
[('apple', 1), ('banana', 2), ('cherry', 3)]
```

Explanation:

- `OrderedDict` is a subclass of the built-in `dict` that preserves order.
- Insertion order is maintained throughout operations.
- It provides additional features like `move_to_end()` to reorder keys, `popitem()` to remove items from ends, and
  order-sensitive equality checks.

Starting with Python 3.7, the standard `dict` type itself preserves insertion order, but `OrderedDict` is still useful for
some advanced use cases requiring specialized methods.[2][3][4]

This is how you create and use an ordered dictionary in Python.

[1](https://sqlpey.com/python/python-dictionary-order-preservation/)
[2](https://www.geeksforgeeks.org/python/ordereddict-in-python/) [3](https://realpython.com/python-ordereddict/)
[4](https://coderivers.org/blog/python-dict-ordered/) [5](https://datagy.io/python-collections-ordereddict/)
[6](https://stackoverflow.com/questions/39980323/are-dictionaries-ordered-in-python-3-6)
[7](https://peps.python.org/pep-0372/)
