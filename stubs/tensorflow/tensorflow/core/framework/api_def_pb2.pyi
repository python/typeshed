"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Defines the text format for including per-op API definition and
overrides for client language op code generators.
"""
import builtins
import collections.abc
import sys
import typing

import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import tensorflow.core.framework.attr_value_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class ApiDef(google.protobuf.message.Message):
    """Used to specify and override the default API & behavior in the
    generated code for client languages, from what you would get from
    the OpDef alone. There will be a set of ApiDefs that are common
    to all client languages, and another set per client language.
    The per-client-language ApiDefs will inherit values from the
    common ApiDefs which it can either replace or modify.

    We separate the API definition from the OpDef so we can evolve the
    API while remaining backwards compatible when interpreting old
    graphs.  Overrides go in an "api_def.pbtxt" file with a text-format
    ApiDefs message.

    WARNING: Be *very* careful changing the API for any existing op --
    you can change the semantics of existing code.  These changes may
    need to wait until a major release of TensorFlow to avoid breaking
    our compatibility promises.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Visibility:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _VisibilityEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ApiDef._Visibility.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        DEFAULT_VISIBILITY: ApiDef._Visibility.ValueType  # 0
        """Normally this is "VISIBLE" unless you are inheriting a
        different value from another ApiDef.
        """
        VISIBLE: ApiDef._Visibility.ValueType  # 1
        """Publicly visible in the API."""
        SKIP: ApiDef._Visibility.ValueType  # 2
        """Do not include this op in the generated API. If visibility is
        set to 'SKIP', other fields are ignored for this op.
        """
        HIDDEN: ApiDef._Visibility.ValueType  # 3
        """Hide this op by putting it into an internal namespace (or whatever
        is appropriate in the target language).
        """

    class Visibility(_Visibility, metaclass=_VisibilityEnumTypeWrapper): ...
    DEFAULT_VISIBILITY: ApiDef.Visibility.ValueType  # 0
    """Normally this is "VISIBLE" unless you are inheriting a
    different value from another ApiDef.
    """
    VISIBLE: ApiDef.Visibility.ValueType  # 1
    """Publicly visible in the API."""
    SKIP: ApiDef.Visibility.ValueType  # 2
    """Do not include this op in the generated API. If visibility is
    set to 'SKIP', other fields are ignored for this op.
    """
    HIDDEN: ApiDef.Visibility.ValueType  # 3
    """Hide this op by putting it into an internal namespace (or whatever
    is appropriate in the target language).
    """

    @typing_extensions.final
    class Endpoint(google.protobuf.message.Message):
        """If you specify any endpoint, this will replace all of the
        inherited endpoints.  The first endpoint should be the
        "canonical" endpoint, and should not be deprecated (unless all
        endpoints are deprecated).
        """

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        NAME_FIELD_NUMBER: builtins.int
        DEPRECATED_FIELD_NUMBER: builtins.int
        DEPRECATION_VERSION_FIELD_NUMBER: builtins.int
        name: builtins.str
        """Name should be either like "CamelCaseName" or
        "Package.CamelCaseName". Client-language-specific ApiDefs may
        use a snake_case convention instead of CamelCase.
        """
        deprecated: builtins.bool
        """Set if this endpoint is deprecated. If set to true, a message suggesting
        to use a non-deprecated endpoint instead will be printed. If all
        endpoints are deprecated, set deprecation_message in ApiDef instead.
        """
        deprecation_version: builtins.int
        """Major version when an endpoint will be deleted. For e.g. set this
        value to 2 if endpoint should be removed in TensorFlow 2.0 and
        deprecated in versions before that.
        """
        def __init__(
            self,
            *,
            name: builtins.str | None = ...,
            deprecated: builtins.bool | None = ...,
            deprecation_version: builtins.int | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["deprecated", b"deprecated", "deprecation_version", b"deprecation_version", "name", b"name"]) -> None: ...

    @typing_extensions.final
    class Arg(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        NAME_FIELD_NUMBER: builtins.int
        RENAME_TO_FIELD_NUMBER: builtins.int
        DESCRIPTION_FIELD_NUMBER: builtins.int
        name: builtins.str
        rename_to: builtins.str
        """Change the name used to access this arg in the API from what
        is used in the GraphDef.  Note that these names in `backticks`
        will also be replaced in the summary & description fields.
        """
        description: builtins.str
        """Note: this will replace any inherited arg doc. There is no
        current way of modifying arg descriptions (other than replacing
        them entirely) as can be done with op descriptions.
        """
        def __init__(
            self,
            *,
            name: builtins.str | None = ...,
            rename_to: builtins.str | None = ...,
            description: builtins.str | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "name", b"name", "rename_to", b"rename_to"]) -> None: ...

    @typing_extensions.final
    class Attr(google.protobuf.message.Message):
        """Description of the graph-construction-time configuration of this
        Op.  That is to say, this describes the attr fields that will
        be specified in the NodeDef.
        """

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        NAME_FIELD_NUMBER: builtins.int
        RENAME_TO_FIELD_NUMBER: builtins.int
        DEFAULT_VALUE_FIELD_NUMBER: builtins.int
        DESCRIPTION_FIELD_NUMBER: builtins.int
        name: builtins.str
        rename_to: builtins.str
        """Change the name used to access this attr in the API from what
        is used in the GraphDef.  Note that these names in `backticks`
        will also be replaced in the summary & description fields.
        """
        @property
        def default_value(self) -> tensorflow.core.framework.attr_value_pb2.AttrValue:
            """Specify a new default value to use for this attr.  This default
            will be used when creating new graphs, as opposed to the
            default in the OpDef, which will be used when interpreting old
            GraphDefs.
            """
        description: builtins.str
        """Note: this will replace any inherited attr doc, there is no current
        way of modifying attr descriptions as can be done with op descriptions.
        """
        def __init__(
            self,
            *,
            name: builtins.str | None = ...,
            rename_to: builtins.str | None = ...,
            default_value: tensorflow.core.framework.attr_value_pb2.AttrValue | None = ...,
            description: builtins.str | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["default_value", b"default_value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["default_value", b"default_value", "description", b"description", "name", b"name", "rename_to", b"rename_to"]) -> None: ...

    GRAPH_OP_NAME_FIELD_NUMBER: builtins.int
    DEPRECATION_MESSAGE_FIELD_NUMBER: builtins.int
    DEPRECATION_VERSION_FIELD_NUMBER: builtins.int
    VISIBILITY_FIELD_NUMBER: builtins.int
    ENDPOINT_FIELD_NUMBER: builtins.int
    IN_ARG_FIELD_NUMBER: builtins.int
    OUT_ARG_FIELD_NUMBER: builtins.int
    ARG_ORDER_FIELD_NUMBER: builtins.int
    ATTR_FIELD_NUMBER: builtins.int
    SUMMARY_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    DESCRIPTION_PREFIX_FIELD_NUMBER: builtins.int
    DESCRIPTION_SUFFIX_FIELD_NUMBER: builtins.int
    graph_op_name: builtins.str
    """Name of the op (in the OpDef) to specify the API for."""
    deprecation_message: builtins.str
    """If this op is deprecated, set deprecation message to the message
    that should be logged when this op is used.
    The message should indicate alternative op to use, if any.
    """
    deprecation_version: builtins.int
    """Major version when the op will be deleted. For e.g. set this
    value to 2 if op API should be removed in TensorFlow 2.0 and
    deprecated in versions before that.
    """
    visibility: global___ApiDef.Visibility.ValueType
    @property
    def endpoint(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ApiDef.Endpoint]: ...
    @property
    def in_arg(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ApiDef.Arg]: ...
    @property
    def out_arg(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ApiDef.Arg]: ...
    @property
    def arg_order(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of original in_arg names to specify new argument order.
        Length of arg_order should be either empty to keep current order
        or match size of in_arg.
        """
    @property
    def attr(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ApiDef.Attr]: ...
    summary: builtins.str
    """One-line human-readable description of what the Op does."""
    description: builtins.str
    """Additional, longer human-readable description of what the Op does."""
    description_prefix: builtins.str
    """Modify an existing/inherited description by adding text to the beginning
    or end.
    """
    description_suffix: builtins.str
    def __init__(
        self,
        *,
        graph_op_name: builtins.str | None = ...,
        deprecation_message: builtins.str | None = ...,
        deprecation_version: builtins.int | None = ...,
        visibility: global___ApiDef.Visibility.ValueType | None = ...,
        endpoint: collections.abc.Iterable[global___ApiDef.Endpoint] | None = ...,
        in_arg: collections.abc.Iterable[global___ApiDef.Arg] | None = ...,
        out_arg: collections.abc.Iterable[global___ApiDef.Arg] | None = ...,
        arg_order: collections.abc.Iterable[builtins.str] | None = ...,
        attr: collections.abc.Iterable[global___ApiDef.Attr] | None = ...,
        summary: builtins.str | None = ...,
        description: builtins.str | None = ...,
        description_prefix: builtins.str | None = ...,
        description_suffix: builtins.str | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["arg_order", b"arg_order", "attr", b"attr", "deprecation_message", b"deprecation_message", "deprecation_version", b"deprecation_version", "description", b"description", "description_prefix", b"description_prefix", "description_suffix", b"description_suffix", "endpoint", b"endpoint", "graph_op_name", b"graph_op_name", "in_arg", b"in_arg", "out_arg", b"out_arg", "summary", b"summary", "visibility", b"visibility"]) -> None: ...

global___ApiDef = ApiDef

@typing_extensions.final
class ApiDefs(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OP_FIELD_NUMBER: builtins.int
    @property
    def op(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ApiDef]: ...
    def __init__(
        self,
        *,
        op: collections.abc.Iterable[global___ApiDef] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["op", b"op"]) -> None: ...

global___ApiDefs = ApiDefs
