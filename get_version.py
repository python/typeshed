import argparse
import os.path
from typing import Optional

import requests
import toml
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# TODO: remove the "out" part after migration is done.
THIRD_PARTY_NAMESPACE = "out/stubs"
PREFIX = "types-"
URL_TEMPLATE = "https://pypi.org/pypi/{}/json"
RETRIES = 5
RETRY_ON = [429, 500, 502, 503, 504]
TIMEOUT = 3


def read_base_version(distribution: str) -> str:
    """Read distribution version from metadata."""
    metadata_file = os.path.join(THIRD_PARTY_NAMESPACE, distribution, "METADATA.toml")
    with open(metadata_file) as f:
        data = toml.loads(f.read())
    return data["version"]


def main(distribution: str, version: Optional[str]) -> int:
    """A simple function to get version increment of a third-party stub package.

    Supports basic reties and timeouts (as module constants).
    """
    url = URL_TEMPLATE.format(PREFIX + distribution)
    retry_strategy = Retry(
        total=RETRIES, status_forcelist=RETRY_ON
    )
    with requests.Session() as session:
        session.mount("https://", HTTPAdapter(max_retries=retry_strategy))
        resp = session.get(url, timeout=TIMEOUT)
    if not resp.ok:
        raise ValueError("Error while retrieving version")
    data = resp.json()
    if not version:
        # Use the METADATA.toml version, if not given one.
        version = read_base_version(distribution)
    latest = max(v for v in data["releases"].keys() if v.startswith(version))
    assert latest.count(".") == 2
    increment = latest.split(".")[-1]
    return int(increment)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("distribution", help="Third-party distribution to build")
    parser.add_argument("version", nargs="?", help="Base version for which to get increment")
    args = parser.parse_args()
    print(main(args.distribution, args.version))
