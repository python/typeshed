"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import sys
import typing

import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _FullTypeId:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _FullTypeIdEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_FullTypeId.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    TFT_UNSET: _FullTypeId.ValueType  # 0
    """The default represents an uninitialized values."""
    TFT_VAR: _FullTypeId.ValueType  # 1
    """Type symbols. Used to construct more complex type expressions like
    algebraic data types.

    Type variables may serve as placeholder for any other type ID in type
    templates.

    Examples:
      TFT_DATASET[TFT_VAR["T"]] is a Dataset returning a type indicated by "T".
      TFT_TENSOR[TFT_VAR["T"]] is a Tensor of n element type indicated by "T".
      TFT_TENSOR[TFT_VAR["T"]], TFT_TENSOR[TFT_VAR["T"]] are two tensors of
        identical element types.
      TFT_TENSOR[TFT_VAR["P"]], TFT_TENSOR[TFT_VAR["Q"]] are two tensors of
        independent element types.
    """
    TFT_ANY: _FullTypeId.ValueType  # 2
    """Wildcard type. Describes a parameter of unknown type. In TensorFlow, that
    can mean either a "Top" type (accepts any type), or a dynamically typed
    object whose type is unknown in context.
    Important: "unknown" does not necessarily mean undeterminable!
    """
    TFT_PRODUCT: _FullTypeId.ValueType  # 3
    """The algebraic product type. This is an algebraic type that may be used just
    for logical grouping. Not to confused with TFT_TUPLE which describes a
    concrete object of several elements.

    Example:
      TFT_DATASET[TFT_PRODUCT[TFT_TENSOR[TFT_INT32], TFT_TENSOR[TFT_FLOAT64]]]
        is a Dataset producing two tensors, an integer one and a float one.
    """
    TFT_NAMED: _FullTypeId.ValueType  # 4
    """Represents a named field, with the name stored in the attribute.

    Parametrization:
      TFT_NAMED[<type>]{<name>}
      * <type> is the type of the field
      * <name> is the field name, as string (thpugh can theoretically be an int
        as well)

    Example:
      TFT_RECORD[
        TFT_NAMED[TFT_TENSOR[TFT_INT32]]{'foo'},
        TFT_NAMED[TFT_TENSOR[TFT_FLOAT32]]{'bar'},
      ]
        is a structure with two fields, an int tensor "foo" and a float tensor
        "bar".
    """
    TFT_FOR_EACH: _FullTypeId.ValueType  # 20
    """Template definition. Expands the variables by repeating a template as
    arguments of container.

    Parametrization:
      TFT_FOR_EACH[<container_type>, <template>, <expansions>]
      * <container_type> is the type of the container that the template will be
        expanded into
      * <template> is any type definition that potentially contains type
        variables
      * <expansions> is a TFT_VAR and may include more types in the future

    Example:
      TFT_FOR_EACH[
            TFT_PRODUCT,
            TFT_TENSOR[TFT_VAR["t"]],
            TFT_VAR["t"]
        ]
        will substitute a T = TFT_INT32 to TFT_PRODUCT[TFT_TENSOR[TFT_INT32]]
        and a T = (TFT_INT32, TFT_INT64) to
        TFT_PRODUCT[TFT_TENSOR[TFT_INT32], TFT_TENSOR[TFT_INT64]].
    """
    TFT_CALLABLE: _FullTypeId.ValueType  # 100
    """Callable types describe functions and ops.

    Parametrization:
      TFT_CALLABLE[<arg type>, <return type>]
      * <arg type> is the type of the arguments; TFT_PRODUCT represents
      multiple
        arguments.
      * <return type> is the return type; TFT_PRODUCT represents multiple
        return values (that means that callables returning multiple things
        don't necessarily return a single tuple).

    Example:
      TFT_CALLABLE[
        TFT_ANY,
        TFT_PRODUCT[TFT_TENSOR[TFT_INT32], TFT_TENSOR[TFT_FLOAT64]],
      ]
        is a callable with unspecified (for now) input arguments, and
        two return values of type tensor.
    """
    TFT_TENSOR: _FullTypeId.ValueType  # 1000
    """Concrete type IDs, representing "proper" data types that can describe
    runtime TensorFlow objects.

    The usual Tensor. This is a parametric type.

    Parametrization:
      TFT_TENSOR[<element type>, <shape type>]
      * <element type> is currently limited to one of the element types
        defined below.
      * <shape type> is not yet defined, and may only be TFT_UNKNOWN for now.

    A TFT_SHAPE type will be defined in the future.

    Example:
      TFT_TENSOR[TFT_INT32, TFT_UNKNOWN]
        is a Tensor of int32 element type and unknown shape.

    TODO(mdan): Define TFT_SHAPE and add more examples.
    """
    TFT_ARRAY: _FullTypeId.ValueType  # 1001
    """Array (or tensorflow::TensorList in the variant type registry).
    Note: this is not to be confused with the deprecated `TensorArray*` ops
    which are not supported by FullType.
    This type represents a random-access list whose elements can be
    described by a single type. Although immutable, Array is expected to
    support efficient mutation semantics (i.e. element update) in the
    user-facing API.
    The element type may be generic or even TFT_ANY for a heterogenous list.

    Parametrization:
      TFT_ARRAY[<element type>]
      * <element type> may be any concrete type.

    Examples:
      TFT_ARRAY[TFT_TENSOR[TFT_INT32]] is a TensorArray holding int32 Tensors
        of any shape.
      TFT_ARRAY[TFT_TENSOR[TFT_UNKNOWN]] is a TensorArray holding Tensors of
        mixed element types.
      TFT_ARRAY[TFT_UNKNOWN] is a TensorArray holding any element type.
      TFT_ARRAY[] is equivalent to TFT_ARRAY[TFT_UNKNOWN].
      TFT_ARRAY[TFT_ARRAY[]] is an array or arrays (of unknown types).
    """
    TFT_OPTIONAL: _FullTypeId.ValueType  # 1002
    """Optional (or tensorflow::OptionalVariant in the variant type registry).
    This type represents a value that may either hold an element of a single
    specified type, or nothing at all.

    Parametrization:
      TFT_OPTIONAL[<element type>]
      * <element type> may be any concrete type.

    Examples:
      TFT_OPTIONAL[TFT_TENSOR[TFT_INT32]] is an Optional holding an int32
        Tensor of any shape.
    """
    TFT_LITERAL: _FullTypeId.ValueType  # 1003
    """Literal types describe compile-time constant values.
    Literal types may also participate in dependent types.

    Parametrization:
      TFT_LITERAL[<value type>]{<value>}
      * <value type> may be any concrete type compatible that can hold <value>
      * <value> is the type's attribute, and holds the actual literal value

    Examples:
      TFT_LITERAL[TFT_INT32]{1} is the compile-time constant 1.
    """
    TFT_ENCODED: _FullTypeId.ValueType  # 1004
    """Encoding types describe a value of a certain type, encoded as a different
    type.

    Parametrization:
      TFT_ENCODED[<encoded type>, <encoding type>]
      * <encoded type> may be any type
      * <encoding type> may be any type

    Examples:
      TFT_ENCODING[TFT_INT32, TFT_STRING] is an integer encoded as string.
    """
    TFT_SHAPE_TENSOR: _FullTypeId.ValueType  # 1005
    """The type of "shape tensors" where the runtime value is the shape of
    some tensor(s), i.e. the output of tf.shape.
    Shape tensors have special, host-only placement, in contrast to
    TFT_TENSOR[TFT_INT32] which is the type of a normal numeric tensor
    with no special placement.

    Examples:
      TFT_SHAPE_TENSOR[TFT_INT32] is the most common
      TFT_SHAPE_TENSOR[TFT_INT64] is also allowed
    """
    TFT_BOOL: _FullTypeId.ValueType  # 200
    """Type attributes. These always appear in the parametrization of a type,
    never alone. For example, there is no such thing as a "bool" TensorFlow
    object (for now).

    The bool element type.
    TODO(mdan): Quantized types, legacy representations (e.g. ref)
    """
    TFT_UINT8: _FullTypeId.ValueType  # 201
    """Integer element types."""
    TFT_UINT16: _FullTypeId.ValueType  # 202
    TFT_UINT32: _FullTypeId.ValueType  # 203
    TFT_UINT64: _FullTypeId.ValueType  # 204
    TFT_INT8: _FullTypeId.ValueType  # 205
    TFT_INT16: _FullTypeId.ValueType  # 206
    TFT_INT32: _FullTypeId.ValueType  # 207
    TFT_INT64: _FullTypeId.ValueType  # 208
    TFT_HALF: _FullTypeId.ValueType  # 209
    """Floating-point element types."""
    TFT_FLOAT: _FullTypeId.ValueType  # 210
    TFT_DOUBLE: _FullTypeId.ValueType  # 211
    TFT_BFLOAT16: _FullTypeId.ValueType  # 215
    TFT_COMPLEX64: _FullTypeId.ValueType  # 212
    """Complex element types.
    TODO(mdan): Represent as TFT_COMPLEX[TFT_DOUBLE] instead?
    """
    TFT_COMPLEX128: _FullTypeId.ValueType  # 213
    TFT_STRING: _FullTypeId.ValueType  # 214
    """The string element type."""
    TFT_DATASET: _FullTypeId.ValueType  # 10102
    """Other types that we don't know yet whether they will become part of the
    core type system or be consisdered third-party (and consequently moved to
    user-defined type mechanisms). Presently, they are effectively in the core
    type system, because key compilation passes like Placer account for their
    existence.

    Datasets created by tf.data ops and APIs. Datasets have generator/iterable
    semantics, that is, one can construct an iterator from them. Like
    Array, they are considered to return elements that can be described
    by a single type. Unlike Array, they do not support random access or
    mutation, and can potentially produce an infinite number of elements.
    A datasets can produce logical structures (e.g. multiple elements). This
    is expressed using TFT_PRODUCT.


    Parametrization: TFT_DATASET[<element type>].
      * <element type> may be a concrete type or a type symbol. It represents
        the data type of the elements produced by the dataset.

    Examples:
      TFT_DATSET[TFT_TENSOR[TFT_INT32]] is a Dataset producing single int32
        Tensors of unknown shape.
      TFT_DATSET[TFT_PRODUCT[TFT_TENSOR[TFT_INT32], TFT_TENSOR[TFT_FLOAT32]] is
        a Dataset producing pairs of Tensors, one integer and one float.
    Note: The high ID number is to prepare for the eventuality that Datasets
    will be supported by user types in the future.
    """
    TFT_RAGGED: _FullTypeId.ValueType  # 10103
    """A ragged tensor created by tf.ragged ops and APIs.

    Parametrization: TFT_RAGGED[<element_type>].
    """
    TFT_ITERATOR: _FullTypeId.ValueType  # 10104
    """Iterators created by tf.data ops and APIs. Very similar to Datasets, except
    they are mutable.


    Parametrization: TFT_ITERATOR[<element type>].
      * <element type> may be a concrete type or a type symbol. It represents
        the data type of the elements produced by the dataset.
    """
    TFT_MUTEX_LOCK: _FullTypeId.ValueType  # 10202
    """A mutex lock tensor, produced by tf.raw_ops.MutexLock.
    Unlike strict execution models, where ownership of a lock is denoted by
    "running after the lock has been acquired", in non-strict mode, lock
    ownership is in the true sense: "the op argument representing the lock is
    available".
    Mutex locks are the dynamic counterpart of control dependencies.
    TODO(mdan): Properly document this thing.

    Parametrization: TFT_MUTEX_LOCK[].
    """
    TFT_LEGACY_VARIANT: _FullTypeId.ValueType  # 10203
    """The equivalent of a Tensor with DT_VARIANT dtype, kept here to simplify
    translation. This type should not normally appear after type inference.
    Note that LEGACY_VARIANT != ANY: TENSOR[INT32] is a subtype of ANY, but is
    not a subtype of LEGACY_VARIANT.
    """

