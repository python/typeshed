from __future__ import annotations

import functools
import os
import sys
import tempfile
from collections.abc import Generator, Iterable
from enum import Enum
from typing import Any, NamedTuple

import tomli

from ts_utils.metadata import metadata_path

# We need to work around a limitation of tempfile.NamedTemporaryFile on Windows
# For details, see https://github.com/python/typeshed/pull/13620#discussion_r1990185997
# Python 3.12 added a workaround with `tempfile.NamedTemporaryFile("w+", delete_on_close=False)`
if sys.platform != "win32":
    _named_temporary_file = functools.partial(tempfile.NamedTemporaryFile, "w+")
else:
    from contextlib import contextmanager

    @contextmanager
    def _named_temporary_file() -> Generator[tempfile._TemporaryFileWrapper[str]]:  # pyright: ignore[reportPrivateUsage]
        temp = tempfile.NamedTemporaryFile("w+", delete=False)  # noqa: SIM115
        try:
            yield temp
        finally:
            temp.close()
            os.remove(temp.name)


class MypyDistConf(NamedTuple):
    module_name: str
    values: dict[str, dict[str, Any]]


class MypyResult(Enum):
    SUCCESS = 0
    FAILURE = 1
    CRASH = 2


# The configuration section in the metadata file looks like the following, with multiple module sections possible
# [mypy-tests]
# [mypy-tests.yaml]
# module_name = "yaml"
# [mypy-tests.yaml.values]
# disallow_incomplete_defs = true
# disallow_untyped_defs = true


def mypy_configuration_from_distribution(distribution: str) -> list[MypyDistConf]:
    with metadata_path(distribution).open("rb") as f:
        data = tomli.load(f)

    # TODO: This could be added to ts_utils.metadata
    mypy_tests_conf: dict[str, dict[str, Any]] = data.get("mypy-tests", {})
    if not mypy_tests_conf:
        return []

    def validate_configuration(section_name: str, mypy_section: dict[str, Any]) -> MypyDistConf:
        assert isinstance(mypy_section, dict), f"{section_name} should be a section"
        module_name = mypy_section.get("module_name")

        assert module_name is not None, f"{section_name} should have a module_name key"
        assert isinstance(module_name, str), f"{section_name} should be a key-value pair"

        assert "values" in mypy_section, f"{section_name} should have a values section"
        values: dict[str, dict[str, Any]] = mypy_section["values"]
        assert isinstance(values, dict), "values should be a section"
        return MypyDistConf(module_name, values.copy())

    assert isinstance(mypy_tests_conf, dict), "mypy-tests should be a section"
    return [validate_configuration(section_name, mypy_section) for section_name, mypy_section in mypy_tests_conf.items()]


def temporary_mypy_config_file(configurations: Iterable[MypyDistConf]) -> tempfile._TemporaryFileWrapper[str]:
    temp = _named_temporary_file()
    temp.write("[mypy]\n")
    for dist_conf in configurations:
        temp.write(f"[mypy-{dist_conf.module_name}]\n")
        for k, v in dist_conf.values.items():
            temp.write(f"{k} = {v}\n")
    temp.flush()
    return temp
