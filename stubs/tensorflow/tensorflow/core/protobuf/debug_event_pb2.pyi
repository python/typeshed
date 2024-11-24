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
import tensorflow.core.framework.graph_debug_info_pb2
import tensorflow.core.framework.tensor_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _TensorDebugMode:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _TensorDebugModeEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_TensorDebugMode.ValueType], builtins.type
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNSPECIFIED: _TensorDebugMode.ValueType  # 0
    NO_TENSOR: _TensorDebugMode.ValueType  # 1
    """Only records what tensors are computed, eagerly or in graphs.
    No information regarding the value of the tensor is available.
    """
    CURT_HEALTH: _TensorDebugMode.ValueType  # 2
    """A minimalist health summary for float-type tensors.
    Contains information only about the presence/absence of pathological
    values including Infinity and NaN.
    Applicable only to float dtypes.
    """
    CONCISE_HEALTH: _TensorDebugMode.ValueType  # 3
    """A concise health summary for float-type tensors.
    Contains more information that CURT_HEALTH.
    Infinity and NaN are treated differently.
    Applicable only to float and integer dtypes.
    """
    FULL_HEALTH: _TensorDebugMode.ValueType  # 4
    """A detailed health summary.
    Contains further detailed information than `CONCISE_HEALTH`.
    Information about device, dtype and shape are included.
    Counts for various types of values (Infinity, NaN, negative, zero,
    positive) are included.
    Applicable to float, integer and boolean dtypes.
    """
    SHAPE: _TensorDebugMode.ValueType  # 5
    """Provides full runtime shape information, up to a maximum rank, beyond
    which the dimension sizes are truncated.
    """
    FULL_NUMERICS: _TensorDebugMode.ValueType  # 6
    """Full numeric summary.
    Including device, dtype, shape, counts of various types of values
    (Infinity, NaN, negative, zero, positive), and summary statistics
    (minimum, maximum, mean and variance).
    Applicable to float, integer and boolean dtypes.
    """
    FULL_TENSOR: _TensorDebugMode.ValueType  # 7
    """Full tensor value."""
    REDUCE_INF_NAN_THREE_SLOTS: _TensorDebugMode.ValueType  # 8
    """Reduce the elements of a tensor to a rank-1 tensor of shape [3], in which
    - the 1st element is -inf if any element of the tensor is -inf,
      or zero otherwise.
    - the 2nd element is +inf if any element of the tensor is +inf,
      or zero otherwise.
    - the 3rd element is nan if any element of the tensor is nan, or zero
      otherwise.
    """

class TensorDebugMode(_TensorDebugMode, metaclass=_TensorDebugModeEnumTypeWrapper):
    """Available modes for extracting debugging information from a Tensor.
    TODO(cais): Document the detailed column names and semantics in a separate
    markdown file once the implementation settles.
    """

UNSPECIFIED: TensorDebugMode.ValueType  # 0
NO_TENSOR: TensorDebugMode.ValueType  # 1
"""Only records what tensors are computed, eagerly or in graphs.
No information regarding the value of the tensor is available.
"""
CURT_HEALTH: TensorDebugMode.ValueType  # 2
"""A minimalist health summary for float-type tensors.
Contains information only about the presence/absence of pathological
values including Infinity and NaN.
Applicable only to float dtypes.
"""
CONCISE_HEALTH: TensorDebugMode.ValueType  # 3
"""A concise health summary for float-type tensors.
Contains more information that CURT_HEALTH.
Infinity and NaN are treated differently.
Applicable only to float and integer dtypes.
"""
FULL_HEALTH: TensorDebugMode.ValueType  # 4
"""A detailed health summary.
Contains further detailed information than `CONCISE_HEALTH`.
Information about device, dtype and shape are included.
Counts for various types of values (Infinity, NaN, negative, zero,
positive) are included.
Applicable to float, integer and boolean dtypes.
"""
SHAPE: TensorDebugMode.ValueType  # 5
"""Provides full runtime shape information, up to a maximum rank, beyond
which the dimension sizes are truncated.
"""
FULL_NUMERICS: TensorDebugMode.ValueType  # 6
"""Full numeric summary.
Including device, dtype, shape, counts of various types of values
(Infinity, NaN, negative, zero, positive), and summary statistics
(minimum, maximum, mean and variance).
Applicable to float, integer and boolean dtypes.
"""
FULL_TENSOR: TensorDebugMode.ValueType  # 7
"""Full tensor value."""
REDUCE_INF_NAN_THREE_SLOTS: TensorDebugMode.ValueType  # 8
"""Reduce the elements of a tensor to a rank-1 tensor of shape [3], in which
- the 1st element is -inf if any element of the tensor is -inf,
  or zero otherwise.
- the 2nd element is +inf if any element of the tensor is +inf,
  or zero otherwise.
- the 3rd element is nan if any element of the tensor is nan, or zero
  otherwise.
"""
global___TensorDebugMode = TensorDebugMode

