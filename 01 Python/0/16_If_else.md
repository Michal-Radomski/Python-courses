Here is a comparison of if..else conditional statements in Python, JavaScript/TypeScript, and Bash:

Syntax Style:

| Feature            | Python                        | JavaScript / TypeScript      | Bash                                          |
| ------------------ | ----------------------------- | ---------------------------- | --------------------------------------------- |
| If statement       | if condition:                 | if (condition) { ... }       | if condition; then                            |
| Else statement     | else:                         | else { ... }                 | else                                          |
| Else if (elif)     | elif condition:               | else if (condition) { ... }  | elif condition; then                          |
| Block delimitation | Indentation-based             | Curly braces {}              | Keywords then/fi and indentation not relevant |
| Condition syntax   | condition without parentheses | Condition in parentheses     | Condition without parentheses                 |
| Example            | if x > 0:                     | if (x > 0) {                 | if [ $x -gt 0 ]; then                         |
|                    | print("Positive")             | console.log("Positive");     | echo "Positive"                               |
|                    | else:                         | } else {                     | else                                          |
|                    | print("Non-positive")         | console.log("Non-positive"); | echo "Non-positive"                           |
|                    |                               | }                            | fi                                            |

Key Differences:

- Python uses colons and indentation to define code blocks, making the structure visually apparent.
- JavaScript/TypeScript requires parentheses around the condition and curly braces to delimit blocks.
- Bash uses keywords like then and fi to delimit blocks, and conditions are typically enclosed in brackets [] or [[]] with
  different test commands.
- Python uses "elif" for else-if, while both JS/TS and Bash use "else if" or "elif" respectively.
- Bash conditions compare strings, file properties, or numbers using specific syntax like -gt (greater than).

Example Code Snippets:

Python:

```python
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
```

JavaScript/TypeScript:

```typescript
if (x > 0) {
  console.log("Positive");
} else if (x === 0) {
  console.log("Zero");
} else {
  console.log("Negative");
}
```

Bash:

```bash
if [ $x -gt 0 ]; then
    echo "Positive"
elif [ $x -eq 0 ]; then
    echo "Zero"
else
    echo "Negative"
fi
```

This comparison covers the core syntax and structural differences in if..else statements across these common programming
languages and shell scripting.[1][2]

[1](https://pythonguides.com/typescript-if-else-conditionals/)
[2](https://objectcomputing.com/resources/publications/sett/december-2020-comparing-python-and-javascript)
[3](https://swapcode.ai/code-compare-difference) [4](https://www.webdevtutor.net/blog/typescript-vs-javascript-vs-python)
[5](https://stackinterface.com/is-typescript-better-than-python/)
[6](https://thelinuxcode.com/python-vs-javascript-a-thorough-comparison-of-two-popular-programming-languages/)
[7](https://langshift.dev/en/docs/js2py/module-01-syntax-comparison)
[8](https://blogs.purecode.ai/blogs/typescript-vs-python) [9](https://www.xjavascript.com/blog/typescript-vs-python/)
