from __future__ import annotations

import re
from typing_extensions import assert_type

from xdg.IniFile import IniFile

# The "get" method is quite complex with many overloads. Check that many forms
# are valid.
# The function definition is:
# def get(self, key, group=None, locale=False, type="string", list=False, strict=False):

# Get str
assert_type(IniFile().get("some_key"), str)
assert_type(IniFile().get("some_key", None), str)
assert_type(IniFile().get("some_key", "group"), str)
assert_type(IniFile().get("some_key", "group", False), str)
assert_type(IniFile().get("some_key", "group", True), str)
assert_type(IniFile().get("some_key", "group", True, "string"), str)
assert_type(IniFile().get("some_key", "group", True, "string", False), str)
assert_type(IniFile().get("some_key", "group", True, "string", False, False), str)
assert_type(IniFile().get("some_key", "group", True, "string", False, True), str)
# Keyword parameters
assert_type(IniFile().get("some_key", group=None), str)
assert_type(IniFile().get("some_key", group="group"), str)
assert_type(IniFile().get("some_key", locale=False), str)
assert_type(IniFile().get("some_key", locale=True), str)
assert_type(IniFile().get("some_key", strict=False), str)
assert_type(IniFile().get("some_key", strict=True), str)
assert_type(IniFile().get("some_key", group="group", locale=True, strict=True), str)
# Explicitly set type as string in keyword parameters.
assert_type(IniFile().get("some_key", type="string"), str)
assert_type(IniFile().get("some_key", group=None, type="string"), str)
assert_type(IniFile().get("some_key", group="group", type="string"), str)
assert_type(IniFile().get("some_key", locale=False, type="string"), str)
assert_type(IniFile().get("some_key", locale=True, type="string"), str)
assert_type(IniFile().get("some_key", strict=False, type="string"), str)
assert_type(IniFile().get("some_key", strict=True, type="string"), str)
assert_type(IniFile().get("some_key", group="group", locale=True, strict=True, type="string"), str)
# Explicitly set list.
assert_type(IniFile().get("some_key", list=False), str)
assert_type(IniFile().get("some_key", group=None, list=False), str)
assert_type(IniFile().get("some_key", group="group", list=False), str)
assert_type(IniFile().get("some_key", locale=False, list=False), str)
assert_type(IniFile().get("some_key", locale=True, list=False), str)
assert_type(IniFile().get("some_key", strict=False, list=False), str)
assert_type(IniFile().get("some_key", strict=True, list=False), str)
assert_type(IniFile().get("some_key", group="group", locale=True, strict=True, list=False), str)
# Explicitly set both.
assert_type(IniFile().get("some_key", list=False, type="string"), str)
assert_type(IniFile().get("some_key", group=None, list=False, type="string"), str)
assert_type(IniFile().get("some_key", group="group", list=False, type="string"), str)
assert_type(IniFile().get("some_key", locale=False, list=False, type="string"), str)
assert_type(IniFile().get("some_key", locale=True, list=False, type="string"), str)
assert_type(IniFile().get("some_key", strict=False, list=False, type="string"), str)
assert_type(IniFile().get("some_key", strict=True, list=False, type="string"), str)
assert_type(IniFile().get("some_key", group="group", locale=True, strict=True, list=False, type="string"), str)