class FullTypeId(_FullTypeId, metaclass=_FullTypeIdEnumTypeWrapper):
    """LINT.IfChange
    Experimental. Represents the complete type information of a TensorFlow value.
    """

TFT_UNSET: FullTypeId.ValueType  # 0
"""The default represents an uninitialized values."""
TFT_VAR: FullTypeId.ValueType  # 1
"""Type symbols. Used to construct more complex type expressions like
algebraic data types.

Type variables may serve as placeholder for any other type ID in type
templates.

Examples:
  TFT_DATASET[TFT_VAR["T"]] is a Dataset returning a type indicated by "T".
  TFT_TENSOR[TFT_VAR["T"]] is a Tensor of n element type indicated by "T".
  TFT_TENSOR[TFT_VAR["T"]], TFT_TENSOR[TFT_VAR["T"]] are two tensors of
    identical element types.
  TFT_TENSOR[TFT_VAR["P"]], TFT_TENSOR[TFT_VAR["Q"]] are two tensors of
    independent element types.
"""
TFT_ANY: FullTypeId.ValueType  # 2
"""Wildcard type. Describes a parameter of unknown type. In TensorFlow, that
can mean either a "Top" type (accepts any type), or a dynamically typed
object whose type is unknown in context.
Important: "unknown" does not necessarily mean undeterminable!
"""
TFT_PRODUCT: FullTypeId.ValueType  # 3
"""The algebraic product type. This is an algebraic type that may be used just
for logical grouping. Not to confused with TFT_TUPLE which describes a
concrete object of several elements.

Example:
  TFT_DATASET[TFT_PRODUCT[TFT_TENSOR[TFT_INT32], TFT_TENSOR[TFT_FLOAT64]]]
    is a Dataset producing two tensors, an integer one and a float one.
"""
TFT_NAMED: FullTypeId.ValueType  # 4
"""Represents a named field, with the name stored in the attribute.

Parametrization:
  TFT_NAMED[<type>]{<name>}
  * <type> is the type of the field
  * <name> is the field name, as string (thpugh can theoretically be an int
    as well)

Example:
  TFT_RECORD[
    TFT_NAMED[TFT_TENSOR[TFT_INT32]]{'foo'},
    TFT_NAMED[TFT_TENSOR[TFT_FLOAT32]]{'bar'},
  ]
    is a structure with two fields, an int tensor "foo" and a float tensor
    "bar".
"""
TFT_FOR_EACH: FullTypeId.ValueType  # 20
"""Template definition. Expands the variables by repeating a template as
arguments of container.

Parametrization:
  TFT_FOR_EACH[<container_type>, <template>, <expansions>]
  * <container_type> is the type of the container that the template will be
    expanded into
  * <template> is any type definition that potentially contains type
    variables
  * <expansions> is a TFT_VAR and may include more types in the future

Example:
  TFT_FOR_EACH[
        TFT_PRODUCT,
        TFT_TENSOR[TFT_VAR["t"]],
        TFT_VAR["t"]
    ]
    will substitute a T = TFT_INT32 to TFT_PRODUCT[TFT_TENSOR[TFT_INT32]]
    and a T = (TFT_INT32, TFT_INT64) to
    TFT_PRODUCT[TFT_TENSOR[TFT_INT32], TFT_TENSOR[TFT_INT64]].
"""
TFT_CALLABLE: FullTypeId.ValueType  # 100
"""Callable types describe functions and ops.

Parametrization:
  TFT_CALLABLE[<arg type>, <return type>]
  * <arg type> is the type of the arguments; TFT_PRODUCT represents
  multiple
    arguments.
  * <return type> is the return type; TFT_PRODUCT represents multiple
    return values (that means that callables returning multiple things
    don't necessarily return a single tuple).

Example:
  TFT_CALLABLE[
    TFT_ANY,
    TFT_PRODUCT[TFT_TENSOR[TFT_INT32], TFT_TENSOR[TFT_FLOAT64]],
  ]
    is a callable with unspecified (for now) input arguments, and
    two return values of type tensor.
"""
TFT_TENSOR: FullTypeId.ValueType  # 1000
"""Concrete type IDs, representing "proper" data types that can describe
runtime TensorFlow objects.

The usual Tensor. This is a parametric type.

Parametrization:
  TFT_TENSOR[<element type>, <shape type>]
  * <element type> is currently limited to one of the element types
    defined below.
  * <shape type> is not yet defined, and may only be TFT_UNKNOWN for now.

A TFT_SHAPE type will be defined in the future.

Example:
  TFT_TENSOR[TFT_INT32, TFT_UNKNOWN]
    is a Tensor of int32 element type and unknown shape.

TODO(mdan): Define TFT_SHAPE and add more examples.
"""
TFT_ARRAY: FullTypeId.ValueType  # 1001
"""Array (or tensorflow::TensorList in the variant type registry).
Note: this is not to be confused with the deprecated `TensorArray*` ops
which are not supported by FullType.
This type represents a random-access list whose elements can be
described by a single type. Although immutable, Array is expected to
support efficient mutation semantics (i.e. element update) in the
user-facing API.
The element type may be generic or even TFT_ANY for a heterogenous list.

Parametrization:
  TFT_ARRAY[<element type>]
  * <element type> may be any concrete type.

Examples:
  TFT_ARRAY[TFT_TENSOR[TFT_INT32]] is a TensorArray holding int32 Tensors
    of any shape.
  TFT_ARRAY[TFT_TENSOR[TFT_UNKNOWN]] is a TensorArray holding Tensors of
    mixed element types.
  TFT_ARRAY[TFT_UNKNOWN] is a TensorArray holding any element type.
  TFT_ARRAY[] is equivalent to TFT_ARRAY[TFT_UNKNOWN].
  TFT_ARRAY[TFT_ARRAY[]] is an array or arrays (of unknown types).
"""
TFT_OPTIONAL: FullTypeId.ValueType  # 1002
"""Optional (or tensorflow::OptionalVariant in the variant type registry).
This type represents a value that may either hold an element of a single
specified type, or nothing at all.

Parametrization:
  TFT_OPTIONAL[<element type>]
  * <element type> may be any concrete type.

Examples:
  TFT_OPTIONAL[TFT_TENSOR[TFT_INT32]] is an Optional holding an int32
    Tensor of any shape.
"""
TFT_LITERAL: FullTypeId.ValueType  # 1003
"""Literal types describe compile-time constant values.
Literal types may also participate in dependent types.

Parametrization:
  TFT_LITERAL[<value type>]{<value>}
  * <value type> may be any concrete type compatible that can hold <value>
  * <value> is the type's attribute, and holds the actual literal value

Examples:
  TFT_LITERAL[TFT_INT32]{1} is the compile-time constant 1.
"""
TFT_ENCODED: FullTypeId.ValueType  # 1004
"""Encoding types describe a value of a certain type, encoded as a different
type.

Parametrization:
  TFT_ENCODED[<encoded type>, <encoding type>]
  * <encoded type> may be any type
  * <encoding type> may be any type

Examples:
  TFT_ENCODING[TFT_INT32, TFT_STRING] is an integer encoded as string.
"""
TFT_SHAPE_TENSOR: FullTypeId.ValueType  # 1005
"""The type of "shape tensors" where the runtime value is the shape of
some tensor(s), i.e. the output of tf.shape.
Shape tensors have special, host-only placement, in contrast to
TFT_TENSOR[TFT_INT32] which is the type of a normal numeric tensor
with no special placement.

Examples:
  TFT_SHAPE_TENSOR[TFT_INT32] is the most common
  TFT_SHAPE_TENSOR[TFT_INT64] is also allowed
"""
TFT_BOOL: FullTypeId.ValueType  # 200
"""Type attributes. These always appear in the parametrization of a type,
never alone. For example, there is no such thing as a "bool" TensorFlow
object (for now).

The bool element type.
TODO(mdan): Quantized types, legacy representations (e.g. ref)
"""
TFT_UINT8: FullTypeId.ValueType  # 201
"""Integer element types."""
TFT_UINT16: FullTypeId.ValueType  # 202
TFT_UINT32: FullTypeId.ValueType  # 203
TFT_UINT64: FullTypeId.ValueType  # 204
TFT_INT8: FullTypeId.ValueType  # 205
TFT_INT16: FullTypeId.ValueType  # 206
TFT_INT32: FullTypeId.ValueType  # 207
TFT_INT64: FullTypeId.ValueType  # 208
TFT_HALF: FullTypeId.ValueType  # 209
"""Floating-point element types."""
TFT_FLOAT: FullTypeId.ValueType  # 210
TFT_DOUBLE: FullTypeId.ValueType  # 211
TFT_BFLOAT16: FullTypeId.ValueType  # 215
TFT_COMPLEX64: FullTypeId.ValueType  # 212
"""Complex element types.
TODO(mdan): Represent as TFT_COMPLEX[TFT_DOUBLE] instead?
"""
TFT_COMPLEX128: FullTypeId.ValueType  # 213
TFT_STRING: FullTypeId.ValueType  # 214
"""The string element type."""
TFT_DATASET: FullTypeId.ValueType  # 10102
"""Other types that we don't know yet whether they will become part of the
core type system or be consisdered third-party (and consequently moved to
user-defined type mechanisms). Presently, they are effectively in the core
type system, because key compilation passes like Placer account for their
existence.

Datasets created by tf.data ops and APIs. Datasets have generator/iterable
semantics, that is, one can construct an iterator from them. Like
Array, they are considered to return elements that can be described
by a single type. Unlike Array, they do not support random access or
mutation, and can potentially produce an infinite number of elements.
A datasets can produce logical structures (e.g. multiple elements). This
is expressed using TFT_PRODUCT.


Parametrization: TFT_DATASET[<element type>].
  * <element type> may be a concrete type or a type symbol. It represents
    the data type of the elements produced by the dataset.

Examples:
  TFT_DATSET[TFT_TENSOR[TFT_INT32]] is a Dataset producing single int32
    Tensors of unknown shape.
  TFT_DATSET[TFT_PRODUCT[TFT_TENSOR[TFT_INT32], TFT_TENSOR[TFT_FLOAT32]] is
    a Dataset producing pairs of Tensors, one integer and one float.
Note: The high ID number is to prepare for the eventuality that Datasets
will be supported by user types in the future.
"""
TFT_RAGGED: FullTypeId.ValueType  # 10103
"""A ragged tensor created by tf.ragged ops and APIs.

Parametrization: TFT_RAGGED[<element_type>].
"""
TFT_ITERATOR: FullTypeId.ValueType  # 10104
"""Iterators created by tf.data ops and APIs. Very similar to Datasets, except
they are mutable.


Parametrization: TFT_ITERATOR[<element type>].
  * <element type> may be a concrete type or a type symbol. It represents
    the data type of the elements produced by the dataset.
"""
TFT_MUTEX_LOCK: FullTypeId.ValueType  # 10202
"""A mutex lock tensor, produced by tf.raw_ops.MutexLock.
Unlike strict execution models, where ownership of a lock is denoted by
"running after the lock has been acquired", in non-strict mode, lock
ownership is in the true sense: "the op argument representing the lock is
available".
Mutex locks are the dynamic counterpart of control dependencies.
TODO(mdan): Properly document this thing.

Parametrization: TFT_MUTEX_LOCK[].
"""
TFT_LEGACY_VARIANT: FullTypeId.ValueType  # 10203
"""The equivalent of a Tensor with DT_VARIANT dtype, kept here to simplify
translation. This type should not normally appear after type inference.
Note that LEGACY_VARIANT != ANY: TENSOR[INT32] is a subtype of ANY, but is
not a subtype of LEGACY_VARIANT.
"""
global___FullTypeId = FullTypeId

