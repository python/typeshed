import sys
from array import array
from typing_extensions import assert_type

assert_type(array("f", [1.0]), array[float])
assert_type(array("d"), array[float])

if sys.version_info >= (3, 15):
    assert_type(array("Zf", [1 + 2j]), array[complex])
    assert_type(array("Zd", [1.0]), array[complex])
    assert_type(array("Zf"), array[complex])
    assert_type(array("Zd", bytes()), array[complex])
    assert_type(array("e", [1.0]), array[float])
