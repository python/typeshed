# Stubs for getpass

from typing import TextIO


def getpass(prompt: str = ..., stream: TextIO = None): ...


def getuser() -> str: ...


class GetPassWarning(UserWarning):
    pass
