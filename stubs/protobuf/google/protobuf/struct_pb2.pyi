"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.internal.well_known_types
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

# `NullValue` is a singleton enumeration to represent the null value for the
# `Value` type union.
#
#  The JSON representation for `NullValue` is JSON `null`.
class NullValue(_NullValue, metaclass=_NullValueEnumTypeWrapper):
    pass
class _NullValue:
    V = typing.NewType('V', builtins.int)
class _NullValueEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_NullValue.V], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    # Null value.
    NULL_VALUE = NullValue.V(0)

# Null value.
NULL_VALUE = NullValue.V(0)
global___NullValue = NullValue


# `Struct` represents a structured data value, consisting of fields
# which map to dynamically typed values. In some languages, `Struct`
# might be supported by a native representation. For example, in
# scripting languages like JS a struct is represented as an
# object. The details of that representation are described together
# with the proto support for the language.
#
# The JSON representation for `Struct` is JSON object.
class Struct(google.protobuf.message.Message, google.protobuf.internal.well_known_types.Struct):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class FieldsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> global___Value: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.global___Value | None = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    FIELDS_FIELD_NUMBER: builtins.int
    # Unordered map of dynamically typed values.
    @property
    def fields(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___Value]: ...
    def __init__(self,
        *,
        fields : typing.typing.Mapping[typing.Text, global___Value] | None = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"fields",b"fields"]) -> None: ...
global___Struct = Struct

# `Value` represents a dynamically typed value which can be either
# null, a number, a string, a boolean, a recursive struct value, or a
# list of values. A producer of value is expected to set one of that
# variants, absence of any variant indicates an error.
#
# The JSON representation for `Value` is JSON value.
class Value(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NULL_VALUE_FIELD_NUMBER: builtins.int
    NUMBER_VALUE_FIELD_NUMBER: builtins.int
    STRING_VALUE_FIELD_NUMBER: builtins.int
    BOOL_VALUE_FIELD_NUMBER: builtins.int
    STRUCT_VALUE_FIELD_NUMBER: builtins.int
    LIST_VALUE_FIELD_NUMBER: builtins.int
    # Represents a null value.
    null_value: global___NullValue.V = ...
    # Represents a double value.
    number_value: builtins.float = ...
    # Represents a string value.
    string_value: typing.Text = ...
    # Represents a boolean value.
    bool_value: builtins.bool = ...
    # Represents a structured value.
    @property
    def struct_value(self) -> global___Struct: ...
    # Represents a repeated `Value`.
    @property
    def list_value(self) -> global___ListValue: ...
    def __init__(self,
        *,
        null_value : global___NullValue.V = ...,
        number_value : builtins.float = ...,
        string_value : typing.Text = ...,
        bool_value : builtins.bool = ...,
        struct_value : typing.global___Struct | None = ...,
        list_value : typing.global___ListValue | None = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"bool_value",b"bool_value",u"kind",b"kind",u"list_value",b"list_value",u"null_value",b"null_value",u"number_value",b"number_value",u"string_value",b"string_value",u"struct_value",b"struct_value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"bool_value",b"bool_value",u"kind",b"kind",u"list_value",b"list_value",u"null_value",b"null_value",u"number_value",b"number_value",u"string_value",b"string_value",u"struct_value",b"struct_value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"kind",b"kind"]) -> typing.typing_extensions.Literal["null_value","number_value","string_value","bool_value","struct_value","list_value"] | None: ...
global___Value = Value

# `ListValue` is a wrapper around a repeated field of values.
#
# The JSON representation for `ListValue` is JSON array.
class ListValue(google.protobuf.message.Message, google.protobuf.internal.well_known_types.ListValue):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VALUES_FIELD_NUMBER: builtins.int
    # Repeated field of dynamically typed values.
    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Value]: ...
    def __init__(self,
        *,
        values : typing.typing.Iterable[global___Value] | None = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"values",b"values"]) -> None: ...
global___ListValue = ListValue
