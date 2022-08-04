from typing_extensions import TypedDict

# TODO: remove if python/typeshed#8484 is merged
# from .__version__ import __version__ as requests_version

class _VersionDict(TypedDict):
    version: str

class _OptionalVersionDict(TypedDict):
    version: str | None

class _PlatformDict(TypedDict):
    system: str
    release: str

class _ImplementationDict(_VersionDict):
    name: str

class _PyOpenSSLDict(_OptionalVersionDict):
    openssl_version: str

class _InfoDict(TypedDict):
    platform: _PlatformDict
    implementation: _ImplementationDict
    system_ssl: _VersionDict
    using_pyopenssl: bool
    using_charset_normalizer: bool
    pyOpenSSL: _PyOpenSSLDict
    urllib3: _VersionDict
    chardet: _OptionalVersionDict
    charset_normalizer: _OptionalVersionDict
    cryptography: _VersionDict
    idna: _VersionDict
    requests: _VersionDict

def info() -> _InfoDict: ...
def main() -> None: ...
