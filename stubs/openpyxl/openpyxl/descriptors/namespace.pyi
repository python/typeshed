from typing import overload

@overload
def namespaced(obj: object, tagname: str, namespace: str | None = None) -> str: ...
@overload
def namespaced(obj: object, tagname: str | None, namespace: str) -> str: ...
@overload
def namespaced(obj: object, tagname: str | None, namespace: str | None = None) -> str | None: ...
