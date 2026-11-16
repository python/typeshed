# Pyright may resolve the published types-PyYAML package, which predates these overloads.
# pyright: reportUnnecessaryTypeIgnoreComment=false

from io import BytesIO, StringIO
from typing_extensions import assert_type

import yaml

node = yaml.ScalarNode("tag:yaml.org,2002:str", "example")

assert_type(yaml.dump({}, StringIO()), None)
assert_type(yaml.dump({}, StringIO(), encoding="utf-8"), None)
assert_type(yaml.dump({}, BytesIO(), encoding="utf-8"), None)
assert_type(yaml.dump_all([{}], BytesIO(), encoding="utf-8"), None)
assert_type(yaml.safe_dump({}, BytesIO(), encoding="utf-8"), None)
assert_type(yaml.safe_dump_all([{}], BytesIO(), encoding="utf-8"), None)
assert_type(yaml.serialize(node, BytesIO(), encoding="utf-8"), None)  # pyright: ignore[reportUnknownMemberType]
assert_type(yaml.serialize_all([node], BytesIO(), encoding="utf-8"), None)  # pyright: ignore[reportUnknownMemberType]
assert_type(yaml.safe_dump({}), str)
assert_type(yaml.safe_dump({}, encoding="utf-8"), bytes)

yaml.dump({}, BytesIO())  # type: ignore
yaml.dump_all([{}], BytesIO())  # type: ignore
yaml.safe_dump({}, BytesIO())  # type: ignore
yaml.safe_dump_all([{}], BytesIO())  # type: ignore
yaml.serialize(node, BytesIO())  # type: ignore
yaml.serialize_all([node], BytesIO())  # type: ignore


class TextWriter:
    def write(self, data: str, /) -> None: ...


assert_type(yaml.safe_dump({}, TextWriter()), None)
yaml.safe_dump({}, TextWriter(), encoding="utf-8")  # type: ignore
