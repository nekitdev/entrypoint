from entrypoint import entrypoint, is_main
from tests.track import track

MAIN = "__main__"
TEST = "__test__"


def test_is_main() -> None:
    assert is_main(MAIN)
    assert not is_main(TEST)


entrypoint_call = entrypoint(MAIN)
entrypoint_no_call = entrypoint(TEST)


def main() -> None:
    pass


def test_call() -> None:
    with track(main) as tracked:
        entrypoint_call(tracked)

        assert tracked.called_once()


def test_no_call() -> None:
    with track(main) as tracked:
        entrypoint_no_call(tracked)

        assert tracked.not_called()
