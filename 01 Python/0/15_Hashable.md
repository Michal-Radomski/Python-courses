In Python, an object is considered hashable if it has a hash value that remains constant during the object's lifetime. This
means the object implements a `__hash__()` method that returns an integer hash value, and an `__eq__()` method for
comparison. Hashable objects can be used as keys in dictionaries or as elements in sets because these data structures rely on
hashing for fast lookup and storage.

Hashability requires that the hash value does not change over time, which is why only immutable objects like integers,
strings, and tuples containing only hashable elements are hashable. Mutable objects such as lists or dictionaries are not
hashable, as their content can change, which would change their hash value and violate this requirement.

In summary, "hashable" means having a fixed, consistent hash value throughout the object's lifetime, enabling its use in
hash-based collections like sets and dictionaries.[1][2][3]

[1](https://realpython.com/ref/glossary/hashable/) [2](https://www.askpython.com/python-modules/python-hashable-objects)
[3](https://stackoverflow.com/questions/14535730/what-does-hashable-mean-in-python)
[4](https://www.geeksforgeeks.org/python/why-and-how-are-python-functions-hashable/)
[5](https://realpython.com/videos/immutable-vs-hashable/) [6](https://www.pythonmorsels.com/what-are-hashable-objects/)
[7](https://pythonforthelab.com/blog/what-are-hashable-objects) [8](https://www.youtube.com/watch?v=DKR0-PDWb20)
[9](https://www.reddit.com/r/learnpython/comments/6zwefw/sets_requires_item_to_be_hashable_what_does_this/)
