import logging
import re
import subprocess
import sys
from _typeshed import ReadableBuffer, StrOrBytesPath, SupportsRead
from collections.abc import Callable, Iterable, Mapping
from datetime import datetime
from typing import Any, ClassVar, Final, Literal, TypeAlias, TypeVar, overload

_T = TypeVar("_T")

# A file-like object or a path to a file.
_FileObjOrPath: TypeAlias = SupportsRead[bytes] | str
# A single key id, or a list/tuple/set of them. Other iterables are
# treated as a single key id at runtime.
_KeyIds: TypeAlias = str | list[str] | tuple[str, ...] | set[str] | frozenset[str]
# A key record parsed from `gpg --with-colons` output
_KeyInfo: TypeAlias = dict[str, Any]
_TrustLevel: TypeAlias = Literal[
    "TRUST_EXPIRED", "TRUST_UNDEFINED", "TRUST_NEVER", "TRUST_MARGINAL", "TRUST_FULLY", "TRUST_ULTIMATE"
]

__version__: str
__author__: str
__date__: str

if sys.platform == "win32":
    STARTUPINFO: type[subprocess.STARTUPINFO] | None
else:
    STARTUPINFO: None
    UNSAFE: re.Pattern[str]

string_types: type[str]
text_type: type[str]
path_types: tuple[type[str]]
logger: logging.Logger
log_everything: bool
fsencoding: str

def shell_quote(s: str) -> str: ...
def no_quote(s: _T) -> _T: ...

class StatusHandler:
    on_data_failure: Exception | None
    gpg: GPG
    # Set once the gpg subprocess has run
    data: bytes
    stderr: str
    returncode: int | None
    def __init__(self, gpg: GPG) -> None: ...
    def handle_status(self, key: str, value: str) -> None: ...

class Verify(StatusHandler):
    TRUST_EXPIRED: Final = 0
    TRUST_UNDEFINED: Final = 1
    TRUST_NEVER: Final = 2
    TRUST_MARGINAL: Final = 3
    TRUST_FULLY: Final = 4
    TRUST_ULTIMATE: Final = 5
    TRUST_LEVELS: ClassVar[dict[str, int]]
    GPG_SYSTEM_ERROR_CODES: ClassVar[dict[int, str]]
    GPG_ERROR_CODES: ClassVar[dict[int, str]]
    valid: bool
    fingerprint: str | None
    creation_date: str | None
    timestamp: str | None
    signature_id: str | None
    key_id: str | None
    username: str | None
    key_status: str | None
    status: str | None
    pubkey_fingerprint: str | None
    expire_timestamp: str | None
    sig_timestamp: str | None
    trust_text: str | None
    trust_level: int | None
    sig_info: dict[str, dict[str, str | int | None]]
    problems: list[dict[str, str | None]]
    def __init__(self, gpg: GPG) -> None: ...
    def __bool__(self) -> bool: ...
    __nonzero__ = __bool__
    def handle_status(self, key: str, value: str) -> None: ...

class ImportResult(StatusHandler):
    counts: ClassVar[list[str]]
    results: list[dict[str, str | None]]
    fingerprints: list[str]
    count: int
    no_user_id: int
    imported: int
    imported_rsa: int
    unchanged: int
    n_uids: int
    n_subk: int
    n_sigs: int
    n_revoc: int
    sec_read: int
    sec_imported: int
    sec_dups: int
    not_imported: int
    ok_reason: ClassVar[dict[str, str]]
    problem_reason: ClassVar[dict[str, str]]
    def __init__(self, gpg: GPG) -> None: ...
    def __bool__(self) -> bool: ...
    __nonzero__ = __bool__
    def handle_status(self, key: str, value: str) -> None: ...
    def summary(self) -> str: ...

ESCAPE_PATTERN: re.Pattern[str]
BASIC_ESCAPES: dict[str, str]

class SendResult(StatusHandler):
    def handle_status(self, key: str, value: str) -> None: ...

class SearchKeys(StatusHandler, list[_KeyInfo]):
    UID_INDEX: ClassVar[int]
    FIELDS: ClassVar[list[str]]
    curkey: _KeyInfo | None
    fingerprints: list[str]
    uids: list[str]
    uid_map: dict[str, dict[str, str]]
    def __init__(self, gpg: GPG) -> None: ...
    def get_fields(self, args: list[str]) -> _KeyInfo: ...
    def pub(self, args: list[str]) -> None: ...
    def uid(self, args: list[str]) -> None: ...
    def handle_status(self, key: str, value: str) -> None: ...

class ListKeys(SearchKeys):
    in_subkey: bool
    key_map: dict[str, _KeyInfo]
    def __init__(self, gpg: GPG) -> None: ...
    def key(self, args: list[str]) -> None: ...
    pub = key
    sec = key
    def fpr(self, args: list[str]) -> None: ...
    def grp(self, args: list[str]) -> None: ...
    def sub(self, args: list[str]) -> None: ...
    def ssb(self, args: list[str]) -> None: ...
    def sig(self, args: list[str]) -> None: ...

