from runpy import run_module

from entrypoint import MAIN

TRACKER = "CALLED"
MODULE_WITH_ENTRYPOINT = "tests.module_with_entrypoint"


def test_entrypoint() -> None:
    assert run_module(MODULE_WITH_ENTRYPOINT, run_name=MAIN)[TRACKER] == 1
    assert run_module(MODULE_WITH_ENTRYPOINT)[TRACKER] == 0
    assert run_module(
        MODULE_WITH_ENTRYPOINT,
        run_name=MAIN,
        init_globals={"CALL_AGAIN": True}
    )[TRACKER] == 2