# Get list[str]
assert_type(IniFile().get("some_key", "group", True, "string", True), list[str])
assert_type(IniFile().get("some_key", "group", True, "string", True, False), list[str])
assert_type(IniFile().get("some_key", "group", True, "string", True, True), list[str])
# Keyword parameters
assert_type(IniFile().get("some_key", list=True, group=None), list[str])
assert_type(IniFile().get("some_key", list=True, group="group"), list[str])
assert_type(IniFile().get("some_key", list=True, locale=False), list[str])
assert_type(IniFile().get("some_key", list=True, locale=True), list[str])
assert_type(IniFile().get("some_key", list=True, strict=False), list[str])
assert_type(IniFile().get("some_key", list=True, strict=True), list[str])
assert_type(IniFile().get("some_key", list=True, group="group", locale=True, strict=True), list[str])
# Explicitly set list
assert_type(IniFile().get("some_key", list=True), list[str])
assert_type(IniFile().get("some_key", group=None, list=True), list[str])
assert_type(IniFile().get("some_key", group="group", list=True), list[str])
assert_type(IniFile().get("some_key", locale=False, list=True), list[str])
assert_type(IniFile().get("some_key", locale=True, list=True), list[str])
assert_type(IniFile().get("some_key", strict=False, list=True), list[str])
assert_type(IniFile().get("some_key", strict=True, list=True), list[str])
assert_type(IniFile().get("some_key", group="group", locale=True, strict=True, list=True), list[str])
# Explicitly set both
assert_type(IniFile().get("some_key", list=True, type="string"), list[str])
assert_type(IniFile().get("some_key", group=None, list=True, type="string"), list[str])
assert_type(IniFile().get("some_key", group="group", list=True, type="string"), list[str])
assert_type(IniFile().get("some_key", locale=False, list=True, type="string"), list[str])
assert_type(IniFile().get("some_key", locale=True, list=True, type="string"), list[str])
assert_type(IniFile().get("some_key", strict=False, list=True, type="string"), list[str])
assert_type(IniFile().get("some_key", strict=True, list=True, type="string"), list[str])
assert_type(IniFile().get("some_key", group="group", locale=True, strict=True, list=True, type="string"), list[str])

# Get bool
assert_type(IniFile().get("some_key", "group", True, "boolean"), bool)
assert_type(IniFile().get("some_key", "group", True, "boolean", False), bool)
assert_type(IniFile().get("some_key", "group", True, "boolean", False, False), bool)
assert_type(IniFile().get("some_key", "group", True, "boolean", False, True), bool)
# Keyword parameters
assert_type(IniFile().get("some_key", type="boolean"), bool)
assert_type(IniFile().get("some_key", type="boolean", group=None), bool)
assert_type(IniFile().get("some_key", type="boolean", group="group"), bool)
assert_type(IniFile().get("some_key", type="boolean", locale=False), bool)
assert_type(IniFile().get("some_key", type="boolean", locale=True), bool)
assert_type(IniFile().get("some_key", type="boolean", strict=False), bool)
assert_type(IniFile().get("some_key", type="boolean", strict=True), bool)
assert_type(IniFile().get("some_key", type="boolean", group="group", locale=True, strict=True), bool)
# Explicitly set list
assert_type(IniFile().get("some_key", type="boolean", list=False), bool)
assert_type(IniFile().get("some_key", type="boolean", group=None, list=False), bool)
assert_type(IniFile().get("some_key", type="boolean", group="group", list=False), bool)
assert_type(IniFile().get("some_key", type="boolean", locale=False, list=False), bool)
assert_type(IniFile().get("some_key", type="boolean", locale=True, list=False), bool)
assert_type(IniFile().get("some_key", type="boolean", strict=False, list=False), bool)
assert_type(IniFile().get("some_key", type="boolean", strict=True, list=False), bool)
assert_type(IniFile().get("some_key", type="boolean", group="group", locale=True, strict=True, list=False), bool)

# Get list[bool]
assert_type(IniFile().get("some_key", "group", True, "boolean", True), list[bool])
assert_type(IniFile().get("some_key", "group", True, "boolean", True, False), list[bool])
assert_type(IniFile().get("some_key", "group", True, "boolean", True, True), list[bool])
# Keyword parameters
assert_type(IniFile().get("some_key", type="boolean", list=True), list[bool])
assert_type(IniFile().get("some_key", type="boolean", list=True, group=None), list[bool])
assert_type(IniFile().get("some_key", type="boolean", list=True, group="group"), list[bool])
assert_type(IniFile().get("some_key", type="boolean", list=True, locale=False), list[bool])
assert_type(IniFile().get("some_key", type="boolean", list=True, locale=True), list[bool])
assert_type(IniFile().get("some_key", type="boolean", list=True, strict=False), list[bool])
assert_type(IniFile().get("some_key", type="boolean", list=True, strict=True), list[bool])
assert_type(IniFile().get("some_key", type="boolean", list=True, group="group", locale=True, strict=True), list[bool])

