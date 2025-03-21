import html
import re
from typing import AnyStr, Final, Literal, overload

HTMLunescape = html.unescape
ENTITY: Final[str]
TAGNAME: Final[str]
ATTRIBUTENAME: Final[str]
UNQUOTEDVALUE: Final[str]
SINGLEQUOTEDVALUE: Final[str]
DOUBLEQUOTEDVALUE: Final[str]
ATTRIBUTEVALUE: Final[str]
ATTRIBUTEVALUESPEC: Final[str]
ATTRIBUTE: Final[str]
OPENTAG: Final[str]
CLOSETAG: Final[str]
HTMLCOMMENT: Final[str]
PROCESSINGINSTRUCTION: Final[str]
DECLARATION: Final[str]
CDATA: Final[str]
HTMLTAG: Final[str]
reHtmlTag: Final[re.Pattern[str]]
reBackslashOrAmp: Final[re.Pattern[str]]
ESCAPABLE: Final[str]
reEntityOrEscapedChar: Final[re.Pattern[str]]
XMLSPECIAL: Final[str]
reXmlSpecial: Final[re.Pattern[str]]

def unescape_char(s: AnyStr) -> AnyStr: ...
def unescape_string(s: str) -> str: ...
def normalize_uri(uri: str) -> str: ...

UNSAFE_MAP: Final[dict[str, str]]

def replace_unsafe_char(s: str) -> str: ...
@overload
def escape_xml(s: None) -> Literal[""]: ...
@overload
def escape_xml(s: str) -> str: ...
