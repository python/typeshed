from __future__ import annotations

from xdg.IniFile import IniFile

ini_file = IniFile()

# The "get" method is quite complex with many overloads. Check that many forms
# are valid.
# The function definition is:
# def get(self, key, group=None, locale=False, type="string", list=False, strict=False):

# Get str
IniFile().get("some_key")
IniFile().get("some_key", None)
IniFile().get("some_key", "group")
IniFile().get("some_key", "group", False)
IniFile().get("some_key", "group", True)
IniFile().get("some_key", "group", True, "string")
IniFile().get("some_key", "group", True, "string", False)
IniFile().get("some_key", "group", True, "string", False, False)
IniFile().get("some_key", "group", True, "string", False, True)
# Keyword parameters
IniFile().get("some_key", group=None)
IniFile().get("some_key", group="group")
IniFile().get("some_key", locale=False)
IniFile().get("some_key", locale=True)
IniFile().get("some_key", strict=False)
IniFile().get("some_key", strict=True)
IniFile().get("some_key", group="group", locale=True, strict=True)
# Explicitly set type as string in keyword parameters.
IniFile().get("some_key", type="string")
IniFile().get("some_key", group=None, type="string")
IniFile().get("some_key", group="group", type="string")
IniFile().get("some_key", locale=False, type="string")
IniFile().get("some_key", locale=True, type="string")
IniFile().get("some_key", strict=False, type="string")
IniFile().get("some_key", strict=True, type="string")
IniFile().get("some_key", group="group", locale=True, strict=True, type="string")
# Explicitly set list.
IniFile().get("some_key", list=False)
IniFile().get("some_key", group=None, list=False)
IniFile().get("some_key", group="group", list=False)
IniFile().get("some_key", locale=False, list=False)
IniFile().get("some_key", locale=True, list=False)
IniFile().get("some_key", strict=False, list=False)
IniFile().get("some_key", strict=True, list=False)
IniFile().get("some_key", group="group", locale=True, strict=True, list=False)
# Explicitly set both.
IniFile().get("some_key", list=False, type="string")
IniFile().get("some_key", group=None, list=False, type="string")
IniFile().get("some_key", group="group", list=False, type="string")
IniFile().get("some_key", locale=False, list=False, type="string")
IniFile().get("some_key", locale=True, list=False, type="string")
IniFile().get("some_key", strict=False, list=False, type="string")
IniFile().get("some_key", strict=True, list=False, type="string")
IniFile().get("some_key", group="group", locale=True, strict=True, list=False, type="string")

# Get list[str]
IniFile().get("some_key", "group", True, "string", True)
IniFile().get("some_key", "group", True, "string", True, False)
IniFile().get("some_key", "group", True, "string", True, True)
# Keyword parameters
IniFile().get("some_key", list=True, group=None)
IniFile().get("some_key", list=True, group="group")
IniFile().get("some_key", list=True, locale=False)
IniFile().get("some_key", list=True, locale=True)
IniFile().get("some_key", list=True, strict=False)
IniFile().get("some_key", list=True, strict=True)
IniFile().get("some_key", list=True, group="group", locale=True, strict=True)
# Explicitly set list.
IniFile().get("some_key", list=True)
IniFile().get("some_key", group=None, list=True)
IniFile().get("some_key", group="group", list=True)
IniFile().get("some_key", locale=False, list=True)
IniFile().get("some_key", locale=True, list=True)
IniFile().get("some_key", strict=False, list=True)
IniFile().get("some_key", strict=True, list=True)
IniFile().get("some_key", group="group", locale=True, strict=True, list=True)
# Explicitly set both.
IniFile().get("some_key", list=True, type="string")
IniFile().get("some_key", group=None, list=True, type="string")
IniFile().get("some_key", group="group", list=True, type="string")
IniFile().get("some_key", locale=False, list=True, type="string")
IniFile().get("some_key", locale=True, list=True, type="string")
IniFile().get("some_key", strict=False, list=True, type="string")
IniFile().get("some_key", strict=True, list=True, type="string")
IniFile().get("some_key", group="group", locale=True, strict=True, list=True, type="string")

# Get bool
IniFile().get("some_key", "group", True, "boolean")
IniFile().get("some_key", "group", True, "boolean", False)
IniFile().get("some_key", "group", True, "boolean", False, False)
IniFile().get("some_key", "group", True, "boolean", False, True)
# Keyword parameters
IniFile().get("some_key", type="boolean")
IniFile().get("some_key", type="boolean", group=None)
IniFile().get("some_key", type="boolean", group="group")
IniFile().get("some_key", type="boolean", locale=False)
IniFile().get("some_key", type="boolean", locale=True)
IniFile().get("some_key", type="boolean", strict=False)
IniFile().get("some_key", type="boolean", strict=True)
IniFile().get("some_key", type="boolean", group="group", locale=True, strict=True)
# Explicitly set list.
IniFile().get("some_key", type="boolean", list=False)
IniFile().get("some_key", type="boolean", group=None, list=False)
IniFile().get("some_key", type="boolean", group="group", list=False)
IniFile().get("some_key", type="boolean", locale=False, list=False)
IniFile().get("some_key", type="boolean", locale=True, list=False)
IniFile().get("some_key", type="boolean", strict=False, list=False)
IniFile().get("some_key", type="boolean", strict=True, list=False)
IniFile().get("some_key", type="boolean", group="group", locale=True, strict=True, list=False)

