from _typeshed import Incomplete
from collections.abc import Iterator, Mapping
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path
from types import TracebackType
from typing import Any, Final, Literal, NoReturn, NotRequired, Self, TypeAlias, TypedDict, Unpack, overload, type_check_only

import P4API

class P4Exception(Exception):
    value: str
    errors: list[str] | None
    warnings: list[str] | None
    def __init__(self, value: str | tuple[str, list[str], list[str]]) -> None: ...

class Spec(dict[str, str | list[Any]]):
    def __init__(self, fieldmap: Mapping[str, str] | None = None) -> None: ...
    def __getattr__(self, attr: str) -> str | list[Any]: ...
    def __setitem__(self, key: str, value: str | list[Any]) -> Any: ...
    def __setattr__(self, attr: str, value: str | list[Any]) -> None: ...
    def permitted_fields(self) -> Mapping[str, str] | None: ...

class Integration:
    how: str
    file: str
    srev: int
    erev: int
    def __init__(self, how: str, file: str, srev: int, erev: int) -> None: ...

class Revision:
    depotFile: DepotFile
    integrations: list[Integration]
    rev: int | None
    change: int | None
    action: _RevisionAction | None
    type: str | None
    time: datetime | None
    user: str | None
    client: str | None
    desc: str | None
    digest: str | None
    fileSize: str | None
    def __init__(self, depotFile: DepotFile) -> None: ...
    def integration(self, how: str, file: str, srev: int, erev: int) -> Integration: ...
    def each_integration(self) -> Iterator[Integration]: ...

_RevisionAction: TypeAlias = Literal["add", "edit", "delete", "branch", "integrate"]

class DepotFile:
    depotFile: str
    revisions: list[Revision]
    def __init__(self, name: str) -> None: ...
    def new_revision(self) -> Revision: ...
    def each_revision(self) -> Iterator[Revision]: ...
    def str_revision(self, rev: Revision, revFormat: str, changeFormat: str) -> str: ...
    def str_integration(self, integ: Integration) -> str: ...

class Resolver:
    def __init__(self) -> None: ...
    def resolve(self, mergeInfo: P4API.P4MergeData, /) -> P4API.ResolveAction: ...
    def actionResolve(self, mergeInfo: P4API.P4ActionMergeData, /) -> P4API.ResolveAction: ...

class OutputHandler:
    REPORT: _HandlerResultReport
    HANDLED: _HandlerResultHandled
    CANCEL: _HandlerResultCancel

    def __init__(self) -> None: ...
    def outputText(self, s: str, /) -> _HandlerResult: ...
    def outputBinary(self, b: bytes, /) -> _HandlerResult: ...
    def outputStat(self, h: Spec | dict[str, Any], /) -> _HandlerResult: ...
    def outputInfo(self, i: str, /) -> _HandlerResult: ...
    def outputMessage(self, e: P4API.P4Message, /) -> _HandlerResult: ...

class ReportHandler(OutputHandler): ...

_HandlerResultReport: TypeAlias = Literal[0]
_HandlerResultHandled: TypeAlias = Literal[1]
_HandlerResultCancel: TypeAlias = Literal[2]
_HandlerResult: TypeAlias = _HandlerResultReport | _HandlerResultHandled | _HandlerResultCancel

class Progress:
    TYPE_SENDFILE: _ProgressTypeSendFile
    TYPE_RECEIVEFILE: _ProgressTypeReceiveFile
    TYPE_TRANSFER: _ProgressTypeTransfer
    TYPE_COMPUTATION: _ProgressTypeComputation
    UNIT_PERCENT: _ProgressUnitPercent
    UNIT_FILES: _ProgressUnitFiles
    UNIT_KBYTES: _ProgressUnitKBytes
    UNIT_MBYTES: _ProgressUnitMBytes
    UNIT_DELTAS: _ProgressUnitDeltas

    def __init__(self) -> None: ...
    def init(self, type: _ProgressType) -> None: ...
    def setDescription(self, description: str, units: _ProgressUnit) -> None: ...
    def setTotal(self, total: int) -> None: ...
    def update(self, position: int) -> None: ...
    def done(self, fail: bool | int) -> None: ...

