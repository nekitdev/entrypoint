from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING, Protocol, TypeVar

from named import Moduled, get_module

if TYPE_CHECKING:
    from typing_extensions import ParamSpec

    _P = ParamSpec("_P")
    _R = TypeVar("_R")
    _R_co = TypeVar("_R_co", covariant=True)

    class _EntrypointFunction(Protocol[_P, _R_co], Moduled):  # pragma: no cover
        def __call__(self, *args: _P.args, **kwargs: _P.kwargs) -> _R_co:
            ...


MAIN = "__main__"
"""The `__main__` name constant."""


def entrypoint(main: _EntrypointFunction[_P, _R]) -> Callable[_P, _R]:
    """Defines decorated functions as entry points.

    Calls the wrapped function if the module it is defined in is run directly.

    Args:
        main: The function to be run as an entrypoint to the program.

    Returns:
        The same function, unchanged.
    """
    if get_module(main) == MAIN:
        main()
    return main
