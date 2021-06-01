from _typeshed import StrOrBytesPath, SupportsWrite
from distutils.cmd import Command
from typing import IO, Any, Dict, Iterable, List, Mapping, Tuple, Type, Union

class DistributionMetadata:
    def __init__(self, path: int | StrOrBytesPath | None = ...) -> None: ...
    name: str | None
    version: str | None
    author: str | None
    author_email: str | None
    maintainer: str | None
    maintainer_email: str | None
    url: str | None
    license: str | None
    description: str | None
    long_description: str | None
    keywords: str | List[str] | None
    platforms: str | List[str] | None
    classifiers: str | List[str] | None
    download_url: str | None
    provides: List[str] | None
    requires: List[str] | None
    obsoletes: List[str] | None
    def read_pkg_file(self, file: IO[str]) -> None: ...
    def write_pkg_info(self, base_dir: str) -> None: ...
    def write_pkg_file(self, file: SupportsWrite[str]) -> None: ...
    def get_name(self) -> str: ...
    def get_version(self) -> str: ...
    def get_fullname(self) -> str: ...
    def get_author(self) -> str: ...
    def get_author_email(self) -> str: ...
    def get_maintainer(self) -> str: ...
    def get_maintainer_email(self) -> str: ...
    def get_contact(self) -> str: ...
    def get_contact_email(self) -> str: ...
    def get_url(self) -> str: ...
    def get_license(self) -> str: ...
    def get_licence(self) -> str: ...
    def get_description(self) -> str: ...
    def get_long_description(self) -> str: ...
    def get_keywords(self) -> str | List[str]: ...
    def get_platforms(self) -> str | List[str]: ...
    def get_classifiers(self) -> str | List[str]: ...
    def get_download_url(self) -> str: ...
    def get_requires(self) -> List[str]: ...
    def set_requires(self, value: Iterable[str]) -> None: ...
    def get_provides(self) -> List[str]: ...
    def set_provides(self, value: Iterable[str]) -> None: ...
    def get_obsoletes(self) -> List[str]: ...
    def set_obsoletes(self, value: Iterable[str]) -> None: ...

class Distribution:
    cmdclass: Dict[str, Type[Command]]
    metadata: DistributionMetadata
    def __init__(self, attrs: Mapping[str, Any] | None = ...) -> None: ...
    def get_option_dict(self, command: str) -> Dict[str, Tuple[str, str]]: ...
    def parse_config_files(self, filenames: Iterable[str] | None = ...) -> None: ...
    def get_command_obj(self, command: str, create: bool = ...) -> Command | None: ...
