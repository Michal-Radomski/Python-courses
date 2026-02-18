Here is a list of most Python keywords compared with their closest JavaScript (JS) / TypeScript (TS) equivalents or concepts:

| Python Keyword | Description / Use                     | JS/TS Equivalent(s)              | Notes                              |
| -------------- | ------------------------------------- | -------------------------------- | ---------------------------------- |
| `False`        | Boolean false                         | `false`                          | Same boolean literal               |
| `True`         | Boolean true                          | `true`                           | Same boolean literal               |
| `None`         | Null or no value                      | `null`, `undefined`              | Python’s `None` most like `null`   |
| `and`          | Logical and                           | `&&`                             | Logical AND operator               |
| `or`           | Logical or                            | `\|\|`                           | Logical OR operator                |
| `not`          | Logical not                           | `!`                              | Logical NOT operator               |
| `if`           | Conditional statement                 | `if`                             | Same                               |
| `elif`         | Else if branch                        | `else if`                        | Control flow                       |
| `else`         | Else branch                           | `else`                           | Control flow                       |
| `while`        | Loop while condition is true          | `while`                          | Same                               |
| `for`          | Loop over sequence                    | `for`, `for...of`, `for...in`    | More loop styles in JS/TS          |
| `break`        | Exit loop                             | `break`                          | Same                               |
| `continue`     | Skip to next loop iteration           | `continue`                       | Same                               |
| `def`          | Define a function                     | `function` keyword               | Or arrow function syntax in JS/TS  |
| `return`       | Return value from function            | `return`                         | Same                               |
| `class`        | Define a class                        | `class`                          | Same                               |
| `try`          | Exception handling block              | `try`                            | Same                               |
| `except`       | Handle exception                      | `catch`                          | Similar purpose                    |
| `finally`      | Always execute block                  | `finally`                        | Same                               |
| `raise`        | Throw an exception                    | `throw`                          | Same functionality                 |
| `import`       | Import modules                        | `import`                         | ES6 modules                        |
| `from`         | Import specific elements from module  | `import {}`                      | ES6 modules various import forms   |
| `as`           | Alias in import                       | `as` (TypeScript), aliasing      | Used in different contexts         |
| `lambda`       | Anonymous function                    | Arrow function `( ) => { }`      | Functional syntax                  |
| `global`       | Declare global variable               | Globals accessible by default    | JS globals handled differently     |
| `nonlocal`     | Access enclosing scope variable       | No direct equivalent             | JS closures achieve similar effect |
| `is`           | Identity comparison (object identity) | Strict equality `===`            | Similar but different uses         |
| `in`           | Membership test (value in container)  | `in` operator                    | Similar for objects/arrays         |
| `pass`         | No operation                          | Empty block `{}`                 | Used to do nothing                 |
| `yield`        | Generator function output             | `yield` (ES6 generators)         | Same generator concept             |
| `assert`       | Debug assertion                       | No direct keyword, manual checks | Can throw error with condition     |
| `async`        | Define asynchronous function          | `async` keyword                  | Same async/await support           |
| `await`        | Wait for async function result        | `await`                          | Same                               |
| `del`          | Delete object/property                | `delete`                         | Same operator                      |

### Summary

Python and JS/TS share many language concepts despite syntax differences. Both support conditionals, loops, functions,
classes, exception handling, modules, async programming, and generators, though the exact keywords differ or have slightly
different syntaxes.

Python's keyword list is smaller and more specialized towards readability, while JS/TS have some more complex syntax forms,
especially for functions and modules.

This table covers the majority of frequently used keywords and their closest JS/TS equivalents.[1][2][10]

[1](https://www.geeksforgeeks.org/python/python-keywords/) [2](https://flexiple.com/python/python-reserved-words)
[3](https://www.youtube.com/watch?v=rKk8XPLysj8) [4](https://www.programiz.com/python-programming/keyword-list)
[5](https://www.w3schools.com/python/python_ref_keywords.asp) [6](https://docs.python.org/3/library/functions.html)
[7](https://realpython.com/python-keywords/)
[8](https://stackoverflow.com/questions/9642087/is-it-possible-to-get-a-list-of-keywords-in-python)
[9](https://labex.io/tutorials/python-understand-keywords-and-built-in-identifiers-in-python-585777)
[10](https://www.scholarhat.com/tutorial/python/keywords-in-python)

JavaScript and TypeScript have no direct `pass` keyword like Python, since block syntax doesn't require indentation or
content—empty blocks `{}` serve the same purpose as a no-op placeholder.
[stackoverflow](https://stackoverflow.com/questions/33383840/is-there-a-javascript-equivalent-of-the-python-pass-statement-that-does-nothing)

## Common Equivalents

- **Empty block**: Use `{}` in functions, loops, conditionals, or `catch` blocks.
  ```javascript
  if (condition) {
    // pass equivalent - does nothing
  }
  function noop() {} // Empty function body
  ```
- **Comments**: Add `// pass` for readability in empty blocks.
  [stackoverflow](https://stackoverflow.com/questions/33383840/is-there-a-javascript-equivalent-of-the-python-pass-statement-that-does-nothing)

## Examples

```javascript
// Python: def func(): pass
function func() {} // JS/TS equivalent

// Python: try: risky() except: pass
try {
  risky();
} catch {} // Empty catch block[web:12]
```

This works identically in both JS and TS, maintaining structure without executing code.
[webdevtutor](https://www.webdevtutor.net/blog/typescript-equivalent-of-pass)
