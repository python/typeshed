
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer,
)
from google.protobuf.message import (
    Message,
)
from google.protobuf.unittest_arena_pb2 import (
    ArenaMessage,
)
from google.protobuf.unittest_import_pb2 import (
    ImportEnum,
    ImportMessage,
)
from google.protobuf.unittest_import_public_pb2 import (
    PublicImportMessage,
)
from typing import (
    Iterable,
    List,
    Optional,
    Text,
    Tuple,
    cast,
)


class ForeignEnum(int):

    @classmethod
    def Name(cls, number: int) -> bytes: ...

    @classmethod
    def Value(cls, name: bytes) -> ForeignEnum: ...

    @classmethod
    def keys(cls) -> List[bytes]: ...

    @classmethod
    def values(cls) -> List[ForeignEnum]: ...

    @classmethod
    def items(cls) -> List[Tuple[bytes, ForeignEnum]]: ...


FOREIGN_FOO: ForeignEnum
FOREIGN_BAR: ForeignEnum
FOREIGN_BAZ: ForeignEnum


class TestAllTypes(Message):

    class NestedEnum(int):

        @classmethod
        def Name(cls, number: int) -> bytes: ...

        @classmethod
        def Value(cls, name: bytes) -> TestAllTypes.NestedEnum: ...

        @classmethod
        def keys(cls) -> List[bytes]: ...

        @classmethod
        def values(cls) -> List[TestAllTypes.NestedEnum]: ...

        @classmethod
        def items(cls) -> List[Tuple[bytes, TestAllTypes.NestedEnum]]: ...
    FOO: TestAllTypes.NestedEnum
    BAR: TestAllTypes.NestedEnum
    BAZ: TestAllTypes.NestedEnum
    NEG: TestAllTypes.NestedEnum

    class NestedMessage(Message):
        bb: int

        def __init__(self,
                     bb: Optional[int] = ...,
                     ) -> None: ...

    class OptionalGroup(Message):
        a: int

        def __init__(self,
                     a: Optional[int] = ...,
                     ) -> None: ...

    class RepeatedGroup(Message):
        a: int

        def __init__(self,
                     a: Optional[int] = ...,
                     ) -> None: ...

    @property
    def optionalgroup(self) -> TestAllTypes.OptionalGroup: ...

    @property
    def optional_nested_message(self) -> TestAllTypes.NestedMessage: ...

    @property
    def optional_foreign_message(self) -> ForeignMessage: ...

    @property
    def optional_import_message(self) -> ImportMessage: ...

    @property
    def optional_public_import_message(self) -> PublicImportMessage: ...

    @property
    def optional_message(self) -> TestAllTypes.NestedMessage: ...

    @property
    def repeatedgroup(
        self) -> RepeatedCompositeFieldContainer[TestAllTypes.RepeatedGroup]: ...

    @property
    def repeated_nested_message(
        self) -> RepeatedCompositeFieldContainer[TestAllTypes.NestedMessage]: ...

    @property
    def repeated_foreign_message(
        self) -> RepeatedCompositeFieldContainer[ForeignMessage]: ...

    @property
    def repeated_import_message(
        self) -> RepeatedCompositeFieldContainer[ImportMessage]: ...

    @property
    def repeated_lazy_message(
        self) -> RepeatedCompositeFieldContainer[TestAllTypes.NestedMessage]: ...

    @property
    def oneof_nested_message(self) -> TestAllTypes.NestedMessage: ...

    @property
    def lazy_oneof_nested_message(self) -> TestAllTypes.NestedMessage: ...

    def __init__(self,
                 optional_int32: Optional[int] = ...,
                 optional_int64: Optional[int] = ...,
                 optional_uint32: Optional[int] = ...,
                 optional_uint64: Optional[int] = ...,
                 optional_sint32: Optional[int] = ...,
                 optional_sint64: Optional[int] = ...,
                 optional_fixed32: Optional[int] = ...,
                 optional_fixed64: Optional[int] = ...,
                 optional_sfixed32: Optional[int] = ...,
                 optional_sfixed64: Optional[int] = ...,
                 optional_float: Optional[float] = ...,
                 optional_double: Optional[float] = ...,
                 optional_bool: Optional[bool] = ...,
                 optional_string: Optional[Text] = ...,
                 optional_bytes: Optional[bytes] = ...,
                 optionalgroup: Optional[TestAllTypes.OptionalGroup] = ...,
                 optional_nested_message: Optional[TestAllTypes.NestedMessage] = ...,
                 optional_foreign_message: Optional[ForeignMessage] = ...,
                 optional_import_message: Optional[ImportMessage] = ...,
                 optional_nested_enum: Optional[TestAllTypes.NestedEnum] = ...,
                 optional_foreign_enum: Optional[ForeignEnum] = ...,
                 optional_import_enum: Optional[ImportEnum] = ...,
                 optional_string_piece: Optional[Text] = ...,
                 optional_cord: Optional[Text] = ...,
                 optional_public_import_message: Optional[PublicImportMessage] = ...,
                 optional_message: Optional[TestAllTypes.NestedMessage] = ...,
                 repeated_int32: Optional[Iterable[int]] = ...,
                 repeated_int64: Optional[Iterable[int]] = ...,
                 repeated_uint32: Optional[Iterable[int]] = ...,
                 repeated_uint64: Optional[Iterable[int]] = ...,
                 repeated_sint32: Optional[Iterable[int]] = ...,
                 repeated_sint64: Optional[Iterable[int]] = ...,
                 repeated_fixed32: Optional[Iterable[int]] = ...,
                 repeated_fixed64: Optional[Iterable[int]] = ...,
                 repeated_sfixed32: Optional[Iterable[int]] = ...,
                 repeated_sfixed64: Optional[Iterable[int]] = ...,
                 repeated_float: Optional[Iterable[float]] = ...,
                 repeated_double: Optional[Iterable[float]] = ...,
                 repeated_bool: Optional[Iterable[bool]] = ...,
                 repeated_string: Optional[Iterable[Text]] = ...,
                 repeated_bytes: Optional[Iterable[bytes]] = ...,
                 repeatedgroup: Optional[Iterable[TestAllTypes.RepeatedGroup]] = ...,
                 repeated_nested_message: Optional[Iterable[TestAllTypes.NestedMessage]] = ...,
                 repeated_foreign_message: Optional[Iterable[ForeignMessage]] = ...,
                 repeated_import_message: Optional[Iterable[ImportMessage]] = ...,
                 repeated_nested_enum: Optional[Iterable[TestAllTypes.NestedEnum]] = ...,
                 repeated_foreign_enum: Optional[Iterable[ForeignEnum]] = ...,
                 repeated_import_enum: Optional[Iterable[ImportEnum]] = ...,
                 repeated_string_piece: Optional[Iterable[Text]] = ...,
                 repeated_cord: Optional[Iterable[Text]] = ...,
                 repeated_lazy_message: Optional[Iterable[TestAllTypes.NestedMessage]] = ...,
                 default_int32: Optional[int] = ...,
                 default_int64: Optional[int] = ...,
                 default_uint32: Optional[int] = ...,
                 default_uint64: Optional[int] = ...,
                 default_sint32: Optional[int] = ...,
                 default_sint64: Optional[int] = ...,
                 default_fixed32: Optional[int] = ...,
                 default_fixed64: Optional[int] = ...,
                 default_sfixed32: Optional[int] = ...,
                 default_sfixed64: Optional[int] = ...,
                 default_float: Optional[float] = ...,
                 default_double: Optional[float] = ...,
                 default_bool: Optional[bool] = ...,
                 default_string: Optional[Text] = ...,
                 default_bytes: Optional[bytes] = ...,
                 default_nested_enum: Optional[TestAllTypes.NestedEnum] = ...,
                 default_foreign_enum: Optional[ForeignEnum] = ...,
                 default_import_enum: Optional[ImportEnum] = ...,
                 default_string_piece: Optional[Text] = ...,
                 default_cord: Optional[Text] = ...,
                 oneof_uint32: Optional[int] = ...,
                 oneof_nested_message: Optional[TestAllTypes.NestedMessage] = ...,
                 oneof_string: Optional[Text] = ...,
                 oneof_bytes: Optional[bytes] = ...,
                 lazy_oneof_nested_message: Optional[TestAllTypes.NestedMessage] = ...,
                 ) -> None: ...


class ForeignMessage(Message):
    c: int

    def __init__(self,
                 c: Optional[int] = ...,
                 ) -> None: ...


class TestNoArenaMessage(Message):

    @property
    def arena_message(self) -> ArenaMessage: ...

    def __init__(self,
                 arena_message: Optional[ArenaMessage] = ...,
                 ) -> None: ...
