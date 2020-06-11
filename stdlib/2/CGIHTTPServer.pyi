# Stubs for CGIHTTPServer (Python 2.7)

import SimpleHTTPServer
from typing import List

class CGIHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    cgi_directories: List[str]
    def do_POST(self) -> None: ...
