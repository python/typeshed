# This file is part of gunicorn released under the MIT license.
# See the NOTICE for more information.
import argparse
from _typeshed import ConvertibleToInt
from collections.abc import Callable, Container
from ssl import SSLContext, _SSLMethod
from typing import Any, overload
from typing_extensions import TypeAlias, override

from gunicorn.arbiter import Arbiter
from gunicorn.glogging import Logger as GLogger
from gunicorn.http import Request
from gunicorn.http.wsgi import Response
from gunicorn.workers.base import Worker

from ._types import _AddressType, _EnvironType

_OnStartingHookType: TypeAlias = Callable[[Arbiter], None]
_OnReloadHookType: TypeAlias = Callable[[Arbiter], None]
_WhenReadyHookType: TypeAlias = Callable[[Arbiter], None]
_PreForkHookType: TypeAlias = Callable[[Arbiter, Worker], None]
_PostForkHookType: TypeAlias = Callable[[Arbiter, Worker], None]
_PostWorkerInitHookType: TypeAlias = Callable[[Worker], None]
_WorkerIntHookType: TypeAlias = Callable[[Worker], None]
_WorkerAbortHookType: TypeAlias = Callable[[Worker], None]
_PreExecHookType: TypeAlias = Callable[[Arbiter], None]
_PreRequestHookType: TypeAlias = Callable[[Worker, Request], None]
_PostRequestHookType: TypeAlias = Callable[[Worker, Request, _EnvironType, Response], None]
_ChildExitHookType: TypeAlias = Callable[[Arbiter, Worker], None]
_WorkerExitHookType: TypeAlias = Callable[[Arbiter, Worker], None]
_NumWorkersChangedHookType: TypeAlias = Callable[[Arbiter, int, int | None], None]
_OnExitHookType: TypeAlias = Callable[[Arbiter], None]
_SSLContextHookType: TypeAlias = Callable[[Config, Callable[[], SSLContext]], SSLContext]
_BoolValidatorType: TypeAlias = Callable[[bool | str | None], bool | None]
_StringValidatorType: TypeAlias = Callable[[str | None], str | None]
_ListStringValidatorType: TypeAlias = Callable[[str | list[str] | None], list[str]]
_IntValidatorType: TypeAlias = Callable[[int | ConvertibleToInt], int]
_DictValidatorType: TypeAlias = Callable[[dict[str, Any]], dict[str, Any]]
_ClassValidatorType: TypeAlias = Callable[[object | str | None], type[Any] | None]
_UserGroupValidatorType: TypeAlias = Callable[[str | int | None], int]
_AddressValidatorType: TypeAlias = Callable[[str | None], _AddressType | None]

KNOWN_SETTINGS: list[Setting]
PLATFORM: str

def make_settings(ignore: Container[Setting] | None = None) -> dict[str, Setting]: ...
def auto_int(_: Any, x: str) -> int: ...

class Config:
    settings: dict[str, Setting]
    usage: str | None
    prog: str | None
    env_orig: dict[str, str]

    def __init__(self, usage: str | None = None, prog: str | None = None) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    @override
    def __setattr__(self, name: str, value: Any) -> None: ...
    def set(self, name: str, value: Any) -> None: ...
    def get_cmd_args_from_env(self) -> list[str]: ...
    def parser(self) -> argparse.ArgumentParser: ...
    @property
    def worker_class_str(self) -> str: ...
    @property
    def worker_class(self) -> type[Worker]: ...
    @property
    def address(self) -> list[_AddressType]: ...
    @property
    def uid(self) -> int: ...
    @property
    def gid(self) -> int: ...
    @property
    def proc_name(self) -> str | None: ...
    @property
    def logger_class(self) -> type[GLogger]: ...
    @property
    def is_ssl(self) -> bool: ...
    @property
    def ssl_options(self) -> dict[str, Any]: ...
    @property
    def env(self) -> dict[str, str]: ...
    @property
    def sendfile(self) -> bool: ...
    @property
    def reuse_port(self) -> bool: ...
    @property
    def paste_global_conf(self) -> dict[str, str] | None: ...

class SettingMeta(type):
    def __new__(cls, name: str, bases: tuple[type, ...], attrs: dict[str, Any]) -> type: ...
    def fmt_desc(cls, desc: str) -> None: ...

