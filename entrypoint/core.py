from typing import Any, Callable, Type, TypeVar, overload

__all__ = ("MAIN", "EntryPoint", "entrypoint", "is_main")

R = TypeVar("R")

Main = Callable[[], R]

# XXX: change to M[R] if/when HKTs get added?
M = TypeVar("M", bound=Main[Any])

MAIN = "__main__"


def is_main(name: str) -> bool:
    """Checks if `name` equals `__main__`.

    Arguments:
        name: The name to check.

    Returns:
        Whether the `name` is equal to `__main__`.
    """
    return name == MAIN


class EntryPoint:
    """Handlers for [`@entrypoint`][entrypoint.core.entrypoint] decorators."""

    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self) -> str:
        return self._name

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


def entrypoint(
    name: str, entrypoint_type: Type[EntryPoint] = EntryPoint
) -> EntryPoint:
    """Defines decorated functions as entry points.

    Calls the wrapped function if the module gets run directly.

    Instead of applying dark magic, this function expects
    callers to pass the `__name__` variable as an argument,
    and merely checks it against `__main__` when needed.

    `entrypoint_type(name)` is created under the hood, and is
    then used to handle calls.

    Args:
        name: The `__name__` of the module
        entrypoint_type: An [`EntryPoint`][entrypoint.core.EntryPoint]
            type that is used to handle calls.

    Returns:
        An [`EntryPoint`][entrypoint.core.EntryPoint] instance.
    """
    return entrypoint_type(name)
