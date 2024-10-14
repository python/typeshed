from pathlib import Path
from typing import Final

TS_BASE_PATH: Final = Path(__file__).parent.parent.parent.relative_to(Path.cwd(), walk_up=True)
STDLIB_PATH: Final = TS_BASE_PATH / "stdlib"
STUBS_PATH: Final = TS_BASE_PATH / "stubs"

PYPROJECT_PATH: Final = TS_BASE_PATH / "pyproject.toml"
REQUIREMENTS_PATH: Final = TS_BASE_PATH / "requirements-tests.txt"

TESTS_DIR: Final = "@tests"
TEST_CASES_DIR: Final = "test_cases"


def distribution_path(distribution_name: str) -> Path:
    """Return the path to the directory of a third-party distribution."""
    return STUBS_PATH / distribution_name


def tests_path(distribution_name: str) -> Path:
    if distribution_name == "stdlib":
        return STDLIB_PATH / TESTS_DIR
    else:
        return STUBS_PATH / distribution_name / TESTS_DIR


def test_cases_path(distribution_name: str) -> Path:
    return tests_path(distribution_name) / TEST_CASES_DIR


def allowlists_path(distribution_name: str) -> Path:
    if distribution_name == "stdlib":
        return tests_path("stdlib") / "stubtest_allowlists"
    else:
        return tests_path(distribution_name)
