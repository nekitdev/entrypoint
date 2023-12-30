"""Decorated functions as entry points.

# Example

```python
# file.py
from entrypoint import entrypoint

@entrypoint
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
__url__ = "https://github.com/nekitdev/entrypoint"

__title__ = "entrypoint"
__author__ = "nekitdev"
__license__ = "MIT"
__version__ = "1.4.0"

from entrypoint.core import MAIN, entrypoint

__all__ = ("MAIN", "entrypoint")
