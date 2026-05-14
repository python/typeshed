from typing_extensions import Literal, assert_type

assert_type(bool(), Literal[False])
assert_type(bool(False), Literal[False])
assert_type(bool(True), Literal[True])
assert_type(bool(42), bool)


class Truthy:
    def __bool__(self) -> Literal[True]:
        return True


class Falsy:
    def __bool__(self) -> Literal[False]:
        return False


assert_type(bool(Truthy()), Literal[True])
assert_type(bool(Falsy()), Literal[False])
