from entrypoint import entrypoint

CALLED = 0


@entrypoint
def main() -> None:
    """The entrypoint of the module."""
    global CALLED
    CALLED += 1


if globals().get("CALL_AGAIN"):
    main()
