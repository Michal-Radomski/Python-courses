Poetry is a Python dependency management and packaging tool that simplifies managing project dependencies, running
development tasks, building and publishing packages. It uses a configuration file named pyproject.toml for managing project
settings.

The pyproject.toml file is a TOML format configuration file that Poetry creates and manages. It contains metadata about the
project such as the project name, version, authors, and dependencies. It also includes configuration for build systems and
scripts associated with the project.

To create a new Poetry project and the associated pyproject.toml file, you can run the command:

```
poetry new project-name
```

This command creates a new directory named after the project with a standard structure including the pyproject.toml file
filled with initial configuration.

Alternatively, if you have an existing project directory, you can initialize Poetry in it and create the pyproject.toml file
using:

```
cd existing-project
poetry init
```

Poetry then uses pyproject.toml to manage dependencies, handle virtual environments, and build or publish the project
package.

Summary:

- Poetry is a Python dependency management and packaging tool.
- pyproject.toml is the configuration file used by Poetry.
- Create them with `poetry new project-name` or `poetry init` in an existing project folder.[1][2][3][5]

[1](https://python-poetry.org/docs/basic-usage/)
[2](https://hexlet.io/courses/python-setup-environment/lessons/start-with-poetry/theory_unit)
[3](https://realpython.com/dependency-management-python-poetry/) [4](https://www.jetbrains.com/help/pycharm/poetry.html)
[5](https://www.datacamp.com/tutorial/python-poetry)
[6](https://stackoverflow.com/questions/59286983/how-to-run-a-script-using-pyproject-toml-settings-and-poetry)
[7](https://www.geeksforgeeks.org/python/using-poetry-dependency-management-tool-in-python/)
[8](https://python-poetry.org/docs/pyproject/) [9](https://python-poetry.org/docs/)
[10](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)

To add dependencies automatically to your pyproject.toml file using Poetry, you use the `poetry add` command followed by the
package name(s). For example:

```
poetry add requests beautifulsoup4
```

This command does the following:

- Automatically finds the latest compatible versions of the specified packages.
- Installs these packages into your project's virtual environment.
- Adds the packages and their version constraints as dependencies in the `pyproject.toml` file under the
  `[tool.poetry.dependencies]` section.

This way, you don't need to manually edit `pyproject.toml`; Poetry manages the dependency versions and installation for you.

To summarize:

- Open your terminal in your Poetry project directory.
- Use `poetry add package-name` to add new dependencies.
- Poetry updates `pyproject.toml` and installs the dependency automatically.

This workflow simplifies dependency management and ensures your `pyproject.toml` is always in sync with installed
packages.[1][5][6]

[1](https://realpython.com/dependency-management-python-poetry/) [2](https://github.com/python-poetry/poetry/issues/951)
[3](https://discuss.python.org/t/manually-adding-dependencies-to-pyproject-toml/18345)
[4](https://stackoverflow.com/questions/60971502/python-poetry-how-to-install-optional-dependencies)
[5](https://python-poetry.org/docs/pyproject/) [6](https://python-poetry.org/docs/basic-usage/)
[7](https://python-poetry.org/docs/dependency-specification/) [8](https://python-poetry.org/docs/managing-dependencies/)
[9](https://www.reddit.com/r/learnpython/comments/14k97p4/dynamically_specify_dependencies_in_pyprojecttoml/)
