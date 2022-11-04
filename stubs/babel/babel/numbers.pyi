from typing import Any

long = int
LC_NUMERIC: Any

class UnknownCurrencyError(Exception):
    identifier: Any
    def __init__(self, identifier) -> None: ...

def list_currencies(locale: Any | None = ...): ...
def validate_currency(currency, locale: Any | None = ...) -> None: ...
def is_currency(currency, locale: Any | None = ...): ...
def normalize_currency(currency, locale: Any | None = ...): ...
def get_currency_name(currency, count: Any | None = ..., locale=...): ...
def get_currency_symbol(currency, locale=...): ...
def get_currency_precision(currency): ...
def get_currency_unit_pattern(currency, count: Any | None = ..., locale=...): ...
def get_territory_currencies(
    territory,
    start_date: Any | None = ...,
    end_date: Any | None = ...,
    tender: bool = ...,
    non_tender: bool = ...,
    include_details: bool = ...,
): ...
def get_decimal_symbol(locale=...): ...
def get_plus_sign_symbol(locale=...): ...
def get_minus_sign_symbol(locale=...): ...
def get_exponential_symbol(locale=...): ...
def get_group_symbol(locale=...): ...
def format_number(number, locale=...): ...
def get_decimal_precision(number): ...
def get_decimal_quantum(precision): ...
def format_decimal(
    number, format: Any | None = ..., locale=..., decimal_quantization: bool = ..., group_separator: bool = ...
): ...
def format_compact_decimal(
    number, *, format_type: str = ..., locale=..., fraction_digits: int = ...
): ...

class UnknownCurrencyFormatError(KeyError): ...

def format_currency(
    number,
    currency,
    format: Any | None = ...,
    locale=...,
    currency_digits: bool = ...,
    format_type: str = ...,
    decimal_quantization: bool = ...,
    group_separator: bool = ...,
): ...
def format_percent(
    number, format: Any | None = ..., locale=..., decimal_quantization: bool = ..., group_separator: bool = ...
): ...
def format_scientific(number, format: Any | None = ..., locale=..., decimal_quantization: bool = ...): ...

class NumberFormatError(ValueError):
    suggestions: Any
    def __init__(self, message, suggestions: Any | None = ...) -> None: ...

def parse_number(string, locale=...): ...
def parse_decimal(string, locale=..., strict: bool = ...): ...

PREFIX_END: str
NUMBER_TOKEN: str
PREFIX_PATTERN: Any
NUMBER_PATTERN: Any
SUFFIX_PATTERN: str
number_re: Any

def parse_grouping(p): ...
def parse_pattern(pattern): ...

class NumberPattern:
    pattern: Any
    prefix: Any
    suffix: Any
    grouping: Any
    int_prec: Any
    frac_prec: Any
    exp_prec: Any
    exp_plus: Any
    scale: Any
    def __init__(self, pattern, prefix, suffix, grouping, int_prec, frac_prec, exp_prec, exp_plus) -> None: ...
    def compute_scale(self): ...
    def scientific_notation_elements(self, value, locale): ...
    def apply(
        self,
        value,
        locale,
        currency: Any | None = ...,
        currency_digits: bool = ...,
        decimal_quantization: bool = ...,
        force_frac: Any | None = ...,
        group_separator: bool = ...,
    ): ...
