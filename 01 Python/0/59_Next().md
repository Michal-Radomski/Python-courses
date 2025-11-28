The Python `next()` function is a built-in function that returns the next item from an iterator. If the iterator is exhausted
(no more items), it raises a `StopIteration` exception unless a default value is provided, in which case that default is
returned instead. This function is commonly used to manually iterate over items in an iterable.

In JavaScript (and TypeScript), an equivalent concept exists mainly in generator functions. These generators have a `next()`
method that returns an object with two properties: `value` (the next yielded value) and `done` (a boolean indicating if the
generator is finished). You call `next()` on a generator instance to get the next value, similar to Python's `next()`
function behavior.

### Python next() Function

- Used to get the next item from an iterator.
- Raises `StopIteration` if no items left unless a default is provided.
- Useful for manual iteration and can be combined with conditions.

### JavaScript/TypeScript Equivalent

- Generators are the closest feature providing a `next()` method.
- Calling `next()` returns `{ value, done }`, where `value` is the yielded item and `done` indicates completion.
- Regular iterators also support `next()` method but mostly used with generators.

This means the essential functionality of Python's `next()` is available in JavaScript/TypeScript through generators and
iterators, but it is accessed as a method on objects rather than a standalone function like in Python.[2][3][6]

[1](https://stackoverflow.com/questions/8273047/javascript-function-similar-to-python-range)
[2](https://favtutor.com/blogs/next-function-python)
[3](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator/next)
[4](https://www.youtube.com/watch?v=QTM_S5RtNco)
[5](https://www.reddit.com/r/learnjavascript/comments/1fag8ks/does_javascript_have_a_function_that_is/)
[6](https://www.geeksforgeeks.org/python/python-next-method/)
[7](https://www.geeksforgeeks.org/python/js-equivalent-to-python-range/)
[8](https://stackoverflow.com/questions/1733004/python-next-function)
[9](https://objectcomputing.com/resources/publications/sett/december-2020-comparing-python-and-javascript)
[10](https://www.codecademy.com/resources/docs/python/built-in-functions/next)
