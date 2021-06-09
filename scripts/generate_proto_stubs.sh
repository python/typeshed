#!/bin/bash
# Some of the proto .pyi stubs in stubs/protobuf/
# are autogenerated using the mypy-protobuf project on the
# latest `.proto` files shipped with protoc.
#
# When run, this script will autogenerate the _pb2.pyi stubs to
# stubs/protobuf. It should be run any time there's
# a meaningful update to either PROTOBUF_VERSION or MYPY_PROTOBUF_VERSION,
# followed by committing the changes to typeshed
#
# Update these two variables when rerunning script
PROTOBUF_VERSION=3.14.0
MYPY_PROTOBUF_VERSION=v1.24

set -ex

if uname -a | grep Darwin; then
    PLAT=osx
else
    PLAT=linux
fi
REPO_ROOT=$(realpath $(dirname "${BASH_SOURCE[0]}")/..)
TMP_DIR=$(mktemp -d)
PYTHON_PROTOBUF_FILENAME=protobuf-python-${PROTOBUF_VERSION}.zip
PROTOC_FILENAME=protoc-${PROTOBUF_VERSION}-${PLAT}-x86_64.zip
PROTOC_URL=https://github.com/protocolbuffers/protobuf/releases/download/v${PROTOBUF_VERSION}/${PROTOC_FILENAME}
PYTHON_PROTOBUF_URL=https://github.com/protocolbuffers/protobuf/releases/download/v${PROTOBUF_VERSION}/${PYTHON_PROTOBUF_FILENAME}

cd $TMP_DIR
echo "Working in $TMP_DIR"

# Install protoc
wget $PROTOC_URL
mkdir protoc_install
unzip $PROTOC_FILENAME -d protoc_install

# Fetch protoc-python (which contains all the .proto files)
wget $PYTHON_PROTOBUF_URL
unzip $PYTHON_PROTOBUF_FILENAME
PYTHON_PROTOBUF_DIR=protobuf-$PROTOBUF_VERSION

# Install mypy-protobuf
VENV=venv
python3 -m venv $VENV
source $VENV/bin/activate
python3 -m pip install git+https://github.com/dropbox/mypy-protobuf@${MYPY_PROTOBUF_VERSION}#subdirectory=python

# Remove existing pyi
find $REPO_ROOT/stubs/protobuf/ -name "*_pb2.pyi" -delete

# Roughly reproduce the subset of .proto files on the public interface as described
# by find_package_modules in the protobuf setup.py.
# The logic (as of 3.14.0) can roughly be described as a whitelist of .proto files
# further limited to exclude *test* and internal/
# https://github.com/protocolbuffers/protobuf/blob/master/python/setup.py
PROTO_FILES=$(grep "generate_proto.*google" $PYTHON_PROTOBUF_DIR/python/setup.py | \
    cut -d\" -f2 | \
    grep -v "test" | \
    grep -v google/protobuf/internal/ | \
    grep -v google/protobuf/pyext/python.proto | \
    grep -v src/google/protobuf/util/json_format.proto | \
    grep -v src/google/protobuf/util/json_format_proto3.proto | \
    sed "s:^:$PYTHON_PROTOBUF_DIR/python/:" | \
    xargs -L1 realpath --relative-to=. \
)

# And regenerate!
protoc_install/bin/protoc --proto_path=$PYTHON_PROTOBUF_DIR/src --mypy_out=$REPO_ROOT/stubs/protobuf $PROTO_FILES
isort $REPO_ROOT/stubs/protobuf
black $REPO_ROOT/stubs/protobuf