class ScanKeys(ListKeys):
    def sub(self, args: list[str]) -> None: ...

class TextHandler: ...

class Crypt(Verify, TextHandler):
    ok: bool
    status: str
    status_detail: str
    def __init__(self, gpg: GPG) -> None: ...
    def __bool__(self) -> bool: ...
    __nonzero__ = __bool__
    def handle_status(self, key: str, value: str) -> None: ...

class GenKey(StatusHandler):
    type: str | None
    fingerprint: str
    status: str | None
    def __init__(self, gpg: GPG) -> None: ...
    def __bool__(self) -> bool: ...
    __nonzero__ = __bool__
    def handle_status(self, key: str, value: str) -> None: ...

class AddSubkey(StatusHandler):
    type: str | None
    fingerprint: str
    status: str | None
    def __init__(self, gpg: GPG) -> None: ...
    def __bool__(self) -> bool: ...
    __nonzero__ = __bool__
    def handle_status(self, key: str, value: str) -> None: ...

class ExportResult(GenKey):
    def handle_status(self, key: str, value: str) -> None: ...

class DeleteResult(StatusHandler):
    status: str
    problem_reason: ClassVar[dict[str, str]]
    def __init__(self, gpg: GPG) -> None: ...
    def handle_status(self, key: str, value: str) -> None: ...
    def __bool__(self) -> bool: ...
    __nonzero__ = __bool__

class TrustResult(DeleteResult): ...

class Sign(StatusHandler, TextHandler):
    type: str | None
    hash_algo: str | None
    fingerprint: str | None
    timestamp: str | None
    status: str | None
    status_detail: str | None
    key_id: str | None
    username: str | None
    def __init__(self, gpg: GPG) -> None: ...
    def __bool__(self) -> bool: ...
    __nonzero__ = __bool__
    def handle_status(self, key: str, value: str) -> None: ...

class AutoLocateKey(StatusHandler):
    fingerprint: str | None
    type: str | None
    key_length: int
    created_at: datetime | None
    email: str | None
    email_real_name: str | None
    def __init__(self, gpg: GPG) -> None: ...
    def handle_status(self, key: str, value: str) -> None: ...
    def pub(self, args: list[str]) -> None: ...
    def uid(self, args: list[str]) -> None: ...
    def sub(self, args: list[str]) -> None: ...
    def fpr(self, args: list[str]) -> None: ...

VERSION_RE: re.Pattern[bytes]
HEX_DIGITS_RE: re.Pattern[str]
PUBLIC_KEY_RE: re.Pattern[str]

