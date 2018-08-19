# TODO(MichalPokorny): more precise types

from typing import Any, Tuple

GLOBAL_ACK_EINTR = ...  # type: int
GLOBAL_ALL = ...  # type: int
GLOBAL_DEFAULT = ...  # type: int
GLOBAL_NOTHING = ...  # type: int
GLOBAL_SSL = ...  # type: int
GLOBAL_WIN32 = ...  # type: int

def global_init(option: int) -> None: ...
def global_cleanup() -> None: ...

version = ...  # type: str

def version_info() -> Tuple[int, str, int, str, int, str,
                            int, str, tuple, Any, int, Any]: ...

class error(Exception): ...

class Curl(object):
    def close(self) -> None: ...
    def setopt(self, option: int, value: Any) -> None: ...
    def perform(self) -> None: ...
    def getinfo(self, info: Any) -> Any: ...
    def reset(self) -> None: ...
    def unsetopt(self, option: int) -> Any: ...
    def pause(self, bitmask: Any) -> Any: ...
    def errstr(self) -> str: ...

    # TODO(MichalPokorny): wat?
    USERPWD = ...  # type: int

class CurlMulti(object):
    def close(self) -> None: ...
    def add_handle(self, obj: Curl) -> None: ...
    def remove_handle(self, obj: Curl) -> None: ...
    def perform(self) -> Tuple[Any, int]: ...
    def fdset(self) -> tuple: ...
    def select(self, timeout: float = ...) -> int: ...
    def info_read(self, max_objects: int = ...) -> tuple: ...

class CurlShare(object):
    def close(self) -> None: ...
    def setopt(self, option: int, value: Any) -> Any: ...

