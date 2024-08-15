from __future__ import annotations

import subprocess
import sys
import zipfile
from pathlib import Path
from typing import TYPE_CHECKING, Iterable

import requests
import tomlkit

if TYPE_CHECKING:
    from _typeshed import FileDescriptorOrPath, StrOrBytesPath, StrPath

REPO_ROOT = Path(__file__).absolute().parent.parent.parent


def download_file(url: str | bytes, destination: FileDescriptorOrPath) -> None:
    print(f"Downloading {url!r} to '{destination}'")
    resp = requests.get(url, stream=True)
    if resp.status_code != 200:
        raise RuntimeError(f"Error downloading {url}")
    with open(destination, "wb") as file:
        file.write(resp.raw.read())


def extract_archive(archive_path: StrPath, destination: StrPath) -> None:
    print(f"Extracting '{archive_path}' to '{destination}'")
    with zipfile.ZipFile(archive_path) as file_in:
        file_in.extractall(destination)


def update_metadata(metadata_folder: StrPath, new_extra_description: str) -> None:
    metadata_path = Path(metadata_folder) / "METADATA.toml"
    with open(metadata_path) as file:
        metadata = tomlkit.load(file)
    metadata["extra_description"] = new_extra_description
    with open(metadata_path, "w") as file:
        tomlkit.dump(metadata, file)
    print(f"Updated {metadata_path}")


def run_protoc(
    proto_paths: Iterable[StrPath], stubs_folder: StrPath, proto_globs: Iterable[str], cwd: StrOrBytesPath | None = None
) -> str:
    """TODO: Describe parameters and return"""
    protoc_version = (
        subprocess.run([sys.executable, "-m", "grpc_tools.protoc", "--version"], capture_output=True).stdout.decode().strip()
    )
    print(protoc_version)
    protoc_args = [
        *[f"--proto_path={proto_path}" for proto_path in proto_paths],
        "--mypy_out",
        f"relax_strict_optional_primitives:{stubs_folder}",
        *proto_globs,
    ]
    print("Running: protoc\n    " + "\n    ".join(protoc_args) + "\n")
    subprocess.run([sys.executable, "-m", "grpc_tools.protoc", *protoc_args], cwd=cwd, check=True)
    return protoc_version
