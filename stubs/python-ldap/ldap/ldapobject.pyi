from _typeshed import Incomplete
from typing import Any, BinaryIO, TextIO

import ldap
import ldap.sasl
from ldap._types import LDAPAddModList, LDAPEntryDict, LDAPModifyModList
from ldap.controls import RequestControl, ResponseControl
from ldap.extop import ExtendedRequest, ExtendedResponse, PasswordModifyResponse

__all__ = ["LDAPObject", "SimpleLDAPObject", "ReconnectLDAPObject", "LDAPBytesWarning"]

class LDAPBytesWarning(BytesWarning):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class NO_UNIQUE_ENTRY(ldap.NO_SUCH_OBJECT): ...

class SimpleLDAPObject:
    CLASSATTR_OPTION_MAPPING: Incomplete
    timeout: int
    protocol_version: Incomplete
    def __init__(
        self,
        uri: str | None = None,
        trace_level: int = 0,
        trace_file: TextIO | None = None,
        trace_stack_limit: int | None = 5,
        bytes_mode: Any | None = None,
        bytes_strictness: str | None = None,
        fileno: int | BinaryIO | None = None,
    ) -> None: ...
    @property
    def bytes_mode(self) -> bool: ...
    @property
    def bytes_strictness(self) -> str: ...
    def __setattr__(self, name: str, value: Any) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    def fileno(self) -> int: ...
    def connect(self) -> None: ...
    def abandon_ext(
        self, msgid: int, serverctrls: list[RequestControl] | None = None, clientctrls: list[RequestControl] | None = None
    ) -> None: ...
    def abandon(self, msgid: int) -> None: ...
    def cancel(
        self, cancelid: int, serverctrls: list[RequestControl] | None = None, clientctrls: list[RequestControl] | None = None
    ) -> int: ...
    def cancel_s(
        self, cancelid: int, serverctrls: list[RequestControl] | None = None, clientctrls: list[RequestControl] | None = None
    ) -> int | None: ...
    def add_ext(
        self,
        dn: str,
        modlist: LDAPAddModList,
        serverctrls: list[RequestControl] | None = None,
        clientctrls: list[RequestControl] | None = None,
    ) -> int: ...
    def add_ext_s(
        self,
        dn: str,
        modlist: LDAPAddModList,
        serverctrls: list[RequestControl] | None = None,
        clientctrls: list[RequestControl] | None = None,
    ) -> tuple[Any, Any, Any, Any]: ...
    def add(self, dn: str, modlist: LDAPAddModList) -> int: ...
    def add_s(self, dn: str, modlist: LDAPAddModList) -> tuple[Any, Any, Any, Any]: ...
    def simple_bind(
        self,
        who: str | None = None,
        cred: str | None = None,
        serverctrls: list[RequestControl] | None = None,
        clientctrls: list[RequestControl] | None = None,
    ) -> int: ...
    def simple_bind_s(
        self,
        who: str | None = None,
        cred: str | None = None,
        serverctrls: list[RequestControl] | None = None,
        clientctrls: list[RequestControl] | None = None,
    ) -> tuple[Any, Any, Any, Any]: ...
    def bind(self, who: str, cred: str, method: int = ...) -> int: ...
    def bind_s(self, who: str, cred: str, method: int = ...) -> None: ...
    def sasl_interactive_bind_s(
        self,
        who: str,
        auth: ldap.sasl.sasl,
        serverctrls: list[RequestControl] | None = None,
        clientctrls: list[RequestControl] | None = None,
        sasl_flags: int = ...,
    ) -> None: ...
    def sasl_non_interactive_bind_s(
        self,
        sasl_mech: str,
        serverctrls: list[RequestControl] | None = None,
        clientctrls: list[RequestControl] | None = None,
        sasl_flags: int = ...,
        authz_id: str = "",
    ) -> None: ...
    def sasl_external_bind_s(
        self,
        serverctrls: list[RequestControl] | None = None,
        clientctrls: list[RequestControl] | None = None,
        sasl_flags: int = ...,
        authz_id: str = "",
    ) -> None: ...
    def sasl_gssapi_bind_s(
        self,
        serverctrls: list[RequestControl] | None = None,
        clientctrls: list[RequestControl] | None = None,
        sasl_flags: int = ...,
        authz_id: str = "",
    ) -> None: ...
    def sasl_bind_s(
        self,
        dn: str,
        mechanism: str,
        cred: str,
        serverctrls: list[RequestControl] | None = None,
        clientctrls: list[RequestControl] | None = None,
    ) -> int | str: ...
    def compare_ext(
        self,
        dn: str,
        attr: str,
        value: bytes,
        serverctrls: list[RequestControl] | None = None,
        clientctrls: list[RequestControl] | None = None,
    ) -> int: ...
    def compare_ext_s(
        self,
        dn: str,
        attr: str,
        value: bytes,
        serverctrls: list[RequestControl] | None = None,
        clientctrls: list[RequestControl] | None = None,
    ) -> bool: ...
    def compare(self, dn: str, attr: str, value: bytes) -> int: ...
    def compare_s(self, dn: str, attr: str, value: bytes) -> bool: ...
    def delete_ext(
        self, dn: str, serverctrls: list[RequestControl] | None = None, clientctrls: list[RequestControl] | None = None
    ) -> int: ...
    def delete_ext_s(
        self, dn: str, serverctrls: list[RequestControl] | None = None, clientctrls: list[RequestControl] | None = None
    ) -> tuple[Any, Any, Any, Any]: ...
    def delete(self, dn: str) -> int: ...
    def delete_s(self, dn: str) -> None: ...
    def extop(
        self,
        extreq: ExtendedRequest,
        serverctrls: list[RequestControl] | None = None,
        clientctrls: list[RequestControl] | None = None,
    ) -> int: ...
    def extop_result(self, msgid: int = ..., all: int = 1, timeout: int | float | None = None) -> tuple[str | None, bytes]: ...
    def extop_s(
        self,
        extreq: ExtendedRequest,
        serverctrls: list[RequestControl] | None = None,
        clientctrls: list[RequestControl] | None = None,
        extop_resp_class: type[ExtendedResponse] | None = None,
    ) -> tuple[str | None, bytes] | ExtendedResponse: ...
    def modify_ext(
        self,
        dn: str,
        modlist: LDAPModifyModList,
        serverctrls: list[RequestControl] | None = None,
        clientctrls: list[RequestControl] | None = None,
    ) -> int: ...
    def modify_ext_s(
        self,
        dn: str,
        modlist: LDAPModifyModList,
        serverctrls: list[RequestControl] | None = None,
        clientctrls: list[RequestControl] | None = None,
    ) -> tuple[Any, Any, Any, Any]: ...
    def modify(self, dn: str, modlist: LDAPModifyModList) -> int: ...
    def modify_s(self, dn: str, modlist: LDAPModifyModList) -> None: ...
    def modrdn(self, dn: str, newrdn: str, delold: int = 1) -> int: ...
    def modrdn_s(self, dn: str, newrdn: str, delold: int = 1) -> None: ...
    def passwd(
        self,
        user: str,
        oldpw: str,
        newpw: str,
        serverctrls: list[RequestControl] | None = None,
        clientctrls: list[RequestControl] | None = None,
    ) -> int: ...
    def passwd_s(
        self,
        user: str,
        oldpw: str,
        newpw: str,
        serverctrls: list[RequestControl] | None = None,
        clientctrls: list[RequestControl] | None = None,
        extract_newpw: bool = False,
    ) -> tuple[None, bytes | PasswordModifyResponse]: ...
    def rename(
        self,
        dn: str,
        newrdn: str,
        newsuperior: str | None = None,
        delold: int = 1,
        serverctrls: list[RequestControl] | None = None,
        clientctrls: list[RequestControl] | None = None,
    ) -> int: ...
    def rename_s(
        self,
        dn: str,
        newrdn: str,
        newsuperior: str | None = None,
        delold: int = 1,
        serverctrls: list[RequestControl] | None = None,
        clientctrls: list[RequestControl] | None = None,
    ) -> None: ...
    def result(self, msgid: int = ..., all: int = 1, timeout: int | float | None = None) -> tuple[int | None, Any | None]: ...
    def result2(
        self, msgid: int = ..., all: int = 1, timeout: int | float | None = None
    ) -> tuple[int | None, Any | None, int | None]: ...
    def result3(
        self,
        msgid: int = ...,
        all: int = 1,
        timeout: int | float | None = None,
        resp_ctrl_classes: dict[str, type[ResponseControl]] | None = None,
    ) -> tuple[int | None, Any | None, int | None, list[ResponseControl] | None]: ...
    def result4(
        self,
        msgid: int = ...,
        all: int = 1,
        timeout: int | float | None = None,
        add_ctrls: int = 0,
        add_intermediates: int = 0,
        add_extop: int = 0,
        resp_ctrl_classes: dict[str, type[ResponseControl]] | None = None,
    ) -> tuple[int | None, Any | None, int | None, list[ResponseControl] | None, Any | None, Any | None]: ...
    def search_ext(
        self,
        base: str,
        scope: int,
        filterstr: str | None = None,
        attrlist: list[str] | None = None,
        attrsonly: int = 0,
        serverctrls: list[RequestControl] | None = None,
        clientctrls: list[RequestControl] | None = None,
        timeout: int | float = -1,
        sizelimit: int = 0,
    ) -> int: ...
    def search_ext_s(
        self,
        base: str,
        scope: int,
        filterstr: str | None = None,
        attrlist: list[str] | None = None,
        attrsonly: int = 0,
        serverctrls: list[RequestControl] | None = None,
        clientctrls: list[RequestControl] | None = None,
        timeout: int | float = -1,
        sizelimit: int = 0,
    ) -> list[tuple[str, LDAPEntryDict]]: ...
    def search(
        self, base: str, scope: int, filterstr: str | None = None, attrlist: list[str] | None = None, attrsonly: int = 0
    ) -> int: ...
    def search_s(
        self, base: str, scope: int, filterstr: str | None = None, attrlist: list[str] | None = None, attrsonly: int = 0
    ) -> list[tuple[str, LDAPEntryDict]]: ...
    def search_st(
        self,
        base: str,
        scope: int,
        filterstr: str | None = None,
        attrlist: list[str] | None = None,
        attrsonly: int = 0,
        timeout: int | float = -1,
    ) -> list[tuple[str, LDAPEntryDict]]: ...
    def start_tls_s(self) -> None: ...
    def unbind_ext(
        self, serverctrls: list[RequestControl] | None = None, clientctrls: list[RequestControl] | None = None
    ) -> int: ...
    def unbind_ext_s(
        self, serverctrls: list[RequestControl] | None = None, clientctrls: list[RequestControl] | None = None
    ) -> None: ...
    def unbind(self) -> int: ...
    def unbind_s(self) -> None: ...
    def whoami_s(
        self, serverctrls: list[RequestControl] | None = None, clientctrls: list[RequestControl] | None = None
    ) -> str: ...
    def get_option(self, option: int) -> Any: ...
    def set_option(self, option: int, invalue: Any) -> Any: ...
    def search_subschemasubentry_s(self, dn: str | None = None) -> str | None: ...
    def read_s(
        self,
        dn: str,
        filterstr: str | None = None,
        attrlist: list[str] | None = None,
        serverctrls: list[RequestControl] | None = None,
        clientctrls: list[RequestControl] | None = None,
        timeout: int | float = -1,
    ) -> LDAPEntryDict | None: ...
    def read_subschemasubentry_s(self, subschemasubentry_dn: str, attrs: list[str] | None = None) -> LDAPEntryDict | None: ...
    def find_unique_entry(
        self,
        base: str,
        scope: int = ...,
        filterstr: str | None = None,
        attrlist: list[str] | None = None,
        attrsonly: int = 0,
        serverctrls: list[RequestControl] | None = None,
        clientctrls: list[RequestControl] | None = None,
        timeout: int | float = -1,
    ) -> tuple[str, LDAPEntryDict]: ...
    def read_rootdse_s(self, filterstr: str | None = None, attrlist: list[str] | None = None) -> LDAPEntryDict | None: ...
    def get_naming_contexts(self) -> list[bytes]: ...