@typing.final
class DebugEvent(google.protobuf.message.Message):
    """An Event related to the debugging of a TensorFlow program."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WALL_TIME_FIELD_NUMBER: builtins.int
    STEP_FIELD_NUMBER: builtins.int
    DEBUG_METADATA_FIELD_NUMBER: builtins.int
    SOURCE_FILE_FIELD_NUMBER: builtins.int
    STACK_FRAME_WITH_ID_FIELD_NUMBER: builtins.int
    GRAPH_OP_CREATION_FIELD_NUMBER: builtins.int
    DEBUGGED_GRAPH_FIELD_NUMBER: builtins.int
    EXECUTION_FIELD_NUMBER: builtins.int
    GRAPH_EXECUTION_TRACE_FIELD_NUMBER: builtins.int
    GRAPH_ID_FIELD_NUMBER: builtins.int
    DEBUGGED_DEVICE_FIELD_NUMBER: builtins.int
    wall_time: builtins.float
    """Timestamp in seconds (with microsecond precision)."""
    step: builtins.int
    """Step of training (if available)."""
    graph_id: builtins.str
    """The ID of the graph (i.e., FuncGraph) executed here: applicable only
    to the execution of a FuncGraph.
    """
    @property
    def debug_metadata(self) -> global___DebugMetadata:
        """Metadata related to this debugging data."""

    @property
    def source_file(self) -> global___SourceFile:
        """The content of a source file."""

    @property
    def stack_frame_with_id(self) -> global___StackFrameWithId:
        """A stack frame (filename, line number and column number, function name and
        code string) with ID.
        """

    @property
    def graph_op_creation(self) -> global___GraphOpCreation:
        """The creation of an op within a graph (e.g., a FuncGraph compiled from
        a Python function).
        """

    @property
    def debugged_graph(self) -> global___DebuggedGraph:
        """Information about a debugged graph."""

    @property
    def execution(self) -> global___Execution:
        """Execution of an op or a Graph (e.g., a tf.function)."""

    @property
    def graph_execution_trace(self) -> global___GraphExecutionTrace:
        """A graph execution trace: Contains information about the intermediate
        tensors computed during the graph execution.
        """

    @property
    def debugged_device(self) -> global___DebuggedDevice:
        """A device on which debugger-instrumented ops and/or tensors reside."""

    def __init__(
        self,
        *,
        wall_time: builtins.float | None = ...,
        step: builtins.int | None = ...,
        debug_metadata: global___DebugMetadata | None = ...,
        source_file: global___SourceFile | None = ...,
        stack_frame_with_id: global___StackFrameWithId | None = ...,
        graph_op_creation: global___GraphOpCreation | None = ...,
        debugged_graph: global___DebuggedGraph | None = ...,
        execution: global___Execution | None = ...,
        graph_execution_trace: global___GraphExecutionTrace | None = ...,
        graph_id: builtins.str | None = ...,
        debugged_device: global___DebuggedDevice | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing.Literal[
            "debug_metadata",
            b"debug_metadata",
            "debugged_device",
            b"debugged_device",
            "debugged_graph",
            b"debugged_graph",
            "execution",
            b"execution",
            "graph_execution_trace",
            b"graph_execution_trace",
            "graph_id",
            b"graph_id",
            "graph_op_creation",
            b"graph_op_creation",
            "source_file",
            b"source_file",
            "stack_frame_with_id",
            b"stack_frame_with_id",
            "what",
            b"what",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "debug_metadata",
            b"debug_metadata",
            "debugged_device",
            b"debugged_device",
            "debugged_graph",
            b"debugged_graph",
            "execution",
            b"execution",
            "graph_execution_trace",
            b"graph_execution_trace",
            "graph_id",
            b"graph_id",
            "graph_op_creation",
            b"graph_op_creation",
            "source_file",
            b"source_file",
            "stack_frame_with_id",
            b"stack_frame_with_id",
            "step",
            b"step",
            "wall_time",
            b"wall_time",
            "what",
            b"what",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing.Literal["what", b"what"]
    ) -> (
        typing.Literal[
            "debug_metadata",
            "source_file",
            "stack_frame_with_id",
            "graph_op_creation",
            "debugged_graph",
            "execution",
            "graph_execution_trace",
            "graph_id",
            "debugged_device",
        ]
        | None
    ): ...

global___DebugEvent = DebugEvent

@typing.final
class DebugMetadata(google.protobuf.message.Message):
    """Metadata about the debugger and the debugged TensorFlow program."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TENSORFLOW_VERSION_FIELD_NUMBER: builtins.int
    FILE_VERSION_FIELD_NUMBER: builtins.int
    TFDBG_RUN_ID_FIELD_NUMBER: builtins.int
    tensorflow_version: builtins.str
    """Version of TensorFlow."""
    file_version: builtins.str
    """Version of the DebugEvent file format.
    Has a format of "debug.Event:<number>", e.g., "debug.Event:1".
    """
    tfdbg_run_id: builtins.str
    """A unique ID for the current run of tfdbg.
    A run of tfdbg is defined as a TensorFlow job instrumented by tfdbg.
    Multiple hosts in a distributed TensorFlow job instrumented by tfdbg
    have the same ID.
    """
    def __init__(
        self,
        *,
        tensorflow_version: builtins.str | None = ...,
        file_version: builtins.str | None = ...,
        tfdbg_run_id: builtins.str | None = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "file_version", b"file_version", "tensorflow_version", b"tensorflow_version", "tfdbg_run_id", b"tfdbg_run_id"
        ],
    ) -> None: ...