class Setting(metaclass=SettingMeta):
    name: str | None
    value: Any
    section: str | None
    cli: list[str] | None
    validator: Callable[..., Any] | None
    type: type[Any] | Callable[..., Any] | None
    meta: str | None
    action: str | None
    default: Any
    short: str | None
    desc: str | None
    nargs: int | str | None
    const: bool | None
    order: int

    def __init__(self) -> None: ...
    def add_option(self, parser: argparse.ArgumentParser) -> None: ...
    def copy(self) -> Setting: ...
    def get(self) -> Any: ...
    def set(self, val: Any) -> None: ...
    def __lt__(self, other: Setting) -> bool: ...

    __cmp__ = __lt__

@overload
def validate_bool(val: bool) -> bool: ...
@overload
def validate_bool(val: str | None) -> bool | None: ...
def validate_dict(val: dict[str, Any]) -> dict[str, Any]: ...
@overload
def validate_pos_int(val: int) -> int: ...
@overload
def validate_pos_int(val: ConvertibleToInt) -> int: ...
def validate_ssl_version(val: _SSLMethod) -> _SSLMethod: ...
def validate_string(val: str | None) -> str | None: ...
def validate_file_exists(val: str | None) -> str | None: ...
@overload
def validate_list_string(val: str) -> list[str]: ...
@overload
def validate_list_string(val: list[str]) -> list[str]: ...
@overload
def validate_list_string(val: None) -> list[str]: ...
@overload
def validate_list_of_existing_files(val: str) -> list[str]: ...
@overload
def validate_list_of_existing_files(val: list[str]) -> list[str]: ...
@overload
def validate_list_of_existing_files(val: None) -> list[str]: ...
def validate_string_to_addr_list(val: str | None) -> list[str]: ...
def validate_string_to_list(val: str | None) -> list[str]: ...
@overload
def validate_class(val: str) -> type[Any]: ...
@overload
def validate_class(val: None) -> None: ...
@overload
def validate_class(val: object) -> type[Any]: ...
def validate_callable(arity: int) -> Callable[[str | Callable[..., Any]], Callable[..., Any]]: ...
def validate_user(val: int | str | None) -> int: ...
def validate_group(val: int | str | None) -> int: ...
def validate_post_request(val: str | Callable[..., Any]) -> _PostRequestHookType: ...
def validate_chdir(val: str) -> str: ...
@overload
def validate_statsd_address(val: str) -> _AddressType: ...
@overload
def validate_statsd_address(val: None) -> None: ...
def validate_reload_engine(val: str) -> str: ...
@overload
def validate_header_map_behaviour(val: str) -> str: ...
@overload
def validate_header_map_behaviour(val: None) -> None: ...
def get_default_config_file() -> str | None: ...