# Get int
assert_type(IniFile().get("some_key", "group", True, "integer"), int)
assert_type(IniFile().get("some_key", "group", True, "integer", False), int)
assert_type(IniFile().get("some_key", "group", True, "integer", False, False), int)
assert_type(IniFile().get("some_key", "group", True, "integer", False, True), int)
# Keyword parameters
assert_type(IniFile().get("some_key", type="integer"), int)
assert_type(IniFile().get("some_key", type="integer", group=None), int)
assert_type(IniFile().get("some_key", type="integer", group="group"), int)
assert_type(IniFile().get("some_key", type="integer", locale=False), int)
assert_type(IniFile().get("some_key", type="integer", locale=True), int)
assert_type(IniFile().get("some_key", type="integer", strict=False), int)
assert_type(IniFile().get("some_key", type="integer", strict=True), int)
assert_type(IniFile().get("some_key", type="integer", group="group", locale=True, strict=True), int)
# Explicitly set list.
assert_type(IniFile().get("some_key", type="integer", list=False), int)
assert_type(IniFile().get("some_key", type="integer", group=None, list=False), int)
assert_type(IniFile().get("some_key", type="integer", group="group", list=False), int)
assert_type(IniFile().get("some_key", type="integer", locale=False, list=False), int)
assert_type(IniFile().get("some_key", type="integer", locale=True, list=False), int)
assert_type(IniFile().get("some_key", type="integer", strict=False, list=False), int)
assert_type(IniFile().get("some_key", type="integer", strict=True, list=False), int)
assert_type(IniFile().get("some_key", type="integer", group="group", locale=True, strict=True, list=False), int)

# Get list[int]
assert_type(IniFile().get("some_key", "group", True, "integer", True), list[int])
assert_type(IniFile().get("some_key", "group", True, "integer", True, False), list[int])
assert_type(IniFile().get("some_key", "group", True, "integer", True, True), list[int])
# Keyword parameters
assert_type(IniFile().get("some_key", type="integer", list=True), list[int])
assert_type(IniFile().get("some_key", type="integer", list=True, group=None), list[int])
assert_type(IniFile().get("some_key", type="integer", list=True, group="group"), list[int])
assert_type(IniFile().get("some_key", type="integer", list=True, locale=False), list[int])
assert_type(IniFile().get("some_key", type="integer", list=True, locale=True), list[int])
assert_type(IniFile().get("some_key", type="integer", list=True, strict=False), list[int])
assert_type(IniFile().get("some_key", type="integer", list=True, strict=True), list[int])
assert_type(IniFile().get("some_key", type="integer", list=True, group="group", locale=True, strict=True), list[int])

# Get float
assert_type(IniFile().get("some_key", "group", True, "numeric"), float)
assert_type(IniFile().get("some_key", "group", True, "numeric", False), float)
assert_type(IniFile().get("some_key", "group", True, "numeric", False, False), float)
assert_type(IniFile().get("some_key", "group", True, "numeric", False, True), float)
# Keyword parameters
assert_type(IniFile().get("some_key", type="numeric"), float)
assert_type(IniFile().get("some_key", type="numeric", group=None), float)
assert_type(IniFile().get("some_key", type="numeric", group="group"), float)
assert_type(IniFile().get("some_key", type="numeric", locale=False), float)
assert_type(IniFile().get("some_key", type="numeric", locale=True), float)
assert_type(IniFile().get("some_key", type="numeric", strict=False), float)
assert_type(IniFile().get("some_key", type="numeric", strict=True), float)
assert_type(IniFile().get("some_key", type="numeric", group="group", locale=True, strict=True), float)
# Explicitly set list.
assert_type(IniFile().get("some_key", type="numeric", list=False), float)
assert_type(IniFile().get("some_key", type="numeric", group=None, list=False), float)
assert_type(IniFile().get("some_key", type="numeric", group="group", list=False), float)
assert_type(IniFile().get("some_key", type="numeric", locale=False, list=False), float)
assert_type(IniFile().get("some_key", type="numeric", locale=True, list=False), float)
assert_type(IniFile().get("some_key", type="numeric", strict=False, list=False), float)
assert_type(IniFile().get("some_key", type="numeric", strict=True, list=False), float)
assert_type(IniFile().get("some_key", type="numeric", group="group", locale=True, strict=True, list=False), float)

