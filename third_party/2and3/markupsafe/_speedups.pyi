from typing import Text, Union

from . import Markup
from ._compat import string_types, text_type

def escape(s: Union[Markup, Text]) -> Markup: ...
def escape_silent(s: Union[None, Markup, Text]) -> Markup: ...
def soft_unicode(s: Text) -> text_type: ...
