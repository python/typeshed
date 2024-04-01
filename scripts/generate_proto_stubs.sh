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
# Whenever you update PROTOBUF_VERSION here, version should be updated
# in stubs/protobuf/METADATA.toml and vice-versa.
#
# Update these two variables when rerunning script
PROTOBUF_VERSION=25.3
MYPY_PROTOBUF_VERSION=3.5.0

if uname -a | grep Darwin; then
    # brew install coreutils wget
    PLAT=osx
else
    PLAT=linux
fi
REPO_ROOT="$(realpath "$(dirname "${BASH_SOURCE[0]}")"/..)"
TMP_DIR="$(mktemp -d)"
PYTHON_PROTOBUF_FILENAME="protobuf-$PROTOBUF_VERSION.zip"
PROTOC_FILENAME="protoc-$PROTOBUF_VERSION-$PLAT-x86_64.zip"
PROTOC_URL="https://github.com/protocolbuffers/protobuf/releases/download/v$PROTOBUF_VERSION/$PROTOC_FILENAME"
PYTHON_PROTOBUF_URL="https://github.com/protocolbuffers/protobuf/releases/download/v$PROTOBUF_VERSION/$PYTHON_PROTOBUF_FILENAME"

cd "$TMP_DIR"
echo "Working in $TMP_DIR"

# Install protoc
wget "$PROTOC_URL"
mkdir protoc_install
unzip "$PROTOC_FILENAME" -d protoc_install

# Fetch protoc-python (which contains all the .proto files)
wget "$PYTHON_PROTOBUF_URL"
unzip "$PYTHON_PROTOBUF_FILENAME"
PYTHON_PROTOBUF_DIR="protobuf-$PROTOBUF_VERSION"

# Prepare virtualenv
uv venv .venv
source .venv/bin/activate
uv pip install pre-commit mypy-protobuf=="$MYPY_PROTOBUF_VERSION"

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

PYTHON_PROTOBUF_VERSION=$(jq -r '.[] | .languages.python' "$PYTHON_PROTOBUF_DIR/version.json")

sed --in-place="" \
  "s/extra_description = .*$/extra_description = \"Generated using [mypy-protobuf==$MYPY_PROTOBUF_VERSION](https:\/\/github.com\/nipunn1313\/mypy-protobuf\/tree\/v$MYPY_PROTOBUF_VERSION) on [protobuf v$PROTOBUF_VERSION](https:\/\/github.com\/protocolbuffers\/protobuf\/releases\/tag\/v$PROTOBUF_VERSION) (python protobuf==$PYTHON_PROTOBUF_VERSION)\"/" \
  "$REPO_ROOT/stubs/protobuf/METADATA.toml"

# Must be run in a git repository
cd $REPO_ROOT
# use `|| true` so the script still continues even if a pre-commit hook
# applies autofixes (which will result in a nonzero exit code)
pre-commit run --files $(git ls-files -- "$REPO_ROOT/stubs/protobuf/**.pyi") || true
# Ruff takes two passes to fix everything, re-running all of pre-commit is *slow*
# and we don't need --unsafe-fixes to remove imports
ruff check "$REPO_ROOT/stubs/protobuf" --fix --exit-zero
