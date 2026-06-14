from collections.abc import Iterator
from http.cookiejar import Cookie
from typing_extensions import assert_type

from requests.cookies import RequestsCookieJar

jar = RequestsCookieJar()
jar["a"] = "b"

assert_type(iter(jar), Iterator[Cookie])
assert_type(next(iter(jar)), Cookie)