# Get list[bool]
IniFile().get("some_key", "group", True, "boolean", True)
IniFile().get("some_key", "group", True, "boolean", True, False)
IniFile().get("some_key", "group", True, "boolean", True, True)
# Keyword parameters
IniFile().get("some_key", type="boolean", list=True)
IniFile().get("some_key", type="boolean", list=True, group=None)
IniFile().get("some_key", type="boolean", list=True, group="group")
IniFile().get("some_key", type="boolean", list=True, locale=False)
IniFile().get("some_key", type="boolean", list=True, locale=True)
IniFile().get("some_key", type="boolean", list=True, strict=False)
IniFile().get("some_key", type="boolean", list=True, strict=True)
IniFile().get("some_key", type="boolean", list=True, group="group", locale=True, strict=True)

# Get int
IniFile().get("some_key", "group", True, "integer")
IniFile().get("some_key", "group", True, "integer", False)
IniFile().get("some_key", "group", True, "integer", False, False)
IniFile().get("some_key", "group", True, "integer", False, True)
# Keyword parameters
IniFile().get("some_key", type="integer")
IniFile().get("some_key", type="integer", group=None)
IniFile().get("some_key", type="integer", group="group")
IniFile().get("some_key", type="integer", locale=False)
IniFile().get("some_key", type="integer", locale=True)
IniFile().get("some_key", type="integer", strict=False)
IniFile().get("some_key", type="integer", strict=True)
IniFile().get("some_key", type="integer", group="group", locale=True, strict=True)
# Explicitly set list.
IniFile().get("some_key", type="integer", list=False)
IniFile().get("some_key", type="integer", group=None, list=False)
IniFile().get("some_key", type="integer", group="group", list=False)
IniFile().get("some_key", type="integer", locale=False, list=False)
IniFile().get("some_key", type="integer", locale=True, list=False)
IniFile().get("some_key", type="integer", strict=False, list=False)
IniFile().get("some_key", type="integer", strict=True, list=False)
IniFile().get("some_key", type="integer", group="group", locale=True, strict=True, list=False)

# Get list[int]
IniFile().get("some_key", "group", True, "integer", True)
IniFile().get("some_key", "group", True, "integer", True, False)
IniFile().get("some_key", "group", True, "integer", True, True)
# Keyword parameters
IniFile().get("some_key", type="integer", list=True)
IniFile().get("some_key", type="integer", list=True, group=None)
IniFile().get("some_key", type="integer", list=True, group="group")
IniFile().get("some_key", type="integer", list=True, locale=False)
IniFile().get("some_key", type="integer", list=True, locale=True)
IniFile().get("some_key", type="integer", list=True, strict=False)
IniFile().get("some_key", type="integer", list=True, strict=True)
IniFile().get("some_key", type="integer", list=True, group="group", locale=True, strict=True)

# Get float
IniFile().get("some_key", "group", True, "numeric")
IniFile().get("some_key", "group", True, "numeric", False)
IniFile().get("some_key", "group", True, "numeric", False, False)
IniFile().get("some_key", "group", True, "numeric", False, True)
# Keyword parameters
IniFile().get("some_key", type="numeric")
IniFile().get("some_key", type="numeric", group=None)
IniFile().get("some_key", type="numeric", group="group")
IniFile().get("some_key", type="numeric", locale=False)
IniFile().get("some_key", type="numeric", locale=True)
IniFile().get("some_key", type="numeric", strict=False)
IniFile().get("some_key", type="numeric", strict=True)
IniFile().get("some_key", type="numeric", group="group", locale=True, strict=True)
# Explicitly set list.
IniFile().get("some_key", type="numeric", list=False)
IniFile().get("some_key", type="numeric", group=None, list=False)
IniFile().get("some_key", type="numeric", group="group", list=False)
IniFile().get("some_key", type="numeric", locale=False, list=False)
IniFile().get("some_key", type="numeric", locale=True, list=False)
IniFile().get("some_key", type="numeric", strict=False, list=False)
IniFile().get("some_key", type="numeric", strict=True, list=False)
IniFile().get("some_key", type="numeric", group="group", locale=True, strict=True, list=False)

