import subprocess
import sys

from ts_utils.requirements import get_external_stub_requirements


def main() -> None:
    requirements = get_external_stub_requirements()
    subprocess.check_call(("uv", "pip", "install", *sys.argv[1:], *[str(requirement) for requirement in requirements]))


if __name__ == "__main__":
    main()
