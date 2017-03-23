# Stubs for sqlalchemy.testing.pickleable (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
import fixtures

class User(fixtures.ComparableEntity): ...
class Order(fixtures.ComparableEntity): ...
class Dingaling(fixtures.ComparableEntity): ...
class EmailUser(User): ...
class Address(fixtures.ComparableEntity): ...
class Child1(fixtures.ComparableEntity): ...
class Child2(fixtures.ComparableEntity): ...
class Parent(fixtures.ComparableEntity): ...

class Screen:
    obj = ...  # type: Any
    parent = ...  # type: Any
    def __init__(self, obj, parent: Optional[Any] = ...) -> None: ...

class Foo:
    data = ...  # type: str
    stuff = ...  # type: str
    moredata = ...  # type: Any
    def __init__(self, moredata) -> None: ...
    __hash__ = ...  # type: Any
    def __eq__(self, other): ...

class Bar:
    x = ...  # type: Any
    y = ...  # type: Any
    def __init__(self, x, y) -> None: ...
    __hash__ = ...  # type: Any
    def __eq__(self, other): ...

class OldSchool:
    x = ...  # type: Any
    y = ...  # type: Any
    def __init__(self, x, y) -> None: ...
    def __eq__(self, other): ...

class OldSchoolWithoutCompare:
    x = ...  # type: Any
    y = ...  # type: Any
    def __init__(self, x, y) -> None: ...

class BarWithoutCompare:
    x = ...  # type: Any
    y = ...  # type: Any
    def __init__(self, x, y) -> None: ...

class NotComparable:
    data = ...  # type: Any
    def __init__(self, data) -> None: ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

class BrokenComparable:
    data = ...  # type: Any
    def __init__(self, data) -> None: ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
