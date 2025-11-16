Decorators are a way to modify or extend the behavior of functions, methods, classes, or other entities without changing
their actual code. They work by wrapping or annotating the target with additional logic, and they are applied using a special
syntax that instructs the language runtime to run extra code around the original declaration.

What they are

- In general: a decorator is a higher-order construct that takes a function (or class, or method) and returns a new function
  (or modified class) that adds or changes behavior.
- In Python: decorators are functions (or callables) that receive another function and return a modified function. They’re
  commonly used with the @decorator syntax placed directly above the function or method.
- In TypeScript: decorators are metadata-based wrappers that can be attached to classes, methods, accessors, properties, or
  parameters. They use the @expression syntax, where the expression evaluates to a function invoked at runtime.

Key ideas

- They enable cross-cutting concerns (like logging, authorization, caching, timing) to be kept separate from business logic.
- They often rely on closures to preserve the original function and to insert pre/post behavior around the call.
- They can be stacked, allowing multiple decorators to apply in a specified order.

Examples

1. Python example: a simple logging decorator

- Intent: log entry and exit of a function.

---

## Python Decorator Example

A simple logging decorator that prints info before and after a function call:

```python
def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result!r}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

# Usage
add(2, 3)
```

---

- How it works: log_calls takes the original function add and returns wrapper, which runs before and after the original
  function, logging details.

2. TypeScript example: a class/method decorator that logs method calls

- Intent: log when a method on a class is invoked.

---

## TypeScript Decorator Example

A method decorator that logs method calls on a class:

```typescript
function log(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
  const originalMethod = descriptor.value;
  descriptor.value = function (...args: any[]) {
    console.log(`Calling ${propertyKey} with`, args);
    const result = originalMethod.apply(this, args);
    console.log(`Result from ${propertyKey}:`, result);
    return result;
  };
  return descriptor;
}

class Calculator {
  @log
  add(a: number, b: number): number {
    return a + b;
  }
}

// Usage
const calc = new Calculator();
calc.add(5, 7);
```

---

- How it works: the decorator replaces the original method with a wrapper that logs before and after the call.

Notes and caveats

- Python decorators can be applied to functions, methods, and classes. When decorating methods in classes, you typically
  define the decorator to preserve the method’s signature and behave correctly with self/cls parameters.
- TypeScript decorators are experimental in some environments and require appropriate compiler options (e.g.,
  experimentalDecorators) to be enabled. They operate at runtime and can access metadata depending on the decorators’ design.
- Decorators should be used to augment behavior without changing the core logic. Overusing decorators or creating highly
  opaque wrappers can make code harder to understand.

If you’d like, I can tailor examples to a specific use case (e.g., timing, authorization checks, memoization) and in a
particular Python or TypeScript project setup.

[1](https://en.wikipedia.org/wiki/Decorator_pattern) [2](https://www.typescriptlang.org/docs/handbook/decorators)
[3](https://www.datacamp.com/tutorial/decorators-python) [4](https://refine.dev/blog/typescript-decorators/)
[5](https://realpython.com/primer-on-python-decorators/)
[6](https://www.reddit.com/r/learnpython/comments/tbifwd/what_are_your_favorite_python_decorator_examples/)
[7](https://www.geeksforgeeks.org/python/decorators-in-python/) [8](https://blog.apify.com/using-decorators-in-typescript/)
[9](https://www.programiz.com/python-programming/decorator) [10](https://reliasoftware.com/blog/decorators-in-typescript)