ACCEPTTIMEOUT_MS = ...  # type: int
ACCEPT_ENCODING = ...  # type: int
ADDRESS_SCOPE = ...  # type: int
APPCONNECT_TIME = ...  # type: int
APPEND = ...  # type: int
AUTOREFERER = ...  # type: int
BUFFERSIZE = ...  # type: int
CAINFO = ...  # type: int
CAPATH = ...  # type: int
CLOSESOCKETFUNCTION = ...  # type: int
COMPILE_DATE = ...  # type: str
COMPILE_LIBCURL_VERSION_NUM = ...  # type: int
COMPILE_PY_VERSION_HEX = ...  # type: int
CONDITION_UNMET = ...  # type: int
CONNECTTIMEOUT = ...  # type: int
CONNECTTIMEOUT_MS = ...  # type: int
CONNECT_ONLY = ...  # type: int
CONNECT_TIME = ...  # type: int
CONTENT_LENGTH_DOWNLOAD = ...  # type: int
CONTENT_LENGTH_UPLOAD = ...  # type: int
CONTENT_TYPE = ...  # type: int
COOKIE = ...  # type: int
COOKIEFILE = ...  # type: int
COOKIEJAR = ...  # type: int
COOKIELIST = ...  # type: int
COOKIESESSION = ...  # type: int
COPYPOSTFIELDS = ...  # type: int
CRLF = ...  # type: int
CRLFILE = ...  # type: int
CSELECT_ERR = ...  # type: int
CSELECT_IN = ...  # type: int
CSELECT_OUT = ...  # type: int
CURL_HTTP_VERSION_1_0 = ...  # type: int
CURL_HTTP_VERSION_1_1 = ...  # type: int
CURL_HTTP_VERSION_2 = ...  # type: int
CURL_HTTP_VERSION_2_0 = ...  # type: int
CURL_HTTP_VERSION_LAST = ...  # type: int
CURL_HTTP_VERSION_NONE = ...  # type: int
CUSTOMREQUEST = ...  # type: int
DEBUGFUNCTION = ...  # type: int
DIRLISTONLY = ...  # type: int
DNS_CACHE_TIMEOUT = ...  # type: int
DNS_SERVERS = ...  # type: int
DNS_USE_GLOBAL_CACHE = ...  # type: int
EFFECTIVE_URL = ...  # type: int
EGDSOCKET = ...  # type: int
ENCODING = ...  # type: int
EXPECT_100_TIMEOUT_MS = ...  # type: int
FAILONERROR = ...  # type: int
FILE = ...  # type: int
FOLLOWLOCATION = ...  # type: int
FORBID_REUSE = ...  # type: int
FORM_BUFFER = ...  # type: int
FORM_BUFFERPTR = ...  # type: int
FORM_CONTENTS = ...  # type: int
FORM_CONTENTTYPE = ...  # type: int
FORM_FILE = ...  # type: int
FORM_FILENAME = ...  # type: int
FRESH_CONNECT = ...  # type: int
FTPAPPEND = ...  # type: int
FTPAUTH_DEFAULT = ...  # type: int
FTPAUTH_SSL = ...  # type: int
FTPAUTH_TLS = ...  # type: int
FTPLISTONLY = ...  # type: int
FTPMETHOD_DEFAULT = ...  # type: int
FTPMETHOD_MULTICWD = ...  # type: int
FTPMETHOD_NOCWD = ...  # type: int
FTPMETHOD_SINGLECWD = ...  # type: int
FTPPORT = ...  # type: int
FTPSSLAUTH = ...  # type: int
FTPSSL_ALL = ...  # type: int
FTPSSL_CONTROL = ...  # type: int
FTPSSL_NONE = ...  # type: int
FTPSSL_TRY = ...  # type: int
FTP_ACCOUNT = ...  # type: int
FTP_ALTERNATIVE_TO_USER = ...  # type: int
FTP_CREATE_MISSING_DIRS = ...  # type: int
FTP_ENTRY_PATH = ...  # type: int
FTP_FILEMETHOD = ...  # type: int
FTP_RESPONSE_TIMEOUT = ...  # type: int
FTP_SKIP_PASV_IP = ...  # type: int
FTP_SSL = ...  # type: int
FTP_SSL_CCC = ...  # type: int
FTP_USE_EPRT = ...  # type: int
FTP_USE_EPSV = ...  # type: int
FTP_USE_PRET = ...  # type: int
GSSAPI_DELEGATION = ...  # type: int
GSSAPI_DELEGATION_FLAG = ...  # type: int
GSSAPI_DELEGATION_NONE = ...  # type: int
GSSAPI_DELEGATION_POLICY_FLAG = ...  # type: int
HEADER = ...  # type: int
HEADERFUNCTION = ...  # type: int
HEADEROPT = ...  # type: int
HEADER_SEPARATE = ...  # type: int
HEADER_SIZE = ...  # type: int
HEADER_UNIFIED = ...  # type: int
HTTP200ALIASES = ...  # type: int
HTTPAUTH = ...  # type: int
HTTPAUTH_ANY = ...  # type: int
HTTPAUTH_ANYSAFE = ...  # type: int
HTTPAUTH_AVAIL = ...  # type: int
HTTPAUTH_BASIC = ...  # type: int
HTTPAUTH_DIGEST = ...  # type: int
HTTPAUTH_DIGEST_IE = ...  # type: int
HTTPAUTH_GSSNEGOTIATE = ...  # type: int
HTTPAUTH_NEGOTIATE = ...  # type: int
HTTPAUTH_NONE = ...  # type: int
HTTPAUTH_NTLM = ...  # type: int
HTTPAUTH_NTLM_WB = ...  # type: int
HTTPAUTH_ONLY = ...  # type: int
HTTPGET = ...  # type: int
HTTPHEADER = ...  # type: int
HTTPPOST = ...  # type: int
HTTPPROXYTUNNEL = ...  # type: int
HTTP_CODE = ...  # type: int
HTTP_CONNECTCODE = ...  # type: int
HTTP_CONTENT_DECODING = ...  # type: int
HTTP_TRANSFER_DECODING = ...  # type: int
HTTP_VERSION = ...  # type: int
IGNORE_CONTENT_LENGTH = ...  # type: int
INFILE = ...  # type: int
INFILESIZE = ...  # type: int
INFILESIZE_LARGE = ...  # type: int
INFOTYPE_DATA_IN = ...  # type: int
INFOTYPE_DATA_OUT = ...  # type: int
INFOTYPE_HEADER_IN = ...  # type: int
INFOTYPE_HEADER_OUT = ...  # type: int
INFOTYPE_SSL_DATA_IN = ...  # type: int
INFOTYPE_SSL_DATA_OUT = ...  # type: int
INFOTYPE_TEXT = ...  # type: int
INFO_CERTINFO = ...  # type: int
INFO_COOKIELIST = ...  # type: int
INFO_FILETIME = ...  # type: int
INFO_RTSP_CLIENT_CSEQ = ...  # type: int
INFO_RTSP_CSEQ_RECV = ...  # type: int
INFO_RTSP_SERVER_CSEQ = ...  # type: int
INFO_RTSP_SESSION_ID = ...  # type: int
INTERFACE = ...  # type: int
IOCMD_NOP = ...  # type: int
IOCMD_RESTARTREAD = ...  # type: int
IOCTLDATA = ...  # type: int
IOCTLFUNCTION = ...  # type: int
IOE_FAILRESTART = ...  # type: int
IOE_OK = ...  # type: int
IOE_UNKNOWNCMD = ...  # type: int
IPRESOLVE = ...  # type: int
IPRESOLVE_V4 = ...  # type: int
IPRESOLVE_V6 = ...  # type: int
IPRESOLVE_WHATEVER = ...  # type: int
ISSUERCERT = ...  # type: int
KEYPASSWD = ...  # type: int
KHMATCH_MISMATCH = ...  # type: int
KHMATCH_MISSING = ...  # type: int
KHMATCH_OK = ...  # type: int
KHSTAT_DEFER = ...  # type: int
KHSTAT_FINE = ...  # type: int
KHSTAT_FINE_ADD_TO_FILE = ...  # type: int
KHSTAT_REJECT = ...  # type: int
KHTYPE_DSS = ...  # type: int
KHTYPE_RSA = ...  # type: int
KHTYPE_RSA1 = ...  # type: int
KHTYPE_UNKNOWN = ...  # type: int
KRB4LEVEL = ...  # type: int
KRBLEVEL = ...  # type: int
LASTSOCKET = ...  # type: int
LOCALPORT = ...  # type: int
LOCALPORTRANGE = ...  # type: int
LOCAL_IP = ...  # type: int
LOCAL_PORT = ...  # type: int
LOCK_DATA_COOKIE = ...  # type: int
LOCK_DATA_DNS = ...  # type: int
LOCK_DATA_SSL_SESSION = ...  # type: int
LOGIN_OPTIONS = ...  # type: int
LOW_SPEED_LIMIT = ...  # type: int
LOW_SPEED_TIME = ...  # type: int
MAIL_AUTH = ...  # type: int
MAIL_FROM = ...  # type: int
MAIL_RCPT = ...  # type: int
MAXCONNECTS = ...  # type: int
MAXFILESIZE = ...  # type: int
MAXFILESIZE_LARGE = ...  # type: int
MAXREDIRS = ...  # type: int
MAX_RECV_SPEED_LARGE = ...  # type: int
MAX_SEND_SPEED_LARGE = ...  # type: int
M_CHUNK_LENGTH_PENALTY_SIZE = ...  # type: int
M_CONTENT_LENGTH_PENALTY_SIZE = ...  # type: int
M_MAXCONNECTS = ...  # type: int
M_MAX_HOST_CONNECTIONS = ...  # type: int
M_MAX_PIPELINE_LENGTH = ...  # type: int
M_MAX_TOTAL_CONNECTIONS = ...  # type: int
M_PIPELINING = ...  # type: int
M_PIPELINING_SERVER_BL = ...  # type: int
M_PIPELINING_SITE_BL = ...  # type: int
M_SOCKETFUNCTION = ...  # type: int
M_TIMERFUNCTION = ...  # type: int
NAMELOOKUP_TIME = ...  # type: int
NETRC = ...  # type: int
NETRC_FILE = ...  # type: int
NETRC_IGNORED = ...  # type: int
NETRC_OPTIONAL = ...  # type: int
NETRC_REQUIRED = ...  # type: int
NEW_DIRECTORY_PERMS = ...  # type: int
NEW_FILE_PERMS = ...  # type: int
NOBODY = ...  # type: int
NOPROGRESS = ...  # type: int
NOPROXY = ...  # type: int
NOSIGNAL = ...  # type: int
NUM_CONNECTS = ...  # type: int
OPENSOCKETFUNCTION = ...  # type: int
OPT_CERTINFO = ...  # type: int
OPT_FILETIME = ...  # type: int
OS_ERRNO = ...  # type: int
PASSWORD = ...  # type: int
PATH_AS_IS = ...  # type: int
PAUSE_ALL = ...  # type: int
PAUSE_CONT = ...  # type: int
PAUSE_RECV = ...  # type: int
PAUSE_SEND = ...  # type: int
PINNEDPUBLICKEY = ...  # type: int
PIPEWAIT = ...  # type: int
PIPE_HTTP1 = ...  # type: int
PIPE_MULTIPLEX = ...  # type: int
PIPE_NOTHING = ...  # type: int
POLL_IN = ...  # type: int
POLL_INOUT = ...  # type: int
POLL_NONE = ...  # type: int
POLL_OUT = ...  # type: int
POLL_REMOVE = ...  # type: int
PORT = ...  # type: int
POST = ...  # type: int
POST301 = ...  # type: int
POSTFIELDS = ...  # type: int
POSTFIELDSIZE = ...  # type: int
POSTFIELDSIZE_LARGE = ...  # type: int
POSTQUOTE = ...  # type: int
POSTREDIR = ...  # type: int
PREQUOTE = ...  # type: int
PRETRANSFER_TIME = ...  # type: int
PRIMARY_IP = ...  # type: int
PRIMARY_PORT = ...  # type: int
PROGRESSFUNCTION = ...  # type: int
PROTOCOLS = ...  # type: int
PROTO_ALL = ...  # type: int
PROTO_DICT = ...  # type: int
PROTO_FILE = ...  # type: int
PROTO_FTP = ...  # type: int
PROTO_FTPS = ...  # type: int
PROTO_GOPHER = ...  # type: int
PROTO_HTTP = ...  # type: int
PROTO_HTTPS = ...  # type: int
PROTO_IMAP = ...  # type: int
PROTO_IMAPS = ...  # type: int
PROTO_LDAP = ...  # type: int
PROTO_LDAPS = ...  # type: int
PROTO_POP3 = ...  # type: int
PROTO_POP3S = ...  # type: int
PROTO_RTMP = ...  # type: int
PROTO_RTMPE = ...  # type: int
PROTO_RTMPS = ...  # type: int
PROTO_RTMPT = ...  # type: int
PROTO_RTMPTE = ...  # type: int
PROTO_RTMPTS = ...  # type: int
PROTO_RTSP = ...  # type: int
PROTO_SCP = ...  # type: int
PROTO_SFTP = ...  # type: int
PROTO_SMB = ...  # type: int
PROTO_SMBS = ...  # type: int
PROTO_SMTP = ...  # type: int
PROTO_SMTPS = ...  # type: int
PROTO_TELNET = ...  # type: int
PROTO_TFTP = ...  # type: int
PROXY = ...  # type: int
PROXYAUTH = ...  # type: int
PROXYAUTH_AVAIL = ...  # type: int
PROXYHEADER = ...  # type: int
PROXYPASSWORD = ...  # type: int
PROXYPORT = ...  # type: int
PROXYTYPE = ...  # type: int
PROXYTYPE_HTTP = ...  # type: int
PROXYTYPE_HTTP_1_0 = ...  # type: int
PROXYTYPE_SOCKS4 = ...  # type: int
PROXYTYPE_SOCKS4A = ...  # type: int
PROXYTYPE_SOCKS5 = ...  # type: int
PROXYTYPE_SOCKS5_HOSTNAME = ...  # type: int
PROXYUSERNAME = ...  # type: int
PROXYUSERPWD = ...  # type: int
PROXY_SERVICE_NAME = ...  # type: int
PROXY_TRANSFER_MODE = ...  # type: int
PUT = ...  # type: int
QUOTE = ...  # type: int
RANDOM_FILE = ...  # type: int
RANGE = ...  # type: int
READDATA = ...  # type: int
READFUNCTION = ...  # type: int
READFUNC_ABORT = ...  # type: int
READFUNC_PAUSE = ...  # type: int
REDIRECT_COUNT = ...  # type: int
REDIRECT_TIME = ...  # type: int
REDIRECT_URL = ...  # type: int
REDIR_POST_301 = ...  # type: int
REDIR_POST_302 = ...  # type: int
REDIR_POST_303 = ...  # type: int
REDIR_POST_ALL = ...  # type: int
REDIR_PROTOCOLS = ...  # type: int
REFERER = ...  # type: int
REQUEST_SIZE = ...  # type: int
RESOLVE = ...  # type: int
RESPONSE_CODE = ...  # type: int
RESUME_FROM = ...  # type: int
RESUME_FROM_LARGE = ...  # type: int
SASL_IR = ...  # type: int
SEEKFUNCTION = ...  # type: int
SEEKFUNC_CANTSEEK = ...  # type: int
SEEKFUNC_FAIL = ...  # type: int
SEEKFUNC_OK = ...  # type: int
SERVICE_NAME = ...  # type: int
SHARE = ...  # type: int
SH_SHARE = ...  # type: int
SH_UNSHARE = ...  # type: int
SIZE_DOWNLOAD = ...  # type: int
SIZE_UPLOAD = ...  # type: int
SOCKET_TIMEOUT = ...  # type: int
SOCKOPTFUNCTION = ...  # type: int
SOCKOPT_ALREADY_CONNECTED = ...  # type: int
SOCKOPT_ERROR = ...  # type: int
SOCKOPT_OK = ...  # type: int
SOCKS5_GSSAPI_NEC = ...  # type: int
SOCKS5_GSSAPI_SERVICE = ...  # type: int
SOCKTYPE_ACCEPT = ...  # type: int
SOCKTYPE_IPCXN = ...  # type: int
SPEED_DOWNLOAD = ...  # type: int
SPEED_UPLOAD = ...  # type: int
SSH_AUTH_ANY = ...  # type: int
SSH_AUTH_DEFAULT = ...  # type: int
SSH_AUTH_HOST = ...  # type: int
SSH_AUTH_KEYBOARD = ...  # type: int
SSH_AUTH_NONE = ...  # type: int
SSH_AUTH_PASSWORD = ...  # type: int
SSH_AUTH_PUBLICKEY = ...  # type: int
SSH_AUTH_TYPES = ...  # type: int
SSH_HOST_PUBLIC_KEY_MD5 = ...  # type: int
SSH_KEYFUNCTION = ...  # type: int
SSH_KNOWNHOSTS = ...  # type: int
SSH_PRIVATE_KEYFILE = ...  # type: int
SSH_PUBLIC_KEYFILE = ...  # type: int
SSLCERT = ...  # type: int
SSLCERTPASSWD = ...  # type: int
SSLCERTTYPE = ...  # type: int
SSLENGINE = ...  # type: int
SSLENGINE_DEFAULT = ...  # type: int
SSLKEY = ...  # type: int
SSLKEYPASSWD = ...  # type: int
SSLKEYTYPE = ...  # type: int
SSLOPT_ALLOW_BEAST = ...  # type: int
SSLVERSION = ...  # type: int
SSLVERSION_DEFAULT = ...  # type: int
SSLVERSION_SSLv2 = ...  # type: int
SSLVERSION_SSLv3 = ...  # type: int
SSLVERSION_TLSv1 = ...  # type: int
SSLVERSION_TLSv1_0 = ...  # type: int
SSLVERSION_TLSv1_1 = ...  # type: int
SSLVERSION_TLSv1_2 = ...  # type: int
SSL_CIPHER_LIST = ...  # type: int
SSL_ENABLE_ALPN = ...  # type: int
SSL_ENABLE_NPN = ...  # type: int
SSL_ENGINES = ...  # type: int
SSL_FALSESTART = ...  # type: int
SSL_OPTIONS = ...  # type: int
SSL_SESSIONID_CACHE = ...  # type: int
SSL_VERIFYHOST = ...  # type: int
SSL_VERIFYPEER = ...  # type: int
SSL_VERIFYRESULT = ...  # type: int
SSL_VERIFYSTATUS = ...  # type: int
STARTTRANSFER_TIME = ...  # type: int
STDERR = ...  # type: int
TCP_KEEPALIVE = ...  # type: int
TCP_KEEPIDLE = ...  # type: int
TCP_KEEPINTVL = ...  # type: int
TCP_NODELAY = ...  # type: int
TELNETOPTIONS = ...  # type: int
TFTP_BLKSIZE = ...  # type: int
TIMECONDITION = ...  # type: int
TIMECONDITION_IFMODSINCE = ...  # type: int
TIMECONDITION_IFUNMODSINCE = ...  # type: int
TIMECONDITION_LASTMOD = ...  # type: int
TIMECONDITION_NONE = ...  # type: int
TIMEOUT = ...  # type: int
TIMEOUT_MS = ...  # type: int
TIMEVALUE = ...  # type: int
TLSAUTH_PASSWORD = ...  # type: int
TLSAUTH_TYPE = ...  # type: int
TLSAUTH_USERNAME = ...  # type: int
TOTAL_TIME = ...  # type: int
TRANSFERTEXT = ...  # type: int
TRANSFER_ENCODING = ...  # type: int
UNIX_SOCKET_PATH = ...  # type: int
UNRESTRICTED_AUTH = ...  # type: int
UPLOAD = ...  # type: int
URL = ...  # type: int
USERAGENT = ...  # type: int
USERNAME = ...  # type: int
USERPWD = ...  # type: int
USESSL_ALL = ...  # type: int
USESSL_CONTROL = ...  # type: int
USESSL_NONE = ...  # type: int
USESSL_TRY = ...  # type: int
USE_SSL = ...  # type: int
VERBOSE = ...  # type: int
VERSION_ASYNCHDNS = ...  # type: int
VERSION_CONV = ...  # type: int
VERSION_CURLDEBUG = ...  # type: int
VERSION_DEBUG = ...  # type: int
VERSION_GSSAPI = ...  # type: int
VERSION_GSSNEGOTIATE = ...  # type: int
VERSION_HTTP2 = ...  # type: int
VERSION_IDN = ...  # type: int
VERSION_IPV6 = ...  # type: int
VERSION_KERBEROS4 = ...  # type: int
VERSION_KERBEROS5 = ...  # type: int
VERSION_LARGEFILE = ...  # type: int
VERSION_LIBZ = ...  # type: int
VERSION_NTLM = ...  # type: int
VERSION_NTLM_WB = ...  # type: int
VERSION_SPNEGO = ...  # type: int
VERSION_SSL = ...  # type: int
VERSION_SSPI = ...  # type: int
VERSION_TLSAUTH_SRP = ...  # type: int
VERSION_UNIX_SOCKETS = ...  # type: int
WILDCARDMATCH = ...  # type: int
WRITEDATA = ...  # type: int
WRITEFUNCTION = ...  # type: int
WRITEFUNC_PAUSE = ...  # type: int
WRITEHEADER = ...  # type: int
XFERINFOFUNCTION = ...  # type: int
XOAUTH2_BEARER = ...  # type: int

