from typing import Any, Optional
from werkzeug.exceptions import HTTPException

def parse_converter_args(argstr): ...
def parse_rule(rule): ...

class RoutingException(Exception): ...

class RequestRedirect(HTTPException, RoutingException):
    code = ...  # type: Any
    new_url = ...  # type: Any
    def __init__(self, new_url): ...
    def get_response(self, environ): ...

class RequestSlash(RoutingException): ...

class RequestAliasRedirect(RoutingException):
    matched_values = ...  # type: Any
    def __init__(self, matched_values): ...

class BuildError(RoutingException, LookupError):
    endpoint = ...  # type: Any
    values = ...  # type: Any
    method = ...  # type: Any
    adapter: Optional[MapAdapter]
    def __init__(self, endpoint, values, method, adapter: Optional[MapAdapter] = ...) -> None: ...
    @property
    def suggested(self) -> Optional[Rule]: ...
    def closest_rule(self, adapter: Optional[MapAdapter]) -> Optional[Rule]: ...

class ValidationError(ValueError): ...

class RuleFactory:
    def get_rules(self, map): ...

class Subdomain(RuleFactory):
    subdomain = ...  # type: Any
    rules = ...  # type: Any
    def __init__(self, subdomain, rules): ...
    def get_rules(self, map): ...

class Submount(RuleFactory):
    path = ...  # type: Any
    rules = ...  # type: Any
    def __init__(self, path, rules): ...
    def get_rules(self, map): ...

class EndpointPrefix(RuleFactory):
    prefix = ...  # type: Any
    rules = ...  # type: Any
    def __init__(self, prefix, rules): ...
    def get_rules(self, map): ...

class RuleTemplate:
    rules = ...  # type: Any
    def __init__(self, rules): ...
    def __call__(self, *args, **kwargs): ...

class RuleTemplateFactory(RuleFactory):
    rules = ...  # type: Any
    context = ...  # type: Any
    def __init__(self, rules, context): ...
    def get_rules(self, map): ...

