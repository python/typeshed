from __future__ import annotations

from collections.abc import Iterator
from concurrent.futures import Future, ThreadPoolExecutor, as_completed
from typing_extensions import assert_type


class Parent:
    ...


class Child(Parent):
    ...


def check_as_completed_covariance() -> None:
    with ThreadPoolExecutor() as executor:
        f1 = executor.submit(lambda: Parent())
        f2 = executor.submit(lambda: Child())
        fs: list[Future[Parent] | Future[Child]] = [f1, f2]
        assert_type(as_completed(fs), Iterator[Future[Parent]])
        for future in as_completed(fs):
            assert_type(future.result(), Parent)
