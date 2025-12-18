In Pytest, a fixture is a function decorated with `@pytest.fixture` that sets up and provides reusable resources, data, or
state for tests, such as database connections or test objects.[1][5]

## Key Benefits

Fixtures replace traditional setup/teardown methods with explicit, modular functions that tests request by name as arguments,
enabling consistent test initialization and cleanup. They support dependency chains, where one fixture can use others, and
automatic execution based on test needs.[2][1]

## Usage Example

Tests declare fixtures as parameters, like `def test_example(fixture_name):`, prompting Pytest to run the fixture and pass
its return value. For teardown, fixtures use `yield` to execute cleanup code afterward.[3][5]

## Scopes

Fixtures have scopes controlling lifetime: `function` (default, per test), `class`, `module`, or `session` (once per run),
reducing overhead for expensive setups like services.[4][1]

[1](https://docs.pytest.org/en/6.2.x/fixture.html)
[2](https://www.reddit.com/r/learnpython/comments/1287gfl/what_is_the_difference_between_fixtures_and/)
[3](https://www.tutorialspoint.com/pytest/pytest_fixtures.htm) [4](https://pytest-with-eric.com/fixtures/pytest-fixtures/)
[5](https://docs.pytest.org/en/stable/explanation/fixtures.html)
[6](https://campus.datacamp.com/courses/introduction-to-testing-in-python/pytest-fixtures?ex=1)
[7](https://www.geeksforgeeks.org/python/fixtures-in-pytest/) [8](https://www.youtube.com/watch?v=6_ngzfZygGg)
[9](https://www.testim.io/blog/using-pytest-fixtures/)
[10](https://www.lambdatest.com/blog/end-to-end-tutorial-for-pytest-fixtures-with-examples/)
