from typing import Optional, TypeVar, final

from attrs import frozen
from named import get_module
from typing_aliases import Nullary

__all__ = ("MAIN", "Main", "EntryPoint", "entrypoint", "is_main")

Main = Nullary[None]
"""The `main` function that does not take arguments and returns nothing."""

M = TypeVar("M", bound=Main)

MAIN = "__main__"
"""The `__main__` name constant."""


def is_main(name: str) -> bool:
    """Checks if the `name` is equal to `__main__`.

    Arguments:
        name: The name to check.

    Returns:
        Whether the `name` is equal to `__main__`.
    """
    return name == MAIN


@final
@frozen()
class EntryPoint:
    """Represents handlers for [`@entrypoint`][entrypoint.core.entrypoint] decorators."""

    name: Optional[str] = None

    def __call__(self, main: M) -> M:
        return self.call(main)

    def call(self, main: M) -> M:
        name = self.name

        if name is None:
            name = get_module(main)

        if is_main(name):
            main()

        return main


def entrypoint(name: Optional[str] = None) -> EntryPoint:
    """Defines decorated functions as entry points.

    Calls the wrapped function if the module gets run directly.

    Instead of applying dark magic, this function expects
    callers to pass the `__name__` variable as an argument,
    and merely checks it against `__main__` when needed.

    In case `__name__` is not provided, this function will attempt to read
    the module name from the function given (via `__module__`).

    `EntryPoint(name)` is created under the hood, and is
    then used to handle calls.

    Args:
        name: The `__name__` of the module.

    Returns:
        The created [`EntryPoint`][entrypoint.core.EntryPoint] instance.
    """
    return EntryPoint(name)