# Get list[float]
IniFile().get("some_key", "group", True, "numeric", True)
IniFile().get("some_key", "group", True, "numeric", True, False)
IniFile().get("some_key", "group", True, "numeric", True, True)
# Keyword parameters
IniFile().get("some_key", type="numeric", list=True)
IniFile().get("some_key", type="numeric", list=True, group=None)
IniFile().get("some_key", type="numeric", list=True, group="group")
IniFile().get("some_key", type="numeric", list=True, locale=False)
IniFile().get("some_key", type="numeric", list=True, locale=True)
IniFile().get("some_key", type="numeric", list=True, strict=False)
IniFile().get("some_key", type="numeric", list=True, strict=True)
IniFile().get("some_key", type="numeric", list=True, group="group", locale=True, strict=True)

# Get regex
IniFile().get("some_key", "group", True, "regex")
IniFile().get("some_key", "group", True, "regex", False)
IniFile().get("some_key", "group", True, "regex", False, False)
IniFile().get("some_key", "group", True, "regex", False, True)
# Keyword parameters
IniFile().get("some_key", type="regex")
IniFile().get("some_key", type="regex", group=None)
IniFile().get("some_key", type="regex", group="group")
IniFile().get("some_key", type="regex", locale=False)
IniFile().get("some_key", type="regex", locale=True)
IniFile().get("some_key", type="regex", strict=False)
IniFile().get("some_key", type="regex", strict=True)
IniFile().get("some_key", type="regex", group="group", locale=True, strict=True)
# Explicitly set list.
IniFile().get("some_key", type="regex", list=False)
IniFile().get("some_key", type="regex", group=None, list=False)
IniFile().get("some_key", type="regex", group="group", list=False)
IniFile().get("some_key", type="regex", locale=False, list=False)
IniFile().get("some_key", type="regex", locale=True, list=False)
IniFile().get("some_key", type="regex", strict=False, list=False)
IniFile().get("some_key", type="regex", strict=True, list=False)
IniFile().get("some_key", type="regex", group="group", locale=True, strict=True, list=False)

# Get list[regex]
IniFile().get("some_key", "group", True, "regex", True)
IniFile().get("some_key", "group", True, "regex", True, False)
IniFile().get("some_key", "group", True, "regex", True, True)
# Keyword parameters
IniFile().get("some_key", type="regex", list=True)
IniFile().get("some_key", type="regex", list=True, group=None)
IniFile().get("some_key", type="regex", list=True, group="group")
IniFile().get("some_key", type="regex", list=True, locale=False)
IniFile().get("some_key", type="regex", list=True, locale=True)
IniFile().get("some_key", type="regex", list=True, strict=False)
IniFile().get("some_key", type="regex", list=True, strict=True)
IniFile().get("some_key", type="regex", list=True, group="group", locale=True, strict=True)

# Get point
IniFile().get("some_key", "group", True, "point")
IniFile().get("some_key", "group", True, "point", False)
IniFile().get("some_key", "group", True, "point", False, False)
IniFile().get("some_key", "group", True, "point", False, True)
# Keyword parameters
IniFile().get("some_key", type="point")
IniFile().get("some_key", type="point", group=None)
IniFile().get("some_key", type="point", group="group")
IniFile().get("some_key", type="point", locale=False)
IniFile().get("some_key", type="point", locale=True)
IniFile().get("some_key", type="point", strict=False)
IniFile().get("some_key", type="point", strict=True)
IniFile().get("some_key", type="point", group="group", locale=True, strict=True)
# Explicitly set list.
IniFile().get("some_key", type="point", list=False)
IniFile().get("some_key", type="point", group=None, list=False)
IniFile().get("some_key", type="point", group="group", list=False)
IniFile().get("some_key", type="point", locale=False, list=False)
IniFile().get("some_key", type="point", locale=True, list=False)
IniFile().get("some_key", type="point", strict=False, list=False)
IniFile().get("some_key", type="point", strict=True, list=False)
IniFile().get("some_key", type="point", group="group", locale=True, strict=True, list=False)

# Get list[point]
IniFile().get("some_key", "group", True, "point", True)
IniFile().get("some_key", "group", True, "point", True, False)
IniFile().get("some_key", "group", True, "point", True, True)
# Keyword parameters
IniFile().get("some_key", type="point", list=True)
IniFile().get("some_key", type="point", list=True, group=None)
IniFile().get("some_key", type="point", list=True, group="group")
IniFile().get("some_key", type="point", list=True, locale=False)
IniFile().get("some_key", type="point", list=True, locale=True)
IniFile().get("some_key", type="point", list=True, strict=False)
IniFile().get("some_key", type="point", list=True, strict=True)
IniFile().get("some_key", type="point", list=True, group="group", locale=True, strict=True)