E_ABORTED_BY_CALLBACK = ...  # type: int
E_AGAIN = ...  # type: int
E_ALREADY_COMPLETE = ...  # type: int
E_BAD_CALLING_ORDER = ...  # type: int
E_BAD_CONTENT_ENCODING = ...  # type: int
E_BAD_DOWNLOAD_RESUME = ...  # type: int
E_BAD_FUNCTION_ARGUMENT = ...  # type: int
E_BAD_PASSWORD_ENTERED = ...  # type: int
E_CALL_MULTI_PERFORM = ...  # type: int
E_CHUNK_FAILED = ...  # type: int
E_CONV_FAILED = ...  # type: int
E_CONV_REQD = ...  # type: int
E_COULDNT_CONNECT = ...  # type: int
E_COULDNT_RESOLVE_HOST = ...  # type: int
E_COULDNT_RESOLVE_PROXY = ...  # type: int
E_FAILED_INIT = ...  # type: int
E_FILESIZE_EXCEEDED = ...  # type: int
E_FILE_COULDNT_READ_FILE = ...  # type: int
E_FTP_ACCEPT_FAILED = ...  # type: int
E_FTP_ACCEPT_TIMEOUT = ...  # type: int
E_FTP_ACCESS_DENIED = ...  # type: int
E_FTP_BAD_DOWNLOAD_RESUME = ...  # type: int
E_FTP_BAD_FILE_LIST = ...  # type: int
E_FTP_CANT_GET_HOST = ...  # type: int
E_FTP_CANT_RECONNECT = ...  # type: int
E_FTP_COULDNT_GET_SIZE = ...  # type: int
E_FTP_COULDNT_RETR_FILE = ...  # type: int
E_FTP_COULDNT_SET_ASCII = ...  # type: int
E_FTP_COULDNT_SET_BINARY = ...  # type: int
E_FTP_COULDNT_SET_TYPE = ...  # type: int
E_FTP_COULDNT_STOR_FILE = ...  # type: int
E_FTP_COULDNT_USE_REST = ...  # type: int
E_FTP_PARTIAL_FILE = ...  # type: int
E_FTP_PORT_FAILED = ...  # type: int
E_FTP_PRET_FAILED = ...  # type: int
E_FTP_QUOTE_ERROR = ...  # type: int
E_FTP_SSL_FAILED = ...  # type: int
E_FTP_USER_PASSWORD_INCORRECT = ...  # type: int
E_FTP_WEIRD_227_FORMAT = ...  # type: int
E_FTP_WEIRD_PASS_REPLY = ...  # type: int
E_FTP_WEIRD_PASV_REPLY = ...  # type: int
E_FTP_WEIRD_SERVER_REPLY = ...  # type: int
E_FTP_WEIRD_USER_REPLY = ...  # type: int
E_FTP_WRITE_ERROR = ...  # type: int
E_FUNCTION_NOT_FOUND = ...  # type: int
E_GOT_NOTHING = ...  # type: int
E_HTTP2 = ...  # type: int
E_HTTP_NOT_FOUND = ...  # type: int
E_HTTP_PORT_FAILED = ...  # type: int
E_HTTP_POST_ERROR = ...  # type: int
E_HTTP_RANGE_ERROR = ...  # type: int
E_HTTP_RETURNED_ERROR = ...  # type: int
E_INTERFACE_FAILED = ...  # type: int
E_LDAP_CANNOT_BIND = ...  # type: int
E_LDAP_INVALID_URL = ...  # type: int
E_LDAP_SEARCH_FAILED = ...  # type: int
E_LIBRARY_NOT_FOUND = ...  # type: int
E_LOGIN_DENIED = ...  # type: int
E_MALFORMAT_USER = ...  # type: int
E_MULTI_ADDED_ALREADY = ...  # type: int
E_MULTI_BAD_EASY_HANDLE = ...  # type: int
E_MULTI_BAD_HANDLE = ...  # type: int
E_MULTI_BAD_SOCKET = ...  # type: int
E_MULTI_CALL_MULTI_PERFORM = ...  # type: int
E_MULTI_CALL_MULTI_SOCKET = ...  # type: int
E_MULTI_INTERNAL_ERROR = ...  # type: int
E_MULTI_OK = ...  # type: int
E_MULTI_OUT_OF_MEMORY = ...  # type: int
E_MULTI_UNKNOWN_OPTION = ...  # type: int
E_NOT_BUILT_IN = ...  # type: int
E_NO_CONNECTION_AVAILABLE = ...  # type: int
E_OK = ...  # type: int
E_OPERATION_TIMEDOUT = ...  # type: int
E_OPERATION_TIMEOUTED = ...  # type: int
E_OUT_OF_MEMORY = ...  # type: int
E_PARTIAL_FILE = ...  # type: int
E_PEER_FAILED_VERIFICATION = ...  # type: int
E_QUOTE_ERROR = ...  # type: int
E_RANGE_ERROR = ...  # type: int
E_READ_ERROR = ...  # type: int
E_RECV_ERROR = ...  # type: int
E_REMOTE_ACCESS_DENIED = ...  # type: int
E_REMOTE_DISK_FULL = ...  # type: int
E_REMOTE_FILE_EXISTS = ...  # type: int
E_REMOTE_FILE_NOT_FOUND = ...  # type: int
E_RTSP_CSEQ_ERROR = ...  # type: int
E_RTSP_SESSION_ERROR = ...  # type: int
E_SEND_ERROR = ...  # type: int
E_SEND_FAIL_REWIND = ...  # type: int
E_SHARE_IN_USE = ...  # type: int
E_SSH = ...  # type: int
E_SSL_CACERT = ...  # type: int
E_SSL_CACERT_BADFILE = ...  # type: int
E_SSL_CERTPROBLEM = ...  # type: int
E_SSL_CIPHER = ...  # type: int
E_SSL_CONNECT_ERROR = ...  # type: int
E_SSL_CRL_BADFILE = ...  # type: int
E_SSL_ENGINE_INITFAILED = ...  # type: int
E_SSL_ENGINE_NOTFOUND = ...  # type: int
E_SSL_ENGINE_SETFAILED = ...  # type: int
E_SSL_INVALIDCERTSTATUS = ...  # type: int
E_SSL_ISSUER_ERROR = ...  # type: int
E_SSL_PEER_CERTIFICATE = ...  # type: int
E_SSL_PINNEDPUBKEYNOTMATCH = ...  # type: int
E_SSL_SHUTDOWN_FAILED = ...  # type: int
E_TELNET_OPTION_SYNTAX = ...  # type: int
E_TFTP_DISKFULL = ...  # type: int
E_TFTP_EXISTS = ...  # type: int
E_TFTP_ILLEGAL = ...  # type: int
E_TFTP_NOSUCHUSER = ...  # type: int
E_TFTP_NOTFOUND = ...  # type: int
E_TFTP_PERM = ...  # type: int
E_TFTP_UNKNOWNID = ...  # type: int
E_TOO_MANY_REDIRECTS = ...  # type: int
E_UNKNOWN_OPTION = ...  # type: int
E_UNKNOWN_TELNET_OPTION = ...  # type: int
E_UNSUPPORTED_PROTOCOL = ...  # type: int
E_UPLOAD_FAILED = ...  # type: int
E_URL_MALFORMAT = ...  # type: int
E_URL_MALFORMAT_USER = ...  # type: int
E_USE_SSL_FAILED = ...  # type: int
E_WRITE_ERROR = ...  # type: int
