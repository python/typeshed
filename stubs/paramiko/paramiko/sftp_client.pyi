from logging import Logger
from typing import IO, Any, Callable, Iterator, Text

from paramiko.channel import Channel
from paramiko.sftp import BaseSFTP
from paramiko.sftp_attr import SFTPAttributes
from paramiko.sftp_file import SFTPFile
from paramiko.transport import Transport
from paramiko.util import ClosingContextManager

_Callback = Callable[[int, int], Any]

b_slash: bytes

class SFTPClient(BaseSFTP, ClosingContextManager):
    sock: Channel
    ultra_debug: bool
    request_number: int
    logger: Logger
    def __init__(self, sock: Channel) -> None: ...
    @classmethod
    def from_transport(
        cls, t: Transport, window_size: int | None = ..., max_packet_size: int | None = ...
    ) -> SFTPClient | None: ...
    def close(self) -> None: ...
    def get_channel(self) -> Channel | None: ...
    def listdir(self, path: str = ...) -> list[str]: ...
    def listdir_attr(self, path: str = ...) -> list[SFTPAttributes]: ...
    def listdir_iter(self, path: bytes | Text = ..., read_aheads: int = ...) -> Iterator[SFTPAttributes]: ...
    def open(self, filename: bytes | Text, mode: str = ..., bufsize: int = ...) -> SFTPFile: ...
    file = open
    def remove(self, path: bytes | Text) -> None: ...
    unlink = remove
    def rename(self, oldpath: bytes | Text, newpath: bytes | Text) -> None: ...
    def posix_rename(self, oldpath: bytes | Text, newpath: bytes | Text) -> None: ...
    def mkdir(self, path: bytes | Text, mode: int = ...) -> None: ...
    def rmdir(self, path: bytes | Text) -> None: ...
    def stat(self, path: bytes | Text) -> SFTPAttributes: ...
    def lstat(self, path: bytes | Text) -> SFTPAttributes: ...
    def symlink(self, source: bytes | Text, dest: bytes | Text) -> None: ...
    def chmod(self, path: bytes | Text, mode: int) -> None: ...
    def chown(self, path: bytes | Text, uid: int, gid: int) -> None: ...
    def utime(self, path: bytes | Text, times: tuple[float, float] | None) -> None: ...
    def truncate(self, path: bytes | Text, size: int) -> None: ...
    def readlink(self, path: bytes | Text) -> Text | None: ...
    def normalize(self, path: bytes | Text) -> Text: ...
    def chdir(self, path: None | bytes | Text = ...) -> None: ...
    def getcwd(self) -> Text | None: ...
    def putfo(
        self, fl: IO[bytes], remotepath: bytes | Text, file_size: int = ..., callback: _Callback | None = ..., confirm: bool = ...
    ) -> SFTPAttributes: ...
    def put(
        self, localpath: bytes | Text, remotepath: bytes | Text, callback: _Callback | None = ..., confirm: bool = ...
    ) -> SFTPAttributes: ...
    def getfo(self, remotepath: bytes | Text, fl: IO[bytes], callback: _Callback | None = ...) -> int: ...
    def get(
        self, remotepath: bytes | Text, localpath: bytes | Text, callback: _Callback | None = ..., prefetch: bool = ...
    ) -> None: ...

class SFTP(SFTPClient): ...
