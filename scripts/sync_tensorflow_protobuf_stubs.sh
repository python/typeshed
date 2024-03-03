#!/bin/bash
set -euxo pipefail

# Partly based on scripts/generate_proto_stubs.sh.

# Generates the protobuf stubs for the given tensorflow version using mypy-protobuf.
# Generally, new minor versions are a good time to update the stubs.
REPO_ROOT="$(realpath "$(dirname "${BASH_SOURCE[0]}")"/..)"

# This version should be consistent with the version in tensorflow's METADATA.toml.
TENSORFLOW_VERSION=2.12.1
# Latest mypy-protobuf has dependency on protobuf >4, which is incompatible at runtime
# with tensorflow. However, the stubs produced do still work with tensorflow. So after
# installing mypy-protobuf, before running stubtest on tensorflow you should downgrade
# protobuf<4.
MYPY_PROTOBUF_VERSION=3.5.0

pip install pre-commit mypy-protobuf=="$MYPY_PROTOBUF_VERSION"

cd "$(dirname "$0")" > /dev/null
cd ../stubs/tensorflow
mkdir -p repository
pushd repository &> /dev/null
    # If the script fails halfway, it's nice to be able to re-run it immediately
    if [ ! -d "tensorflow" ] ; then
        git clone --depth 1 --branch v"$TENSORFLOW_VERSION" https://github.com/tensorflow/tensorflow.git
    fi
    pushd tensorflow &> /dev/null
        # Folders here cover the more commonly used protobufs externally and
        # their dependencies. Tensorflow has more protobufs and can be added if requested.
        protoc --mypy_out "relax_strict_optional_primitives:$REPO_ROOT/stubs/tensorflow" \
            tensorflow/compiler/xla/*.proto \
            tensorflow/compiler/xla/service/*.proto \
            tensorflow/core/example/*.proto \
            tensorflow/core/framework/*.proto \
            tensorflow/core/protobuf/*.proto \
            tensorflow/core/protobuf/tpu/*.proto \
            tensorflow/core/util/*.proto \
            tensorflow/python/keras/protobuf/*.proto \
            tensorflow/tsl/protobuf/*.proto
    popd &> /dev/null
popd &> /dev/null

# These protos exist in a folder with protos used in python, but are not
# included in the python wheel. They are likely only used for other
# language builds. stubtest was used to identify them by looking for
# ModuleNotFoundError.
rm tensorflow/compiler/xla/service/hlo_execution_profile_data_pb2.pyi \
   tensorflow/compiler/xla/service/hlo_profile_printer_data_pb2.pyi \
   tensorflow/compiler/xla/service/test_compilation_environment_pb2.pyi \
   tensorflow/compiler/xla/xla_pb2.pyi \
   tensorflow/core/protobuf/autotuning_pb2.pyi \
   tensorflow/core/protobuf/conv_autotuning_pb2.pyi \
   tensorflow/core/protobuf/critical_section_pb2.pyi \
   tensorflow/core/protobuf/eager_service_pb2.pyi \
   tensorflow/core/protobuf/master_pb2.pyi \
   tensorflow/core/protobuf/master_service_pb2.pyi \
   tensorflow/core/protobuf/replay_log_pb2.pyi \
   tensorflow/core/protobuf/tpu/compile_metadata_pb2.pyi \
   tensorflow/core/protobuf/worker_pb2.pyi \
   tensorflow/core/protobuf/worker_service_pb2.pyi \
   tensorflow/core/util/example_proto_fast_parsing_test_pb2.pyi

# use `|| true` so the script still continues even if a pre-commit hook
# applies autofixes (which will result in a nonzero exit code)
pre-commit run --files "$REPO_ROOT/stubs/tensorflow/tensorflow" || true

sed --in-place="" \
    "s/extra_description = .*$/extra_description = \"Partially generated using [mypy-protobuf==$MYPY_PROTOBUF_VERSION](https:\/\/github.com\/nipunn1313\/mypy-protobuf\/tree\/v$MYPY_PROTOBUF_VERSION) on tensorflow==$TENSORFLOW_VERSION\"/" \
    "$REPO_ROOT/stubs/tensorflow/METADATA.toml"

# Cleanup last. If the script fails halfway, it's nice to be able to re-run it immediately
rm -rf repository/