global___DebugMetadata = DebugMetadata

@typing.final
class SourceFile(google.protobuf.message.Message):
    """Content of a source file involved in the execution of the debugged TensorFlow
    program.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FILE_PATH_FIELD_NUMBER: builtins.int
    HOST_NAME_FIELD_NUMBER: builtins.int
    LINES_FIELD_NUMBER: builtins.int
    file_path: builtins.str
    """Path to the file."""
    host_name: builtins.str
    """Name of the host on which the file is located."""
    @property
    def lines(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Line-by-line content of the file."""

    def __init__(
        self,
        *,
        file_path: builtins.str | None = ...,
        host_name: builtins.str | None = ...,
        lines: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing.Literal["file_path", b"file_path", "host_name", b"host_name", "lines", b"lines"]
    ) -> None: ...

global___SourceFile = SourceFile

@typing.final
class StackFrameWithId(google.protobuf.message.Message):
    """A stack frame with ID."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    FILE_LINE_COL_FIELD_NUMBER: builtins.int
    id: builtins.str
    """A unique ID for the stack frame: A UUID-like string."""
    @property
    def file_line_col(self) -> tensorflow.core.framework.graph_debug_info_pb2.GraphDebugInfo.FileLineCol:
        """Stack frame, i.e., a frame of a stack trace, containing information
        regarding the file name, line number, function name, code content
        of the line, and column number (if available).
        """

    def __init__(
        self,
        *,
        id: builtins.str | None = ...,
        file_line_col: tensorflow.core.framework.graph_debug_info_pb2.GraphDebugInfo.FileLineCol | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["file_line_col", b"file_line_col"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["file_line_col", b"file_line_col", "id", b"id"]) -> None: ...

global___StackFrameWithId = StackFrameWithId

@typing.final
class CodeLocation(google.protobuf.message.Message):
    """Code location information: A stack trace with host-name information.
    Instead of encoding the detailed stack trace, this proto refers to IDs of
    stack frames stored as `StackFrameWithId` protos.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOST_NAME_FIELD_NUMBER: builtins.int
    STACK_FRAME_IDS_FIELD_NUMBER: builtins.int
    host_name: builtins.str
    """Host name on which the source files are located."""
    @property
    def stack_frame_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """ID to a stack frame, each of which is pointed to
        by a unique ID. The ordering of the frames is consistent with Python's
        `traceback.extract_tb()`.
        """

    def __init__(
        self,
        *,
        host_name: builtins.str | None = ...,
        stack_frame_ids: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing.Literal["host_name", b"host_name", "stack_frame_ids", b"stack_frame_ids"]
    ) -> None: ...

