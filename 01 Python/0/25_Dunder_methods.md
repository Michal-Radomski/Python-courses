The most common Python dunder (double underscore) methods are special predefined methods that allow objects to interact with
built-in functions and operators. Some key ones include:

- `__init__(self, ...)`: Constructor method called when an object is created.
- `__str__(self)`: Defines the string representation for printing.
- `__repr__(self)`: Official string representation for debugging.
- `__len__(self)`: Called by the built-in `len()` to get the object's length.
- `__getitem__(self, key)`: Defines behavior for indexing using square brackets.
- `__setitem__(self, key, value)`: Defines item assignment using square brackets.
- `__delitem__(self, key)`: Defines deletion of an item.
- `__iter__(self)`: Returns an iterator for the object to support loops.
- `__next__(self)`: Returns the next item in an iterator.
- `__contains__(self, item)`: Supports the `in` keyword to check membership.
- Arithmetic operator overrides like `__add__`, `__sub__`, `__mul__`, and their in-place forms such as `__iadd__`.
- Comparison operators like `__eq__`, `__lt__`, `__le__`, etc.

These dunder methods enable customizing object behavior with Python’s syntax and built-in operations.[1][3][9][10]

In JavaScript/TypeScript, there are no direct equivalents called dunder methods, but similar customization can be achieved
through other mechanisms:

- JavaScript’s `Symbol` type provides behavior customization similar to dunder methods, e.g., `Symbol.iterator` for
  iteration, `Symbol.toStringTag` for string representation, `Symbol.hasInstance` for `instanceof` checks.
- Proxy objects can intercept and customize operations like property access, assignment, etc.
- Method overriding and class inheritance enable some operator-like method customizations manually.
- No built-in magic methods for arithmetic or comparison operators exist; these must be implemented as regular methods and
  explicitly called.

So, while Python has formalized “dunder” magic methods that integrate closely into syntax and built-in functions,
JavaScript/TypeScript relies on Symbols, proxies, and conventions for similar customization but without direct operator
overloading or all-encompassing magic methods.[3][1]

This overview captures the most common Python dunder methods and their closest analogues in JavaScript/TypeScript.

[1](https://www.pythonmorsels.com/every-dunder-method/)
[2](https://www.reddit.com/r/Python/comments/1bioxer/every_dunder_method_in_python/)
[3](https://www.datacamp.com/tutorial/python-dunder-methods)
[4](https://www.geeksforgeeks.org/python/dunder-magic-methods-python/) [5](https://mathspp.com/blog/pydonts/dunder-methods)
[6](https://stackoverflow.com/questions/68140279/is-there-a-magic-and-dunder-method-to-make-a-list-object-in-python-oop)
[7](https://www.reddit.com/r/Python/comments/br9ok2/list_of_all_python_dunder_methods/)
[8](https://codesolid.com/dunder-methods-in-python-the-ugliest-awesome-sauce/)
[9](https://realpython.com/python-magic-methods/) [10](https://www.tutorialsteacher.com/python/magic-methods-in-python)