class GPG:
    error_map: Mapping[int, str] | None
    decode_errors: str
    buffer_size: int
    result_map: dict[str, type[StatusHandler]]
    gpgbinary: str
    gnupghome: str | None
    env: Mapping[str, str] | None
    keyring: list[str] | None
    secret_keyring: list[str] | None
    verbose: bool
    use_agent: bool
    options: list[str] | None
    # Called with each chunk of output data; return False to discard the chunk
    on_data: Callable[[bytes], object] | None
    encoding: str
    version: tuple[int, ...] | None
    check_fingerprint_collisions: bool
    def __init__(
        self,
        gpgbinary: str = "gpg",
        gnupghome: str | None = None,
        verbose: bool = False,
        use_agent: bool = False,
        keyring: str | list[str] | None = None,
        options: str | list[str] | None = None,
        secret_keyring: str | list[str] | None = None,
        env: Mapping[str, str] | None = None,
        encoding: str = "latin-1",
    ) -> None: ...
    def make_args(self, args: Iterable[str], passphrase: bool) -> list[str]: ...
    def is_valid_file(self, fileobj: object) -> bool: ...
    def sign(
        self,
        message: str | ReadableBuffer,
        *,
        keyid: str | None = None,
        passphrase: str | None = None,
        clearsign: bool = True,
        detach: bool = False,
        binary: bool = False,
        output: str | None = None,
        extra_args: Iterable[str] | None = None,
    ) -> Sign: ...
    def set_output_without_confirmation(self, args: list[str], output: str) -> None: ...
    def is_valid_passphrase(self, passphrase: str) -> bool: ...
    def sign_file(
        self,
        fileobj_or_path: _FileObjOrPath,
        keyid: str | None = None,
        passphrase: str | None = None,
        clearsign: bool = True,
        detach: bool = False,
        binary: bool = False,
        output: str | None = None,
        extra_args: Iterable[str] | None = None,
    ) -> Sign: ...
    def verify(
        self,
        data: str | ReadableBuffer,
        *,
        data_filename: str | None = None,
        close_file: bool = True,
        extra_args: Iterable[str] | None = None,
    ) -> Verify: ...
    def verify_file(
        self,
        fileobj_or_path: _FileObjOrPath,
        data_filename: str | None = None,
        close_file: bool = True,
        extra_args: Iterable[str] | None = None,
    ) -> Verify: ...
    def verify_data(self, sig_filename: str, data: ReadableBuffer, extra_args: Iterable[str] | None = None) -> Verify: ...
    def import_keys(
        self, key_data: str | ReadableBuffer, extra_args: Iterable[str] | None = None, passphrase: str | None = None
    ) -> ImportResult: ...
    def import_keys_file(
        self, key_path: StrOrBytesPath, *, extra_args: Iterable[str] | None = None, passphrase: str | None = None
    ) -> ImportResult: ...
    def recv_keys(self, keyserver: str, *keyids: str, extra_args: Iterable[str] = ...) -> ImportResult: ...
    def send_keys(self, keyserver: str, *keyids: str, extra_args: Iterable[str] = ...) -> SendResult: ...
    def delete_keys(
        self,
        fingerprints: _KeyIds,
        secret: bool = False,
        passphrase: str | None = None,
        expect_passphrase: bool = True,
        exclamation_mode: bool = False,
    ) -> DeleteResult: ...

    @overload
    def export_keys(
        self,
        keyids: _KeyIds,
        secret: bool = False,
        armor: Literal[True] = True,
        minimal: bool = False,
        passphrase: str | None = None,
        expect_passphrase: bool = True,
        output: str | None = None,
    ) -> str: ...
    @overload
    def export_keys(
        self,
        keyids: _KeyIds,
        secret: bool,
        armor: Literal[False],
        minimal: bool = False,
        passphrase: str | None = None,
        expect_passphrase: bool = True,
        output: str | None = None,
    ) -> bytes: ...
    @overload
    def export_keys(
        self,
        keyids: _KeyIds,
        secret: bool = False,
        *,
        armor: Literal[False],
        minimal: bool = False,
        passphrase: str | None = None,
        expect_passphrase: bool = True,
        output: str | None = None,
    ) -> bytes: ...
    @overload
    def export_keys(
        self,
        keyids: _KeyIds,
        secret: bool = False,
        armor: bool = True,
        minimal: bool = False,
        passphrase: str | None = None,
        expect_passphrase: bool = True,
        output: str | None = None,
    ) -> str | bytes: ...

    def list_keys(self, secret: bool = False, keys: str | Iterable[str] | None = None, sigs: bool = False) -> ListKeys: ...
    def scan_keys(self, filename: str) -> ScanKeys: ...
    def scan_keys_mem(self, key_data: str | ReadableBuffer) -> ScanKeys: ...
    def search_keys(self, query: str, keyserver: str = "pgp.mit.edu", extra_args: Iterable[str] | None = None) -> SearchKeys: ...
    def auto_locate_key(
        self, email: str, mechanisms: Iterable[str] | None = None, *, extra_args: Iterable[str] = ...
    ) -> AutoLocateKey: ...
    def gen_key(self, input: str | ReadableBuffer) -> GenKey: ...
    def gen_key_input(self, *, no_protection: bool = False, **kwargs: object) -> str: ...
    def add_subkey(
        self,
        master_key: str,
        master_passphrase: str | None = None,
        algorithm: str = "rsa",
        usage: str = "encrypt",
        expire: str = "-",
    ) -> AddSubkey: ...
    def quick_sign_key(
        self, certifier_fingerprint: str, recipient_fingerprint: str, certifier_passphrase: str | None = None
    ) -> Sign: ...
    def encrypt_file(
        self,
        fileobj_or_path: _FileObjOrPath,
        recipients: _KeyIds | None,
        hidden_recipients: _KeyIds | None = None,
        sign: str | bool | None = None,
        always_trust: bool = False,
        passphrase: str | None = None,
        armor: bool = True,
        output: str | None = None,
        symmetric: str | bool = False,
        extra_args: Iterable[str] | None = None,
    ) -> Crypt: ...
    def encrypt(
        self,
        data: str | ReadableBuffer,
        recipients: _KeyIds | None,
        *,
        hidden_recipients: _KeyIds | None = None,
        sign: str | bool | None = None,
        always_trust: bool = False,
        passphrase: str | None = None,
        armor: bool = True,
        output: str | None = None,
        symmetric: str | bool = False,
        extra_args: Iterable[str] | None = None,
    ) -> Crypt: ...
    def decrypt(
        self,
        message: str | ReadableBuffer,
        *,
        always_trust: bool = False,
        passphrase: str | None = None,
        output: str | None = None,
        extra_args: Iterable[str] | None = None,
    ) -> Crypt: ...
    def decrypt_file(
        self,
        fileobj_or_path: _FileObjOrPath,
        always_trust: bool = False,
        passphrase: str | None = None,
        output: str | None = None,
        extra_args: Iterable[str] | None = None,
    ) -> Crypt: ...
    def get_recipients(self, message: str | ReadableBuffer, *, extra_args: Iterable[str] | None = None) -> list[str]: ...
    def get_recipients_file(self, fileobj_or_path: _FileObjOrPath, extra_args: Iterable[str] | None = None) -> list[str]: ...
    def trust_keys(self, fingerprints: str | Iterable[str], trustlevel: _TrustLevel) -> TrustResult: ...
