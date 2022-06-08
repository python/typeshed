#!/usr/bin/env python3
from __future__ import annotations

import argparse
import asyncio
import datetime
import os
import re
import subprocess
import sys
import urllib.parse
from dataclasses import dataclass
from pathlib import Path

import aiohttp
import packaging.specifiers
import packaging.version
import tomli
import tomlkit


@dataclass
class StubInfo:
    distribution: str
    version_spec: str
    obsolete: bool
    no_longer_updated: bool


def read_typeshed_stub_metadata(stub_path: Path) -> StubInfo:
    with (stub_path / "METADATA.toml").open("rb") as f:
        meta = tomli.load(f)
    return StubInfo(
        distribution=stub_path.name,
        version_spec=meta["version"],
        obsolete="obsolete_since" in meta,
        no_longer_updated=meta.get("no_longer_updated", False),
    )


@dataclass
class PypiInfo:
    distribution: str
    version: packaging.version.Version
    upload_date: datetime.datetime


async def fetch_pypi_info(distribution: str, session: aiohttp.ClientSession) -> PypiInfo:
    url = f"https://pypi.org/pypi/{urllib.parse.quote(distribution)}/json"
    async with session.get(url) as response:
        response.raise_for_status()
        j = await response.json()
        version = j["info"]["version"]
        date = datetime.datetime.fromisoformat(j["releases"][version][0]["upload_time"])
        return PypiInfo(
            distribution=distribution, version=packaging.version.Version(version), upload_date=date
        )


@dataclass
class Update:
    distribution: str
    stub_path: Path
    old_version_spec: str
    new_version_spec: str


@dataclass
class NoUpdate:
    distribution: str
    reason: str


def _check_spec(updated_spec: str, version: packaging.version.Version) -> str:
    assert version in packaging.specifiers.SpecifierSet(
        "==" + updated_spec
    ), f"{version} not in {updated_spec}"
    return updated_spec


def get_updated_version_spec(spec: str, version: packaging.version.Version) -> str:
    if not spec.endswith(".*"):
        return _check_spec(version.base_version, version)

    specificity = spec.count(".") if spec.removesuffix(".*") else 0
    rounded_version = version.base_version.split(".")[:specificity]
    rounded_version.extend(["0"] * (specificity - len(rounded_version)))

    return _check_spec(".".join(rounded_version) + ".*", version)


async def determine_action(stub_path: Path, session: aiohttp.ClientSession) -> Update | NoUpdate:
    stub_info = read_typeshed_stub_metadata(stub_path)
    if stub_info.obsolete:
        return NoUpdate(stub_info.distribution, "obsolete")
    if stub_info.no_longer_updated:
        return NoUpdate(stub_info.distribution, "no longer updated")

    pypi_info = await fetch_pypi_info(stub_info.distribution, session)
    spec = packaging.specifiers.SpecifierSet("==" + stub_info.version_spec)
    if pypi_info.version in spec:
        return NoUpdate(stub_info.distribution, "up to date")

    return Update(
        distribution=stub_info.distribution,
        stub_path=stub_path,
        old_version_spec=stub_info.version_spec,
        new_version_spec=get_updated_version_spec(stub_info.version_spec, pypi_info.version),
    )


def normalize(name: str) -> str:
    # PEP 503 normalization
    return re.sub(r"[-_.]+", "-", name).lower()


_repo_lock = asyncio.Lock()

TYPESHED_OWNER = "python"
FORK_OWNER = "hauntsaninja"


async def suggest_typeshed_update(
    update: Update, session: aiohttp.ClientSession, dry_run: bool
) -> None:
    title = f"[stubsabot] Bump {update.distribution} to {update.new_version_spec}"

    # lock should be unnecessary, but can't hurt to enforce mutual exclusion
    async with _repo_lock:
        branch_name = f"stubsabot/{normalize(update.distribution)}"
        subprocess.check_call(["git", "checkout", "-B", branch_name, "origin/master"])
        with open(update.stub_path / "METADATA.toml", "rb") as f:
            meta = tomlkit.load(f)
        meta["version"] = update.new_version_spec
        with open(update.stub_path / "METADATA.toml", "w") as f:
            tomlkit.dump(meta, f)
        subprocess.check_call(["git", "commit", "--all", "-m", title])
        if dry_run:
            return
        subprocess.check_call(["git", "push", "origin", branch_name, "--force-with-lease"])

    secret = os.environ["GITHUB_TOKEN"]
    if secret.startswith("ghp"):
        auth = f"token {secret}"
    else:
        auth = f"Bearer {secret}"

    async with session.post(
        f"https://api.github.com/repos/{TYPESHED_OWNER}/typeshed/pulls",
        json={"title": title, "head": f"{FORK_OWNER}:{branch_name}", "base": "master"},
        headers={"Accept": "application/vnd.github.v3+json", "Authorization": auth},
    ) as response:
        body = await response.json()
        if response.status == 422 and any(
            "A pull request already exists" in e.get("message", "") for e in body.get("errors", [])
        ):
            # TODO: diff and update existing pull request
            return
        response.raise_for_status()


async def main() -> None:
    assert sys.version_info >= (3, 9)

    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    try:
        conn = aiohttp.TCPConnector(limit_per_host=10)
        async with aiohttp.ClientSession(connector=conn) as session:
            tasks = [
                asyncio.create_task(determine_action(stubs_path, session))
                for stubs_path in Path("stubs").iterdir()
            ]
            for task in asyncio.as_completed(tasks):
                update = await task
                if isinstance(update, NoUpdate):
                    continue
                if isinstance(update, Update):
                    await suggest_typeshed_update(update, session, dry_run=args.dry_run)
                    continue
                raise AssertionError
    finally:
        # if you need to cleanup, try:
        # git branch -D $(git branch --list 'stubsabot/*')
        subprocess.check_call(["git", "checkout", "master"])


if __name__ == "__main__":
    asyncio.run(main())
