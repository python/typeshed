import sys
from _typeshed import FileDescriptorLike
from typing import Any
from typing_extensions import TypeAlias

# Must be a list of length 7, containing 6 ints and a list of NCCS 1-character bytes or ints.
_Attr: TypeAlias = list[int | list[bytes | int]]
# Same as _Attr for return types; we use Any to avoid a union.
_AttrReturn: TypeAlias = list[Any]

if sys.platform != "win32":
    B0: int
    B1000000: int
    B110: int
    B115200: int
    B1152000: int
    B1200: int
    B134: int
    B150: int
    B1500000: int
    B1800: int
    B19200: int
    B200: int
    B2000000: int
    B230400: int
    B2400: int
    B2500000: int
    B300: int
    B3000000: int
    B3500000: int
    B38400: int
    B4000000: int
    B460800: int
    B4800: int
    B50: int
    B500000: int
    B57600: int
    B576000: int
    B600: int
    B75: int
    B921600: int
    B9600: int
    BRKINT: int
    BS0: int
    BS1: int
    BSDLY: int
    CBAUD: int
    CBAUDEX: int
    CDEL: int
    CDSUSP: int
    CEOF: int
    CEOL: int
    CEOL2: int
    CEOT: int
    CERASE: int
    CESC: int
    CFLUSH: int
    CIBAUD: int
    CINTR: int
    CKILL: int
    CLNEXT: int
    CLOCAL: int
    CNUL: int
    COMMON: int
    CQUIT: int
    CR0: int
    CR1: int
    CR2: int
    CR3: int
    CRDLY: int
    CREAD: int
    CRPRNT: int
    CRTSCTS: int
    CS5: int
    CS6: int
    CS7: int
    CS8: int
    CSIZE: int
    CSTART: int
    CSTOP: int
    CSTOPB: int
    CSUSP: int
    CSWTCH: int
    CWERASE: int
    ECHO: int
    ECHOCTL: int
    ECHOE: int
    ECHOK: int
    ECHOKE: int
    ECHONL: int
    ECHOPRT: int
    EXTA: int
    EXTB: int
    FF0: int
    FF1: int
    FFDLY: int
    FIOASYNC: int
    FIOCLEX: int
    FIONBIO: int
    FIONCLEX: int
    FIONREAD: int
    FLUSHO: int
    HUPCL: int
    IBSHIFT: int
    ICANON: int
    ICRNL: int
    IEXTEN: int
    IGNBRK: int
    IGNCR: int
    IGNPAR: int
    IMAXBEL: int
    INIT_C_CC: int
    INLCR: int
    INPCK: int
    IOCSIZE_MASK: int
    IOCSIZE_SHIFT: int
    ISIG: int
    ISTRIP: int
    IUCLC: int
    IXANY: int
    IXOFF: int
    IXON: int
    N_MOUSE: int
    N_PPP: int
    N_SLIP: int
    N_STRIP: int
    N_TTY: int
    NCC: int
    NCCS: int
    NL0: int
    NL1: int
    NLDLY: int
    NOFLSH: int
    NSWTCH: int
    OCRNL: int
    OFDEL: int
    OFILL: int
    OLCUC: int
    ONLCR: int
    ONLRET: int
    ONOCR: int
    OPOST: int
    PARENB: int
    PARMRK: int
    PARODD: int
    PENDIN: int
    TAB0: int
    TAB1: int
    TAB2: int
    TAB3: int
    TABDLY: int
    TCFLSH: int
    TCGETA: int
    TCGETS: int
    TCIFLUSH: int
    TCIOFF: int
    TCIOFLUSH: int
    TCION: int
    TCOFLUSH: int
    TCOOFF: int
    TCOON: int
    TCSADRAIN: int
    TCSAFLUSH: int
    TCSANOW: int
    TCSASOFT: int
    TCSBRK: int
    TCSBRKP: int
    TCSETA: int
    TCSETAF: int
    TCSETAW: int
    TCSETS: int
    TCSETSF: int
    TCSETSW: int
    TCXONC: int
    TIOCCONS: int
    TIOCEXCL: int
    TIOCGETD: int
    TIOCGICOUNT: int
    TIOCGLCKTRMIOS: int
    TIOCGPGRP: int
    TIOCGSERIAL: int
    TIOCGSIZE: int
    TIOCGSOFTCAR: int
    TIOCGWINSZ: int
    TIOCINQ: int
    TIOCLINUX: int
    TIOCM_CAR: int
    TIOCM_CD: int
    TIOCM_CTS: int
    TIOCM_DSR: int
    TIOCM_DTR: int
    TIOCM_LE: int
    TIOCM_RI: int
    TIOCM_RNG: int
    TIOCM_RTS: int
    TIOCM_SR: int
    TIOCM_ST: int
    TIOCMBIC: int
    TIOCMBIS: int
    TIOCMGET: int
    TIOCMIWAIT: int
    TIOCMSET: int
    TIOCNOTTY: int
    TIOCNXCL: int
    TIOCOUTQ: int
    TIOCPKT_DATA: int
    TIOCPKT_DOSTOP: int
    TIOCPKT_FLUSHREAD: int
    TIOCPKT_FLUSHWRITE: int
    TIOCPKT_NOSTOP: int
    TIOCPKT_START: int
    TIOCPKT_STOP: int
    TIOCPKT: int
    TIOCSCTTY: int
    TIOCSER_TEMT: int
    TIOCSERCONFIG: int
    TIOCSERGETLSR: int
    TIOCSERGETMULTI: int
    TIOCSERGSTRUCT: int
    TIOCSERGWILD: int
    TIOCSERSETMULTI: int
    TIOCSERSWILD: int
    TIOCSETD: int
    TIOCSLCKTRMIOS: int
    TIOCSPGRP: int
    TIOCSSERIAL: int
    TIOCSSIZE: int
    TIOCSSOFTCAR: int
    TIOCSTI: int
    TIOCSWINSZ: int
    TIOCTTYGSTRUCT: int
    TOSTOP: int
    VDISCARD: int
    VEOF: int
    VEOL: int
    VEOL2: int
    VERASE: int
    VINTR: int
    VKILL: int
    VLNEXT: int
    VMIN: int
    VQUIT: int
    VREPRINT: int
    VSTART: int
    VSTOP: int
    VSUSP: int
    VSWTC: int
    VSWTCH: int
    VT0: int
    VT1: int
    VTDLY: int
    VTIME: int
    VWERASE: int
    XCASE: int
    XTABS: int

    def tcgetattr(__fd: FileDescriptorLike) -> _AttrReturn: ...
    def tcsetattr(__fd: FileDescriptorLike, __when: int, __attributes: _Attr) -> None: ...
    def tcsendbreak(__fd: FileDescriptorLike, __duration: int) -> None: ...
    def tcdrain(__fd: FileDescriptorLike) -> None: ...
    def tcflush(__fd: FileDescriptorLike, __queue: int) -> None: ...
    def tcflow(__fd: FileDescriptorLike, __action: int) -> None: ...
    if sys.version_info >= (3, 11):
        def tcgetwinsize(__fd: FileDescriptorLike) -> tuple[int, int]: ...
        def tcsetwinsize(__fd: FileDescriptorLike, __winsize: tuple[int, int]) -> None: ...

    class error(Exception): ...
