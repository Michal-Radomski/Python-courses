The equivalent of JavaScript/TypeScript BigInt in Python is simply the Python integer type (`int`), which supports arbitrary
precision integers without any special suffix or constructor. Python's `int` can handle very large numbers beyond typical
fixed-size integer limits, similar to JS/TS BigInt.

### Python integer ranges

- Python integers (`int`) have unlimited precision, only limited by available memory.
- Unlike JavaScript numbers (which are IEEE 754 doubles), Python integers automatically expand in size to accommodate very
  large values without loss of precision.

### JavaScript/TypeScript number ranges

- JS/TS `Number` type is based on 64-bit IEEE 754 floating point and can safely represent integers between \(-(2^{53} - 1)\)
  and \(2^{53} - 1\) (approximately \(-9,007,199,254,740,991\) to \(9,007,199,254,740,991\)).
- For integers outside this range, `BigInt` is used, which supports arbitrarily large integers by appending `n` to literals
  or using the `BigInt()` constructor.

| Feature                   | Python `int`           | JavaScript/TypeScript `Number`                 | JavaScript/TypeScript `BigInt`                  |
| ------------------------- | ---------------------- | ---------------------------------------------- | ----------------------------------------------- |
| Precision                 | Arbitrary precision    | 64-bit floating point (approx. 15 digits)      | Arbitrary precision integers                    |
| Range                     | Limited by memory      | Safe integers: \(-2^{53} +1\) to \(2^{53} -1\) | Unlimited, constrained by memory                |
| Syntax for large integers | Just normal integers   | Normal integers up to safe limit               | Append `n` suffix or use `BigInt()` constructor |
| Usage                     | No special type needed | Default numeric type                           | Used when integers exceed safe `Number` range   |

In conclusion, Python's native integer type is the direct counterpart to JavaScript/TypeScript's BigInt, both designed to
handle large integers without precision loss, but Python does it transparently for all integers.[1][3][5][7]

[1](https://stackoverflow.com/questions/73925572/bigint-equivalent-to-long-js)
[2](https://stackoverflow.com/questions/23556873/different-answer-in-javascript-and-python-with-large-number-division-or-mod-ope)
[3](https://www.tutorialspoint.com/typescript-bigint-vs-number) [4](https://exploringjs.com/js/book/ch_bigints.html)
[5](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
[6](https://www.geeksforgeeks.org/python/js-equivalent-to-python-range/) [7](https://www.w3schools.com/js/js_bigint.asp)
[8](https://news.ycombinator.com/item?id=18404743) [9](https://www.youtube.com/watch?v=RX85GuiOVkk)
[10](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation)
