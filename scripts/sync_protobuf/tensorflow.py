"""
Generates the protobuf stubs for the given tensorflow version using mypy-protobuf.
Generally, new minor versions are a good time to update the stubs.
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from _utils import MYPY_PROTOBUF_VERSION, REPO_ROOT, download_file, extract_archive, run_protoc, update_metadata

# Whenever you update PACKAGE_VERSION here, version should be updated
# in stubs/tensorflow/METADATA.toml and vice-versa.
PACKAGE_VERSION = "2.17.0"

STUBS_FOLDER = REPO_ROOT / "stubs" / "tensorflow"
ARCHIVE_FILENAME = f"v{PACKAGE_VERSION}.zip"
ARCHIVE_URL = f"https://github.com/tensorflow/tensorflow/archive/refs/tags/{ARCHIVE_FILENAME}"
EXTRACTED_PACKAGE_DIR = f"tensorflow-{PACKAGE_VERSION}"

PROTOS_TO_REMOVE = (
    "compiler/xla/autotune_results_pb2.pyi",
    "compiler/xla/autotuning_pb2.pyi",
    "compiler/xla/service/buffer_assignment_pb2.pyi",
    "compiler/xla/service/hlo_execution_profile_data_pb2.pyi",
    "core/protobuf/autotuning_pb2.pyi",
    "core/protobuf/conv_autotuning_pb2.pyi",
    "core/protobuf/critical_section_pb2.pyi",
    "core/protobuf/eager_service_pb2.pyi",
    "core/protobuf/master_pb2.pyi",
    "core/protobuf/master_service_pb2.pyi",
    "core/protobuf/replay_log_pb2.pyi",
    "core/protobuf/tpu/compile_metadata_pb2.pyi",
    "core/protobuf/worker_pb2.pyi",
    "core/protobuf/worker_service_pb2.pyi",
    "core/util/example_proto_fast_parsing_test_pb2.pyi",
)
"""
These protos exist in a folder with protos used in python,
but are not included in the python wheel.
They are likely only used for other language builds.
stubtest was used to identify them by looking for ModuleNotFoundError.
(comment out ".*_pb2.*" from the allowlist)
"""

TSL_IMPORT_PATTERN = re.compile(r"(\[|\s)tsl\.")
XLA_IMPORT_PATTERN = re.compile(r"(\[|\s)xla\.")


def post_creation() -> None:
    """Move third-party and fix imports"""
    # Can't use shutil.move because it can't merge existing directories.
    print()
    print(f"Moving '{STUBS_FOLDER}/tsl' to '{STUBS_FOLDER}/tensorflow/tsl'")
    shutil.copytree(f"{STUBS_FOLDER}/tsl", f"{STUBS_FOLDER}/tensorflow/tsl", dirs_exist_ok=True)
    shutil.rmtree(f"{STUBS_FOLDER}/tsl")

    print(f"Moving '{STUBS_FOLDER}/xla' to '{STUBS_FOLDER}/tensorflow/compiler/xla'")
    shutil.copytree(f"{STUBS_FOLDER}/xla", f"{STUBS_FOLDER}/tensorflow/compiler/xla", dirs_exist_ok=True)
    shutil.rmtree(f"{STUBS_FOLDER}/xla")

    for path in STUBS_FOLDER.rglob("*_pb2.pyi"):
        print(f"Fixing imports in '{path}'")
        with open(path) as file:
            filedata = file.read()

        # Replace the target string
        filedata = re.sub(TSL_IMPORT_PATTERN, "\\1tensorflow.tsl.", filedata)
        filedata = re.sub(XLA_IMPORT_PATTERN, "\\1tensorflow.compiler.xla.", filedata)

        # Write the file out again
        with open(path, "w") as file:
            file.write(filedata)

    print()
    for to_remove in PROTOS_TO_REMOVE:
        file_path = STUBS_FOLDER / "tensorflow" / to_remove
        os.remove(file_path)
        print(f"Removed '{file_path}'")


def main() -> None:
    temp_dir = Path(tempfile.mkdtemp())
    # Fetch tensorflow (which contains all the .proto files)
    archive_path = temp_dir / ARCHIVE_FILENAME
    download_file(ARCHIVE_URL, archive_path)
    extract_archive(archive_path, temp_dir)

    # Remove existing pyi
    for old_stub in STUBS_FOLDER.rglob("*_pb2.pyi"):
        old_stub.unlink()

    PROTOC_VERSION = run_protoc(
        proto_paths=(
            f"{EXTRACTED_PACKAGE_DIR}/third_party/xla/third_party/tsl",
            f"{EXTRACTED_PACKAGE_DIR}/third_party/xla",
            f"{EXTRACTED_PACKAGE_DIR}",
        ),
        mypy_out=STUBS_FOLDER,
        proto_globs=(
            f"{EXTRACTED_PACKAGE_DIR}/third_party/xla/xla/*.proto",
            f"{EXTRACTED_PACKAGE_DIR}/third_party/xla/xla/service/*.proto",
            f"{EXTRACTED_PACKAGE_DIR}/tensorflow/core/example/*.proto",
            f"{EXTRACTED_PACKAGE_DIR}/tensorflow/core/framework/*.proto",
            f"{EXTRACTED_PACKAGE_DIR}/tensorflow/core/protobuf/*.proto",
            f"{EXTRACTED_PACKAGE_DIR}/tensorflow/core/protobuf/tpu/*.proto",
            f"{EXTRACTED_PACKAGE_DIR}/tensorflow/core/util/*.proto",
            f"{EXTRACTED_PACKAGE_DIR}/tensorflow/python/keras/protobuf/*.proto",
            f"{EXTRACTED_PACKAGE_DIR}/third_party/xla/third_party/tsl/tsl/protobuf/*.proto",
        ),
        cwd=temp_dir,
    )

    # Cleanup after ourselves, this is a temp dir, but it can still grow fast if run multiple times
    shutil.rmtree(temp_dir)

    post_creation()

    update_metadata(
        STUBS_FOLDER,
        f"""Partially generated using \
[mypy-protobuf=={MYPY_PROTOBUF_VERSION}](https://github.com/nipunn1313/mypy-protobuf/tree/v{MYPY_PROTOBUF_VERSION}) \
and {PROTOC_VERSION} on `tensorflow=={PACKAGE_VERSION}`.""",
    )

    # Run pre-commit to cleanup the stubs
    subprocess.run((sys.executable, "-m", "pre_commit", "run", "--files", *STUBS_FOLDER.rglob("*_pb2.pyi")))


if __name__ == "__main__":
    main()
