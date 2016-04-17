from sys import _version_info

class _Feature:
    def getOptionalRelease(self) -> _version_info: ...
    def getMandatoryRelease(self) -> _version_info: ...

absolute_import = None  # type: _Feature
division = None  # type: _Feature
generators = None  # type: _Feature
nested_scopes = None  # type: _Feature
print_function = None  # type: _Feature
unicode_literals = None  # type: _Feature
with_statement = None  # type: _Feature
