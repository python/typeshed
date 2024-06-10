import operator
from typing import Mapping, Sequence, SupportsIndex
from typing_extensions import assert_type


class MyClass: ...


def supports_item_get_sequence(my_seq: Sequence[str], key: int) -> None:
    operator.getitem(my_seq, key)

    operator.getitem(my_seq, slice(key, key + 1))

    operator.getitem(my_seq, "test")  # type: ignore


def supports_item_get_mapping(my_seq: Mapping[str, str], key: str) -> None:
    my_item = operator.getitem(my_seq, key)
    assert_type(my_item, str)

    operator.getitem(my_seq, 34)  # type: ignore


def supports_item_get_slice(my_seq: Sequence[MyClass], key: slice) -> Sequence[MyClass]:
    return operator.getitem(my_seq, key)


def supports_item_get_sequence_with_any(my_seq: Sequence[MyClass], key: SupportsIndex) -> MyClass:
    return operator.getitem(my_seq, key)
