class ChevronError(SyntaxError): ...

def grab_literal(template: str, l_del: str | None) -> tuple[str, str]: ...  # undocumented
def l_sa_check(template: str, literal: str, is_standalone: bool) -> bool | None: ...  # undocumented
def r_sa_check(template: str, tag_type: str, is_standalone: bool) -> bool: ...  # undocumented
def parse_tag(template: str, l_del: str | None, r_del: str | None): ...  # undocumented
def tokenize(template: str, def_ldel: str | None = ..., def_rdel: str | None = ...): ...  # undocumented
