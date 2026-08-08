from typing_extensions import assert_type

from aiofiles.tempfile import NamedTemporaryFile


async def check_named_temporary_file() -> None:
    async with NamedTemporaryFile() as file:
        assert_type(file.name, str)

    async with NamedTemporaryFile(mode="w") as file:
        assert_type(file.name, str)
