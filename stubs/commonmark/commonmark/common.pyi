import html
import re
from typing import AnyStr, Literal, overload

HTMLunescape = html.unescape
ENTITY: str
TAGNAME: str
ATTRIBUTENAME: str
UNQUOTEDVALUE: str
SINGLEQUOTEDVALUE: str
DOUBLEQUOTEDVALUE: str
ATTRIBUTEVALUE: str
ATTRIBUTEVALUESPEC: str
ATTRIBUTE: str
OPENTAG: str
CLOSETAG: str
HTMLCOMMENT: str
PROCESSINGINSTRUCTION: str
DECLARATION: str
CDATA: str
HTMLTAG: str
reHtmlTag: re.Pattern[str]
reBackslashOrAmp: re.Pattern[str]
ESCAPABLE: str
reEntityOrEscapedChar: re.Pattern[str]
XMLSPECIAL: str
reXmlSpecial: re.Pattern[str]

def unescape_char(s: AnyStr) -> AnyStr: ...
def unescape_string(s: str) -> str: ...
def normalize_uri(uri: str) -> str: ...

UNSAFE_MAP: dict[str, str]

def replace_unsafe_char(s: str) -> str: ...
@overload
def escape_xml(s: None) -> Literal[""]: ...
@overload
def escape_xml(s: str) -> str: ...
