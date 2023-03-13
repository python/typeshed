#!/bin/bash
set -euxo pipefail

# Partly based on scripts/generate_proto_stubs.sh.

# Generates the protobuf stubs for the given tensorflow version using
# mypy-protobuf. Should be run like ./sync_protobuf_stubs.sh 2.11.0.
# Generally, new minor versions are a good time to update the stubs.
cd "$(dirname "$0")" > /dev/null
REPO_ROOT="$(realpath "$(dirname "${BASH_SOURCE[0]}")"/../..)"


# This version should be consistent with the version in METADATA.toml.
TENSORFLOW_VERSION=2.11.0
MYPY_PROTOBUF_VERSION=3.4.0

pip install mypy-protobuf=="$MYPY_PROTOBUF_VERSION"

mkdir repository
pushd repository &> /dev/null
    git clone https://github.com/tensorflow/tensorflow.git
    pushd tensorflow &> /dev/null
        git checkout v"$TENSORFLOW_VERSION"

        # Folders here cover the more commonly used protobufs externally and
        # there dependencies. Tensorflow has more protobufs and can be added if requested.
        protoc --mypy_out "relax_strict_optional_primitives:$REPO_ROOT/stubs/tensorflow" \
            tensorflow/core/protobuf/*.proto \
            tensorflow/core/protobuf/tpu/*.proto \
            tensorflow/core/framework/*.proto \
            tensorflow/core/util/*.proto \
            tensorflow/core/example/*.proto \
            tensorflow/python/keras/protobuf/*.proto \
            tensorflow/tsl/protobuf/*.proto \
            tensorflow/compiler/xla/*.proto \
            tensorflow/compiler/xla/stream_executor/*.proto \
            tensorflow/compiler/xla/service/*.proto \
            tensorflow/compiler/xla/pjrt/*.proto \
            tensorflow/compiler/xla/pjrt/distributed/*.proto
    popd &> /dev/null
popd &> /dev/null

rm -rf repository/
