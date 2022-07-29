from typing_extensions import TypedDict

class VersionDict(TypedDict):
    version: str

class OptionalVersionDict(TypedDict):
    version: str | None

class PlatformDict(TypedDict):
    system: str
    release: str

class ImplementationDict(VersionDict):
    name: str

class PyOpenSSLDict(OptionalVersionDict):
    openssl_version: str

class InfoDict(TypedDict):
    platform: PlatformDict
    implementation: ImplementationDict
    system_ssl: VersionDict
    using_pyopenssl: bool
    using_charset_normalizer: bool
    pyOpenSSL: PyOpenSSLDict
    urllib3: VersionDict
    chardet: OptionalVersionDict
    charset_normalizer: OptionalVersionDict
    cryptography: VersionDict
    idna: VersionDict
    requests: VersionDict

def _implementation() -> dict[str, str]: ...
def info() -> InfoDict: ...
def main() -> None: ...
