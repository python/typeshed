# This comment serves as a workaround for timothycrosley/isort#1027 and can
# be removed when a release with a fix was released.

import codecs

def search_function(encoding: str) -> codecs.CodecInfo: ...
