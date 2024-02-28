from _typeshed import StrOrBytesPath
from collections.abc import Callable
from contextlib import AbstractContextManager
from typing import Protocol
from typing_extensions import ParamSpec, Self, TypeAlias

from _cffi_backend import _CDataBase

from ._pygit2 import DiffFile, Oid
from .enums import CheckoutNotify, CheckoutStrategy, CredentialType, StashApplyProgress
from .remotes import TransferProgress
from .utils import _IntoStrArray

class Payload:
    def __init__(self, **kw: dict[str, object]) -> None: ...
    def check_error(self, error_code: int) -> None: ...

# Upstream is not yet defining a concrete type for certificates, and no usage example is
# available either.
_Certificate: TypeAlias = None

class _Credentials(Protocol):
    @property
    def credential_type(self) -> CredentialType: ...
    @property
    def credential_tuple(self) -> tuple[str, ...]: ...
    def __call__(self, _url: str, _username: str | None, _allowed: CredentialType) -> Self: ...

class RemoteCallbacks(Payload):
    # Upstream code is broken: the credentials() method is shadowed if the constructor
    # gets passed a non-None "credentials".
    # credentials: _Credentials | None
    certificate: _Certificate | None
    def __init__(self, credentials: _Credentials | None = None, certificate: _Certificate | None = None) -> None: ...
    def sideband_progress(self, string: str) -> None: ...
    def credentials(self, url: str, username_from_url: str | None, allowed_types: CredentialType) -> _Credentials: ...
    def certificate_check(self, certificate: _Certificate, valid: bool, host: str) -> bool: ...
    def transfer_progress(self, stats: TransferProgress) -> None: ...
    def update_tips(self, refname: str, old: Oid, new: Oid) -> None: ...
    def push_update_reference(self, refname: str, message: str) -> None: ...

class CheckoutCallbacks(Payload):
    def __init__(self) -> None: ...
    def checkout_notify_flags(self) -> CheckoutNotify: ...
    def checkout_notify(
        self, why: CheckoutNotify, path: str, baseline: DiffFile | None, target: DiffFile | None, workdir: DiffFile | None
    ) -> None: ...
    def checkout_progress(self, path: str, completed_steps: int, total_steps: int) -> None: ...

class StashApplyCallbacks(CheckoutCallbacks):
    def stash_apply_progress(self, progress: StashApplyProgress) -> None: ...

def git_clone_options(payload: Payload, opts: _CDataBase | None = None) -> AbstractContextManager[Payload]: ...
def git_fetch_options(payload: Payload, opts: _CDataBase | None = None) -> AbstractContextManager[Payload]: ...
def git_push_options(payload: Payload, opts: _CDataBase | None = None) -> AbstractContextManager[Payload]: ...
def git_remote_callbacks(payload: Payload) -> AbstractContextManager[Payload]: ...

_P = ParamSpec("_P")

def libgit2_callback(f: Callable[_P, int]) -> Callable[_P, int]: ...
def libgit2_callback_void(f: Callable[_P, None]) -> Callable[_P, None]: ...

_CredentialsFn: TypeAlias = Callable[[str | None, str | None, CredentialType], _Credentials]

def get_credentials(fn: _CredentialsFn, url: _CDataBase, username: _CDataBase, allowed: CredentialType) -> _CDataBase: ...
def git_checkout_options(
    callbacks: CheckoutCallbacks | None = None,
    strategy: CheckoutStrategy | None = None,
    directory: StrOrBytesPath | None = None,
    paths: _IntoStrArray = None,
) -> AbstractContextManager[Payload]: ...
def git_stash_apply_options(
    callbacks: StashApplyCallbacks | None = None,
    reinstate_index: bool = False,
    strategy: CheckoutStrategy | None = None,
    directory: StrOrBytesPath | None = None,
    paths: _IntoStrArray = None,
) -> AbstractContextManager[Payload]: ...