@typing_extensions.final
class FullTypeDef(google.protobuf.message.Message):
    """Highly experimental and very likely to change.
    This encoding uses tags instead of dedicated messages for regularity. In
    particular the encoding imposes no restrictions on what the parameters of any
    type should be, which in particular needs to be true for type symbols.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TYPE_ID_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    S_FIELD_NUMBER: builtins.int
    I_FIELD_NUMBER: builtins.int
    type_id: global___FullTypeId.ValueType
    """The principal type represented by this object. This may be a concrete type
    (Tensor, Dataset) a type variable (used for dependent types) a type
    symbol (Any, Union). See FullTypeId for details.
    """
    @property
    def args(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FullTypeDef]: ...
    s: builtins.str
    i: builtins.int
    """TODO(mdan): list/tensor, map? Need to reconcile with TFT_RECORD, etc."""
    def __init__(
        self,
        *,
        type_id: global___FullTypeId.ValueType | None = ...,
        args: collections.abc.Iterable[global___FullTypeDef] | None = ...,
        s: builtins.str | None = ...,
        i: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["attr", b"attr", "i", b"i", "s", b"s"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["args", b"args", "attr", b"attr", "i", b"i", "s", b"s", "type_id", b"type_id"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["attr", b"attr"]) -> typing_extensions.Literal["s", "i"] | None: ...

global___FullTypeDef = FullTypeDef
