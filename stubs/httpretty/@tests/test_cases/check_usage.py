from typing_extensions import assert_type

import httpretty


@httpretty.activate(allow_net_connect=False)
def decorated() -> int:
    httpretty.register_uri(httpretty.GET, "https://example.com/", body="ok", status=200, content_type="text/plain")
    assert_type(httpretty.last_request(), httpretty.HTTPrettyRequest | httpretty.HTTPrettyRequestEmpty)
    assert_type(httpretty.latest_requests(), list[httpretty.HTTPrettyRequest])
    assert_type(httpretty.has_request(), bool)
    return 1


with httpretty.enabled(allow_net_connect=False):
    response = httpretty.Response("ok", status=201)
    assert_type(response, httpretty.Entry)
