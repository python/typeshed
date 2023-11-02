"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import sys

import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import tensorflow.core.framework.graph_pb2
import tensorflow.core.framework.op_def_pb2
import tensorflow.core.framework.tensor_shape_pb2
import tensorflow.core.framework.types_pb2
import tensorflow.core.protobuf.saved_object_graph_pb2
import tensorflow.core.protobuf.saver_pb2
import tensorflow.core.protobuf.struct_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class MetaGraphDef(google.protobuf.message.Message):
    """Protocol buffer containing the following which are necessary to restart
    training, run inference. It can be used to serialize/de-serialize memory
    objects necessary for running computation in a graph when crossing the
    process boundary. It can be used for long term storage of graphs,
    cross-language execution of graphs, etc.
      MetaInfoDef
      GraphDef
      SaverDef
      CollectionDef
      TensorInfo
      SignatureDef
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class MetaInfoDef(google.protobuf.message.Message):
        """Meta information regarding the graph to be exported.  To be used by users
        of this protocol buffer to encode information regarding their meta graph.
        """

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        @typing_extensions.final
        class FunctionAliasesEntry(google.protobuf.message.Message):
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

        META_GRAPH_VERSION_FIELD_NUMBER: builtins.int
        STRIPPED_OP_LIST_FIELD_NUMBER: builtins.int
        ANY_INFO_FIELD_NUMBER: builtins.int
        TAGS_FIELD_NUMBER: builtins.int
        TENSORFLOW_VERSION_FIELD_NUMBER: builtins.int
        TENSORFLOW_GIT_VERSION_FIELD_NUMBER: builtins.int
        STRIPPED_DEFAULT_ATTRS_FIELD_NUMBER: builtins.int
        FUNCTION_ALIASES_FIELD_NUMBER: builtins.int
        meta_graph_version: builtins.str
        """User specified Version string. Can be the name of the model and revision,
        steps this model has been trained to, etc.
        """
        @property
        def stripped_op_list(self) -> tensorflow.core.framework.op_def_pb2.OpList:
            """A copy of the OpDefs used by the producer of this graph_def.
            Descriptions and Ops not used in graph_def are stripped out.
            """
        @property
        def any_info(self) -> google.protobuf.any_pb2.Any:
            """A serialized protobuf. Can be the time this meta graph is created, or
            modified, or name of the model.
            """
        @property
        def tags(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
            """User supplied tag(s) on the meta_graph and included graph_def.

            MetaGraphDefs should be tagged with their capabilities or use-cases.
            Examples: "train", "serve", "gpu", "tpu", etc.
            These tags enable loaders to access the MetaGraph(s) appropriate for a
            specific use-case or runtime environment.
            """
        tensorflow_version: builtins.str
        """The __version__ string of the tensorflow build used to write this graph.
        This will be populated by the framework, which will overwrite any user
        supplied value.
        """
        tensorflow_git_version: builtins.str
        """The __git_version__ string of the tensorflow build used to write this
        graph. This will be populated by the framework, which will overwrite any
        user supplied value.
        """
        stripped_default_attrs: builtins.bool
        """A flag to denote whether default-valued attrs have been stripped from
        the nodes in this graph_def.
        """
        @property
        def function_aliases(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
            """FunctionDef name to aliases mapping."""
        def __init__(
            self,
            *,
            meta_graph_version: builtins.str | None = ...,
            stripped_op_list: tensorflow.core.framework.op_def_pb2.OpList | None = ...,
            any_info: google.protobuf.any_pb2.Any | None = ...,
            tags: collections.abc.Iterable[builtins.str] | None = ...,
            tensorflow_version: builtins.str | None = ...,
            tensorflow_git_version: builtins.str | None = ...,
            stripped_default_attrs: builtins.bool | None = ...,
            function_aliases: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["any_info", b"any_info", "stripped_op_list", b"stripped_op_list"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["any_info", b"any_info", "function_aliases", b"function_aliases", "meta_graph_version", b"meta_graph_version", "stripped_default_attrs", b"stripped_default_attrs", "stripped_op_list", b"stripped_op_list", "tags", b"tags", "tensorflow_git_version", b"tensorflow_git_version", "tensorflow_version", b"tensorflow_version"]) -> None: ...

    @typing_extensions.final
    class CollectionDefEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___CollectionDef: ...
        def __init__(
            self,
            *,
            key: builtins.str | None = ...,
            value: global___CollectionDef | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    @typing_extensions.final
    class SignatureDefEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___SignatureDef: ...
        def __init__(
            self,
            *,
            key: builtins.str | None = ...,
            value: global___SignatureDef | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    META_INFO_DEF_FIELD_NUMBER: builtins.int
    GRAPH_DEF_FIELD_NUMBER: builtins.int
    SAVER_DEF_FIELD_NUMBER: builtins.int
    COLLECTION_DEF_FIELD_NUMBER: builtins.int
    SIGNATURE_DEF_FIELD_NUMBER: builtins.int
    ASSET_FILE_DEF_FIELD_NUMBER: builtins.int
    OBJECT_GRAPH_DEF_FIELD_NUMBER: builtins.int
    @property
    def meta_info_def(self) -> global___MetaGraphDef.MetaInfoDef: ...
    @property
    def graph_def(self) -> tensorflow.core.framework.graph_pb2.GraphDef:
        """GraphDef."""
    @property
    def saver_def(self) -> tensorflow.core.protobuf.saver_pb2.SaverDef:
        """SaverDef."""
    @property
    def collection_def(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___CollectionDef]:
        """collection_def: Map from collection name to collections.
        See CollectionDef section for details.
        """
    @property
    def signature_def(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___SignatureDef]:
        """signature_def: Map from user supplied key for a signature to a single
        SignatureDef.
        """
    @property
    def asset_file_def(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AssetFileDef]:
        """Asset file def to be used with the defined graph."""
    @property
    def object_graph_def(self) -> tensorflow.core.protobuf.saved_object_graph_pb2.SavedObjectGraph:
        """Extra information about the structure of functions and stateful objects."""
    def __init__(
        self,
        *,
        meta_info_def: global___MetaGraphDef.MetaInfoDef | None = ...,
        graph_def: tensorflow.core.framework.graph_pb2.GraphDef | None = ...,
        saver_def: tensorflow.core.protobuf.saver_pb2.SaverDef | None = ...,
        collection_def: collections.abc.Mapping[builtins.str, global___CollectionDef] | None = ...,
        signature_def: collections.abc.Mapping[builtins.str, global___SignatureDef] | None = ...,
        asset_file_def: collections.abc.Iterable[global___AssetFileDef] | None = ...,
        object_graph_def: tensorflow.core.protobuf.saved_object_graph_pb2.SavedObjectGraph | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["graph_def", b"graph_def", "meta_info_def", b"meta_info_def", "object_graph_def", b"object_graph_def", "saver_def", b"saver_def"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["asset_file_def", b"asset_file_def", "collection_def", b"collection_def", "graph_def", b"graph_def", "meta_info_def", b"meta_info_def", "object_graph_def", b"object_graph_def", "saver_def", b"saver_def", "signature_def", b"signature_def"]) -> None: ...

global___MetaGraphDef = MetaGraphDef

@typing_extensions.final
class CollectionDef(google.protobuf.message.Message):
    """CollectionDef should cover most collections.
    To add a user-defined collection, do one of the following:
    1. For simple data types, such as string, int, float:
         tf.add_to_collection("your_collection_name", your_simple_value)
       strings will be stored as bytes_list.

    2. For Protobuf types, there are three ways to add them:
       1) tf.add_to_collection("your_collection_name",
            your_proto.SerializeToString())

          collection_def {
            key: "user_defined_bytes_collection"
            value {
              bytes_list {
                value: "queue_name: \\"test_queue\\"\\n"
              }
            }
          }

     or

       2) tf.add_to_collection("your_collection_name", str(your_proto))

          collection_def {
            key: "user_defined_string_collection"
            value {
             bytes_list {
                value: "\\n\\ntest_queue"
              }
            }
          }

     or

       3) any_buf = any_pb2.Any()
          tf.add_to_collection("your_collection_name",
            any_buf.Pack(your_proto))

          collection_def {
            key: "user_defined_any_collection"
            value {
              any_list {
                value {
                  type_url: "type.googleapis.com/tensorflow.QueueRunnerDef"
                  value: "\\n\\ntest_queue"
                }
              }
            }
          }

    3. For Python objects, implement to_proto() and from_proto(), and register
       them in the following manner:
       ops.register_proto_function("your_collection_name",
                                   proto_type,
                                   to_proto=YourPythonObject.to_proto,
                                   from_proto=YourPythonObject.from_proto)
       These functions will be invoked to serialize and de-serialize the
       collection. For example,
       ops.register_proto_function(ops.GraphKeys.GLOBAL_VARIABLES,
                                   proto_type=variable_pb2.VariableDef,
                                   to_proto=Variable.to_proto,
                                   from_proto=Variable.from_proto)
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class NodeList(google.protobuf.message.Message):
        """NodeList is used for collecting nodes in graph. For example
        collection_def {
          key: "summaries"
          value {
            node_list {
              value: "input_producer/ScalarSummary:0"
              value: "shuffle_batch/ScalarSummary:0"
              value: "ImageSummary:0"
            }
          }
        """

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        VALUE_FIELD_NUMBER: builtins.int
        @property
        def value(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
        def __init__(
            self,
            *,
            value: collections.abc.Iterable[builtins.str] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["value", b"value"]) -> None: ...

    @typing_extensions.final
    class BytesList(google.protobuf.message.Message):
        """BytesList is used for collecting strings and serialized protobufs. For
        example:
        collection_def {
          key: "trainable_variables"
          value {
            bytes_list {
              value: "\\n\\017conv1/weights:0\\022\\024conv1/weights/Assign
                     \\032\\024conv1/weights/read:0"
              value: "\\n\\016conv1/biases:0\\022\\023conv1/biases/Assign\\032
                     \\023conv1/biases/read:0"
            }
          }
        }
        """

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        VALUE_FIELD_NUMBER: builtins.int
        @property
        def value(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bytes]: ...
        def __init__(
            self,
            *,
            value: collections.abc.Iterable[builtins.bytes] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["value", b"value"]) -> None: ...

    @typing_extensions.final
    class Int64List(google.protobuf.message.Message):
        """Int64List is used for collecting int, int64 and long values."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        VALUE_FIELD_NUMBER: builtins.int
        @property
        def value(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
        def __init__(
            self,
            *,
            value: collections.abc.Iterable[builtins.int] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["value", b"value"]) -> None: ...

    @typing_extensions.final
    class FloatList(google.protobuf.message.Message):
        """FloatList is used for collecting float values."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        VALUE_FIELD_NUMBER: builtins.int
        @property
        def value(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
        def __init__(
            self,
            *,
            value: collections.abc.Iterable[builtins.float] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["value", b"value"]) -> None: ...

    @typing_extensions.final
    class AnyList(google.protobuf.message.Message):
        """AnyList is used for collecting Any protos."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        VALUE_FIELD_NUMBER: builtins.int
        @property
        def value(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.any_pb2.Any]: ...
        def __init__(
            self,
            *,
            value: collections.abc.Iterable[google.protobuf.any_pb2.Any] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["value", b"value"]) -> None: ...

    NODE_LIST_FIELD_NUMBER: builtins.int
    BYTES_LIST_FIELD_NUMBER: builtins.int
    INT64_LIST_FIELD_NUMBER: builtins.int
    FLOAT_LIST_FIELD_NUMBER: builtins.int
    ANY_LIST_FIELD_NUMBER: builtins.int
    @property
    def node_list(self) -> global___CollectionDef.NodeList: ...
    @property
    def bytes_list(self) -> global___CollectionDef.BytesList: ...
    @property
    def int64_list(self) -> global___CollectionDef.Int64List: ...
    @property
    def float_list(self) -> global___CollectionDef.FloatList: ...
    @property
    def any_list(self) -> global___CollectionDef.AnyList: ...
    def __init__(
        self,
        *,
        node_list: global___CollectionDef.NodeList | None = ...,
        bytes_list: global___CollectionDef.BytesList | None = ...,
        int64_list: global___CollectionDef.Int64List | None = ...,
        float_list: global___CollectionDef.FloatList | None = ...,
        any_list: global___CollectionDef.AnyList | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["any_list", b"any_list", "bytes_list", b"bytes_list", "float_list", b"float_list", "int64_list", b"int64_list", "kind", b"kind", "node_list", b"node_list"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["any_list", b"any_list", "bytes_list", b"bytes_list", "float_list", b"float_list", "int64_list", b"int64_list", "kind", b"kind", "node_list", b"node_list"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["kind", b"kind"]) -> typing_extensions.Literal["node_list", "bytes_list", "int64_list", "float_list", "any_list"] | None: ...

global___CollectionDef = CollectionDef

@typing_extensions.final
class TensorInfo(google.protobuf.message.Message):
    """Information about a Tensor necessary for feeding or retrieval."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class CooSparse(google.protobuf.message.Message):
        """For sparse tensors, The COO encoding stores a triple of values, indices,
        and shape.
        """

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        VALUES_TENSOR_NAME_FIELD_NUMBER: builtins.int
        INDICES_TENSOR_NAME_FIELD_NUMBER: builtins.int
        DENSE_SHAPE_TENSOR_NAME_FIELD_NUMBER: builtins.int
        values_tensor_name: builtins.str
        """The shape of the values Tensor is [?].  Its dtype must be the dtype of
        the SparseTensor as a whole, given in the enclosing TensorInfo.
        """
        indices_tensor_name: builtins.str
        """The indices Tensor must have dtype int64 and shape [?, ?]."""
        dense_shape_tensor_name: builtins.str
        """The dynamic logical shape represented by the SparseTensor is recorded in
        the Tensor referenced here.  It must have dtype int64 and shape [?].
        """
        def __init__(
            self,
            *,
            values_tensor_name: builtins.str | None = ...,
            indices_tensor_name: builtins.str | None = ...,
            dense_shape_tensor_name: builtins.str | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["dense_shape_tensor_name", b"dense_shape_tensor_name", "indices_tensor_name", b"indices_tensor_name", "values_tensor_name", b"values_tensor_name"]) -> None: ...

    @typing_extensions.final
    class CompositeTensor(google.protobuf.message.Message):
        """Generic encoding for composite tensors."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_SPEC_FIELD_NUMBER: builtins.int
        COMPONENTS_FIELD_NUMBER: builtins.int
        @property
        def type_spec(self) -> tensorflow.core.protobuf.struct_pb2.TypeSpecProto:
            """The serialized TypeSpec for the composite tensor."""
        @property
        def components(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TensorInfo]:
            """A TensorInfo for each flattened component tensor."""
        def __init__(
            self,
            *,
            type_spec: tensorflow.core.protobuf.struct_pb2.TypeSpecProto | None = ...,
            components: collections.abc.Iterable[global___TensorInfo] | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["type_spec", b"type_spec"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["components", b"components", "type_spec", b"type_spec"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    COO_SPARSE_FIELD_NUMBER: builtins.int
    COMPOSITE_TENSOR_FIELD_NUMBER: builtins.int
    DTYPE_FIELD_NUMBER: builtins.int
    TENSOR_SHAPE_FIELD_NUMBER: builtins.int
    name: builtins.str
    """For dense `Tensor`s, the name of the tensor in the graph."""
    @property
    def coo_sparse(self) -> global___TensorInfo.CooSparse:
        """There are many possible encodings of sparse matrices
        (https://en.wikipedia.org/wiki/Sparse_matrix).  Currently, TensorFlow
        uses only the COO encoding.  This is supported and documented in the
        SparseTensor Python class.
        """
    @property
    def composite_tensor(self) -> global___TensorInfo.CompositeTensor:
        """Generic encoding for CompositeTensors."""
    dtype: tensorflow.core.framework.types_pb2.DataType.ValueType
    @property
    def tensor_shape(self) -> tensorflow.core.framework.tensor_shape_pb2.TensorShapeProto:
        """The static shape should be recorded here, to the extent that it can
        be known in advance.  In the case of a SparseTensor, this field describes
        the logical shape of the represented tensor (aka dense_shape).
        """
    def __init__(
        self,
        *,
        name: builtins.str | None = ...,
        coo_sparse: global___TensorInfo.CooSparse | None = ...,
        composite_tensor: global___TensorInfo.CompositeTensor | None = ...,
        dtype: tensorflow.core.framework.types_pb2.DataType.ValueType | None = ...,
        tensor_shape: tensorflow.core.framework.tensor_shape_pb2.TensorShapeProto | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["composite_tensor", b"composite_tensor", "coo_sparse", b"coo_sparse", "encoding", b"encoding", "name", b"name", "tensor_shape", b"tensor_shape"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["composite_tensor", b"composite_tensor", "coo_sparse", b"coo_sparse", "dtype", b"dtype", "encoding", b"encoding", "name", b"name", "tensor_shape", b"tensor_shape"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["encoding", b"encoding"]) -> typing_extensions.Literal["name", "coo_sparse", "composite_tensor"] | None: ...

global___TensorInfo = TensorInfo

@typing_extensions.final
class SignatureDef(google.protobuf.message.Message):
    """SignatureDef defines the signature of a computation supported by a TensorFlow
    graph.

    For example, a model with two loss computations, sharing a single input,
    might have the following signature_def map, in a MetaGraphDef message.

    Note that across the two SignatureDefs "loss_A" and "loss_B", the input key,
    output key, and method_name are identical, and will be used by system(s) that
    implement or rely upon this particular loss method. The output tensor names
    differ, demonstrating how different outputs can exist for the same method.

    signature_def {
      key: "loss_A"
      value {
        inputs {
          key: "input"
          value {
            name: "input:0"
            dtype: DT_STRING
            tensor_shape: ...
          }
        }
        outputs {
          key: "loss_output"
          value {
            name: "loss_output_A:0"
            dtype: DT_FLOAT
            tensor_shape: ...
          }
        }
        method_name: "some/package/compute_loss"
      }
      ...
    }
    signature_def {
      key: "loss_B"
      value {
        inputs {
          key: "input"
          value {
            name: "input:0"
            dtype: DT_STRING
            tensor_shape: ...
          }
        }
        outputs {
          key: "loss_output"
          value {
            name: "loss_output_B:0"
            dtype: DT_FLOAT
            tensor_shape: ...
          }
        }
        method_name: "some/package/compute_loss"
      }
      ...
    }
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class InputsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___TensorInfo: ...
        def __init__(
            self,
            *,
            key: builtins.str | None = ...,
            value: global___TensorInfo | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    @typing_extensions.final
    class OutputsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___TensorInfo: ...
        def __init__(
            self,
            *,
            key: builtins.str | None = ...,
            value: global___TensorInfo | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    INPUTS_FIELD_NUMBER: builtins.int
    OUTPUTS_FIELD_NUMBER: builtins.int
    METHOD_NAME_FIELD_NUMBER: builtins.int
    @property
    def inputs(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___TensorInfo]:
        """Named input parameters."""
    @property
    def outputs(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___TensorInfo]:
        """Named output parameters."""
    method_name: builtins.str
    """Extensible method_name information enabling third-party users to mark a
    SignatureDef as supporting a particular method. This enables producers and
    consumers of SignatureDefs, e.g. a model definition library and a serving
    library to have a clear hand-off regarding the semantics of a computation.

    Note that multiple SignatureDefs in a single MetaGraphDef may have the same
    method_name. This is commonly used to support multi-headed computation,
    where a single graph computation may return multiple results.
    """
    def __init__(
        self,
        *,
        inputs: collections.abc.Mapping[builtins.str, global___TensorInfo] | None = ...,
        outputs: collections.abc.Mapping[builtins.str, global___TensorInfo] | None = ...,
        method_name: builtins.str | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["inputs", b"inputs", "method_name", b"method_name", "outputs", b"outputs"]) -> None: ...

global___SignatureDef = SignatureDef

@typing_extensions.final
class AssetFileDef(google.protobuf.message.Message):
    """An asset file def for a single file or a set of sharded files with the same
    name.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TENSOR_INFO_FIELD_NUMBER: builtins.int
    FILENAME_FIELD_NUMBER: builtins.int
    @property
    def tensor_info(self) -> global___TensorInfo:
        """The tensor to bind the asset filename to."""
    filename: builtins.str
    """The filename within an assets directory. Note: does not include the path
    prefix, i.e. directories. For an asset at /tmp/path/vocab.txt, the filename
    would be "vocab.txt".
    """
    def __init__(
        self,
        *,
        tensor_info: global___TensorInfo | None = ...,
        filename: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["tensor_info", b"tensor_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["filename", b"filename", "tensor_info", b"tensor_info"]) -> None: ...

global___AssetFileDef = AssetFileDef
