"""Check that the installable package carries the canonical pywin32 stubs."""

import hashlib
import json
from pathlib import Path

import tomllib


def main() -> None:
    package = Path(__file__).resolve().parent
    source = package.parent.parent / "stubs" / "pywin32"
    manifest = json.loads((package / "STUB_SOURCE.json").read_bytes())["stubs"]
    canonical = {
        path.relative_to(source).as_posix() for path in source.rglob("*.pyi") if path.relative_to(source).parts[0] != "@tests"
    }
    config = tomllib.loads((package / "pyproject.toml").read_text(encoding="utf-8"))
    declared = {f"{group}/{name}" for group, files in config["tool"]["setuptools"]["package-data"].items() for name in files}
    packaged = {path.relative_to(package).as_posix() for path in package.rglob("*.pyi")}
    expected = {entry["package"] for entry in manifest.values()}
    if canonical != set(manifest) or packaged != expected or {name for name in declared if name.endswith(".pyi")} != expected:
        raise SystemExit("The source and package stub inventories differ")
    for name, entry in manifest.items():
        raw = (source / name).read_bytes()
        if hashlib.sha256(raw).hexdigest() != entry["sha256"] or raw != (package / entry["package"]).read_bytes():
            raise SystemExit(f"Regenerate the package after changing {name}")
    for name in declared:
        path = package / name
        if not path.is_file():
            raise SystemExit(f"Missing package file {name}")
        if path.name == "METADATA.toml" and path.read_bytes() != (source / "METADATA.toml").read_bytes():
            raise SystemExit(f"Stale package metadata in {name}")
    print(f"Verified {len(canonical)} canonical stubs and {len(declared)} declared package files")


if __name__ == "__main__":
    main()
