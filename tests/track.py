from __future__ import annotations

from types import TracebackType as Traceback
from typing import Any, Callable, Generic, Optional, Type, TypeVar

from attrs import define
from typing_extensions import ParamSpec, TypeAlias

__all__ = ("Track", "track")

AnyError: TypeAlias = BaseException

DEFAULT_COUNT = 0

E = TypeVar("E", bound=AnyError)

P = ParamSpec("P")
R = TypeVar("R")

T = TypeVar("T", bound="Track[..., Any]")


@define()
class Track(Generic[P, R]):
    """Tracks function calls."""

    function: Callable[P, R]
    count: int = DEFAULT_COUNT
    saved: int = DEFAULT_COUNT

    def called(self) -> bool:
        return self.count > 0

    def called_once(self) -> bool:
        return self.count == 1

    def not_called(self) -> bool:
        return not self.called()

    def increment(self) -> None:
        self.count += 1

    def reset(self) -> None:
        self.count = 0

    def save(self) -> None:
        self.saved = self.count

    def load(self) -> None:
        self.count = self.saved

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> R:
        self.increment()

        return self.function(*args, **kwargs)

    def __enter__(self: T) -> T:
        self.save()

        return self

    def __exit__(
        self, error: Optional[E], type: Optional[Type[E]], traceback: Optional[Traceback]
    ) -> None:
        self.load()


def track(function: Callable[P, R]) -> Track[P, R]:
    return Track(function)
