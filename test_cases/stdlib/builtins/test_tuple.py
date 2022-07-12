from typing_extensions import assert_type


# Empty tuples, see #8275
class TupleSub(tuple[int, ...]):
    pass


assert_type(TupleSub(), TupleSub)
assert_type(TupleSub([1, 2, 3]), TupleSub)
