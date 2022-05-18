"""
Helper module so we don't have to install types-termcolor in CI.

This is imported by `mypy_test.py` and `stubtest_third_party.py`.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:

    def colored(__str: str, __style: str) -> str:
        ...

else:
    try:
        from termcolor import colored
    except ImportError:

        def colored(s: str, _: str) -> str:
            return s


def print_error(error: str, end: str = "\n") -> None:
    print(colored(error, "red"), end=end)


def print_success_msg() -> None:
    print(colored("success", "green"))
