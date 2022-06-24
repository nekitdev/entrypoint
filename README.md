# entrypoint

[![License][License Badge]][License]
[![Version][Version Badge]][Package]
[![Downloads][Downloads Badge]][Package]
[![Discord][Discord Badge]][Discord]

[![Documentation][Documentation Badge]][Documentation]
[![Check][Check Badge]][Actions]
[![Test][Test Badge]][Actions]
[![Coverage][Coverage Badge]][Coverage]

**Decorated functions as entry points.**

In python, an *entry point* can be thought of as an explicit function
that gets called when the script is run directly from the console.

Defining an entry point requires some boilerplate code, which is
abstracted away by this library.

## Installing

**Python 3.7 or above is required.**

### pip

Installing with `pip` is quite simple:

```console
$ pip install entrypoint
```

Alternatively, the library can be installed from source:

```console
$ git clone https://github.com/nekitdev/entrypoint.git
$ cd entrypoint
$ python -m pip install .
```

### poetry

Adding `entrypoint` to dependencies:

```console
$ poetry add entrypoint
```

Or directly specifying it in the configuration:

```toml
[tool.poetry.dependencies]
entrypoint = "^1.2.1"
```

Alternatively, the latest version can be included, installing from source:

```toml
[tool.poetry.dependencies.entrypoint]
git = "https://github.com/nekitdev/entrypoint.git"
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

### Note

Note that `main` gets called **immediately, before any code below can be executed**:

```python
@entrypoint(__name__)
def main() -> None:
    print("-> in main")

print("<- outside")
```

```console
$ python note.py
-> in main
<- outside
```

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

### Async

`entrypoint` does not provide any specific functionality to run async functions.

Instead, you can specify, for example, a `main` function that runs its `async_main` counterpart:

```python
import asyncio

async def async_main() -> None:
    print("Hello, world!")

@entrypoint(__name__)
def main() -> None:
    asyncio.run(async_main())
```

## Documentation

Documentation is located [here][Documentation].

## Support

Please send an [email][Email] or refer to the official [Discord server][Discord] for support.

## Changelog

Changelog can be found [here][Changelog].

## Contributing

If you are interested in contributing to `entrypoint`, make sure to take a look at the
[Contributing Guide][Contributing Guide], as well as the [Code of Conduct][Code of Conduct].

## License

`entrypoint` is licensed under the MIT License terms. See [License][License] for details.

[Email]: mailto:support@nekit.dev

[Discord]: https://nekit.dev/discord

[Actions]: https://github.com/nekitdev/entrypoint/actions

[Changelog]: https://github.com/nekitdev/entrypoint/blob/main/CHANGELOG.md
[Code of Conduct]: https://github.com/nekitdev/entrypoint/blob/main/CODE_OF_CONDUCT.md
[Contributing Guide]: https://github.com/nekitdev/entrypoint/blob/main/CONTRIBUTING.md
[Security]: https://github.com/nekitdev/entrypoint/blob/main/SECURITY.md

[License]: https://github.com/nekitdev/entrypoint/blob/main/LICENSE

[Package]: https://pypi.org/project/entrypoint
[Coverage]: https://codecov.io/gh/nekitdev/entrypoint
[Documentation]: https://nekitdev.github.io/entrypoint

[Discord Badge]: https://img.shields.io/badge/chat-discord-5865f2
[License Badge]: https://img.shields.io/pypi/l/entrypoint
[Version Badge]: https://img.shields.io/pypi/v/entrypoint
[Downloads Badge]: https://img.shields.io/pypi/dm/entrypoint

[Documentation Badge]: https://img.shields.io/badge/docs-material-blue

[Check Badge]: https://github.com/nekitdev/entrypoint/workflows/check/badge.svg
[Test Badge]: https://github.com/nekitdev/entrypoint/workflows/test/badge.svg
[Coverage Badge]: https://codecov.io/gh/nekitdev/entrypoint/branch/main/graph/badge.svg