_ProgressTypeSendFile: TypeAlias = Literal[1]
_ProgressTypeReceiveFile: TypeAlias = Literal[2]
_ProgressTypeTransfer: TypeAlias = Literal[3]
_ProgressTypeComputation: TypeAlias = Literal[4]
_ProgressTypeItems: TypeAlias = Literal[5]
_ProgressTypeDirs: TypeAlias = Literal[6]
_ProgressTypeDeleteFile: TypeAlias = Literal[7]
_ProgressType: TypeAlias = (
    _ProgressTypeSendFile
    | _ProgressTypeReceiveFile
    | _ProgressTypeTransfer
    | _ProgressTypeComputation
    | _ProgressTypeItems
    | _ProgressTypeDirs
    | _ProgressTypeDeleteFile
)
_ProgressUnitUnspecified: TypeAlias = Literal[0]
_ProgressUnitPercent: TypeAlias = Literal[1]
_ProgressUnitFiles: TypeAlias = Literal[2]
_ProgressUnitKBytes: TypeAlias = Literal[3]
_ProgressUnitMBytes: TypeAlias = Literal[4]
_ProgressUnitDeltas: TypeAlias = Literal[5]
_ProgressUnitItems: TypeAlias = Literal[6]
_ProgressUnitDirectories: TypeAlias = Literal[7]
_ProgressUnit: TypeAlias = (
    _ProgressUnitUnspecified
    | _ProgressUnitPercent
    | _ProgressUnitFiles
    | _ProgressUnitKBytes
    | _ProgressUnitMBytes
    | _ProgressUnitDeltas
    | _ProgressUnitItems
    | _ProgressUnitDirectories
)

class TextProgress(Progress):
    TYPES: Final[list[str]]
    UNITS: Final[list[str]]

    def __init__(self) -> None: ...
    def init(self, type: _ProgressType) -> None: ...
    def setDescription(self, description: str, units: _ProgressUnit) -> None: ...
    def setTotal(self, total: int) -> None: ...
    def update(self, position: int) -> None: ...
    def done(self, fail: bool | int) -> None: ...

def processFilelog(h: Mapping[str, Any]) -> DepotFile: ...

class FilelogOutputHandler(OutputHandler):
    def outputFilelog(self, f: DepotFile) -> _HandlerResult: ...

class Map(P4API.P4Map):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, maps: list[str]) -> None: ...
    @overload
    def __init__(self, map: str) -> None: ...
    @overload
    def __init__(self, lhr: str, rhs: str) -> None: ...

    LEFT2RIGHT: Literal[True]
    RIGHT2LEFT: Literal[False]

    def is_empty(self) -> bool: ...
    def includes(self, path: str, left_to_right: bool = True, /) -> bool: ...
    def reverse(self) -> Map: ...
    @overload
    def insert(self, maps: list[str], /) -> None: ...
    @overload
    def insert(self, lhr: str, rhs: str | None = None, /) -> None: ...