global___CodeLocation = CodeLocation

@typing.final
class GraphOpCreation(google.protobuf.message.Message):
    """The creation of an op in a TensorFlow Graph (e.g., FuncGraph in TF2)."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OP_TYPE_FIELD_NUMBER: builtins.int
    OP_NAME_FIELD_NUMBER: builtins.int
    GRAPH_NAME_FIELD_NUMBER: builtins.int
    GRAPH_ID_FIELD_NUMBER: builtins.int
    DEVICE_NAME_FIELD_NUMBER: builtins.int
    INPUT_NAMES_FIELD_NUMBER: builtins.int
    NUM_OUTPUTS_FIELD_NUMBER: builtins.int
    CODE_LOCATION_FIELD_NUMBER: builtins.int
    OUTPUT_TENSOR_IDS_FIELD_NUMBER: builtins.int
    op_type: builtins.str
    """Type of the op (e.g., "MatMul")."""
    op_name: builtins.str
    """Name of the op (e.g., "Dense/MatMul_1")."""
    graph_name: builtins.str
    """Name of the graph that the op is a part of (if available)."""
    graph_id: builtins.str
    """Unique ID of the graph (generated by debugger).
    This is the ID of the immediately-enclosing graph.
    """
    device_name: builtins.str
    """Name of the device that the op is assigned to (if available)."""
    num_outputs: builtins.int
    """Number of output tensors emitted by the op."""
    @property
    def input_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Names of the input tensors to the op."""

    @property
    def code_location(self) -> global___CodeLocation:
        """The unique ID for code location (stack trace) of the op's creation."""

    @property
    def output_tensor_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """Unique IDs for the output tensors of this op."""

    def __init__(
        self,
        *,
        op_type: builtins.str | None = ...,
        op_name: builtins.str | None = ...,
        graph_name: builtins.str | None = ...,
        graph_id: builtins.str | None = ...,
        device_name: builtins.str | None = ...,
        input_names: collections.abc.Iterable[builtins.str] | None = ...,
        num_outputs: builtins.int | None = ...,
        code_location: global___CodeLocation | None = ...,
        output_tensor_ids: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["code_location", b"code_location"]) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "code_location",
            b"code_location",
            "device_name",
            b"device_name",
            "graph_id",
            b"graph_id",
            "graph_name",
            b"graph_name",
            "input_names",
            b"input_names",
            "num_outputs",
            b"num_outputs",
            "op_name",
            b"op_name",
            "op_type",
            b"op_type",
            "output_tensor_ids",
            b"output_tensor_ids",
        ],
    ) -> None: ...

global___GraphOpCreation = GraphOpCreation

