Python classes vs JavaScript/TypeScript classes: a concise comparison

Core distinction

- Python uses class-based object orientation with single inheritance (via classes) and dynamic typing. JavaScript uses
  prototype-based inheritance in its core, with classes introduced in ES6 as a syntactic sugar that still rely on prototypes
  under the hood. TypeScript adds static type annotations on top of JavaScript’s class syntax.[1][7]

Key differences by language model

- Inheritance model:
  - Python: class-based inheritance; supports multiple inheritance directly (via the class hierarchy).[1]
  - JavaScript/TypeScript: primarily single inheritance via prototypes; ES6 class syntax is a layer over the prototype chain.
    TypeScript adds type-safe declarations but runtime remains prototype-based.[3][7]
- Syntax and declaration:
  - Python: uses indentation, colon, and the class keyword; constructors are defined with **init**(self, ...). Example: class
    C: def **init**(self, x): self.x = x.[5]
  - JavaScript/TypeScript: uses class keyword; constructors defined as constructor(...); instances created with new;
    TypeScript adds type annotations. Example: class C { constructor(x: number) { this.x = x; } }[7][3]
- Access control and privacy:
  - Python: relies on naming conventions (single or double underscore) and runtime behavior; no true private fields in the
    language core, though name mangling for double-underscore attributes exists.[1]
  - JavaScript/TypeScript: JavaScript historically has no true private fields (outside convention). TypeScript offers private
    and protected annotations; modern JavaScript supports private fields using #name syntax (enforced at runtime in compliant
    engines). TypeScript private is a compile-time construct, not runtime in JS.[3]
- Typing and safety:
  - Python: dynamically typed; type hints are optional and not enforced at runtime.[1]
  - TypeScript: statically typed (gradual typing); type annotations compile away to plain JavaScript but provide compile-time
    checking.[3]
- Method and property resolution:
  - Python: attribute lookup follows the MRO (method resolution order) through the class hierarchy; multiple inheritance can
    influence MRO.[1]
  - JavaScript: property lookup follows the prototype chain; method resolution is a straightforward prototype chain walk.
    TypeScript adds compile-time checks, not runtime changes to resolution.[7]
- Runtime characteristics:
  - Python: class definitions are objects themselves (type objects) and can be manipulated at runtime; dynamic nature allows
    adding attributes to instances or classes.[8]
  - JavaScript/TypeScript: classes are syntax for creating constructor functions and prototype-based inheritance; runtime
    behavior is governed by the prototype chain.[7]

Practical implications

- When to use what:
  - For Python: leverage rich standard library, dynamic typing, and straightforward class-based inheritance; good for rapid
    development and data-centric tasks.
  - For JavaScript/TypeScript: leverage the language’s ubiquity in web environments; use TypeScript for stronger type safety
    in large codebases; expect prototype-based inheritance under the hood.
- Interoperability and ecosystem:
  - Python ecosystems favor modules and classes with easy introspection and metaprogramming.[1]
  - JavaScript/TypeScript ecosystems emphasize asynchronous programming, modules, and frontend/backend universality;
    TypeScript tightens types across large JS codebases.[3]

If you’d like, I can tailor a simple side-by-side code example (Python class vs JavaScript/TypeScript class) showing
constructors, methods, and a small inheritance scenario to highlight the differences in practice.

[1](https://dev.to/patarapolw/how-is-javascript-class-prototype-different-from-python-java-1n3g)
[2](https://www.reddit.com/r/learnprogramming/comments/xf0ami/the_differences_and_similarities_between/)
[3](https://www.linkedin.com/pulse/comparison-object-oriented-programming-oop-c-python-javascript-zhu-e22zc)
[4](https://sunscrapers.com/blog/python-vs-javascript-key-differences/)
[5](https://www.freecodecamp.org/news/python-vs-javascript-what-are-the-key-differences-between-the-two-popular-programming-languages/)
[6](https://career.softserveinc.com/en-us/stories/python-or-javascript)
[7](https://www.typescriptlang.org/docs/handbook/classes.html)
[8](https://stackoverflow.com/questions/11620582/the-difference-between-a-class-based-language-like-java-or-python-and-a-protot)
[9](https://www.reddit.com/r/learnjavascript/comments/1h67s2e/how_are_objects_and_classes_different_in/)
[10](https://www.youtube.com/watch?v=H12TrIWPIRI)

Here are straightforward examples of classes in Python and JavaScript/TypeScript to demonstrate their syntax and basic usage:

Python class example:

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return f"{self.name} makes a sound."

# Create an instance
dog = Animal("Buddy", "Dog")
print(dog.speak())  # Output: Buddy makes a sound.
```

JavaScript class example:

```js
class Animal {
  constructor(name, species) {
    this.name = name;
    this.species = species;
  }

  speak() {
    return `${this.name} makes a sound.`;
  }
}

// Create an instance
const dog = new Animal("Buddy", "Dog");
console.log(dog.speak()); // Output: Buddy makes a sound.
```

TypeScript class example with types:

```ts
class Animal {
  name: string;
  species: string;

  constructor(name: string, species: string) {
    this.name = name;
    this.species = species;
  }

  speak(): string {
    return `${this.name} makes a sound.`;
  }
}

const dog = new Animal("Buddy", "Dog");
console.log(dog.speak()); // Output: Buddy makes a sound.
```

These examples show the basic structure of classes with constructors, properties, and methods. Python uses indentation and
the `def` keyword for methods, and `self` to refer to instance members. JavaScript/TypeScript use curly braces, the
`constructor` keyword, and `this` for instance members. TypeScript adds explicit type annotations for stronger typing checks
at compile time.

If you want, examples with inheritance or other advanced features can be provided as well. This should clarify the syntax and
basic usage differences for classes in these languages.[1][5]

[1](https://www.programiz.com/python-programming/class) [2](https://realpython.com/python-classes/)
[3](https://programming-24.mooc.fi/part-8/5-more-examples-of-classes/)
[4](http://www.w3schools.com/PYTHON/python_class_methods.asp) [5](https://mimo.org/glossary/python/class)
[6](https://www.geeksforgeeks.org/python/python-classes-and-objects/)
[7](https://www.w3schools.com/python/python_classes.asp) [8](https://docs.python.org/3/tutorial/classes.html)
[9](https://www.youtube.com/watch?v=RpBBzci_cBk)