# Get list[float]
assert_type(IniFile().get("some_key", "group", True, "numeric", True), list[float])
assert_type(IniFile().get("some_key", "group", True, "numeric", True, False), list[float])
assert_type(IniFile().get("some_key", "group", True, "numeric", True, True), list[float])
# Keyword parameters
assert_type(IniFile().get("some_key", type="numeric", list=True), list[float])
assert_type(IniFile().get("some_key", type="numeric", list=True, group=None), list[float])
assert_type(IniFile().get("some_key", type="numeric", list=True, group="group"), list[float])
assert_type(IniFile().get("some_key", type="numeric", list=True, locale=False), list[float])
assert_type(IniFile().get("some_key", type="numeric", list=True, locale=True), list[float])
assert_type(IniFile().get("some_key", type="numeric", list=True, strict=False), list[float])
assert_type(IniFile().get("some_key", type="numeric", list=True, strict=True), list[float])
assert_type(IniFile().get("some_key", type="numeric", list=True, group="group", locale=True, strict=True), list[float])

# Get regex
assert_type(IniFile().get("some_key", "group", True, "regex"), re.Pattern[str])
assert_type(IniFile().get("some_key", "group", True, "regex", False), re.Pattern[str])
assert_type(IniFile().get("some_key", "group", True, "regex", False, False), re.Pattern[str])
assert_type(IniFile().get("some_key", "group", True, "regex", False, True), re.Pattern[str])
# Keyword parameters
assert_type(IniFile().get("some_key", type="regex"), re.Pattern[str])
assert_type(IniFile().get("some_key", type="regex", group=None), re.Pattern[str])
assert_type(IniFile().get("some_key", type="regex", group="group"), re.Pattern[str])
assert_type(IniFile().get("some_key", type="regex", locale=False), re.Pattern[str])
assert_type(IniFile().get("some_key", type="regex", locale=True), re.Pattern[str])
assert_type(IniFile().get("some_key", type="regex", strict=False), re.Pattern[str])
assert_type(IniFile().get("some_key", type="regex", strict=True), re.Pattern[str])
assert_type(IniFile().get("some_key", type="regex", group="group", locale=True, strict=True), re.Pattern[str])
# Explicitly set list.
assert_type(IniFile().get("some_key", type="regex", list=False), re.Pattern[str])
assert_type(IniFile().get("some_key", type="regex", group=None, list=False), re.Pattern[str])
assert_type(IniFile().get("some_key", type="regex", group="group", list=False), re.Pattern[str])
assert_type(IniFile().get("some_key", type="regex", locale=False, list=False), re.Pattern[str])
assert_type(IniFile().get("some_key", type="regex", locale=True, list=False), re.Pattern[str])
assert_type(IniFile().get("some_key", type="regex", strict=False, list=False), re.Pattern[str])
assert_type(IniFile().get("some_key", type="regex", strict=True, list=False), re.Pattern[str])
assert_type(IniFile().get("some_key", type="regex", group="group", locale=True, strict=True, list=False), re.Pattern[str])

