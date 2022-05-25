from __future__ import annotations

from types import TracebackType as Traceback
from typing import Any, Callable, Generic, Optional, Type, TypeVar

from typing_extensions import ParamSpec, TypeAlias

__all__ = ("Track", "track")

AnyException: TypeAlias = BaseException

E = TypeVar("E", bound=AnyException)

P = ParamSpec("P")
R = TypeVar("R")

T = TypeVar("T", bound="Track[Any, Any]")


class Track(Generic[P, R]):
    def __init__(self, function: Callable[P, R]) -> None:
        self._function = function
        self._count = 0
        self._saved = 0

    @property
    def count(self) -> int:
        return self._count

    @property
    def saved(self) -> int:
        return self._saved

    @property
    def function(self) -> Callable[P, R]:
        return self._function

    def called(self) -> bool:
        return self.count > 0

    def called_once(self) -> bool:
        return self.count == 1

    def not_called(self) -> bool:
        return not self.called()

    def increment(self) -> None:
        self._count += 1

    def reset(self) -> None:
        self._count = 0

    def save(self) -> None:
        self._saved = self._count

    def load(self) -> None:
        self._count = self._saved

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> R:
        self.increment()

        return self.function(*args, **kwargs)

    def __enter__(self: T) -> T:
        self.save()

        return self

    def __exit__(
        self,
        error: Optional[E],
        type: Optional[Type[E]],
        traceback: Optional[Traceback],
    ) -> None:
        self.load()


# XXX: change to T[F[P, R]] if/when HKTs get added?


def track(function: Callable[P, R]) -> Track[P, R]:
    return Track(function)
