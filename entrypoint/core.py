from typing import Callable, Type, TypeVar, overload

from attrs import frozen

__all__ = ("MAIN", "Main", "EntryPoint", "entrypoint", "is_main")

Main = Callable[[], None]
"""The `main` function that does not return anything."""

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


@frozen()
class EntryPoint:
    """Represents handlers for [`@entrypoint`][entrypoint.core.entrypoint] decorators."""

    name: str

    def call(self, main: M) -> M:
        if is_main(self.name):
            main()

        return main

    def __call__(self, main: M) -> M:
        return self.call(main)


EP = TypeVar("EP", bound=EntryPoint)


@overload
def entrypoint(name: str) -> EntryPoint:
    ...


@overload
def entrypoint(name: str, entrypoint_type: Type[EP]) -> EP:
    ...


def entrypoint(name: str, entrypoint_type: Type[EntryPoint] = EntryPoint) -> EntryPoint:
    """Defines decorated functions as entry points.

    Calls the wrapped function if the module gets run directly.

    Instead of applying dark magic, this function expects
    callers to pass the `__name__` variable as an argument,
    and merely checks it against `__main__` when needed.

    `entrypoint_type(name)` is created under the hood, and is
    then used to handle calls.

    Args:
        name: The `__name__` of the module.
        entrypoint_type: The [`EntryPoint`][entrypoint.core.EntryPoint]
            type that is used to handle calls.

    Returns:
        The created [`EntryPoint`][entrypoint.core.EntryPoint] instance.
    """
    return entrypoint_type(name)