class P4(P4API.P4Adapter):
    # See https://help.perforce.com/helix-core/apis/p4python/current/Content/P4Python/python.p4.html
    # for documented public API.  Most documented attributes are inherited from P4API, and are annotated there instead.

    RAISE_ALL: Literal[P4API.RAISE_ALL]
    RAISE_ERROR: Literal[P4API.RAISE_ERRORS]
    RAISE_ERRORS: Literal[P4API.RAISE_ERRORS]
    RAISE_NONE: Literal[P4API.RAISE_NONE]

    E_EMPTY: Literal[P4API.E_EMPTY]
    E_INFO: Literal[P4API.E_INFO]
    E_WARN: Literal[P4API.E_WARN]
    E_FAILED: Literal[P4API.E_FAILED]
    E_FATAL: Literal[P4API.E_FATAL]

    EV_NONE: Literal[0]
    EV_USAGE: Literal[0x01]
    EV_UNKNOWN: Literal[0x02]
    EV_CONTEXT: Literal[0x03]
    EV_ILLEGAL: Literal[0x04]
    EV_NOTYET: Literal[0x05]
    EV_PROTECT: Literal[0x06]
    EV_EMPTY: Literal[0x11]
    EV_FAULT: Literal[0x21]
    EV_CLIENT: Literal[0x22]
    EV_ADMIN: Literal[0x23]
    EV_CONFIG: Literal[0x24]
    EV_UPGRADE: Literal[0x25]
    EV_COMM: Literal[0x26]
    EV_TOOBIG: Literal[0x27]

    specfields: Final[Mapping[str, tuple[str, str]]]

    @classmethod
    def identify(cls) -> str: ...
    def __getattr__(self, name: str) -> Incomplete: ...
    def __init__(self, **kwargs: Unpack[_GlobalOptions]) -> None: ...
    def is_ignored(self, path: str | Path) -> bool | None: ...
    def log_messages(self) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> Literal[False]: ...
    @contextmanager
    def while_tagged(self, t: bool) -> Iterator[None]: ...
    @contextmanager
    def at_exception_level(self, e: P4API.RAISE_ALL | P4API.RAISE_ERRORS | P4API.RAISE_NONE) -> Iterator[None]: ...
    @contextmanager
    def using_handler(self, c: OutputHandler) -> Iterator[None]: ...
    @contextmanager
    def saved_context(self, **kargs: Unpack[_GlobalOptions]) -> Iterator[None]: ...
    @contextmanager
    def temp_client(self, prefix: str, template: str) -> Iterator[str]: ...

    # Generic run command method
    @overload
    def run(
        self,
        cmd: Literal[
            "add",
            "admin",
            "archive",
            "attribute",
            "bgtask",
            "branch",
            "branches",
            "chachepurge",
            "chages",
            "changelist",
            "changelists",
            "check-permission",
            "clean",
            "client",
            "configure",
            "copy",
            "counter",
            "counters",
            "cstat",
            "dbschema",
            "dbstat",
            "dbverify",
            "delete",
            "depot",
            "depots",
            "describe",
            "diagnostics",
            "diff",
            "diff2",
            "dirs",
            "diskspace",
            "edit",
            "export",
            "extension",
            "failback",
            "failover",
            "fetch",
            "filelog",
            "files",
            "fix",
            "fixes",
            "flush",
            "fstat",
            "graph",
            "grep",
            "group",
            "groups",
            "heartbeat",
            "have",
            "help",
            "help-graph",
            # "hotfiles",  # not supported via API
            # "ignores",  # not supported via API; use is_ignored()
            "info",
            "init",
            "integ",
            "integrate",
            "integrated",
            "interchanges",
            "istat",
            "job",
            "jobs",
            "jobspec",
            "journalcopy",
            "journaldbchecksums",
            "journals",
            "key",
            "keys",
            "label",
            "labels",
            "labelsync",
            "ldap",
            "ldaps",
            "ldapsync",
            "license",
            "list",
            "lock",
            "lockstat",
            "logappend",
            "logexport",
            "logger",
            "login",
            "login2",
            "logout",
            "logparse",
            "logrotate",
            "logschema",
            "logstat",
            "logtail",
            "merge",
            "monitor",
            "move",
            "obliterate",
            "opened",
            "passwd",
            "ping",
            "populate",
            "print",
            "property",
            "protect",
            "protects",
            "proxy",
            "prune",
            "pubkey",
            "pubkeys",
            "pull",
            "push",
            "reconcile",
            "reload",
            "remote",
            "remotes",
            "rename",
            "renameclient",
            "renameuser",
            "reopen",
            "replicate",
            "repo",
            "repos",
            "reshelve",
            "resolve",
            "resolved",
            "restore",
            "resubmit",
            "revert",
            "review",
            "reviews",
            "revoke-permission",
            "server",
            "serverid",
            "servers",
            "shelve",
            "show-permission",
            "show-permissions",
            "show-ref",
            "sizes",
            "status",
            "storage",
            "stream",
            "streamlog",
            "streams",
            "streamspec",
            "submit",
            "switch",
            "sync",
            "tag",
            # "tickets",  # Not usable with generic run() up to at least 2025.2; use run_tickets() instead
            "topology",
            "triggers",
            "trust",
            "typemap",
            "undo",
            "unload",
            "unlock",
            "unshelve",
            "unsubmit",
            "unzip",
            "update",
            "upgrades",
            "user",
            "users",
            "verify",
            "webserver",
            "where",
            "workspace",
            "workspaces",
            "zip",
        ],
        /,
        *args: _CommandOption,
        **kargs: Unpack[_GlobalOptions],
    ) -> list[str | dict[str, Any] | Spec]: ...
    @overload
    def run(self, cmd: Literal["tickets"], /, *args: _CommandOption, **kwargs: Unpack[_GlobalOptions]) -> NoReturn: ...
    @overload
    def run(self, /, *args: _CommandOption, **kargs: Unpack[_GlobalOptions]) -> list[_P4Result]: ...

    # Command methods that have explicit implementations with additional processing
    def run_submit(
        self,
        *args: _CommandOption | _ChangelistForm | Spec | dict[str, str | list[str]],
        progress: Progress | None = None,
        **kargs: Unpack[_GlobalOptions],
    ) -> list[_P4Result]: ...
    def run_shelve(
        self, *args: _CommandOption | _ChangelistForm | Spec | dict[str, str | list[str]], **kargs: Unpack[_GlobalOptions]
    ) -> list[_P4Result]: ...
    @overload
    def delete_shelve(self, changelist_number: int | str, /, *args: str, **kargs: Unpack[_GlobalOptions]) -> list[str]: ...
    @overload
    def delete_shelve(self, *args: _CommandOption, **kargs: Unpack[_GlobalOptions]) -> list[str]: ...
    def run_login(self, *args: _CommandOption, **kargs: Unpack[_GlobalOptions]) -> list[_P4Result]: ...
    def run_password(self, oldpass: str, newpass: str, *args: str, **kargs: Unpack[_GlobalOptions]) -> list[str]: ...
    def run_filelog(self, *args: str, **kwargs: Unpack[_GlobalOptions]) -> list[DepotFile | str]: ...
    def run_print(self, *args: _CommandOption, **kargs: Unpack[_GlobalOptions]) -> list[str | bytes]: ...
    def run_resolve(
        self, *args: _CommandOption, resolver: Resolver | None = None, **kargs: Unpack[_GlobalOptions]
    ) -> list[_P4Result]: ...
    def run_tickets(self) -> list[TicketInfo]: ...
    def run_init(self, *args: _CommandOption, **kargs: Any) -> NoReturn: ...
    def run_clone(self, *args: _CommandOption, **kargs: Any) -> NoReturn: ...

    # Command methods that are implicitly available
    # This set covers many core p4 commands, but is not aiming to be exhaustive
    def fetch_client(self, *args: _CommandOption, **kwargs: Unpack[_GlobalOptions]) -> Spec: ...
    def fetch_change(self, *args: _CommandOption, **kwargs: Unpack[_GlobalOptions]) -> Spec: ...
    def fetch_depot(self, *args: _CommandOption, **kwargs: Unpack[_GlobalOptions]) -> Spec: ...
    def fetch_repo(self, *args: _CommandOption, **kwargs: Unpack[_GlobalOptions]) -> Spec: ...
    def fetch_stream(self, *args: _CommandOption, **kwargs: Unpack[_GlobalOptions]) -> Spec: ...
    def fetch_workspace(self, *args: _CommandOption, **kwargs: Unpack[_GlobalOptions]) -> Spec: ...
    def save_client(
        self,
        client: _WorkspaceForm | Spec | dict[str, str | list[str]],
        /,
        *args: _CommandOption,
        **kwargs: Unpack[_GlobalOptions],
    ) -> list[str]: ...
    def save_depot(
        self, depot: _DepotForm | Spec | dict[str, str | list[str]], /, *args: _CommandOption, **kwargs: Unpack[_GlobalOptions]
    ) -> list[str]: ...
    def save_repo(self, repo: Spec | dict[str, Any], /, *args: _CommandOption, **kwargs: Unpack[_GlobalOptions]) -> list[str]: ...
    def save_stream(
        self, stream: Spec | dict[str, str | list[str]], /, *args: _CommandOption, **kwargs: Unpack[_GlobalOptions]
    ) -> list[str]: ...
    def save_workspace(
        self,
        workspace: _WorkspaceForm | Spec | dict[str, str | list[str]],
        /,
        *args: _CommandOption,
        **kwargs: Unpack[_GlobalOptions],
    ) -> list[str]: ...
    @overload
    def run_add(self, file: str | Path, /, *args: _CommandOption, **kwargs: Unpack[_GlobalOptions]) -> list[_P4Result]: ...
    @overload
    def run_add(self, *args: _CommandOption, **kwargs: Unpack[_GlobalOptions]) -> list[_P4Result]: ...
    def run_changes(self, *args: _CommandOption, **kwargs: Unpack[_GlobalOptions]) -> list[_P4Result]: ...
    def run_changelists(self, *args: _CommandOption, **kwargs: Unpack[_GlobalOptions]) -> list[_P4Result]: ...
    def run_configure(
        self,
        action: Literal["set", "unset", "show", "history", "help"],
        /,
        *args: _CommandOption,
        **kwargs: Unpack[_GlobalOptions],
    ) -> Incomplete: ...
    @overload
    def run_edit(self, file: str | Path, /, *args: _CommandOption, **kwargs: Unpack[_GlobalOptions]) -> list[_P4Result]: ...
    @overload
    def run_edit(self, *args: _CommandOption, **kwargs: Unpack[_GlobalOptions]) -> list[_P4Result]: ...
    def run_files(self, *args: _CommandOption, **kwargs: Unpack[_GlobalOptions]) -> list[_P4Result]: ...
    def run_info(self, *args: _CommandOption, **kwargs: Unpack[_GlobalOptions]) -> list[_P4Result]: ...
    def run_integ(self, *args: _CommandOption, **kwargs: Unpack[_GlobalOptions]) -> list[_P4Result]: ...
    def run_integrate(self, *args: _CommandOption, **kwargs: Unpack[_GlobalOptions]) -> list[_P4Result]: ...
    def run_move(
        self, *args: _CommandOption, progress: Progress | None = None, **kwargs: Unpack[_GlobalOptions]
    ) -> list[_P4Result]: ...
    def run_opened(self, *args: _CommandOption, **kwargs: Unpack[_GlobalOptions]) -> list[_P4Result]: ...
    def run_reconcile(
        self, *args: _CommandOption, progress: Progress | None = None, **kwargs: Unpack[_GlobalOptions]
    ) -> list[_P4Result]: ...
    def run_reopen(self, *args: _CommandOption, **kwargs: Unpack[_GlobalOptions]) -> list[_P4Result]: ...
    def run_revert(self, *args: _CommandOption, **kwargs: Unpack[_GlobalOptions]) -> list[_P4Result]: ...
    def run_status(
        self, *args: _CommandOption, progress: Progress | None = None, **kwargs: Unpack[_GlobalOptions]
    ) -> list[_P4Result]: ...
    def run_streams(self, *args: _CommandOption, **kwargs: Unpack[_GlobalOptions]) -> list[_P4Result]: ...
    def run_sync(
        self, *args: _CommandOption, progress: Progress | None = None, **kwargs: Unpack[_GlobalOptions]
    ) -> list[str]: ...
    def run_unshelve(self, *args: _CommandOption, **kwargs: Unpack[_GlobalOptions]) -> list[_P4Result]: ...

