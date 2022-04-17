from typing import Any, Callable, Type, TypeVar, overload

__all__ = ("EntryPoint", "entrypoint", "is_main")

R = TypeVar("R")

Main = Callable[[], R]

# XXX: change to M[R] if/when HKTs get added?
M = TypeVar("M", bound=Main[Any])

MAIN = "__main__"


def is_main(name: str) -> bool:
    """Checks if `name` equals `__main__`."""
    return name == MAIN


class EntryPoint:
    """Actual implementation of `@entrypoint` decorators."""

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
    ...  # pragma: overload


@overload
def entrypoint(name: str, entrypoint_type: Type[EP]) -> EP:
    ...  # pragma: overload


def entrypoint(name: str, entrypoint_type: Type[Any] = EntryPoint) -> Any:
    """Defines decorated functions as entry points.

    Calls the wrapped function if the module gets run directly.

    Instead of applying dark magic, this function expects
    callers to pass the `__name__` variable as an argument,
    and merely checks it against `__main__` when needed.
    """
    return entrypoint_type(name)
