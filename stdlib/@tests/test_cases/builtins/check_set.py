from collections.abc import Iterator, MutableSet, Set as AbstractSet
from typing_extensions import Literal, assert_type


# Note: type checkers / linters are free to point out that the set difference
#   below is redundant. But typeshed should allow it, as its job is to describe
#   what is legal in Python, not what is sensible.
#   For instance, set[Literal] - set[str] should be legal.
def test_set_difference(x: set[Literal["foo", "bar"]], y: set[str], z: set[int]) -> None:
    assert_type(x - y, set[Literal["foo", "bar"]])
    assert_type(y - x, set[str])
    assert_type(x - z, set[Literal["foo", "bar"]])
    assert_type(z - x, set[int])
    assert_type(y - z, set[str])
    assert_type(z - y, set[int])


def test_set_interface_overlapping_type(s: set[Literal["foo", "bar"]], y: set[str], key: str) -> None:
    s.add(key)  # type: ignore
    s.discard(key)
    s.remove(key)  # type: ignore
    s.difference_update(y)
    s.intersection_update(y)
    s.symmetric_difference_update(y)  # type: ignore
    s.update(y)  # type: ignore

    assert_type(s.difference(y), set[Literal["foo", "bar"]])
    assert_type(s.intersection(y), set[Literal["foo", "bar"]])
    assert_type(s.isdisjoint(y), bool)
    assert_type(s.issubset(y), bool)
    assert_type(s.issuperset(y), bool)
    assert_type(s.symmetric_difference(y), set[str])
    assert_type(s.union(y), set[str])

    assert_type(s - y, set[Literal["foo", "bar"]])
    assert_type(s & y, set[Literal["foo", "bar"]])
    assert_type(s | y, set[str])
    assert_type(s ^ y, set[str])

    s -= y
    s &= y
    s |= y  # type: ignore
    s ^= y  # type: ignore


def test_frozenset_interface(s: frozenset[Literal["foo", "bar"]], y: frozenset[str]) -> None:
    assert_type(s.difference(y), frozenset[Literal["foo", "bar"]])
    assert_type(s.intersection(y), frozenset[Literal["foo", "bar"]])
    assert_type(s.isdisjoint(y), bool)
    assert_type(s.issubset(y), bool)
    assert_type(s.issuperset(y), bool)
    assert_type(s.symmetric_difference(y), frozenset[str])
    assert_type(s.union(y), frozenset[str])

    assert_type(s - y, frozenset[Literal["foo", "bar"]])
    assert_type(s & y, frozenset[Literal["foo", "bar"]])
    assert_type(s | y, frozenset[str])
    assert_type(s ^ y, frozenset[str])


# set and frozenset only support set and frozenset operands. Other abstract
# sets are handled by their reflected methods, which return abstract sets.
def test_binary_ops_with_abstract_set(
    s: set[Literal["foo", "bar"]], frozen: frozenset[Literal["foo", "bar"]], other: AbstractSet[str]
) -> None:
    s.__and__(other)  # type: ignore
    s.__or__(other)  # type: ignore
    s.__sub__(other)  # type: ignore
    s.__xor__(other)  # type: ignore
    frozen.__and__(other)  # type: ignore
    frozen.__or__(other)  # type: ignore
    frozen.__sub__(other)  # type: ignore
    frozen.__xor__(other)  # type: ignore
    assert_type(s & other, AbstractSet[Literal["foo", "bar"]])
    assert_type(s | other, AbstractSet[str])
    assert_type(s - other, AbstractSet[Literal["foo", "bar"]])
    assert_type(s ^ other, AbstractSet[str])
    assert_type(frozen & other, AbstractSet[Literal["foo", "bar"]])
    assert_type(frozen | other, AbstractSet[str])
    assert_type(frozen - other, AbstractSet[Literal["foo", "bar"]])
    assert_type(frozen ^ other, AbstractSet[str])

    # The mixin methods accept any iterable, but set and frozenset don't.
    [1] & other  # type: ignore
    [1] | other  # type: ignore
    [1] - other  # type: ignore
    [1] ^ other  # type: ignore


# The in-place operators of set only work in place for set and frozenset
# operands. For other operands, the target is rebound to the result of the
# operand's reflected method.
def test_inplace_ops_with_other_operands(s: set[int], ms: MutableSet[int], d: dict[int, str], other: AbstractSet[int]) -> None:
    assert_type(s.__ior__(d.keys()), set[int])
    assert_type(s.__iand__(d.keys()), set[int])
    assert_type(s.__isub__(d.keys()), set[int])
    assert_type(s.__ixor__(d.keys()), set[int])

    s |= d.keys()
    s &= d.keys()
    s -= d.keys()
    s ^= d.keys()
    ms |= d.keys()
    ms &= d.keys()
    ms -= d.keys()
    ms ^= d.keys()

    # Dict items views rebind the target to a set of tuples.
    pairs: set[tuple[int, str]] = set()
    pairs |= d.items()
    s |= d.items()  # type: ignore

    # At runtime, these rebind the target to an arbitrary abstract set,
    # which is not necessarily a set or even mutable.
    s |= other  # type: ignore
    s &= other  # type: ignore
    s -= other  # type: ignore
    s ^= other  # type: ignore
    ms |= other  # type: ignore
    ms &= other  # type: ignore
    ms -= other  # type: ignore
    ms ^= other  # type: ignore


class _ImmutableSet(AbstractSet[int]):
    def __contains__(self, x: object) -> bool:
        return False

    def __iter__(self) -> Iterator[int]:
        return iter(())

    def __len__(self) -> int:
        return 0


def test_inplace_ops_with_custom_set(s: set[int], ms: MutableSet[int]) -> None:
    # At runtime, s and ms would be rebound to an _ImmutableSet instance.
    s |= _ImmutableSet()  # type: ignore
    s &= _ImmutableSet()  # type: ignore
    s -= _ImmutableSet()  # type: ignore
    s ^= _ImmutableSet()  # type: ignore
    ms |= _ImmutableSet()  # type: ignore
    ms &= _ImmutableSet()  # type: ignore
    ms -= _ImmutableSet()  # type: ignore
    ms ^= _ImmutableSet()  # type: ignore

    # Set operands are still modified in place.
    assert_type(s.__ior__({1}), set[int])
    assert_type(s.__iand__(frozenset({1})), set[int])
    s |= {1}
    s &= frozenset({1})
    ms |= {1}
    ms &= frozenset({1})


def test_binary_ops_with_custom_set(s: set[int], frozen: frozenset[int]) -> None:
    # The result is an _ImmutableSet instance at runtime, not a set.
    x: set[int] = s & _ImmutableSet()  # type: ignore
    y: frozenset[int] = frozen | _ImmutableSet()  # type: ignore
    assert_type(s & _ImmutableSet(), AbstractSet[int])
    assert_type(frozen | _ImmutableSet(), AbstractSet[int])
