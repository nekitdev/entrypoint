# entrypoint.py

[![License][License Badge]][License]
[![Version][Version Badge]][Package]
[![Downloads][Downloads Badge]][Package]
[![Discord][Discord Badge]][Discord]
[![Tests][Tests Badge]][Actions]
[![Coverage][Coverage Badge]][Coverage]
<!--
[![Documentation][Documentation Badge]][Documentation]
-->

**Decorated functions as entry points.**

In python, an *entry point* can be thought of as an explicit function
that gets called when the script is run directly from the console.

Defining an entry point requires some boilerplate code, which is abstracted away by this library.

## Table of Contents

<!--
- [Documentation](#documenation)
-->
- [Installing](#installing)
    - [pip](#pip)
    - [poetry](#poetry)
- [Examples](#examples)
    - [Decorated](#decorated)
    - [Direct](#direct)
    - [Check](#check)
- [Changelog](#changelog)
- [Support](#support)
<!--
- [Contributing](#contributing)
-->

## Installing

**Python 3.7 or above is required.**

### pip

Installing with `pip` is quite simple:

```console
$ pip install entrypoint.py
```

Alternatively, the library can be installed from source:

```console
$ git clone https://github.com/nekitdev/entrypoint.py.git
$ cd entrypoint.py
$ python -m pip install .
```

### poetry

Adding `entrypoint.py` to dependencies:

```console
$ poetry add entrypoint.py
```

Or directly specifying it in the configuration:

```toml
[tool.poetry.dependencies."entrypoint.py"]
version = "^0.1.2"
```

Alternatively, the latest version can be included, installing from source:

```toml
[tool.poetry.dependencies."entrypoint.py"]
git = "https://github.com/nekitdev/entrypoint.py.git"
```

## Examples

### Decorated

Declare `main` function as an *entry point*:

```python
from entrypoint import entrypoint

@entrypoint(__name__)
def main() -> None:
    print("Hello, world!")
```

Run the script directly from the console:

```console
$ python file.py
Hello, world!
```

When importing the module, `main` does not get called:

```python
>>> import file
>>> # no output
```

Note that `main` gets called **immediately, before any code below can be executed**.

### Direct

It is possible to run `main` directly:

```python
entrypoint(__name__).call(main)
```

This method allows to take control over where and when the function gets called.

### Check

The library also provides `is_main` function that resembles
the common (and standard) way of implementing *entry points*:

```python
from entrypoint import is_main

if is_main(__name__):
    print("Hello, world!")
```

<!--
## Documentation
Documentation is located [here][Documentation].
-->

## Changelog

Changelog can be found [here][Changelog].

## Support

Please refer to the [Discord Server][Discord] for support or send an [email][Email].

<!--
## Contributing

If you are interested in contributing to the project, please make sure to take a look at the
[Contributing Guide][Contributing Guide], as well as the [Code of Conduct][Code of Conduct].
-->

[Email]: mailto:support@nekit.dev?subject=entrypoint.py
[Discord]: https://nekit.dev/discord

[Actions]: https://github.com/nekitdev/entrypoint.py/actions

[Changelog]: https://github.com/nekitdev/entrypoint.py/blob/main/CHANGELOG.md
[Code of Conduct]: https://github.com/nekitdev/entrypoint.py/blob/main/CODE_OF_CONDUCT.md
[Contributing Guide]: https://github.com/nekitdev/entrypoint.py/blob/main/CONTRIBUTING.md

[License]: https://github.com/nekitdev/entrypoint.py/blob/main/LICENSE
[Package]: https://pypi.org/project/entrypoint.py
[Coverage]: https://codecov.io/github/nekitdev/entrypoint.py

[Documentation]: https://entrypoint-py.readthedocs.io/

[Discord Badge]: https://img.shields.io/badge/chat-discord-5865f2
[License Badge]: https://img.shields.io/pypi/l/entrypoint.py
[Version Badge]: https://img.shields.io/pypi/v/entrypoint.py
[Downloads Badge]: https://img.shields.io/pypi/dm/entrypoint.py

[Documentation Badge]: https://readthedocs.org/projects/entrypoint-py/badge

[Tests Badge]: https://github.com/nekitdev/entrypoint.py/actions/workflows/tests.yml/badge.svg
[Coverage Badge]: https://codecov.io/gh/nekitdev/entrypoint.py/branch/main/graph/badge.svg
