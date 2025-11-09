Here is a comparison of common list (array) methods in Python with their equivalents in JavaScript/TypeScript:

| Python List Method   | Description                                             | JavaScript/TypeScript Array Method                    | Notes                                                          |
| -------------------- | ------------------------------------------------------- | ----------------------------------------------------- | -------------------------------------------------------------- |
| append()             | Adds an element to the end of the list                  | push()                                                | Similar usage                                                  |
| clear()              | Removes all elements                                    | length = 0 or splice(0)                               | JS does not have clear(), but resetting length or splice works |
| copy()               | Returns a shallow copy                                  | slice() or [...array]                                 | Both create shallow copies                                     |
| count(value)         | Counts occurrences of value                             | filter(v => v === value).length                       | No direct method, but filter can be used                       |
| extend(iterable)     | Extends list by appending elements from iterable        | push(...iterable)                                     | Spread syntax used for multiple elements                       |
| index(value)         | Returns index of first occurrence                       | indexOf(value)                                        | Similar usage                                                  |
| insert(index, value) | Inserts value at specified index                        | splice(index, 0, value)                               | Use splice to insert                                           |
| pop([index])         | Removes and returns element at index (last if no index) | pop() removes last; splice(index, 1) removes at index | JS pop() only removes last element                             |
| remove(value)        | Removes first occurrence of value                       | splice(array.indexOf(value), 1)                       | No direct remove; use indexOf + splice                         |
| reverse()            | Reverses the list in-place                              | reverse()                                             | Same method name and behavior                                  |
| sort()               | Sorts the list in-place (can take key function)         | sort()                                                | JS sort takes comparator function                              |

### Notes:

- Python lists are dynamic arrays similar to JavaScript arrays.
- JavaScript has no direct equivalent of Python's `count()`, but can emulate it using `filter`.
- Python’s `copy()` returns a shallow copy; JavaScript can use `slice()` or spread syntax `[...array]`.
- JavaScript's `pop()` only removes the last element; removing from arbitrary indices uses `splice`.

This comparison covers the most commonly used methods, providing functional parallels and differences in usage between Python
lists and JS/TS arrays.[3][4][7]

[1](https://coderivers.org/blog/array-list-python/) [2](https://ilovepython.net/python-list-array-methods/)
[3](https://pythonexamples.org/python-list-methods/) [4](https://www.w3schools.com/python/python_ref_list.asp)
[5](https://docs.python.org/3/tutorial/datastructures.html)
[6](https://www.geeksforgeeks.org/python/advanced-python-list-methods-and-techniques/)
[7](https://www.programiz.com/python-programming/methods/list)
