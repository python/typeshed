#!/usr/bin/env bash
# Some of the proto .pyi stubs in stubs/protobuf/
# are autogenerated using the mypy-protobuf project on the
# latest `.proto` files shipped with protoc.

set -ex -o pipefail

# When run, this script will autogenerate the _pb2.pyi stubs to
# stubs/protobuf. It should be run any time there's
# a meaningful update to either PROTOBUF_VERSION or MYPY_PROTOBUF_VERSION,
# followed by committing the changes to typeshed
#
# Update these two variables when rerunning script
PROTOBUF_VERSION=21.8
PYTHON_PROTOBUF_VERSION=4.21.8
MYPY_PROTOBUF_VERSION=v3.4.0

if uname -a | grep Darwin; then
    # brew install coreutils wget
    PLAT=osx
else
    PLAT=linux
fi
REPO_ROOT="$(realpath "$(dirname "${BASH_SOURCE[0]}")"/..)"
TMP_DIR="$(mktemp -d)"
PYTHON_PROTOBUF_FILENAME="protobuf-python-${PYTHON_PROTOBUF_VERSION}.zip"
PROTOC_FILENAME="protoc-${PROTOBUF_VERSION}-${PLAT}-x86_64.zip"
PROTOC_URL="https://github.com/protocolbuffers/protobuf/releases/download/v${PROTOBUF_VERSION}/$PROTOC_FILENAME"
PYTHON_PROTOBUF_URL="https://github.com/protocolbuffers/protobuf/releases/download/v${PROTOBUF_VERSION}/$PYTHON_PROTOBUF_FILENAME"

cd "$TMP_DIR"
echo "Working in $TMP_DIR"

# Install protoc
wget "$PROTOC_URL"
mkdir protoc_install
unzip "$PROTOC_FILENAME" -d protoc_install

# Fetch protoc-python (which contains all the .proto files)
wget "$PYTHON_PROTOBUF_URL"
unzip "$PYTHON_PROTOBUF_FILENAME"
PYTHON_PROTOBUF_DIR="protobuf-$PYTHON_PROTOBUF_VERSION"

# Prepare virtualenv
VENV=venv
python3 -m venv "$VENV"
source "$VENV/bin/activate"
pip install -r "$REPO_ROOT/requirements-tests.txt"  # for black and Ruff

# Install mypy-protobuf
pip install "git+https://github.com/dropbox/mypy-protobuf@$MYPY_PROTOBUF_VERSION"

# Remove existing pyi
find "$REPO_ROOT/stubs/protobuf/" -name '*_pb2.pyi' -delete

# Roughly reproduce the subset of .proto files on the public interface as described
# by find_package_modules in the protobuf setup.py.
# The logic (as of 3.20.1) can roughly be described as a allowlist of .proto files
# further limited to exclude *test* and internal/
# https://github.com/protocolbuffers/protobuf/blob/master/python/setup.py
PROTO_FILES=$(grep "GenProto.*google" $PYTHON_PROTOBUF_DIR/python/setup.py | \
    cut -d\' -f2 | \
    grep -v "test" | \
    grep -v google/protobuf/internal/ | \
    grep -v google/protobuf/pyext/python.proto | \
    grep -v src/google/protobuf/util/json_format.proto | \
    grep -v src/google/protobuf/util/json_format_proto3.proto | \
    sed "s:^:$PYTHON_PROTOBUF_DIR/python/:" | \
    xargs -L1 realpath --relative-to=. \
)

# And regenerate!
# shellcheck disable=SC2086
protoc_install/bin/protoc --proto_path="$PYTHON_PROTOBUF_DIR/src" --mypy_out="relax_strict_optional_primitives:$REPO_ROOT/stubs/protobuf" $PROTO_FILES

ruff "$REPO_ROOT/stubs/protobuf" --exit-non-zero-on-fix --fix-only
black "$REPO_ROOT/stubs/protobuf"

sed -i "" "s/mypy-protobuf [^\"]*/mypy-protobuf ${MYPY_PROTOBUF_VERSION}/" "$REPO_ROOT/stubs/protobuf/METADATA.toml"
sed -i "" "s/version = .*$/version = \"$(echo ${PYTHON_PROTOBUF_VERSION} | cut -d. -f1-2)\.\*\"/" "$REPO_ROOT/stubs/protobuf/METADATA.toml"