class PyKeepAlive:
    def __init__(self) -> None: ...
    def isAlive(self) -> Literal[0, 1] | bool: ...

def init(
    user: str | None = None,
    client: str | None = None,
    directory: str | None = None,
    port: str | None = None,
    casesensitive: bool | None = None,
    unicode: bool | None = None,
) -> P4: ...
def clone(
    user: str | None = None,
    client: str | None = None,
    directory: str | None = None,
    depth: int | None = None,
    verbose: bool | None = None,
    port: str | None = None,
    remote: str | None = None,
    file: str | None = None,
    noarchive: bool | None = None,
    progress: Progress | None = None,
) -> P4: ...
@type_check_only
class _GlobalOptions(TypedDict, total=False):
    client: str
    cwd: str
    encoding: str
    exception_level: P4API.RAISE_ALL | P4API.RAISE_ERRORS | P4API.RAISE_NONE
    handler: OutputHandler
    host: str
    maxlocktime: int
    maxresults: int
    maxscanrows: int
    password: str
    prog: str
    port: str
    user: str
    resultLogging: bool
    debug: int
    tagged: bool | Literal[0, 1]

# Type of accepted positional arguments for any p4 command.
# The underlying implementation accepts any type that is convertible to str. Since acceptable values depend on the
# command, and are effectively forwarded as commandline arguments, it is very difficult to annotate more precisely.
_CommandOption: TypeAlias = str | int | tuple[str, Any] | Any

