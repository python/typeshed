import re
import requests
import toml
from typing import Optional


def get_latest_version(package_name: str) -> str:
    """Fetch the latest version of a package from PyPI."""
    response = requests.get(f"https://pypi.org/pypi/{package_name}/json")
    if response.status_code == 200:
        data = response.json()
        return data['info']['version']
    else:
        raise Exception(
            f"Failed to fetch the latest version for {package_name}")


def update_versions(file_path: str) -> None:
    # Read the current content of the file
    with open(file_path, "r") as file:
        content = file.readlines()

    # Pattern to match the packages of interest and capture their current versions
    pattern = re.compile(r"^(pytype|mypy)==([\d.]+)")

    # Updated content
    updated_content = []

    for line in content:
        match = pattern.match(line)
        if match:
            package_name = match.group(1)
            current_version = match.group(2)
            try:
                latest_version = get_latest_version(package_name)
                if current_version != latest_version:
                    print(
                        f"Updating {package_name} from {current_version} to {latest_version}")
                    line = line.replace(current_version, latest_version)
            except Exception as e:
                print(f"Error updating {package_name}: {e}")
        updated_content.append(line)

    # Write the updated content back to the file
    with open(file_path, "w") as file:
        file.writelines(updated_content)


def update_pyright_version(file_path: str) -> None:
    # Load the TOML file
    with open(file_path, "r", encoding="utf-8") as file:
        config = toml.load(file)

    # Get the latest version of pyright
    latest_version = get_latest_version("pyright")

    if latest_version:
        # Update the pyright version in the configuration
        config["tool"]["typeshed"]["pyright_version"] = latest_version

        # Write the updated configuration back to the file
        with open(file_path, "w", encoding="utf-8") as file:
            toml.dump(config, file)
        print(f"Updated pyright to version {latest_version} in {file_path}")
    else:
        print("No update performed.")


# Path to your file
file_path: list[str] = ["requirements-tests.txt", "pyproject.toml"]

if __name__ == "__main__":
    update_versions(file_path[0])
    update_pyright_version(file_path[1])
