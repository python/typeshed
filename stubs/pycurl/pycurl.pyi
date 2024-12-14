import sys
from _typeshed import Incomplete
from typing import Final, final
from typing_extensions import Self

version: str

def global_init(option: int) -> None: ...
def global_cleanup() -> None: ...
def version_info() -> (
    tuple[int, str, int, str, int, str, int, str, tuple[str, ...], Incomplete | None, int, Incomplete | None]
): ...

class error(Exception): ...

@final
class Curl:
    USERPWD: int
    def close(self) -> None: ...
    def setopt(self, option: int, value) -> None: ...
    def setopt_string(self, option: int, value: str) -> None: ...
    def perform(self) -> None: ...
    def perform_rb(self) -> bytes: ...
    def perform_rs(self) -> str: ...
    def getinfo(self, info): ...
    def getinfo_raw(self, info): ...
    def reset(self) -> None: ...
    def unsetopt(self, option: int): ...
    def pause(self, bitmask): ...
    def errstr(self) -> str: ...
    def duphandle(self) -> Self: ...
    def errstr_raw(self) -> bytes: ...
    if sys.platform == "linux" or sys.platform == "macos":
        def set_ca_certs(self, value: bytes | str, /) -> None: ...

@final
class CurlMulti:
    def close(self) -> None: ...
    def add_handle(self, obj: Curl) -> None: ...
    def remove_handle(self, obj: Curl) -> None: ...
    def setopt(self, option: int, value) -> None: ...
    def perform(self) -> tuple[Incomplete, int]: ...
    def fdset(self) -> tuple[list[Incomplete], list[Incomplete], list[Incomplete]]: ...
    def select(self, timeout: float) -> int: ...
    def info_read(self, max_objects: int = ...) -> tuple[int, list[Incomplete], list[Incomplete]]: ...
    def socket_action(self, sockfd: int, ev_bitmask: int) -> tuple[int, int]: ...
    def assign(self, sockfd: int, socket, /): ...
    def socket_all(self) -> tuple[int, int]: ...
    def timeout(self) -> int: ...

@final
class CurlShare:
    def close(self) -> None: ...
    def setopt(self, option: int, value): ...


