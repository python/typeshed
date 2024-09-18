from __future__ import annotations

import subprocess
import sys
from http.client import HTTPResponse
from pathlib import Path
from typing import TYPE_CHECKING, Iterable
from urllib.request import urlopen
from zipfile import ZipFile

import tomlkit
from mypy_protobuf.main import (  # type: ignore[import-untyped]  # pyright: ignore[reportMissingTypeStubs]
    __version__ as mypy_protobuf__version__,
)

if TYPE_CHECKING:
    from _typeshed import StrOrBytesPath, StrPath

REPO_ROOT = Path(__file__).absolute().parent.parent.parent
MYPY_PROTOBUF_VERSION = mypy_protobuf__version__


def download_file(url: str, destination: StrPath) -> None:
    print(f"Downloading '{url}' to '{destination}'")
    resp: HTTPResponse
    with urlopen(url) as resp:
        if resp.getcode() != 200:
            raise RuntimeError(f"Error downloading {url}")
        with open(destination, "wb") as file:
            file.write(resp.read())


def extract_archive(archive_path: StrPath, destination: StrPath) -> None:
    print(f"Extracting '{archive_path}' to '{destination}'")
    with ZipFile(archive_path) as file_in:
        file_in.extractall(destination)


def update_metadata(metadata_folder: StrPath, new_extra_description: str) -> None:
    metadata_path = Path(metadata_folder) / "METADATA.toml"
    with open(metadata_path) as file:
        metadata = tomlkit.load(file)
    metadata["extra_description"] = new_extra_description
    with open(metadata_path, "w") as file:
        # tomlkit.dump has partially unknown IO type
        tomlkit.dump(metadata, file)  # pyright: ignore[reportUnknownMemberType]
    print(f"Updated {metadata_path}")


def run_protoc(
    proto_paths: Iterable[StrPath], mypy_out: StrPath, proto_globs: Iterable[str], cwd: StrOrBytesPath | None = None
) -> str:
    """TODO: Describe parameters and return"""
    protoc_version = (
        subprocess.run([sys.executable, "-m", "grpc_tools.protoc", "--version"], capture_output=True).stdout.decode().strip()
    )
    print()
    print(protoc_version)
    protoc_args = [
        *[f"--proto_path={proto_path}" for proto_path in proto_paths],
        "--mypy_out",
        f"relax_strict_optional_primitives:{mypy_out}",
        *proto_globs,
    ]
    print("Running: protoc\n    " + "\n    ".join(protoc_args) + "\n")
    subprocess.run((sys.executable, "-m", "grpc_tools.protoc", *protoc_args), cwd=cwd, check=True)
    return protoc_version