class Rule(RuleFactory):
    rule = ...  # type: Any
    is_leaf = ...  # type: Any
    map = ...  # type: Any
    strict_slashes = ...  # type: Any
    subdomain = ...  # type: Any
    host = ...  # type: Any
    defaults = ...  # type: Any
    build_only = ...  # type: Any
    alias = ...  # type: Any
    methods = ...  # type: Any
    endpoint = ...  # type: Any
    redirect_to = ...  # type: Any
    arguments = ...  # type: Any
    def __init__(self, string, defaults: Optional[Any] = ..., subdomain: Optional[Any] = ..., methods: Optional[Any] = ...,
                 build_only: bool = ..., endpoint: Optional[Any] = ..., strict_slashes: Optional[Any] = ...,
                 redirect_to: Optional[Any] = ..., alias: bool = ..., host: Optional[Any] = ...): ...
    def empty(self): ...
    def get_empty_kwargs(self): ...
    def get_rules(self, map): ...
    def refresh(self): ...
    def bind(self, map, rebind: bool = ...): ...
    def get_converter(self, variable_name, converter_name, args, kwargs): ...
    def compile(self): ...
    def match(self, path, method: Optional[Any] = ...): ...
    def build(self, values, append_unknown: bool = ...): ...
    def provides_defaults_for(self, rule): ...
    def suitable_for(self, values, method: Optional[Any] = ...): ...
    def match_compare_key(self): ...
    def build_compare_key(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

class BaseConverter:
    regex = ...  # type: Any
    weight = ...  # type: Any
    map = ...  # type: Any
    def __init__(self, map): ...
    def to_python(self, value): ...
    def to_url(self, value): ...

class UnicodeConverter(BaseConverter):
    regex = ...  # type: Any
    def __init__(self, map, minlength: int = ..., maxlength: Optional[Any] = ..., length: Optional[Any] = ...): ...

class AnyConverter(BaseConverter):
    regex = ...  # type: Any
    def __init__(self, map, *items): ...

class PathConverter(BaseConverter):
    regex = ...  # type: Any
    weight = ...  # type: Any

class NumberConverter(BaseConverter):
    weight = ...  # type: Any
    fixed_digits = ...  # type: Any
    min = ...  # type: Any
    max = ...  # type: Any
    def __init__(self, map, fixed_digits: int = ..., min: Optional[Any] = ..., max: Optional[Any] = ...): ...
    def to_python(self, value): ...
    def to_url(self, value): ...

class IntegerConverter(NumberConverter):
    regex = ...  # type: Any
    num_convert = ...  # type: Any

class FloatConverter(NumberConverter):
    regex = ...  # type: Any
    num_convert = ...  # type: Any
    def __init__(self, map, min: Optional[Any] = ..., max: Optional[Any] = ...): ...

class UUIDConverter(BaseConverter):
    regex = ...  # type: Any
    def to_python(self, value): ...
    def to_url(self, value): ...

DEFAULT_CONVERTERS = ...  # type: Any

class Map:
    default_converters = ...  # type: Any
    default_subdomain = ...  # type: Any
    charset = ...  # type: Any
    encoding_errors = ...  # type: Any
    strict_slashes = ...  # type: Any
    redirect_defaults = ...  # type: Any
    host_matching = ...  # type: Any
    converters = ...  # type: Any
    sort_parameters = ...  # type: Any
    sort_key = ...  # type: Any
    def __init__(self, rules: Optional[Any] = ..., default_subdomain: str = ..., charset: str = ...,
                 strict_slashes: bool = ..., redirect_defaults: bool = ..., converters: Optional[Any] = ...,
                 sort_parameters: bool = ..., sort_key: Optional[Any] = ..., encoding_errors: str = ...,
                 host_matching: bool = ...): ...
    def is_endpoint_expecting(self, endpoint, *arguments): ...
    def iter_rules(self, endpoint: Optional[Any] = ...): ...
    def add(self, rulefactory): ...
    def bind(self, server_name, script_name: Optional[Any] = ..., subdomain: Optional[Any] = ..., url_scheme: str = ...,
             default_method: str = ..., path_info: Optional[Any] = ..., query_args: Optional[Any] = ...): ...
    def bind_to_environ(self, environ, server_name: Optional[Any] = ..., subdomain: Optional[Any] = ...): ...
    def update(self): ...

class MapAdapter:
    map = ...  # type: Any
    server_name = ...  # type: Any
    script_name = ...  # type: Any
    subdomain = ...  # type: Any
    url_scheme = ...  # type: Any
    path_info = ...  # type: Any
    default_method = ...  # type: Any
    query_args = ...  # type: Any
    def __init__(self, map, server_name, script_name, subdomain, url_scheme, path_info, default_method,
                 query_args: Optional[Any] = ...): ...
    def dispatch(self, view_func, path_info: Optional[Any] = ..., method: Optional[Any] = ...,
                 catch_http_exceptions: bool = ...): ...
    def match(self, path_info: Optional[Any] = ..., method: Optional[Any] = ..., return_rule: bool = ...,
              query_args: Optional[Any] = ...): ...
    def test(self, path_info: Optional[Any] = ..., method: Optional[Any] = ...): ...
    def allowed_methods(self, path_info: Optional[Any] = ...): ...
    def get_host(self, domain_part): ...
    def get_default_redirect(self, rule, method, values, query_args): ...
    def encode_query_args(self, query_args): ...
    def make_redirect_url(self, path_info, query_args: Optional[Any] = ..., domain_part: Optional[Any] = ...): ...
    def make_alias_redirect_url(self, path, endpoint, values, method, query_args): ...
    def build(self, endpoint, values: Optional[Any] = ..., method: Optional[Any] = ..., force_external: bool = ...,
              append_unknown: bool = ...): ...
