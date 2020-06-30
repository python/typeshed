import argparse
import requests

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

PREFIX = "types-"
URL_TEMPLATE = "https://pypi.org/pypi/{}/json"
RETRIES = 5
RETRY_ON = [429, 500, 502, 503, 504]
TIMEOUT = 3


def main(distribution: str, version: str) -> int:
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
    latest = max(v for v in data["releases"].keys() if v.startswith(version))
    assert latest.count(".") == 2
    increment = latest.split(".")[-1]
    return int(increment)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("distribution", help="Third-party distribution to build")
    parser.add_argument("version", help="Base version for which to get increment")
    args = parser.parse_args()
    print(main(args.distribution, args.version))
