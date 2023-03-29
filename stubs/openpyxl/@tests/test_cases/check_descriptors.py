# TODO: Don't forget to re-enable before PR
# mypy: disable-error-code=assert-type
from __future__ import annotations

from typing import Any, Union
from typing_extensions import Literal, assert_type

from openpyxl.descriptors.base import Descriptor, Typed


class WithDescriptors:
    # Specifically testing infered type without non-runtime type hints
    descriptor = Descriptor()  # type: ignore[var-annotated]
    typed_default = Typed(expected_type=str)
    typed_not_none = Typed(expected_type=str, allow_none=False)
    typed_none = Typed(expected_type=str, allow_none=True)

    # Test inferred annotation
    assert_type(descriptor, Descriptor[Any])
    assert_type(typed_default, Typed[str, Literal[False]])
    assert_type(typed_not_none, Typed[str, Literal[False]])
    assert_type(typed_none, Typed[str, Literal[True]])


with_descriptors = WithDescriptors()

# Test getters
assert_type(with_descriptors.descriptor, Any)
assert_type(with_descriptors.typed_default, str)
assert_type(with_descriptors.typed_none, Union[str, None])

# Test setters (expected type, None, unexpected type)
with_descriptors.descriptor = object()
with_descriptors.descriptor = None
with_descriptors.descriptor = type

with_descriptors.typed_default = ""
# false negative in mypy?
with_descriptors.typed_default = None  # pyright: ignore[reportGeneralTypeIssues]
with_descriptors.typed_default = 0  # type: ignore

with_descriptors.typed_none = ""
# false negative in mypy?
with_descriptors.typed_not_none = None  # pyright: ignore[reportGeneralTypeIssues]
with_descriptors.typed_not_none = 0  # type: ignore

with_descriptors.typed_none = ""
with_descriptors.typed_none = None
with_descriptors.typed_none = 0  # type: ignore
