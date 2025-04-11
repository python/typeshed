import re
from typing import ClassVar

import click

class EmailParamType(click.ParamType):
    EMAIL_REGEX: ClassVar[re.Pattern[str]]
    def convert(self, value: str, param: click.Parameter | None, ctx: click.Context | None) -> str | None: ...

class PasswordParamType(click.ParamType):
    def convert(self, value: str, param: click.Parameter | None, ctx: click.Context | None) -> str | None: ...

class TextAreaParamType(click.ParamType):
    def convert(self, value: str, param: click.Parameter | None, ctx: click.Context | None) -> str | None: ...

EMAIL_TYPE: EmailParamType
PASSWORD_TYPE: PasswordParamType
TEXTAREA_TYPE: TextAreaParamType
