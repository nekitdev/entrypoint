from entrypoint import entrypoint

CALLED = 0


@entrypoint()
def main() -> None:
    global CALLED

    CALLED += 1
