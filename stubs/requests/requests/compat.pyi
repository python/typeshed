import collections
import sys
import urllib.parse
import urllib.request

_ver = sys.version_info

is_py2: bool
is_py3: bool
has_simplejson: bool

OrderedDict = collections.OrderedDict

quote = urllib.parse.quote
quote_plus = urllib.parse.quote_plus
unquote = urllib.parse.unquote
unquote_plus = urllib.parse.unquote_plus
urldefrag = urllib.parse.urldefrag
urlencode = urllib.parse.urlencode
urljoin = urllib.parse.urljoin
urlparse = urllib.parse.urlparse
urlsplit = urllib.parse.urlsplit
urlunparse = urllib.parse.urlunparse

getproxies = urllib.request.getproxies
parse_http_list = urllib.request.parse_http_list
proxy_bypass = urllib.request.proxy_bypass
