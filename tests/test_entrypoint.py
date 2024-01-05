from runpy import run_module

from entrypoint import is_main

CALLED = "CALLED"

MAIN = "__main__"
TEST = "__test__"

MODULE = "tests.module"


def test_is_main() -> None:
    assert is_main(MAIN)
    assert not is_main(TEST)


def test_entrypoint() -> None:
    main = run_module(MODULE, run_name=MAIN)

    assert main[CALLED] == 1

    test = run_module(MODULE, run_name=TEST)

    assert test[CALLED] == 0
