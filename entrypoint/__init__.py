"""Decorated functions as entry points.

# Example

```python
# file.py
from entrypoint import entrypoint

@entrypoint(__name__)
def main() -> None:
    print("Hello, world!")
```

```python
>>> import file
>>> # no output
```

```console
$ python file.py
Hello, world!
```
"""

__description__ = "Decorated functions as entry points."
__url__ = "https://github.com/nekitdev/entrypoint.py"

__title__ = "entrypoint"
__author__ = "nekitdev"
__license__ = "MIT"
__version__ = "0.2.0"

from entrypoint.core import EntryPoint, entrypoint, is_main

__all__ = ("EntryPoint", "entrypoint", "is_main")