@typing.final
class DebuggedGraph(google.protobuf.message.Message):
    """A debugger-instrumented graph."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    GRAPH_ID_FIELD_NUMBER: builtins.int
    GRAPH_NAME_FIELD_NUMBER: builtins.int
    INSTRUMENTED_OPS_FIELD_NUMBER: builtins.int
    ORIGINAL_GRAPH_DEF_FIELD_NUMBER: builtins.int
    INSTRUMENTED_GRAPH_DEF_FIELD_NUMBER: builtins.int
    OUTER_CONTEXT_ID_FIELD_NUMBER: builtins.int
    graph_id: builtins.str
    """An ID for the graph.
    This can be used up to look up graph names. Generated by the debugger.
    """
    graph_name: builtins.str
    """Name of the graph (if available)."""
    original_graph_def: builtins.bytes
    """Original (uninstrumented) GraphDef (if available)."""
    instrumented_graph_def: builtins.bytes
    """An encoded version of a GraphDef.
    This graph may include the debugger-inserted ops.
    """
    outer_context_id: builtins.str
    """IDs of the immediate enclosing context (graph), if any."""
    @property
    def instrumented_ops(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Names of the instrumented ops. This can be used to look up op name
        based on the numeric-summary tensors (2nd column).
        """

    def __init__(
        self,
        *,
        graph_id: builtins.str | None = ...,
        graph_name: builtins.str | None = ...,
        instrumented_ops: collections.abc.Iterable[builtins.str] | None = ...,
        original_graph_def: builtins.bytes | None = ...,
        instrumented_graph_def: builtins.bytes | None = ...,
        outer_context_id: builtins.str | None = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "graph_id",
            b"graph_id",
            "graph_name",
            b"graph_name",
            "instrumented_graph_def",
            b"instrumented_graph_def",
            "instrumented_ops",
            b"instrumented_ops",
            "original_graph_def",
            b"original_graph_def",
            "outer_context_id",
            b"outer_context_id",
        ],
    ) -> None: ...

global___DebuggedGraph = DebuggedGraph

@typing.final
class DebuggedDevice(google.protobuf.message.Message):
    """A device on which ops and/or tensors are instrumented by the debugger."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEVICE_NAME_FIELD_NUMBER: builtins.int
    DEVICE_ID_FIELD_NUMBER: builtins.int
    device_name: builtins.str
    """Name of the device."""
    device_id: builtins.int
    """A debugger-generated ID for the device. Guaranteed to be unique within
    the scope of the debugged TensorFlow program, including single-host and
    multi-host settings.
    TODO(cais): Test the uniqueness guarantee in multi-host settings.
    """
    def __init__(
        self,
        *,
        device_name: builtins.str | None = ...,
        device_id: builtins.int | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["device_id", b"device_id", "device_name", b"device_name"]) -> None: ...

global___DebuggedDevice = DebuggedDevice

@typing.final
class Execution(google.protobuf.message.Message):
    """Data relating to the eager execution of an op or a Graph.
    For a op that generates N output tensors (N >= 0), only one
    Execution proto will be used to describe the execution event.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OP_TYPE_FIELD_NUMBER: builtins.int
    NUM_OUTPUTS_FIELD_NUMBER: builtins.int
    GRAPH_ID_FIELD_NUMBER: builtins.int
    INPUT_TENSOR_IDS_FIELD_NUMBER: builtins.int
    OUTPUT_TENSOR_IDS_FIELD_NUMBER: builtins.int
    TENSOR_DEBUG_MODE_FIELD_NUMBER: builtins.int
    TENSOR_PROTOS_FIELD_NUMBER: builtins.int
    CODE_LOCATION_FIELD_NUMBER: builtins.int
    OUTPUT_TENSOR_DEVICE_IDS_FIELD_NUMBER: builtins.int
    op_type: builtins.str
    """Op type (e.g., "MatMul").
    In the case of a Graph, this is the name of the Graph.
    """
    num_outputs: builtins.int
    """Number of output tensors."""
    graph_id: builtins.str
    """The graph that's executed: applicable only to the eager
    execution of a FuncGraph.
    """
    tensor_debug_mode: global___TensorDebugMode.ValueType
    """Type of the tensor value encapsulated in this proto."""
    @property
    def input_tensor_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """IDs of the input tensors (if available)."""

    @property
    def output_tensor_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """IDs of the output tensors (if availbable).
        If specified, must have the same length as tensor_protos.
        """

    @property
    def tensor_protos(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[tensorflow.core.framework.tensor_pb2.TensorProto]:
        """Output Tensor values in the type described by `tensor_value_type`.
        The length of this should match `num_outputs`.
        """

    @property
    def code_location(self) -> global___CodeLocation:
        """Stack trace of the eager execution."""

    @property
    def output_tensor_device_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """Debugged-generated IDs of the devices on which the output tensors reside.
        To look up details about the device (e.g., name), cross-reference this
        field with the DebuggedDevice messages.
        """

    def __init__(
        self,
        *,
        op_type: builtins.str | None = ...,
        num_outputs: builtins.int | None = ...,
        graph_id: builtins.str | None = ...,
        input_tensor_ids: collections.abc.Iterable[builtins.int] | None = ...,
        output_tensor_ids: collections.abc.Iterable[builtins.int] | None = ...,
        tensor_debug_mode: global___TensorDebugMode.ValueType | None = ...,
        tensor_protos: collections.abc.Iterable[tensorflow.core.framework.tensor_pb2.TensorProto] | None = ...,
        code_location: global___CodeLocation | None = ...,
        output_tensor_device_ids: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["code_location", b"code_location"]) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "code_location",
            b"code_location",
            "graph_id",
            b"graph_id",
            "input_tensor_ids",
            b"input_tensor_ids",
            "num_outputs",
            b"num_outputs",
            "op_type",
            b"op_type",
            "output_tensor_device_ids",
            b"output_tensor_device_ids",
            "output_tensor_ids",
            b"output_tensor_ids",
            "tensor_debug_mode",
            b"tensor_debug_mode",
            "tensor_protos",
            b"tensor_protos",
        ],
    ) -> None: ...

