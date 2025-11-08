Here is a comparison of the main Python data types with their JavaScript (JS) and TypeScript (TS) counterparts:

| Python Type          | Description                          | JavaScript Type(s)          | TypeScript Type(s)            | Notes                                                                                   |
| -------------------- | ------------------------------------ | --------------------------- | ----------------------------- | --------------------------------------------------------------------------------------- |
| `str`                | Textual data, Unicode strings        | `string`                    | `string`                      | Both Python and JS/TS strings are Unicode by default.                                   |
| `int`                | Integer numbers                      | `number`                    | `number` or `bigint`          | JS has floating-point numbers only, with `bigint` for large ints.                       |
| `float`              | Floating-point numbers               | `number`                    | `number`                      | Python separates int and float; JS combines in `number`.                                |
| `complex`            | Complex numbers (a + bi)             | Not built-in                | Not built-in                  | JS/TS require libraries to handle complex numbers.                                      |
| `bool`               | Boolean values, True or False        | `boolean`                   | `boolean`                     | Equivalent boolean types in all three languages.                                        |
| `list`               | Ordered, mutable sequence            | `Array`                     | `Array<T>`                    | Python lists are like JS/TS arrays, both ordered and mutable.                           |
| `tuple`              | Ordered, immutable sequence          | Array                       | `[T1, T2, ...]` (tuple types) | Python tuples are immutable; TS tuples allow fixed types/length. JS arrays are mutable. |
| `dict`               | Key-value mapping (hash map)         | `Object`, `Map`             | `Record<K,V>`, `Map<K,V>`     | Python dicts are more like JS Maps with flexible key types.                             |
| `set`                | Unordered collection of unique items | `Set`                       | `Set<T>`                      | Both Python and JS have built-in set types.                                             |
| `frozenset`          | Immutable set                        | No direct equivalent        | No direct equivalent          | JS/TS sets are mutable; immutability needs external methods.                            |
| `NoneType` (`None`)  | Null/absence of value                | `null` or `undefined`       | `null` or `undefined`         | Represents no value or null in all languages.                                           |
| `bytes`, `bytearray` | Binary data                          | `ArrayBuffer`, `Uint8Array` | `ArrayBuffer`, `Uint8Array`   | Both handle raw binary data, though implementation differs.                             |

### Summary

- Python and JS/TS are dynamically typed (Python and JS) or optionally typed (TS).
- Python separates numeric types more distinctly (`int`, `float`, `complex`), whereas JS/TS mostly use `number`.
- Python tuples are immutable, while TS tuples specify fixed types/length but JS arrays are mutable.
- JS/TS have native `Set` and `Map` which are close to Python’s `set` and `dict`, but dicts have more flexible key types.
- Python’s `None` maps closely to JS/TS `null`/`undefined`.
- Binary data handling differs but all have specialized types for it.

This comparison provides a practical understanding of corresponding data types and their usage in the three
languages.[1][2][3][5][8]

[1](https://www.w3schools.com/python/python_lists.asp) [2](https://realpython.com/python-list/)
[3](https://www.w3schools.com/python/python_datatypes.asp) [4](https://docs.python.org/3/library/stdtypes.html)
[5](https://www.geeksforgeeks.org/python/python-data-types/)
[6](https://jakevdp.github.io/PythonDataScienceHandbook/02.01-understanding-data-types.html)
[7](https://www.digitalocean.com/community/tutorials/python-data-types)
[8](https://www.dataquest.io/blog/data-structures-in-python/)
[9](https://builtin.com/software-engineering-perspectives/python-tuples-vs-lists)
