from typing import NewType, Union

from .version import Version

NormalizedName = NewType("NormalizedName", str)

def canonicalize_name(name: str) -> NormalizedName: ...
def canonicalize_version(_version: str) -> Union[Version, str]: ...