global___Execution = Execution

@typing.final
class GraphExecutionTrace(google.protobuf.message.Message):
    """Data relating to an execution of a Graph (e.g., an eager execution of a
    FuncGraph).
    The values of the intermediate tensors computed in the graph are recorded
    in this proto. A graph execution may correspond to one or more pieces of
    `GraphExecutionTrace`, depending on whether the instrumented tensor values
    are summarized in an aggregated or separate fashion.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TFDBG_CONTEXT_ID_FIELD_NUMBER: builtins.int
    OP_NAME_FIELD_NUMBER: builtins.int
    OUTPUT_SLOT_FIELD_NUMBER: builtins.int
    TENSOR_DEBUG_MODE_FIELD_NUMBER: builtins.int
    TENSOR_PROTO_FIELD_NUMBER: builtins.int
    DEVICE_NAME_FIELD_NUMBER: builtins.int
    tfdbg_context_id: builtins.str
    """Unique ID of the context that the executed op(s) belong to (e.g., a
    compiled concrete tf.function).
    """
    op_name: builtins.str
    """Name of the op (applicable only in the case of the `FULL_TENSOR` trace
    level).
    """
    output_slot: builtins.int
    """Output slot of the tensor (applicable only in the case of the `FULL_TENSOR`
    trace level).
    """
    tensor_debug_mode: global___TensorDebugMode.ValueType
    """Type of the tensor value encapsulated in this proto."""
    device_name: builtins.str
    """Name of the device that the op belongs to."""
    @property
    def tensor_proto(self) -> tensorflow.core.framework.tensor_pb2.TensorProto:
        """Tensor value in the type described by `tensor_value_type`.
        This tensor may summarize the value of a single intermediate op of the
        graph, or those of multiple intermediate tensors.
        """

    def __init__(
        self,
        *,
        tfdbg_context_id: builtins.str | None = ...,
        op_name: builtins.str | None = ...,
        output_slot: builtins.int | None = ...,
        tensor_debug_mode: global___TensorDebugMode.ValueType | None = ...,
        tensor_proto: tensorflow.core.framework.tensor_pb2.TensorProto | None = ...,
        device_name: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["tensor_proto", b"tensor_proto"]) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "device_name",
            b"device_name",
            "op_name",
            b"op_name",
            "output_slot",
            b"output_slot",
            "tensor_debug_mode",
            b"tensor_debug_mode",
            "tensor_proto",
            b"tensor_proto",
            "tfdbg_context_id",
            b"tfdbg_context_id",
        ],
    ) -> None: ...

global___GraphExecutionTrace = GraphExecutionTrace
