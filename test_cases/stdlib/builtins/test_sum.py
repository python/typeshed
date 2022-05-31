# pyright: reportUnnecessaryTypeIgnoreComment=true

from typing import List
from typing_extensions import assert_type

assert_type(sum([2, 4]), int)
assert_type(sum([3, 5], 4), int)

assert_type(sum([True, False]), int)
assert_type(sum([True, False], True), int)

assert_type(sum([['foo'], ['bar']], ['baz']), List[str])

# mypy and pyright infer the types differently for these, so we can't use assert_type
# Just test that no error is emitted for any of these
sum([('foo',), ('bar', 'baz')], ())  # mypy: `tuple[str, ...]`; pyright: `tuple[()] | tuple[str] | tuple[str, str]`
sum([5.6, 3.2])  # mypy: `float`; pyright: `float | Literal[0]`
sum([2.5, 5.8], 5)  # mypy: `float`; pyright: `float | int`

# These all fail at runtime
sum('abcde')  # type: ignore[arg-type]
sum([['foo'], ['bar']])  # type: ignore[list-item]
sum([('foo',), ('bar', 'baz')])  # type: ignore[list-item]

# TODO: these pass pyright with the current stubs, but mypy erroneously emits an error:
# sum([3, Fraction(7, 22), complex(8, 0), 9.83])
# sum([3, Decimal('0.98')])