class ConfigFile(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _StringValidatorType
    default: str
    desc: str

class WSGIApp(Setting):
    name: str
    section: str
    meta: str
    validator: _StringValidatorType
    default: None
    desc: str

class Bind(Setting):
    name: str
    action: str
    section: str
    cli: list[str]
    meta: str
    validator: _ListStringValidatorType
    default: list[str]
    desc: str

class Backlog(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _IntValidatorType
    type: type[int]
    default: int
    desc: str

class Workers(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _IntValidatorType
    type: type[int]
    default: int
    desc: str

class WorkerClass(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _ClassValidatorType
    default: str
    desc: str

class WorkerThreads(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _IntValidatorType
    type: type[int]
    default: int
    desc: str

class WorkerConnections(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _IntValidatorType
    type: type[int]
    default: int
    desc: str

class MaxRequests(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _IntValidatorType
    type: type[int]
    default: int
    desc: str

class MaxRequestsJitter(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _IntValidatorType
    type: type[int]
    default: int
    desc: str

class Timeout(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _IntValidatorType
    type: type[int]
    default: int
    desc: str

class GracefulTimeout(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _IntValidatorType
    type: type[int]
    default: int
    desc: str

class Keepalive(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _IntValidatorType
    type: type[int]
    default: int
    desc: str

class LimitRequestLine(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _IntValidatorType
    type: type[int]
    default: int
    desc: str

class LimitRequestFields(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _IntValidatorType
    type: type[int]
    default: int
    desc: str

class LimitRequestFieldSize(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _IntValidatorType
    type: type[int]
    default: int
    desc: str

class Reload(Setting):
    name: str
    section: str
    cli: list[str]
    validator: _BoolValidatorType
    action: str
    default: bool
    desc: str

class ReloadEngine(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: Callable[[str], str]
    default: str
    desc: str

class ReloadExtraFiles(Setting):
    name: str
    action: str
    section: str
    cli: list[str]
    meta: str
    validator: _ListStringValidatorType
    default: list[str]
    desc: str

class Spew(Setting):
    name: str
    section: str
    cli: list[str]
    validator: _BoolValidatorType
    action: str
    default: bool
    desc: str

class ConfigCheck(Setting):
    name: str
    section: str
    cli: list[str]
    validator: _BoolValidatorType
    action: str
    default: bool
    desc: str

class PrintConfig(Setting):
    name: str
    section: str
    cli: list[str]
    validator: _BoolValidatorType
    action: str
    default: bool
    desc: str

class PreloadApp(Setting):
    name: str
    section: str
    cli: list[str]
    validator: _BoolValidatorType
    action: str
    default: bool
    desc: str

class Sendfile(Setting):
    name: str
    section: str
    cli: list[str]
    validator: _BoolValidatorType
    action: str
    const: bool
    desc: str

class ReusePort(Setting):
    name: str
    section: str
    cli: list[str]
    validator: _BoolValidatorType
    action: str
    default: bool
    desc: str

class Chdir(Setting):
    name: str
    section: str
    cli: list[str]
    validator: Callable[[str], str]
    default: str
    default_doc: str
    desc: str

class Daemon(Setting):
    name: str
    section: str
    cli: list[str]
    validator: _BoolValidatorType
    action: str
    default: bool
    desc: str

class Env(Setting):
    name: str
    action: str
    section: str
    cli: list[str]
    meta: str
    validator: _ListStringValidatorType
    default: list[str]
    desc: str

class Pidfile(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _StringValidatorType
    default: None
    desc: str

class WorkerTmpDir(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _StringValidatorType
    default: None
    desc: str

class User(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _UserGroupValidatorType
    default: int
    default_doc: str
    desc: str

class Group(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _UserGroupValidatorType
    default: int
    default_doc: str
    desc: str

class Umask(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _IntValidatorType
    type: Callable[[Any, str], int]
    default: int
    desc: str

class Initgroups(Setting):
    name: str
    section: str
    cli: list[str]
    validator: _BoolValidatorType
    action: str
    default: bool
    desc: str

class TmpUploadDir(Setting):
    name: str
    section: str
    meta: str
    validator: _StringValidatorType
    default: None
    desc: str

class SecureSchemeHeader(Setting):
    name: str
    section: str
    validator: _DictValidatorType
    default: dict[str, str]
    desc: str

class ForwardedAllowIPS(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _ListStringValidatorType
    default: str
    desc: str

class AccessLog(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _StringValidatorType
    default: None
    desc: str

class DisableRedirectAccessToSyslog(Setting):
    name: str
    section: str
    cli: list[str]
    validator: _BoolValidatorType
    action: str
    default: bool
    desc: str

class AccessLogFormat(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _StringValidatorType
    default: str
    desc: str

class ErrorLog(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _StringValidatorType
    default: str
    desc: str

class Loglevel(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _StringValidatorType
    default: str
    desc: str

class CaptureOutput(Setting):
    name: str
    section: str
    cli: list[str]
    validator: _BoolValidatorType
    action: str
    default: bool
    desc: str

class LoggerClass(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _ClassValidatorType
    default: str
    desc: str

class LogConfig(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _StringValidatorType
    default: None
    desc: str

class LogConfigDict(Setting):
    name: str
    section: str
    validator: _DictValidatorType
    default: dict[str, Any]
    desc: str

class LogConfigJson(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _StringValidatorType
    default: None
    desc: str

class SyslogTo(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _StringValidatorType
    default: str
    desc: str

class Syslog(Setting):
    name: str
    section: str
    cli: list[str]
    validator: _BoolValidatorType
    action: str
    default: bool
    desc: str

class SyslogPrefix(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _StringValidatorType
    default: None
    desc: str

class SyslogFacility(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _StringValidatorType
    default: str
    desc: str

class EnableStdioInheritance(Setting):
    name: str
    section: str
    cli: list[str]
    validator: _BoolValidatorType
    default: bool
    action: str
    desc: str

class StatsdHost(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    default: None
    validator: _AddressValidatorType
    desc: str

class DogstatsdTags(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    default: str
    validator: _StringValidatorType
    desc: str

class StatsdPrefix(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    default: str
    validator: _StringValidatorType
    desc: str

class Procname(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _StringValidatorType
    default: None
    desc: str

class DefaultProcName(Setting):
    name: str
    section: str
    validator: _StringValidatorType
    default: str
    desc: str

class PythonPath(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _StringValidatorType
    default: None
    desc: str

class Paste(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _StringValidatorType
    default: None
    desc: str

class OnStarting(Setting):
    name: str
    section: str
    validator: Callable[[str | _OnStartingHookType], _OnStartingHookType]
    type: Callable[..., Any]
    default: _OnStartingHookType
    desc: str

    def on_starting(server: Arbiter) -> None: ...  # type: ignore[misc]

class OnReload(Setting):
    name: str
    section: str
    validator: Callable[[str | _OnReloadHookType], _OnReloadHookType]
    type: Callable[..., Any]
    default: _OnReloadHookType
    desc: str

    def on_reload(server: Arbiter) -> None: ...  # type: ignore[misc]

class WhenReady(Setting):
    name: str
    section: str
    validator: Callable[[str | _WhenReadyHookType], _WhenReadyHookType]
    type: Callable[..., Any]
    default: _WhenReadyHookType
    desc: str

    def when_ready(server: Arbiter) -> None: ...  # type: ignore[misc]

class Prefork(Setting):
    name: str
    section: str
    validator: Callable[[str | _PreForkHookType], _PreForkHookType]
    type: Callable[..., Any]
    default: _PreForkHookType
    desc: str

    def pre_fork(server: Arbiter, worker: Worker) -> None: ...  # type: ignore[misc]

class Postfork(Setting):
    name: str
    section: str
    validator: Callable[[str | _PostForkHookType], _PostForkHookType]
    type: Callable[..., Any]
    default: _PostForkHookType
    desc: str

    def post_fork(server: Arbiter, worker: Worker) -> None: ...  # type: ignore[misc]

class PostWorkerInit(Setting):
    name: str
    section: str
    validator: Callable[[str | _PostWorkerInitHookType], _PostWorkerInitHookType]
    type: Callable[..., Any]
    default: _PostWorkerInitHookType
    desc: str

    def post_worker_init(worker: Worker) -> None: ...  # type: ignore[misc]

class WorkerInt(Setting):
    name: str
    section: str
    validator: Callable[[str | _WorkerIntHookType], _WorkerIntHookType]
    type: Callable[..., Any]
    default: _WorkerIntHookType
    desc: str

    def worker_int(worker: Worker) -> None: ...  # type: ignore[misc]

class WorkerAbort(Setting):
    name: str
    section: str
    validator: Callable[[str | _WorkerAbortHookType], _WorkerAbortHookType]
    type: Callable[..., Any]
    default: _WorkerAbortHookType
    desc: str

    def worker_abort(worker: Worker) -> None: ...  # type: ignore[misc]

class PreExec(Setting):
    name: str
    section: str
    validator: Callable[[str | _PreExecHookType], _PreExecHookType]
    type: Callable[..., Any]
    default: _PreExecHookType
    desc: str

    def pre_exec(server: Arbiter) -> None: ...  # type: ignore[misc]

class PreRequest(Setting):
    name: str
    section: str
    validator: Callable[[str | _PreRequestHookType], _PreRequestHookType]
    type: Callable[..., Any]
    default: _PreRequestHookType
    desc: str

    def pre_request(worker: Worker, req: Request) -> None: ...  # type: ignore[misc]

class PostRequest(Setting):
    name: str
    section: str
    validator: Callable[[str | Callable[..., Any]], _PostRequestHookType]
    type: Callable[..., Any]
    default: _PostRequestHookType
    desc: str

    def post_request(worker: Worker, req: Request, environ: _EnvironType, resp: Response) -> None: ...  # type: ignore[misc]

class ChildExit(Setting):
    name: str
    section: str
    validator: Callable[[str | _ChildExitHookType], _ChildExitHookType]
    type: Callable[..., Any]
    default: _ChildExitHookType
    desc: str

    def child_exit(server: Arbiter, worker: Worker) -> None: ...  # type: ignore[misc]

class WorkerExit(Setting):
    name: str
    section: str
    validator: Callable[[str | _WorkerExitHookType], _WorkerExitHookType]
    type: Callable[..., Any]
    default: _WorkerExitHookType
    desc: str

    def worker_exit(server: Arbiter, worker: Worker) -> None: ...  # type: ignore[misc]

class NumWorkersChanged(Setting):
    name: str
    section: str
    validator: Callable[[str | _NumWorkersChangedHookType], _NumWorkersChangedHookType]
    type: Callable[..., Any]
    default: _NumWorkersChangedHookType
    desc: str

    def nworkers_changed(server: Arbiter, new_value: int, old_value: int | None) -> None: ...  # type: ignore[misc]

class OnExit(Setting):
    name: str
    section: str
    validator: Callable[[str | _OnExitHookType], _OnExitHookType]
    default: _OnExitHookType
    desc: str

    def on_exit(server: Arbiter) -> None: ...  # type: ignore[misc]

class NewSSLContext(Setting):
    name: str
    section: str
    validator: Callable[[str | _SSLContextHookType], _SSLContextHookType]
    type: Callable[..., Any]
    default: _SSLContextHookType
    desc: str

    def ssl_context(config: Config, default_ssl_context_factory: Callable[[], SSLContext]) -> SSLContext: ...  # type: ignore[misc]

class ProxyProtocol(Setting):
    name: str
    section: str
    cli: list[str]
    validator: _BoolValidatorType
    default: bool
    action: str
    desc: str

class ProxyAllowFrom(Setting):
    name: str
    section: str
    cli: list[str]
    validator: _ListStringValidatorType
    default: str
    desc: str

class KeyFile(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _StringValidatorType
    default: None
    desc: str

class CertFile(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _StringValidatorType
    default: None
    desc: str

class SSLVersion(Setting):
    name: str
    section: str
    cli: list[str]
    validator: Callable[[_SSLMethod], _SSLMethod]
    default: _SSLMethod
    desc: str

class CertReqs(Setting):
    name: str
    section: str
    cli: list[str]
    validator: _IntValidatorType
    default: int
    desc: str

class CACerts(Setting):
    name: str
    section: str
    cli: list[str]
    meta: str
    validator: _StringValidatorType
    default: None
    desc: str

class SuppressRaggedEOFs(Setting):
    name: str
    section: str
    cli: list[str]
    action: str
    default: bool
    validator: _BoolValidatorType
    desc: str

class DoHandshakeOnConnect(Setting):
    name: str
    section: str
    cli: list[str]
    validator: _BoolValidatorType
    action: str
    default: bool
    desc: str

class Ciphers(Setting):
    name: str
    section: str
    cli: list[str]
    validator: _StringValidatorType
    default: None
    desc: str

class PasteGlobalConf(Setting):
    name: str
    action: str
    section: str
    cli: list[str]
    meta: str
    validator: _ListStringValidatorType
    default: list[str]
    desc: str

class PermitObsoleteFolding(Setting):
    name: str
    section: str
    cli: list[str]
    validator: _BoolValidatorType
    action: str
    default: bool
    desc: str

class StripHeaderSpaces(Setting):
    name: str
    section: str
    cli: list[str]
    validator: _BoolValidatorType
    action: str
    default: bool
    desc: str

class PermitUnconventionalHTTPMethod(Setting):
    name: str
    section: str
    cli: list[str]
    validator: _BoolValidatorType
    action: str
    default: bool
    desc: str

class PermitUnconventionalHTTPVersion(Setting):
    name: str
    section: str
    cli: list[str]
    validator: _BoolValidatorType
    action: str
    default: bool
    desc: str

class CasefoldHTTPMethod(Setting):
    name: str
    section: str
    cli: list[str]
    validator: _BoolValidatorType
    action: str
    default: bool
    desc: str

class ForwarderHeaders(Setting):
    name: str
    section: str
    cli: list[str]
    validator: _ListStringValidatorType
    default: str
    desc: str

class HeaderMap(Setting):
    name: str
    section: str
    cli: list[str]
    validator: _StringValidatorType
    default: str
    desc: str
