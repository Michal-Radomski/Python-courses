Async functions in Python use the `async def` syntax to define coroutines, which enable asynchronous programming via the
`asyncio` library.

## Python Syntax

An async function is declared with `async def`, and it returns a coroutine object that must be awaited or scheduled on an
event loop. For example:

```python
import asyncio

async def fetch_data():
    await asyncio.sleep(1)  # Simulate I/O
    return "Data fetched"

async def main():
    result = await fetch_data()
    print(result)

asyncio.run(main())
```

Execution requires `asyncio.run()` or similar to start the event loop, as Python does not have a global loop by
default.[2][7]

## JavaScript/TypeScript Syntax

JS/TS uses `async function` and inherently returns a Promise, runnable directly without an explicit loop since
Node.js/browser environments manage it automatically. Example:

```javascript
async function fetchData() {
  await new Promise((resolve) => setTimeout(resolve, 1000)); // Simulate I/O
  return "Data fetched";
}

fetchData().then((result) => console.log(result));
```

Top-level `await` works in modules, making it more seamless.[4][6]

## Key Comparisons

| Aspect       | Python                                                 | JavaScript/TypeScript                      |
| ------------ | ------------------------------------------------------ | ------------------------------------------ |
| Declaration  | `async def`, returns coroutine [1][7]                  | `async function`, returns Promise [4]      |
| Execution    | Needs `asyncio.run()` or event loop [2]                | Auto via runtime, `.then()` or `await` [6] |
| Concurrency  | Tasks via `asyncio.create_task()` or `gather()` [3][5] | Native Promises, no import needed [4]      |
| Event Loop   | Explicit import/manage `asyncio` [2]                   | Implicit in environment [6]                |
| Use Case Fit | Strong for I/O-bound apps like servers [1]             | Ubiquitous for web/APIs [4]                |

Python emphasizes explicit control for concurrency, while JS/TS prioritizes simplicity in promise-based flows.[6][2]

[1](https://www.geeksforgeeks.org/python/python-async/)
[2](https://monadical.com/posts/python-vs-javascript-dealing-with-the-quirks-of-async-await.html)
[3](https://docs.python.org/3/library/asyncio-task.html)
[4](https://tech.treebo.com/async-programming-in-javascript-vs-python-11fd3e3f1b33)
[5](https://stackoverflow.com/questions/50757497/simplest-async-await-example-possible-in-python)
[6](https://stackoverflow.com/questions/68139555/difference-between-async-await-in-python-vs-javascript)
[7](https://superfastpython.com/python-async-function/) [8](https://www.youtube.com/watch?v=pDnSNYgiQZE)
[9](https://realpython.com/python-async-features/)
[10](https://www.reddit.com/r/Python/comments/r7zdj1/asynchronous_python_vs_asynchronous_javascript/)
