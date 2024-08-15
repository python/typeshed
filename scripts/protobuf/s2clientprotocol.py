"""
Generates the protobuf stubs for the given s2clientprotocol version using mypy-protobuf.
Generally, new minor versions are a good time to update the stubs.
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from _helpers import download_file, extract_archive, run_protoc, update_metadata
from mypy_protobuf.main import __version__ as MYPY_PROTOBUF_VERSION  # pyright: ignore[reportMissingTypeStubs]

# Whenever you update S2CLIENT_PROTO_VERSION here, version should be updated
# in stubs/s2clientprotocol/METADATA.toml and vice-versa.
S2CLIENT_PROTO_VERSION = "c04df4adbe274858a4eb8417175ee32ad02fd609"

REPO_ROOT = Path(__file__).absolute().parent.parent.parent
S2CLIENT_STUBS_FOLDER = REPO_ROOT / "stubs" / "s2clientprotocol"
S2CLIENT_PROTO_FILENAME = f"{S2CLIENT_PROTO_VERSION}.zip"
S2CLIENT_PROTO_URL = f"https://github.com/Blizzard/s2client-proto/archive/{S2CLIENT_PROTO_FILENAME}"
S2CLIENT_PROTO_DIR = f"s2client-proto-{S2CLIENT_PROTO_VERSION}"
VERSION_PATTERN = re.compile(r'def game_version\(\):\n    return "(.+?)"')


def extract_version(file_path: Path):
    match = re.search(VERSION_PATTERN, file_path.read_text())
    assert match
    return match.group(1)


def main() -> None:
    temp_dir = Path(tempfile.mkdtemp())
    # Fetch s2clientprotocol (which contains all the .proto files)
    archive_path = temp_dir / S2CLIENT_PROTO_FILENAME
    download_file(S2CLIENT_PROTO_URL, archive_path)
    extract_archive(archive_path, temp_dir)

    # Remove existing pyi
    for old_stub in S2CLIENT_STUBS_FOLDER.rglob("*_pb2.pyi"):
        old_stub.unlink()

    PROTOC_VERSION = run_protoc(
        proto_paths=[S2CLIENT_PROTO_DIR],
        proto_globs=[f"{S2CLIENT_PROTO_DIR}/s2clientprotocol/*.proto"],
        stubs_folder=S2CLIENT_STUBS_FOLDER,
        cwd=temp_dir,
    )

    PYTHON_S2CLIENT_PROTO_VERSION = extract_version(temp_dir / S2CLIENT_PROTO_DIR / "s2clientprotocol" / "build.py")

    # Cleanup
    shutil.rmtree(temp_dir)

    update_metadata(
        S2CLIENT_STUBS_FOLDER / "METADATA.toml",
        f"""Partially generated using \
[mypy-protobuf=={MYPY_PROTOBUF_VERSION}](https://github.com/nipunn1313/mypy-protobuf/tree/v{MYPY_PROTOBUF_VERSION}) \
and {PROTOC_VERSION} on \
[s2client-proto {PYTHON_S2CLIENT_PROTO_VERSION}](https://github.com/Blizzard/s2client-proto/tree/{S2CLIENT_PROTO_VERSION})
""",
    )

    # Run pre-commit to cleanup the stubs
    subprocess.run([sys.executable, "-m", "pre_commit", "run", "--files", *S2CLIENT_STUBS_FOLDER.rglob("*_pb2.pyi")])


if __name__ == "__main__":
    main()
