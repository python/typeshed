"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import sys

import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import tensorflow.core.framework.attr_value_pb2
import tensorflow.core.framework.node_def_pb2
import tensorflow.core.framework.op_def_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class FunctionDefLibrary(google.protobuf.message.Message):
    """A library is a set of named functions."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FUNCTION_FIELD_NUMBER: builtins.int
    GRADIENT_FIELD_NUMBER: builtins.int
    REGISTERED_GRADIENTS_FIELD_NUMBER: builtins.int
    @property
    def function(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FunctionDef]: ...
    @property
    def gradient(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GradientDef]: ...
    @property
    def registered_gradients(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___RegisteredGradient]: ...
    def __init__(
        self,
        *,
        function: collections.abc.Iterable[global___FunctionDef] | None = ...,
        gradient: collections.abc.Iterable[global___GradientDef] | None = ...,
        registered_gradients: collections.abc.Iterable[global___RegisteredGradient] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["function", b"function", "gradient", b"gradient", "registered_gradients", b"registered_gradients"]) -> None: ...

global___FunctionDefLibrary = FunctionDefLibrary

@typing_extensions.final
class FunctionDef(google.protobuf.message.Message):
    """A function can be instantiated when the runtime can bind every attr
    with a value. When a GraphDef has a call to a function, it must
    have binding for every attr defined in the signature.

    TODO(zhifengc):
      * device spec, etc.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class AttrEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> tensorflow.core.framework.attr_value_pb2.AttrValue: ...
        def __init__(
            self,
            *,
            key: builtins.str | None = ...,
            value: tensorflow.core.framework.attr_value_pb2.AttrValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    @typing_extensions.final
    class ArgAttrs(google.protobuf.message.Message):
        """Attributes for function arguments. These attributes are the same set of
        valid attributes as to _Arg nodes.
        """

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        @typing_extensions.final
        class AttrEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: builtins.str
            @property
            def value(self) -> tensorflow.core.framework.attr_value_pb2.AttrValue: ...
            def __init__(
                self,
                *,
                key: builtins.str | None = ...,
                value: tensorflow.core.framework.attr_value_pb2.AttrValue | None = ...,
            ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

        ATTR_FIELD_NUMBER: builtins.int
        @property
        def attr(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, tensorflow.core.framework.attr_value_pb2.AttrValue]: ...
        def __init__(
            self,
            *,
            attr: collections.abc.Mapping[builtins.str, tensorflow.core.framework.attr_value_pb2.AttrValue] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["attr", b"attr"]) -> None: ...

    @typing_extensions.final
    class ArgAttrEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        @property
        def value(self) -> global___FunctionDef.ArgAttrs: ...
        def __init__(
            self,
            *,
            key: builtins.int | None = ...,
            value: global___FunctionDef.ArgAttrs | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    @typing_extensions.final
    class ResourceArgUniqueIdEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        value: builtins.int
        def __init__(
            self,
            *,
            key: builtins.int | None = ...,
            value: builtins.int | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    @typing_extensions.final
    class RetEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str | None = ...,
            value: builtins.str | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    @typing_extensions.final
    class ControlRetEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str | None = ...,
            value: builtins.str | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    SIGNATURE_FIELD_NUMBER: builtins.int
    ATTR_FIELD_NUMBER: builtins.int
    ARG_ATTR_FIELD_NUMBER: builtins.int
    RESOURCE_ARG_UNIQUE_ID_FIELD_NUMBER: builtins.int
    NODE_DEF_FIELD_NUMBER: builtins.int
    RET_FIELD_NUMBER: builtins.int
    CONTROL_RET_FIELD_NUMBER: builtins.int
    @property
    def signature(self) -> tensorflow.core.framework.op_def_pb2.OpDef:
        """The definition of the function's name, arguments, return values,
        attrs etc.
        """
    @property
    def attr(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, tensorflow.core.framework.attr_value_pb2.AttrValue]:
        """Attributes specific to this function definition."""
    @property
    def arg_attr(self) -> google.protobuf.internal.containers.MessageMap[builtins.int, global___FunctionDef.ArgAttrs]: ...
    @property
    def resource_arg_unique_id(self) -> google.protobuf.internal.containers.ScalarMap[builtins.int, builtins.int]:
        """Unique IDs for each resource argument, used to track aliasing resources. If
        Argument A and Argument B alias each other, then
        resource_arg_unique_ids[A.index] == resource_arg_unique_ids[B.index].

        If this field is empty, none of the arguments could alias; otherwise, every
        resource argument should have an entry in this field.

        When instantiated, the unique IDs will be attached to the _Arg nodes'
        "_resource_arg_unique_id" attribute.
        """
    @property
    def node_def(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[tensorflow.core.framework.node_def_pb2.NodeDef]:
        """The body of the function.  Unlike the NodeDefs in a GraphDef, attrs
        may have values of type `placeholder` and the `input` field uses
        the "output" format above.

        By convention, "op" in node_def is resolved by consulting with a
        user-defined library first. If not resolved, "func" is assumed to
        be a builtin op.
        """
    @property
    def ret(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """A mapping from the output arg names from `signature` to the
        outputs from `node_def` that should be returned by the function.
        """
    @property
    def control_ret(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """A mapping from control output names from `signature` to node names in
        `node_def` which should be control outputs of this function.
        """
    def __init__(
        self,
        *,
        signature: tensorflow.core.framework.op_def_pb2.OpDef | None = ...,
        attr: collections.abc.Mapping[builtins.str, tensorflow.core.framework.attr_value_pb2.AttrValue] | None = ...,
        arg_attr: collections.abc.Mapping[builtins.int, global___FunctionDef.ArgAttrs] | None = ...,
        resource_arg_unique_id: collections.abc.Mapping[builtins.int, builtins.int] | None = ...,
        node_def: collections.abc.Iterable[tensorflow.core.framework.node_def_pb2.NodeDef] | None = ...,
        ret: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        control_ret: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["signature", b"signature"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["arg_attr", b"arg_attr", "attr", b"attr", "control_ret", b"control_ret", "node_def", b"node_def", "resource_arg_unique_id", b"resource_arg_unique_id", "ret", b"ret", "signature", b"signature"]) -> None: ...

global___FunctionDef = FunctionDef

@typing_extensions.final
class GradientDef(google.protobuf.message.Message):
    """GradientDef defines the gradient function of a function defined in
    a function library.

    A gradient function g (specified by gradient_func) for a function f
    (specified by function_name) must follow the following:

    The function 'f' must be a numerical function which takes N inputs
    and produces M outputs. Its gradient function 'g', which is a
    function taking N + M inputs and produces N outputs.

    I.e. if we have
       (y1, y2, ..., y_M) = f(x1, x2, ..., x_N),
    then, g is
       (dL/dx1, dL/dx2, ..., dL/dx_N) = g(x1, x2, ..., x_N,
                                         dL/dy1, dL/dy2, ..., dL/dy_M),
    where L is a scalar-value function of (x1, x2, ..., xN) (e.g., the
    loss function). dL/dx_i is the partial derivative of L with respect
    to x_i.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FUNCTION_NAME_FIELD_NUMBER: builtins.int
    GRADIENT_FUNC_FIELD_NUMBER: builtins.int
    function_name: builtins.str
    """The function name."""
    gradient_func: builtins.str
    """The gradient function's name."""
    def __init__(
        self,
        *,
        function_name: builtins.str | None = ...,
        gradient_func: builtins.str | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["function_name", b"function_name", "gradient_func", b"gradient_func"]) -> None: ...

global___GradientDef = GradientDef

@typing_extensions.final
class RegisteredGradient(google.protobuf.message.Message):
    """RegisteredGradient stores a gradient function that is registered in the
    gradients library and used in the ops of a function in the function library.
    Unlike GradientDef, these gradients are identified by op type, and not
    directly linked to any function.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    GRADIENT_FUNC_FIELD_NUMBER: builtins.int
    REGISTERED_OP_TYPE_FIELD_NUMBER: builtins.int
    gradient_func: builtins.str
    """The gradient function's name."""
    registered_op_type: builtins.str
    """The gradient function's registered op type."""
    def __init__(
        self,
        *,
        gradient_func: builtins.str | None = ...,
        registered_op_type: builtins.str | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["gradient_func", b"gradient_func", "registered_op_type", b"registered_op_type"]) -> None: ...

global___RegisteredGradient = RegisteredGradient