# P4 commands will always output a list of these.  The exact type depends on subcommand, subcommand options, global options,
# as well as the value of specific flags when connect() was invoked.
_P4Result: TypeAlias = dict[str, Any] | str

@type_check_only
class TicketInfo(TypedDict):
    Host: str
    User: str
    Ticket: str

@type_check_only
class _ChangelistForm(TypedDict):
    # https://help.perforce.com/helix-core/server-apps/cmdref/current/Content/CmdRef/p4_submit.html
    Change: int | str | Literal["new"]
    Client: str
    User: str
    Status: Literal["new", "pending", "submitted"]
    Description: str
    Jobs: list[str]
    Type: Literal["restricted", "public"]
    Files: list[str]

@type_check_only
class _DepotForm(TypedDict):
    Depot: str
    Owner: str
    Date: NotRequired[str]
    Description: str
    Type: Literal["local", "remot", "stream", "spec", "unload", "archive", "tangent", "graph", "trait"]
    Address: str
    Suffix: str
    StreamDepth: NotRequired[str]
    Map: NotRequired[str]
    SpecMap: NotRequired[Incomplete]

@type_check_only
class _WorkspaceForm(TypedDict):
    # https://help.perforce.com/helix-core/server-apps/cmdref/current/Content/CmdRef/p4_client.html
    Client: str
    Owner: NotRequired[str]
    Update: NotRequired[str]
    Access: NotRequired[str]
    Host: NotRequired[str]
    Description: NotRequired[str]
    Root: str
    AltRoots: NotRequired[list[str]]
    Options: str
    SubmitOptions: Literal[
        "submitunchanged",
        "submitunchanged+reopen",
        "revertunchanged",
        "revertunchanged+reopen",
        "leaveunchanged",
        "leaveunchanged+reopen",
    ]
    LineEnd: Literal["local", "unix", "mac", "win", "share"]
    LimitView: NotRequired[list[str]]
    Stream: NotRequired[str]
    StreamAtChange: NotRequired[str]
    ServerId: NotRequired[str]
    View: list[str]
    ChangeView: NotRequired[Incomplete]
    Type: NotRequired[Literal["writeable", "readonly", "partitioned", "partitioned-jnl", "graph"]]
    Backup: NotRequired[str]
