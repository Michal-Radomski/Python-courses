Here is a list of the most popular `pip`/`pip3` commands in Python with brief descriptions, along with their closest npm
equivalents in Node.js:

| Task                              | pip Command                       | npm Command                                      | Description                                                                                   |
| --------------------------------- | --------------------------------- | ------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| Install a package                 | `pip install <package_name>`      | `npm install <package_name>`                     | Installs the specified package globally or locally in the environment/project.                |
| Install packages from a file      | `pip install -r requirements.txt` | `npm install`                                    | Installs all packages listed in the requirements file (`requirements.txt` or `package.json`). |
| Uninstall a package               | `pip uninstall <package_name>`    | `npm uninstall <package_name>`                   | Removes the specified package from the environment/project.                                   |
| List installed packages           | `pip list`                        | `npm list`                                       | Lists installed packages in the current environment or project.                               |
| List outdated packages            | `pip list --outdated`             | `npm outdated`                                   | Shows installed packages that have newer versions available.                                  |
| Show package details              | `pip show <package_name>`         | `npm info <package_name>`                        | Displays detailed information about the specified package.                                    |
| Freeze current packages to file   | `pip freeze > requirements.txt`   | `npm shrinkwrap` or `npm install --package-lock` | Saves installed package versions to a file (`requirements.txt` or `package-lock.json`).       |
| Search for a package              | `pip search <package_name>`       | `npm search <package_name>`                      | Searches the package index for a package by name.                                             |
| Configure/get config variables    | `pip config get/set`              | `npm config get/set`                             | Gets or sets pip/npm configuration variables.                                                 |
| List config/environment variables | `pip config list`                 | `npm config list`                                | Lists environment variables related to pip/npm configuration.                                 |

Notes:

- Python's `pip` installs packages for the current environment (usually system or virtualenv).
- Node's `npm` typically installs packages locally within a project folder unless `-g` (global) flag is used.
- `pip freeze` is used to create a snapshot of installed packages to share or recreate environments.
- `npm init` has no direct pip equivalent as Node.js projects use `package.json`. Python projects manually create files like
  `requirements.txt` or use tools like Poetry with `pyproject.toml`.

This table summarizes essential commands to manage dependencies and packages across Python and Node.js ecosystems
efficiently.[1][2][7]

[1](https://deepakkamboj.com/blog/comparison-pip-npm/) [2](https://www.deepakkamboj.com/blog/comparison-pip-npm/)
[3](https://realpython.com/what-is-pip/)
[4](https://stackoverflow.com/questions/58218592/feature-comparison-between-npm-pip-pipenv-and-poetry-package-managers)
[5](https://www.milesweb.com/blog/technology-hub/npm-vs-pip/)
[6](https://dev.to/adamghill/python-package-manager-comparison-1g98)
[7](https://docsaid.org/en/blog/python-js-basic-command-equivalents/)
[8](https://www.activestate.com/resources/quick-reads/how-to-install-and-use-pip3/)
[9](https://www.reddit.com/r/learnpython/comments/jwzxr9/difference_between_pip_pip3_and_pip3x_when_should/)
[10](https://www.diyakamboj.com/guides/comparison-pip-npm-commands)
