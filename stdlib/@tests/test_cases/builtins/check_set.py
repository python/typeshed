from typing_extensions import assert_type

# Note: type checkers / linters are free to point out that the set difference
#   below is redundant. But typeshed should allow it, as its job is to describe
#   what is legal in Python, not what is sensible.
x: set[str] = {"foo", "bar"}
assert_type(x - {123}, set[str])
