from pygments.lexer import RegexLexer
from typing import Any

class IniLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    tokens: Any = ...
    def analyse_text(text: Any): ...

class RegeditLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    tokens: Any = ...
    def analyse_text(text: Any): ...

class PropertiesLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    tokens: Any = ...

class KconfigLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    flags: int = ...
    def call_indent(level: Any): ...
    def do_indent(level: Any): ...
    tokens: Any = ...

class Cfengine3Lexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    tokens: Any = ...

class ApacheConfLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    flags: Any = ...
    tokens: Any = ...

class SquidConfLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    flags: Any = ...
    keywords: Any = ...
    opts: Any = ...
    actions: Any = ...
    actions_stats: Any = ...
    actions_log: Any = ...
    acls: Any = ...
    ip_re: str = ...
    tokens: Any = ...

class NginxConfLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    tokens: Any = ...

class LighttpdConfLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    tokens: Any = ...

class DockerLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    flags: Any = ...
    tokens: Any = ...

class TerraformLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    classes: Any = ...
    classes_re: Any = ...
    types: Any = ...
    numeric_functions: Any = ...
    string_functions: Any = ...
    collection_functions: Any = ...
    encoding_functions: Any = ...
    filesystem_functions: Any = ...
    date_time_functions: Any = ...
    hash_crypto_functions: Any = ...
    ip_network_functions: Any = ...
    type_conversion_functions: Any = ...
    builtins: Any = ...
    builtins_re: Any = ...
    tokens: Any = ...

class TermcapLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    tokens: Any = ...

class TerminfoLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    tokens: Any = ...

class PkgConfigLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    tokens: Any = ...

class PacmanConfLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    mimetypes: Any = ...
    tokens: Any = ...

class AugeasLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    tokens: Any = ...

class TOMLLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    tokens: Any = ...

class NestedTextLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    tokens: Any = ...

class SingularityLexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    filenames: Any = ...
    flags: Any = ...
    tokens: Any = ...
    def analyse_text(text: Any): ...
