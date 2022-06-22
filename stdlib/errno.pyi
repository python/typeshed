import sys
from collections.abc import Mapping

errorcode: Mapping[int, str]

EPERM: int
ENOENT: int
ESRCH: int
EINTR: int
EIO: int
ENXIO: int
E2BIG: int
ENOEXEC: int
EBADF: int
ECHILD: int
EAGAIN: int
ENOMEM: int
EACCES: int
EFAULT: int
if sys.platform != "win32":
    ENOTBLK: int
EBUSY: int
EEXIST: int
EXDEV: int
ENODEV: int
ENOTDIR: int
EISDIR: int
EINVAL: int
ENFILE: int
EMFILE: int
ENOTTY: int
ETXTBSY: int
EFBIG: int
ENOSPC: int
ESPIPE: int
EROFS: int
EMLINK: int
EPIPE: int
EDOM: int
ERANGE: int
EDEADLK: int
ENAMETOOLONG: int
ENOLCK: int
ENOSYS: int
ENOTEMPTY: int
ELOOP: int
EWOULDBLOCK: int
ENOMSG: int
EIDRM: int
if sys.platform != "win32" and sys.platform != "darwin":
    ECHRNG: int
    EL2NSYNC: int
    EL3HLT: int
    EL3RST: int
    ELNRNG: int
    EUNATCH: int
    ENOCSI: int
    EL2HLT: int
    EBADE: int
    EBADR: int
    EXFULL: int
    ENOANO: int
    EBADRQC: int
    EBADSLT: int
if sys.platform != "darwin":
    EDEADLOCK: int
    if sys.platform != "win32":
        EBFONT: int
ENOSTR: int
ENODATA: int
ETIME: int
ENOSR: int
if sys.platform != "win32" and sys.platform != "darwin":
    ENONET: int
    ENOPKG: int
EREMOTE: int
ENOLINK: int
if sys.platform != "win32" and sys.platform != "darwin":
    EADV: int
    ESRMNT: int
    ECOMM: int
EPROTO: int
if sys.platform != "win32":
    EMULTIHOP: int
    if sys.platform != "darwin":
        EDOTDOT: int
EBADMSG: int
EOVERFLOW: int
if sys.platform != "win32" and sys.platform != "darwin":
    ENOTUNIQ: int
    EBADFD: int
    EREMCHG: int
    ELIBACC: int
    ELIBBAD: int
    ELIBSCN: int
    ELIBMAX: int
    ELIBEXEC: int
EILSEQ: int
if sys.platform != "win32" and sys.platform != "darwin":
    ERESTART: int
    ESTRPIPE: int
EUSERS: int
ENOTSOCK: int
EDESTADDRREQ: int
EMSGSIZE: int
EPROTOTYPE: int
ENOPROTOOPT: int
EPROTONOSUPPORT: int
ESOCKTNOSUPPORT: int
ENOTSUP: int
EOPNOTSUPP: int
EPFNOSUPPORT: int
EAFNOSUPPORT: int
EADDRINUSE: int
EADDRNOTAVAIL: int
ENETDOWN: int
ENETUNREACH: int
ENETRESET: int
ECONNABORTED: int
ECONNRESET: int
ENOBUFS: int
EISCONN: int
ENOTCONN: int
ESHUTDOWN: int
ETOOMANYREFS: int
ETIMEDOUT: int
ECONNREFUSED: int
EHOSTDOWN: int
EHOSTUNREACH: int
EALREADY: int
EINPROGRESS: int
ESTALE: int
if sys.platform != "win32" and sys.platform != "darwin":
    EUCLEAN: int
    ENOTNAM: int
    ENAVAIL: int
    EISNAM: int
    EREMOTEIO: int
EDQUOT: int
ECANCELED: int  # undocumented
if sys.platform != "win32" and sys.platform != "darwin":
    EKEYEXPIRED: int  # undocumented
    EKEYREJECTED: int  # undocumented
    EKEYREVOKED: int  # undocumented
    EMEDIUMTYPE: int  # undocumented
    ENOKEY: int  # undocumented
    ENOMEDIUM: int  # undocumented
ENOTRECOVERABLE: int  # undocumented
EOWNERDEAD: int  # undocumented
if sys.platform != "win32":
    if sys.platform != "darwin":
        ERFKILL: int  # undocumented
    EAUTH: int  # undocumented
    EBADARCH: int  # undocumented
    EBADEXEC: int  # undocumented
    EBADMACHO: int  # undocumented
    EBADRPC: int  # undocumented
    EDEVERR: int  # undocumented
    EFTYPE: int  # undocumented
    if sys.platform != "darwin":
        EL: int  # undocumented
        ELOCKUNMAPPED: int  # undocumented
    ENEEDAUTH: int  # undocumented
    ENOATTR: int  # undocumented
    ENOPOLICY: int  # undocumented
    if sys.platform != "darwin":
        ENOTACTIVE: int  # undocumented
    EPROCLIM: int  # undocumented
    EPROCUNAVAIL: int  # undocumented
    EPROGMISMATCH: int  # undocumented
    EPROGUNAVAIL: int  # undocumented
    EPWROFF: int  # undocumented
    if sys.platform != "darwin" or sys.version_info >= (3, 11):
        EQFULL: int  # undocumented
    ERPCMISMATCH: int  # undocumented
    ESHLIBVERS: int  # undocumented

if sys.platform == "win32":
    # All of these are undocumented
    WSABASEERR: int
    WSAEACCES: int
    WSAEADDRINUSE: int
    WSAEADDRNOTAVAIL: int
    WSAEAFNOSUPPORT: int
    WSAEALREADY: int
    WSAEBADF: int
    WSAECONNABORTED: int
    WSAECONNREFUSED: int
    WSAECONNRESET: int
    WSAEDESTADDRREQ: int
    WSAEDISCON: int
    WSAEDQUOT: int
    WSAEFAULT: int
    WSAEHOSTDOWN: int
    WSAEHOSTUNREACH: int
    WSAEINPROGRESS: int
    WSAEINTR: int
    WSAEINVAL: int
    WSAEISCONN: int
    WSAELOOP: int
    WSAEMFILE: int
    WSAEMSGSIZE: int
    WSAENAMETOOLONG: int
    WSAENETDOWN: int
    WSAENETRESET: int
    WSAENETUNREACH: int
    WSAENOBUFS: int
    WSAENOPROTOOPT: int
    WSAENOTCONN: int
    WSAENOTEMPTY: int
    WSAENOTSOCK: int
    WSAEOPNOTSUPP: int
    WSAEPFNOSUPPORT: int
    WSAEPROCLIM: int
    WSAEPROTONOSUPPORT: int
    WSAEPROTOTYPE: int
    WSAEREMOTE: int
    WSAESHUTDOWN: int
    WSAESOCKTNOSUPPORT: int
    WSAESTALE: int
    WSAETIMEDOUT: int
    WSAETOOMANYREFS: int
    WSAEUSERS: int
    WSAEWOULDBLOCK: int
    WSANOTINITIALISED: int
    WSASYSNOTREADY: int
    WSAVERNOTSUPPORTED: int
