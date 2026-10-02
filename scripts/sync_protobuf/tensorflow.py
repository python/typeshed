#!/usr/bin/env python3
"""
Generates the protobuf stubs for the given tensorflow version using mypy-protobuf.
Generally, new minor versions are a good time to update the stubs.
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from _utils import MYPY_PROTOBUF_VERSION, download_file, extract_archive, run_protoc
from ts_utils.metadata import read_metadata, update_metadata
from ts_utils.paths import distribution_path

PACKAGE_VERSION = read_metadata("tensorflow").version_spec.version

STUBS_FOLDER = distribution_path("tensorflow").absolute()
ARCHIVE_FILENAME = f"v{PACKAGE_VERSION}.zip"
ARCHIVE_URL = f"https://github.com/tensorflow/tensorflow/archive/refs/tags/{ARCHIVE_FILENAME}"
EXTRACTED_PACKAGE_DIR = f"tensorflow-{PACKAGE_VERSION}"

PROTOS_TO_REMOVE = (
    "compiler/xla/shape_util_pb2.pyi",
    "compiler/xla/xla_pb2.pyi",
    "compiler/xla/service/gpu_topology_pb2.pyi",
    "compiler/xla/service/hlo_profile_printer_data_pb2.pyi",
    "compiler/xla/service/xla_compile_result_pb2.pyi",
    "compiler/xla/service/test_compilation_environment_pb2.pyi",
    "compiler/xla/service/shaped_slice_pb2.pyi",
    "compiler/xla/tsl/protobuf/coordination_service_pb2.pyi",
    "compiler/xla/tsl/protobuf/dnn_pb2.pyi",
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


def move_tree(source: Path, destination: Path) -> None:
    """Move directory and merge if destination already exists.

    Can't use shutil.move because it can't merge existing directories.
    """
    print(f"Moving '{source}' to '{destination}'")
    shutil.copytree(source, destination, dirs_exist_ok=True)
    shutil.rmtree(source)


def post_creation() -> None:
    """Move third-party and fix imports."""
    print()
    move_tree(STUBS_FOLDER / "xla", STUBS_FOLDER / "tensorflow" / "compiler" / "xla")

    for path in STUBS_FOLDER.rglob("*_pb2.pyi"):
        print(f"Fixing imports in '{path}'")
        filedata = path.read_text(encoding="utf-8").replace("\N{RIGHT SINGLE QUOTATION MARK}", "'")

        filedata = filedata.replace("from xla import", "from tensorflow.compiler.xla import")

        # Replace the target string
        filedata = re.sub(TSL_IMPORT_PATTERN, "\\1tensorflow.tsl.", filedata)
        filedata = re.sub(XLA_IMPORT_PATTERN, "\\1tensorflow.compiler.xla.", filedata)

        # Write the file out again
        path.write_text(filedata, encoding="utf-8")

    print()
    for to_remove in PROTOS_TO_REMOVE:
        file_path = STUBS_FOLDER / "tensorflow" / to_remove
        file_path.unlink(missing_ok=True)
        print(f"Removed '{file_path}'")

    for path in STUBS_FOLDER.rglob("*_pb2.pyi"):
        for parent in path.parents:
            if parent == STUBS_FOLDER:
                break
            (parent / "__init__.pyi").touch(exist_ok=True)


def main() -> None:
    temp_dir = Path(tempfile.mkdtemp())
    # Fetch tensorflow (which contains all the .proto files)
    archive_path = temp_dir / ARCHIVE_FILENAME
    download_file(ARCHIVE_URL, archive_path)
    extract_archive(archive_path, temp_dir)

    # Remove existing pyi
    for old_stub in STUBS_FOLDER.rglob("*_pb2.pyi"):
        old_stub.unlink()

    obsolete_dir = STUBS_FOLDER / "tensorflow" / "tsl" / "protobuf"
    if obsolete_dir.exists():
        obsolete_dir.rmdir()

    protoc_version = run_protoc(
        proto_paths=(f"{EXTRACTED_PACKAGE_DIR}/third_party/xla", f"{EXTRACTED_PACKAGE_DIR}"),
        mypy_out=STUBS_FOLDER,
        proto_globs=sorted(
            str(path.relative_to(temp_dir))
            for pattern in (
                f"{EXTRACTED_PACKAGE_DIR}/third_party/xla/xla/*.proto",
                f"{EXTRACTED_PACKAGE_DIR}/third_party/xla/xla/service/*.proto",
                f"{EXTRACTED_PACKAGE_DIR}/third_party/xla/xla/tsl/protobuf/*.proto",
                f"{EXTRACTED_PACKAGE_DIR}/tensorflow/core/example/*.proto",
                f"{EXTRACTED_PACKAGE_DIR}/tensorflow/core/framework/*.proto",
                f"{EXTRACTED_PACKAGE_DIR}/tensorflow/core/protobuf/*.proto",
                f"{EXTRACTED_PACKAGE_DIR}/tensorflow/core/protobuf/tpu/*.proto",
                f"{EXTRACTED_PACKAGE_DIR}/tensorflow/core/util/*.proto",
                f"{EXTRACTED_PACKAGE_DIR}/tensorflow/python/keras/protobuf/*.proto",
            )
            for path in temp_dir.glob(pattern)
        ),
        cwd=temp_dir,
    )

    # Cleanup after ourselves, this is a temp dir, but it can still grow fast if run multiple times
    shutil.rmtree(temp_dir)

    post_creation()

    update_metadata(
        "tensorflow",
        extra_description=f"""Partially generated using \
[mypy-protobuf=={MYPY_PROTOBUF_VERSION}](https://github.com/nipunn1313/mypy-protobuf/tree/v{MYPY_PROTOBUF_VERSION}) \
and {protoc_version} on `tensorflow=={PACKAGE_VERSION}`.""",
    )
    print("Updated tensorflow/METADATA.toml")

    # Run pre-commit to cleanup the stubs
    subprocess.run((sys.executable, "-m", "pre_commit", "run", "--files", *STUBS_FOLDER.rglob("*_pb2.pyi")), check=False)


if __name__ == "__main__":
    main()
