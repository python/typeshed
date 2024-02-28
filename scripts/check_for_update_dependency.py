import re
import requests
import toml
from typing import List

from typing import Optional


def get_latest_version(package_name: str) -> Optional[str]:
    """Fetch the latest version of a package from PyPI."""
    response = requests.get(f"https://pypi.org/pypi/{package_name}/json")
    if response.status_code == 200:
        data = response.json()
        return str(data["info"]["version"])
    else:
        return None


def update_versions(file_path: str) -> None:
    with open(file_path, "r") as file:
        content = file.readlines()

    pattern = re.compile(r"^(pytype|mypy)==([\d.]+)")

    updated_content: List[str] = []

    for line in content:
        match = pattern.match(line)
        if match:
            package_name = match.group(1)
            current_version = match.group(2)
            latest_version = get_latest_version(package_name)
            if latest_version and current_version != latest_version:
                print(f"Updating {package_name} from {current_version} to {latest_version}")
                line = line.replace(current_version, latest_version)
        updated_content.append(line)

    with open(file_path, "w") as file:
        file.writelines(updated_content)


def update_pyright_version(file_path: str) -> None:
    with open(file_path, "r", encoding="utf-8") as file:
        config = toml.load(file)

    latest_version = get_latest_version("pyright")

    if latest_version:
        config["tool"]["typeshed"]["pyright_version"] = latest_version

        with open(file_path, "w", encoding="utf-8") as file:
            toml.dump(config, file)
        print(f"Updated pyright to version {latest_version} in {file_path}")


file_paths: List[str] = ["requirements-tests.txt", "pyproject.toml"]

if __name__ == "__main__":
    for file_path in file_paths:
        if file_path.endswith(".txt"):
            update_versions(file_path)
        elif file_path.endswith(".toml"):
            update_pyright_version(file_path)
