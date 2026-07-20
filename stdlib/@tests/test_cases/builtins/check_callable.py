from typing import Any


def test_gradual_assignment(arg: Any) -> None:
    if callable(arg):
        _: int = arg()