class ReconnectLDAPObject(SimpleLDAPObject):
    __transient_attrs__: Incomplete
    def __init__(
        self,
        uri: str | None = None,
        trace_level: int = 0,
        trace_file: TextIO | None = None,
        trace_stack_limit: int = 5,
        bytes_mode: Any | None = None,
        bytes_strictness: str | None = None,
        retry_max: int = 1,
        retry_delay: float = 60.0,
        fileno: int | BinaryIO | None = None,
    ) -> None: ...
    def passwd_s(self, *args: Any, **kwargs: Any) -> tuple[None, bytes | PasswordModifyResponse]: ...
    def reconnect(self, uri: str | None, retry_max: int = 1, retry_delay: float = 60.0, force: bool = True) -> None: ...
    def set_option(self, option: int, invalue: Any) -> Any: ...
    def bind_s(self, *args: Any, **kwargs: Any) -> Any: ...
    def simple_bind_s(self, *args: Any, **kwargs: Any) -> Any: ...
    def start_tls_s(self, *args: Any, **kwargs: Any) -> Any: ...
    def sasl_interactive_bind_s(self, *args: Any, **kwargs: Any) -> Any: ...
    def sasl_bind_s(self, *args: Any, **kwargs: Any) -> Any: ...
    def add_ext_s(self, *args: Any, **kwargs: Any) -> Any: ...
    def cancel_s(self, *args: Any, **kwargs: Any) -> Any: ...
    def compare_ext_s(self, *args: Any, **kwargs: Any) -> Any: ...
    def delete_ext_s(self, *args: Any, **kwargs: Any) -> Any: ...
    def extop_s(self, *args: Any, **kwargs: Any) -> Any: ...
    def modify_ext_s(self, *args: Any, **kwargs: Any) -> Any: ...
    def rename_s(self, *args: Any, **kwargs: Any) -> Any: ...
    def search_ext_s(self, *args: Any, **kwargs: Any) -> Any: ...
    def whoami_s(self, *args: Any, **kwargs: Any) -> Any: ...

LDAPObject = SimpleLDAPObject