# Get list[regex]
assert_type(IniFile().get("some_key", "group", True, "regex", True), list[re.Pattern[str]])
assert_type(IniFile().get("some_key", "group", True, "regex", True, False), list[re.Pattern[str]])
assert_type(IniFile().get("some_key", "group", True, "regex", True, True), list[re.Pattern[str]])
# Keyword parameters
assert_type(IniFile().get("some_key", type="regex", list=True), list[re.Pattern[str]])
assert_type(IniFile().get("some_key", type="regex", list=True, group=None), list[re.Pattern[str]])
assert_type(IniFile().get("some_key", type="regex", list=True, group="group"), list[re.Pattern[str]])
assert_type(IniFile().get("some_key", type="regex", list=True, locale=False), list[re.Pattern[str]])
assert_type(IniFile().get("some_key", type="regex", list=True, locale=True), list[re.Pattern[str]])
assert_type(IniFile().get("some_key", type="regex", list=True, strict=False), list[re.Pattern[str]])
assert_type(IniFile().get("some_key", type="regex", list=True, strict=True), list[re.Pattern[str]])
assert_type(IniFile().get("some_key", type="regex", list=True, group="group", locale=True, strict=True), list[re.Pattern[str]])

# Get point
assert_type(IniFile().get("some_key", "group", True, "point"), tuple[int, int])
assert_type(IniFile().get("some_key", "group", True, "point", False), tuple[int, int])
assert_type(IniFile().get("some_key", "group", True, "point", False, False), tuple[int, int])
assert_type(IniFile().get("some_key", "group", True, "point", False, True), tuple[int, int])
# Keyword parameters
assert_type(IniFile().get("some_key", type="point"), tuple[int, int])
assert_type(IniFile().get("some_key", type="point", group=None), tuple[int, int])
assert_type(IniFile().get("some_key", type="point", group="group"), tuple[int, int])
assert_type(IniFile().get("some_key", type="point", locale=False), tuple[int, int])
assert_type(IniFile().get("some_key", type="point", locale=True), tuple[int, int])
assert_type(IniFile().get("some_key", type="point", strict=False), tuple[int, int])
assert_type(IniFile().get("some_key", type="point", strict=True), tuple[int, int])
assert_type(IniFile().get("some_key", type="point", group="group", locale=True, strict=True), tuple[int, int])
# Explicitly set list.
assert_type(IniFile().get("some_key", type="point", list=False), tuple[int, int])
assert_type(IniFile().get("some_key", type="point", group=None, list=False), tuple[int, int])
assert_type(IniFile().get("some_key", type="point", group="group", list=False), tuple[int, int])
assert_type(IniFile().get("some_key", type="point", locale=False, list=False), tuple[int, int])
assert_type(IniFile().get("some_key", type="point", locale=True, list=False), tuple[int, int])
assert_type(IniFile().get("some_key", type="point", strict=False, list=False), tuple[int, int])
assert_type(IniFile().get("some_key", type="point", strict=True, list=False), tuple[int, int])
assert_type(IniFile().get("some_key", type="point", group="group", locale=True, strict=True, list=False), tuple[int, int])

# Get list[point]
assert_type(IniFile().get("some_key", "group", True, "point", True), list[tuple[int, int]])
assert_type(IniFile().get("some_key", "group", True, "point", True, False), list[tuple[int, int]])
assert_type(IniFile().get("some_key", "group", True, "point", True, True), list[tuple[int, int]])
# Keyword parameters
assert_type(IniFile().get("some_key", type="point", list=True), list[tuple[int, int]])
assert_type(IniFile().get("some_key", type="point", list=True, group=None), list[tuple[int, int]])
assert_type(IniFile().get("some_key", type="point", list=True, group="group"), list[tuple[int, int]])
assert_type(IniFile().get("some_key", type="point", list=True, locale=False), list[tuple[int, int]])
assert_type(IniFile().get("some_key", type="point", list=True, locale=True), list[tuple[int, int]])
assert_type(IniFile().get("some_key", type="point", list=True, strict=False), list[tuple[int, int]])
assert_type(IniFile().get("some_key", type="point", list=True, strict=True), list[tuple[int, int]])
assert_type(IniFile().get("some_key", type="point", list=True, group="group", locale=True, strict=True), list[tuple[int, int]])