ACCEPTTIMEOUT_MS: Final = 212
ACCEPT_ENCODING: Final = 10102
ADDRESS_SCOPE: Final = 171
APPCONNECT_TIME: Final = 3145761
APPEND: Final = 50
AUTOREFERER: Final = 58
AWS_SIGV4: Final = 10305
BUFFERSIZE: Final = 98
CAINFO: Final = 10065
CAINFO_BLOB: Final = 40309
CAPATH: Final = 10097
CLOSESOCKETFUNCTION: Final = 20208
COMPILE_LIBCURL_VERSION_NUM: Final = 525824
COMPILE_PY_VERSION_HEX: Final = 50925040
COMPILE_SSL_LIB: Final = "schannel"
CONDITION_UNMET: Final = 2097187
CONNECTTIMEOUT: Final = 78
CONNECTTIMEOUT_MS: Final = 156
CONNECT_ONLY: Final = 141
CONNECT_TIME: Final = 3145733
CONNECT_TO: Final = 10243
CONTENT_LENGTH_DOWNLOAD: Final = 3145743
CONTENT_LENGTH_UPLOAD: Final = 3145744
CONTENT_TYPE: Final = 1048594
COOKIE: Final = 10022
COOKIEFILE: Final = 10031
COOKIEJAR: Final = 10082
COOKIELIST: Final = 10135
COOKIESESSION: Final = 96
COPYPOSTFIELDS: Final = 10165
CRLF: Final = 27
CRLFILE: Final = 10169
CSELECT_ERR: Final = 4
CSELECT_IN: Final = 1
CSELECT_OUT: Final = 2
CURL_HTTP_VERSION_1_0: Final = 1
CURL_HTTP_VERSION_1_1: Final = 2
CURL_HTTP_VERSION_2: Final = 3
CURL_HTTP_VERSION_2TLS: Final = 4
CURL_HTTP_VERSION_2_0: Final = 3
CURL_HTTP_VERSION_2_PRIOR_KNOWLEDGE: Final = 5
CURL_HTTP_VERSION_3: Final = 30
CURL_HTTP_VERSION_3ONLY: Final = 31
CURL_HTTP_VERSION_LAST: Final = 32
CURL_HTTP_VERSION_NONE: Final = 0
CURL_VERSION_ALTSVC: Final = 16777216
CURL_VERSION_BROTLI: Final = 8388608
CURL_VERSION_GSASL: Final = 536870912
CURL_VERSION_HSTS: Final = 268435456
CURL_VERSION_HTTP3: Final = 33554432
CURL_VERSION_HTTPS_PROXY: Final = 2097152
CURL_VERSION_MULTI_SSL: Final = 4194304
CURL_VERSION_UNICODE: Final = 134217728
CURL_VERSION_ZSTD: Final = 67108864
CUSTOMREQUEST: Final = 10036
DEBUGFUNCTION: Final = 20094
DEFAULT_PROTOCOL: Final = 10238
DIRLISTONLY: Final = 48
DNS_CACHE_TIMEOUT: Final = 92
DNS_SERVERS: Final = 10211
DNS_USE_GLOBAL_CACHE: Final = 91
DOH_URL: Final = 10279
EFFECTIVE_URL: Final = 1048577
EFFECTIVE_METHOD: Final = 1048634
EGDSOCKET: Final = 10077
ENCODING: Final = 10102
EXPECT_100_TIMEOUT_MS: Final = 227
E_ABORTED_BY_CALLBACK: Final = 42
E_AGAIN: Final = 81
E_ALREADY_COMPLETE: Final = 99999
E_BAD_CALLING_ORDER: Final = 44
E_BAD_CONTENT_ENCODING: Final = 61
E_BAD_DOWNLOAD_RESUME: Final = 36
E_BAD_FUNCTION_ARGUMENT: Final = 43
E_BAD_PASSWORD_ENTERED: Final = 46
E_CALL_MULTI_PERFORM: Final = -1
E_CHUNK_FAILED: Final = 88
E_CONV_FAILED: Final = 75
E_CONV_REQD: Final = 76
E_COULDNT_CONNECT: Final = 7
E_COULDNT_RESOLVE_HOST: Final = 6
E_COULDNT_RESOLVE_PROXY: Final = 5
E_FAILED_INIT: Final = 2
E_FILESIZE_EXCEEDED: Final = 63
E_FILE_COULDNT_READ_FILE: Final = 37
E_FTP_ACCEPT_FAILED: Final = 10
E_FTP_ACCEPT_TIMEOUT: Final = 12
E_FTP_ACCESS_DENIED: Final = 9
E_FTP_BAD_DOWNLOAD_RESUME: Final = 36
E_FTP_BAD_FILE_LIST: Final = 87
E_FTP_CANT_GET_HOST: Final = 15
E_FTP_CANT_RECONNECT: Final = 16
E_FTP_COULDNT_GET_SIZE: Final = 32
E_FTP_COULDNT_RETR_FILE: Final = 19
E_FTP_COULDNT_SET_ASCII: Final = 29
E_FTP_COULDNT_SET_BINARY: Final = 17
E_FTP_COULDNT_SET_TYPE: Final = 17
E_FTP_COULDNT_STOR_FILE: Final = 25
E_FTP_COULDNT_USE_REST: Final = 31
E_FTP_PARTIAL_FILE: Final = 18
E_FTP_PORT_FAILED: Final = 30
E_FTP_PRET_FAILED: Final = 84
E_FTP_QUOTE_ERROR: Final = 21
E_FTP_SSL_FAILED: Final = 64
E_FTP_USER_PASSWORD_INCORRECT: Final = 10
E_FTP_WEIRD_227_FORMAT: Final = 14
E_FTP_WEIRD_PASS_REPLY: Final = 11
E_FTP_WEIRD_PASV_REPLY: Final = 13
E_FTP_WEIRD_SERVER_REPLY: Final = 8
E_FTP_WEIRD_USER_REPLY: Final = 12
E_FTP_WRITE_ERROR: Final = 20
E_FUNCTION_NOT_FOUND: Final = 41
E_GOT_NOTHING: Final = 52
E_HTTP2: Final = 16
E_HTTP_NOT_FOUND: Final = 22
E_HTTP_PORT_FAILED: Final = 45
E_HTTP_POST_ERROR: Final = 34
E_HTTP_RANGE_ERROR: Final = 33
E_HTTP_RETURNED_ERROR: Final = 22
E_INTERFACE_FAILED: Final = 45
E_LDAP_CANNOT_BIND: Final = 38
E_LDAP_INVALID_URL: Final = 62
E_LDAP_SEARCH_FAILED: Final = 39
E_LIBRARY_NOT_FOUND: Final = 40
E_LOGIN_DENIED: Final = 67
E_MALFORMAT_USER: Final = 24
E_MULTI_ADDED_ALREADY: Final = 7
E_MULTI_BAD_EASY_HANDLE: Final = 2
E_MULTI_BAD_HANDLE: Final = 1
E_MULTI_BAD_SOCKET: Final = 5
E_MULTI_CALL_MULTI_PERFORM: Final = -1
E_MULTI_CALL_MULTI_SOCKET: Final = -1
E_MULTI_INTERNAL_ERROR: Final = 4
E_MULTI_OK: Final = 0
E_MULTI_OUT_OF_MEMORY: Final = 3
E_MULTI_UNKNOWN_OPTION: Final = 6
E_NOT_BUILT_IN: Final = 4
E_NO_CONNECTION_AVAILABLE: Final = 89
E_OK: Final = 0
E_OPERATION_TIMEDOUT: Final = 28
E_OPERATION_TIMEOUTED: Final = 28
E_OUT_OF_MEMORY: Final = 27
E_PARTIAL_FILE: Final = 18
E_PEER_FAILED_VERIFICATION: Final = 60
E_QUOTE_ERROR: Final = 21
E_RANGE_ERROR: Final = 33
E_READ_ERROR: Final = 26
E_RECV_ERROR: Final = 56
E_REMOTE_ACCESS_DENIED: Final = 9
E_REMOTE_DISK_FULL: Final = 70
E_REMOTE_FILE_EXISTS: Final = 73
E_REMOTE_FILE_NOT_FOUND: Final = 78
E_RTSP_CSEQ_ERROR: Final = 85
E_RTSP_SESSION_ERROR: Final = 86
E_SEND_ERROR: Final = 55
E_SEND_FAIL_REWIND: Final = 65
E_SHARE_IN_USE: Final = 57
E_SSH: Final = 79
E_SSL_CACERT: Final = 60
E_SSL_CACERT_BADFILE: Final = 77
E_SSL_CERTPROBLEM: Final = 58
E_SSL_CIPHER: Final = 59
E_SSL_CONNECT_ERROR: Final = 35
E_SSL_CRL_BADFILE: Final = 82
E_SSL_ENGINE_INITFAILED: Final = 66
E_SSL_ENGINE_NOTFOUND: Final = 53
E_SSL_ENGINE_SETFAILED: Final = 54
E_SSL_INVALIDCERTSTATUS: Final = 91
E_SSL_ISSUER_ERROR: Final = 83
E_SSL_PEER_CERTIFICATE: Final = 60
E_SSL_PINNEDPUBKEYNOTMATCH: Final = 90
E_SSL_SHUTDOWN_FAILED: Final = 80
E_TELNET_OPTION_SYNTAX: Final = 49
E_TFTP_DISKFULL: Final = 70
E_TFTP_EXISTS: Final = 73
E_TFTP_ILLEGAL: Final = 71
E_TFTP_NOSUCHUSER: Final = 74
E_TFTP_NOTFOUND: Final = 68
E_TFTP_PERM: Final = 69
E_TFTP_UNKNOWNID: Final = 72
E_TOO_MANY_REDIRECTS: Final = 47
E_UNKNOWN_OPTION: Final = 48
E_UNKNOWN_TELNET_OPTION: Final = 48
E_UNSUPPORTED_PROTOCOL: Final = 1
E_UPLOAD_FAILED: Final = 25
E_URL_MALFORMAT: Final = 3
E_URL_MALFORMAT_USER: Final = 4
E_USE_SSL_FAILED: Final = 64
E_WRITE_ERROR: Final = 23
FAILONERROR: Final = 45
FILE: Final = 10001
FOLLOWLOCATION: Final = 52
FORBID_REUSE: Final = 75
FORM_BUFFER: Final = 11
FORM_BUFFERPTR: Final = 12
FORM_CONTENTS: Final = 4
FORM_CONTENTTYPE: Final = 14
FORM_FILE: Final = 10
FORM_FILENAME: Final = 16
FRESH_CONNECT: Final = 74
FTPAPPEND: Final = 50
FTPAUTH_DEFAULT: Final = 0
FTPAUTH_SSL: Final = 1
FTPAUTH_TLS: Final = 2
FTPLISTONLY: Final = 48
FTPMETHOD_DEFAULT: Final = 0
FTPMETHOD_MULTICWD: Final = 1
FTPMETHOD_NOCWD: Final = 2
FTPMETHOD_SINGLECWD: Final = 3
FTPPORT: Final = 10017
FTPSSLAUTH: Final = 129
FTPSSL_ALL: Final = 3
FTPSSL_CONTROL: Final = 2
FTPSSL_NONE: Final = 0
FTPSSL_TRY: Final = 1
FTP_ACCOUNT: Final = 10134
FTP_ALTERNATIVE_TO_USER: Final = 10147
FTP_CREATE_MISSING_DIRS: Final = 110
FTP_ENTRY_PATH: Final = 1048606
FTP_FILEMETHOD: Final = 138
FTP_RESPONSE_TIMEOUT: Final = 112
FTP_SKIP_PASV_IP: Final = 137
FTP_SSL: Final = 119
FTP_SSL_CCC: Final = 154
FTP_USE_EPRT: Final = 106
FTP_USE_EPSV: Final = 85
FTP_USE_PRET: Final = 188
GLOBAL_ACK_EINTR: Final = 4
GLOBAL_ALL: Final = 3
GLOBAL_DEFAULT: Final = 3
GLOBAL_NOTHING: Final = 0
GLOBAL_SSL: Final = 1
GLOBAL_WIN32: Final = 2
GSSAPI_DELEGATION: Final = 210
GSSAPI_DELEGATION_FLAG: Final = 2
GSSAPI_DELEGATION_NONE: Final = 0
GSSAPI_DELEGATION_POLICY_FLAG: Final = 1
HAPROXYPROTOCOL: Final = 274
HAPROXY_CLIENT_IP: Final = 10323
HEADER: Final = 42
HEADERFUNCTION: Final = 20079
HEADEROPT: Final = 229
HEADER_SEPARATE: Final = 1
HEADER_SIZE: Final = 2097163
HEADER_UNIFIED: Final = 0
HTTP09_ALLOWED: Final = 285
HTTP200ALIASES: Final = 10104
HTTPAUTH: Final = 107
HTTPAUTH_ANY: Final = -17
HTTPAUTH_ANYSAFE: Final = -18
HTTPAUTH_AVAIL: Final = 2097175
HTTPAUTH_BASIC: Final = 1
HTTPAUTH_DIGEST: Final = 2
HTTPAUTH_DIGEST_IE: Final = 16
HTTPAUTH_GSSNEGOTIATE: Final = 4
HTTPAUTH_NEGOTIATE: Final = 4
HTTPAUTH_NONE: Final = 0
HTTPAUTH_NTLM: Final = 8
HTTPAUTH_NTLM_WB: Final = 32
HTTPAUTH_ONLY: Final = -2147483648
HTTPGET: Final = 80
HTTPHEADER: Final = 10023
HTTPPOST: Final = 10024
HTTPPROXYTUNNEL: Final = 61
HTTP_CODE: Final = 2097154
HTTP_CONNECTCODE: Final = 2097174
HTTP_CONTENT_DECODING: Final = 158
HTTP_TRANSFER_DECODING: Final = 157
HTTP_VERSION: Final = 84
IGNORE_CONTENT_LENGTH: Final = 136
INFILE: Final = 10009
INFILESIZE: Final = 30115
INFILESIZE_LARGE: Final = 30115
INFOTYPE_DATA_IN: Final = 3
INFOTYPE_DATA_OUT: Final = 4
INFOTYPE_HEADER_IN: Final = 1
INFOTYPE_HEADER_OUT: Final = 2
INFOTYPE_SSL_DATA_IN: Final = 5
INFOTYPE_SSL_DATA_OUT: Final = 6
INFOTYPE_TEXT: Final = 0
INFO_CERTINFO: Final = 4194338
INFO_COOKIELIST: Final = 4194332
INFO_FILETIME: Final = 2097166
INFO_HTTP_VERSION: Final = 2097198
INFO_RTSP_CLIENT_CSEQ: Final = 2097189
INFO_RTSP_CSEQ_RECV: Final = 2097191
INFO_RTSP_SERVER_CSEQ: Final = 2097190
INFO_RTSP_SESSION_ID: Final = 1048612
INTERFACE: Final = 10062
IOCMD_NOP: Final = 0
IOCMD_RESTARTREAD: Final = 1
IOCTLFUNCTION: Final = 20130
IOE_FAILRESTART: Final = 2
IOE_OK: Final = 0
IOE_UNKNOWNCMD: Final = 1
IPRESOLVE: Final = 113
IPRESOLVE_V4: Final = 1
IPRESOLVE_V6: Final = 2
IPRESOLVE_WHATEVER: Final = 0
ISSUERCERT: Final = 10170
ISSUERCERT_BLOB: Final = 40295
KEYPASSWD: Final = 10026
KHMATCH_MISMATCH: Final = 1
KHMATCH_MISSING: Final = 2
KHMATCH_OK: Final = 0
KHSTAT_DEFER: Final = 3
KHSTAT_FINE: Final = 1
KHSTAT_FINE_ADD_TO_FILE: Final = 0
KHSTAT_REJECT: Final = 2
KHTYPE_DSS: Final = 3
KHTYPE_RSA: Final = 2
KHTYPE_RSA1: Final = 1
KHTYPE_UNKNOWN: Final = 0
KRB4LEVEL: Final = 10063
KRBLEVEL: Final = 10063
LASTSOCKET: Final = 2097181
LOCALPORT: Final = 139
LOCALPORTRANGE: Final = 140
LOCAL_IP: Final = 1048617
LOCAL_PORT: Final = 2097194
LOCK_DATA_CONNECT: Final = 5
LOCK_DATA_COOKIE: Final = 2
LOCK_DATA_DNS: Final = 3
LOCK_DATA_PSL: Final = 6
LOCK_DATA_SSL_SESSION: Final = 4
LOGIN_OPTIONS: Final = 10224
LOW_SPEED_LIMIT: Final = 19
LOW_SPEED_TIME: Final = 20
MAIL_AUTH: Final = 10217
MAIL_FROM: Final = 10186
MAIL_RCPT: Final = 10187
MAXAGE_CONN: Final = 288
MAXCONNECTS: Final = 71
MAXFILESIZE: Final = 30117
MAXFILESIZE_LARGE: Final = 30117
MAXLIFETIME_CONN: Final = 314
MAXREDIRS: Final = 68
MAX_RECV_SPEED_LARGE: Final = 30146
MAX_SEND_SPEED_LARGE: Final = 30145
M_CHUNK_LENGTH_PENALTY_SIZE: Final = 30010
M_CONTENT_LENGTH_PENALTY_SIZE: Final = 30009
M_MAXCONNECTS: Final = 6
M_MAX_CONCURRENT_STREAMS: Final = 16
M_MAX_HOST_CONNECTIONS: Final = 7
M_MAX_PIPELINE_LENGTH: Final = 8
M_MAX_TOTAL_CONNECTIONS: Final = 13
M_PIPELINING: Final = 3
M_PIPELINING_SERVER_BL: Final = 10012
M_PIPELINING_SITE_BL: Final = 10011
M_SOCKETFUNCTION: Final = 20001
M_TIMERFUNCTION: Final = 20004
NAMELOOKUP_TIME: Final = 3145732
NETRC: Final = 51
NETRC_FILE: Final = 10118
NETRC_IGNORED: Final = 0
NETRC_OPTIONAL: Final = 1
NETRC_REQUIRED: Final = 2
NEW_DIRECTORY_PERMS: Final = 160
NEW_FILE_PERMS: Final = 159
NOBODY: Final = 44
NOPROGRESS: Final = 43
NOPROXY: Final = 10177
NOSIGNAL: Final = 99
NUM_CONNECTS: Final = 2097178
OPENSOCKETFUNCTION: Final = 20163
OPT_CERTINFO: Final = 172
OPT_COOKIELIST: Final = 10135
OPT_FILETIME: Final = 69
OPT_RTSP_CLIENT_CSEQ: Final = 193
OPT_RTSP_REQUEST: Final = 189
OPT_RTSP_SERVER_CSEQ: Final = 194
OPT_RTSP_SESSION_ID: Final = 10190
OPT_RTSP_STREAM_URI: Final = 10191
OPT_RTSP_TRANSPORT: Final = 10192
OS_ERRNO: Final = 2097177
PASSWORD: Final = 10174
PATH_AS_IS: Final = 234
PAUSE_ALL: Final = 5
PAUSE_CONT: Final = 0
PAUSE_RECV: Final = 1
PAUSE_SEND: Final = 4
PINNEDPUBLICKEY: Final = 10230
PIPEWAIT: Final = 237
PIPE_HTTP1: Final = 1
PIPE_MULTIPLEX: Final = 2
PIPE_NOTHING: Final = 0
POLL_IN: Final = 1
POLL_INOUT: Final = 3
POLL_NONE: Final = 0
POLL_OUT: Final = 2
POLL_REMOVE: Final = 4
PORT: Final = 3
POST: Final = 47
POST301: Final = 161
POSTFIELDS: Final = 10015
POSTFIELDSIZE: Final = 30120
POSTFIELDSIZE_LARGE: Final = 30120
POSTQUOTE: Final = 10039
POSTREDIR: Final = 161
PREQUOTE: Final = 10093
PRETRANSFER_TIME: Final = 3145734
PRE_PROXY: Final = 10262
PRIMARY_IP: Final = 1048608
PRIMARY_PORT: Final = 2097192
PROGRESSFUNCTION: Final = 20056
PROTOCOLS: Final = 181
PROTO_ALL: Final = -1
PROTO_DICT: Final = 512
PROTO_FILE: Final = 1024
PROTO_FTP: Final = 4
PROTO_FTPS: Final = 8
PROTO_GOPHER: Final = 33554432
PROTO_HTTP: Final = 1
PROTO_HTTPS: Final = 2
PROTO_IMAP: Final = 4096
PROTO_IMAPS: Final = 8192
PROTO_LDAP: Final = 128
PROTO_LDAPS: Final = 256
PROTO_POP3: Final = 16384
PROTO_POP3S: Final = 32768
PROTO_RTMP: Final = 524288
PROTO_RTMPE: Final = 2097152
PROTO_RTMPS: Final = 8388608
PROTO_RTMPT: Final = 1048576
PROTO_RTMPTE: Final = 4194304
PROTO_RTMPTS: Final = 16777216
PROTO_RTSP: Final = 262144
PROTO_SCP: Final = 16
PROTO_SFTP: Final = 32
PROTO_SMB: Final = 67108864
PROTO_SMBS: Final = 134217728
PROTO_SMTP: Final = 65536
PROTO_SMTPS: Final = 131072
PROTO_TELNET: Final = 64
PROTO_TFTP: Final = 2048
PROXY: Final = 10004
PROXYAUTH: Final = 111
PROXYAUTH_AVAIL: Final = 2097176
PROXYHEADER: Final = 10228
PROXYPASSWORD: Final = 10176
PROXYPORT: Final = 59
PROXYTYPE: Final = 101
PROXYTYPE_HTTP: Final = 0
PROXYTYPE_HTTP_1_0: Final = 1
PROXYTYPE_SOCKS4: Final = 4
PROXYTYPE_SOCKS4A: Final = 6
PROXYTYPE_SOCKS5: Final = 5
PROXYTYPE_SOCKS5_HOSTNAME: Final = 7
PROXYUSERNAME: Final = 10175
PROXYUSERPWD: Final = 10006
PROXY_CAINFO: Final = 10246
PROXY_CAINFO_BLOB: Final = 40310
PROXY_CAPATH: Final = 10247
PROXY_CRLFILE: Final = 10260
PROXY_ISSUERCERT: Final = 10296
PROXY_ISSUERCERT_BLOB: Final = 40297
PROXY_KEYPASSWD: Final = 10258
PROXY_PINNEDPUBLICKEY: Final = 10263
PROXY_SERVICE_NAME: Final = 10235
PROXY_SSLCERT: Final = 10254
PROXY_SSLCERTTYPE: Final = 10255
PROXY_SSLCERT_BLOB: Final = 40293
PROXY_SSLKEY: Final = 10256
PROXY_SSLKEYTYPE: Final = 10257
PROXY_SSLKEY_BLOB: Final = 40294
PROXY_SSLVERSION: Final = 250
PROXY_SSL_CIPHER_LIST: Final = 10259
PROXY_SSL_OPTIONS: Final = 261
PROXY_SSL_VERIFYHOST: Final = 249
PROXY_SSL_VERIFYPEER: Final = 248
PROXY_TLS13_CIPHERS: Final = 10277
PROXY_TLSAUTH_PASSWORD: Final = 10252
PROXY_TLSAUTH_TYPE: Final = 10253
PROXY_TLSAUTH_USERNAME: Final = 10251
PROXY_TRANSFER_MODE: Final = 166
PUT: Final = 54
QUOTE: Final = 10028
RANDOM_FILE: Final = 10076
RANGE: Final = 10007
READDATA: Final = 10009
READFUNCTION: Final = 20012
READFUNC_ABORT: Final = 268435456
READFUNC_PAUSE: Final = 268435457
REDIRECT_COUNT: Final = 2097172
REDIRECT_TIME: Final = 3145747
REDIRECT_URL: Final = 1048607
REDIR_POST_301: Final = 1
REDIR_POST_302: Final = 2
REDIR_POST_303: Final = 4
REDIR_POST_ALL: Final = 7
REDIR_PROTOCOLS: Final = 182
REFERER: Final = 10016
REQUEST_SIZE: Final = 2097164
REQUEST_TARGET: Final = 10266
RESOLVE: Final = 10203
RESPONSE_CODE: Final = 2097154
RESUME_FROM: Final = 30116
RESUME_FROM_LARGE: Final = 30116
RTSPREQ_ANNOUNCE: Final = 3
RTSPREQ_DESCRIBE: Final = 2
RTSPREQ_GET_PARAMETER: Final = 8
RTSPREQ_LAST: Final = 12
RTSPREQ_NONE: Final = 0
RTSPREQ_OPTIONS: Final = 1
RTSPREQ_PAUSE: Final = 6
RTSPREQ_PLAY: Final = 5
RTSPREQ_RECEIVE: Final = 11
RTSPREQ_RECORD: Final = 10
RTSPREQ_SETUP: Final = 4
RTSPREQ_SET_PARAMETER: Final = 9
RTSPREQ_TEARDOWN: Final = 7
SASL_IR: Final = 218
SEEKFUNCTION: Final = 20167
SEEKFUNC_CANTSEEK: Final = 2
SEEKFUNC_FAIL: Final = 1
SEEKFUNC_OK: Final = 0
SERVICE_NAME: Final = 10236
SHARE: Final = 10100
SH_SHARE: Final = 1
SH_UNSHARE: Final = 2
SIZE_DOWNLOAD: Final = 3145736
SIZE_UPLOAD: Final = 3145735
SOCKET_BAD: Final = -1
SOCKET_TIMEOUT: Final = -1
SOCKOPTFUNCTION: Final = 20148
SOCKOPT_ALREADY_CONNECTED: Final = 2
SOCKOPT_ERROR: Final = 1
SOCKOPT_OK: Final = 0
SOCKS5_GSSAPI_NEC: Final = 180
SOCKS5_GSSAPI_SERVICE: Final = 10179
SOCKTYPE_ACCEPT: Final = 1
SOCKTYPE_IPCXN: Final = 0
SPEED_DOWNLOAD: Final = 3145737
SPEED_UPLOAD: Final = 3145738
SSH_AUTH_AGENT: Final = 16
SSH_AUTH_ANY: Final = -1
SSH_AUTH_DEFAULT: Final = -1
SSH_AUTH_HOST: Final = 4
SSH_AUTH_KEYBOARD: Final = 8
SSH_AUTH_NONE: Final = 0
SSH_AUTH_PASSWORD: Final = 2
SSH_AUTH_PUBLICKEY: Final = 1
SSH_AUTH_TYPES: Final = 151
SSH_HOST_PUBLIC_KEY_MD5: Final = 10162
SSH_KEYFUNCTION: Final = 20184
SSH_KNOWNHOSTS: Final = 10183
SSH_PRIVATE_KEYFILE: Final = 10153
SSH_PUBLIC_KEYFILE: Final = 10152
SSLCERT: Final = 10025
SSLCERTPASSWD: Final = 10026
SSLCERTTYPE: Final = 10086
SSLCERT_BLOB: Final = 40291
SSLENGINE: Final = 10089
SSLENGINE_DEFAULT: Final = 90
SSLKEY: Final = 10087
SSLKEYPASSWD: Final = 10026
SSLKEYTYPE: Final = 10088
SSLKEY_BLOB: Final = 40292
SSLOPT_ALLOW_BEAST: Final = 1
SSLOPT_NO_REVOKE: Final = 2
SSLVERSION: Final = 32
SSLVERSION_DEFAULT: Final = 0
SSLVERSION_MAX_DEFAULT: Final = 65536
SSLVERSION_MAX_TLSv1_0: Final = 262144
SSLVERSION_MAX_TLSv1_1: Final = 327680
SSLVERSION_MAX_TLSv1_2: Final = 393216
SSLVERSION_MAX_TLSv1_3: Final = 458752
SSLVERSION_SSLv2: Final = 2
SSLVERSION_SSLv3: Final = 3
SSLVERSION_TLSv1: Final = 0
SSLVERSION_TLSv1_0: Final = 4
SSLVERSION_TLSv1_1: Final = 5
SSLVERSION_TLSv1_2: Final = 6
SSLVERSION_TLSv1_3: Final = 7
SSL_CIPHER_LIST: Final = 10083
SSL_ENABLE_ALPN: Final = 226
SSL_ENABLE_NPN: Final = 225
SSL_ENGINES: Final = 4194331
SSL_FALSESTART: Final = 233
SSL_OPTIONS: Final = 216
SSL_SESSIONID_CACHE: Final = 150
SSL_VERIFYHOST: Final = 81
SSL_VERIFYPEER: Final = 64
SSL_VERIFYRESULT: Final = 2097165
SSL_VERIFYSTATUS: Final = 232
STARTTRANSFER_TIME: Final = 3145745
STDERR: Final = 10037
TCP_FASTOPEN: Final = 244
TCP_KEEPALIVE: Final = 213
TCP_KEEPIDLE: Final = 214
TCP_KEEPINTVL: Final = 215
TCP_NODELAY: Final = 121
TELNETOPTIONS: Final = 10070
TFTP_BLKSIZE: Final = 178
TIMECONDITION: Final = 33
TIMECONDITION_IFMODSINCE: Final = 1
TIMECONDITION_IFUNMODSINCE: Final = 2
TIMECONDITION_LASTMOD: Final = 3
TIMECONDITION_NONE: Final = 0
TIMEOUT: Final = 13
TIMEOUT_MS: Final = 155
TIMEVALUE: Final = 34
TLS13_CIPHERS: Final = 10276
TLSAUTH_PASSWORD: Final = 10205
TLSAUTH_TYPE: Final = 10206
TLSAUTH_USERNAME: Final = 10204
TOTAL_TIME: Final = 3145731
TRANSFERTEXT: Final = 53
TRANSFER_ENCODING: Final = 207
UNIX_SOCKET_PATH: Final = 10231
UNRESTRICTED_AUTH: Final = 105
UPLOAD: Final = 46
UPLOAD_BUFFERSIZE: Final = 280
URL: Final = 10002
USERAGENT: Final = 10018
USERNAME: Final = 10173
USERPWD: Final = 10005
USESSL_ALL: Final = 3
USESSL_CONTROL: Final = 2
USESSL_NONE: Final = 0
USESSL_TRY: Final = 1
USE_SSL: Final = 119
VERBOSE: Final = 41
VERSION_ALTSVC: Final = 16777216
VERSION_ASYNCHDNS: Final = 128
VERSION_BROTLI: Final = 8388608
VERSION_CONV: Final = 4096
VERSION_CURLDEBUG: Final = 8192
VERSION_DEBUG: Final = 64
VERSION_GSASL: Final = 536870912
VERSION_GSSAPI: Final = 131072
VERSION_GSSNEGOTIATE: Final = 32
VERSION_HSTS: Final = 268435456
VERSION_HTTP2: Final = 65536
VERSION_HTTP3: Final = 33554432
VERSION_HTTPS_PROXY: Final = 2097152
VERSION_IDN: Final = 1024
VERSION_IPV6: Final = 1
VERSION_KERBEROS4: Final = 2
VERSION_KERBEROS5: Final = 262144
VERSION_LARGEFILE: Final = 512
VERSION_LIBZ: Final = 8
VERSION_MULTI_SSL: Final = 4194304
VERSION_NTLM: Final = 16
VERSION_NTLM_WB: Final = 32768
VERSION_PSL: Final = 1048576
VERSION_SPNEGO: Final = 256
VERSION_SSL: Final = 4
VERSION_SSPI: Final = 2048
VERSION_TLSAUTH_SRP: Final = 16384
VERSION_UNICODE: Final = 134217728
VERSION_UNIX_SOCKETS: Final = 524288
VERSION_ZSTD: Final = 67108864
WILDCARDMATCH: Final = 197
WRITEDATA: Final = 10001
WRITEFUNCTION: Final = 20011
WRITEFUNC_PAUSE: Final = 268435457
WRITEHEADER: Final = 10029
XFERINFOFUNCTION: Final = 20219
XOAUTH2_BEARER: Final = 10220
