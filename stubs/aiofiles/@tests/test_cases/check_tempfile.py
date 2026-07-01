from __future__ import annotations

from typing_extensions import assert_type

from aiofiles.tempfile import NamedTemporaryFile


async def check_named_temporary_file_name() -> None:
    async with NamedTemporaryFile() as binary_file:
        assert_type(binary_file.name, str)

    async with NamedTemporaryFile(mode="w+") as text_file:
        assert_type(text_file.name, str)
