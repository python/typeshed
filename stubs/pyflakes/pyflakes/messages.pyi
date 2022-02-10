from typing import Any

class Message:
    message: str
    message_args: Any
    filename: Any
    lineno: Any
    col: Any
    def __init__(self, filename, loc) -> None: ...

class UnusedImport(Message):
    message: str
    message_args: Any
    def __init__(self, filename, loc, name) -> None: ...

class RedefinedWhileUnused(Message):
    message: str
    message_args: Any
    def __init__(self, filename, loc, name, orig_loc) -> None: ...

class RedefinedInListComp(Message):
    message: str
    message_args: Any
    def __init__(self, filename, loc, name, orig_loc) -> None: ...

class ImportShadowedByLoopVar(Message):
    message: str
    message_args: Any
    def __init__(self, filename, loc, name, orig_loc) -> None: ...

class ImportStarNotPermitted(Message):
    message: str
    message_args: Any
    def __init__(self, filename, loc, modname) -> None: ...

class ImportStarUsed(Message):
    message: str
    message_args: Any
    def __init__(self, filename, loc, modname) -> None: ...

class ImportStarUsage(Message):
    message: str
    message_args: Any
    def __init__(self, filename, loc, name, from_list) -> None: ...

class UndefinedName(Message):
    message: str
    message_args: Any
    def __init__(self, filename, loc, name) -> None: ...

class DoctestSyntaxError(Message):
    message: str
    message_args: Any
    def __init__(self, filename, loc, position: Any | None = ...) -> None: ...

class UndefinedExport(Message):
    message: str
    message_args: Any
    def __init__(self, filename, loc, name) -> None: ...

class UndefinedLocal(Message):
    message: str
    default: str
    builtin: str
    message_args: Any
    def __init__(self, filename, loc, name, orig_loc) -> None: ...

class DuplicateArgument(Message):
    message: str
    message_args: Any
    def __init__(self, filename, loc, name) -> None: ...

class MultiValueRepeatedKeyLiteral(Message):
    message: str
    message_args: Any
    def __init__(self, filename, loc, key) -> None: ...

class MultiValueRepeatedKeyVariable(Message):
    message: str
    message_args: Any
    def __init__(self, filename, loc, key) -> None: ...

class LateFutureImport(Message):
    message: str
    message_args: Any
    def __init__(self, filename, loc, names) -> None: ...

class FutureFeatureNotDefined(Message):
    message: str
    message_args: Any
    def __init__(self, filename, loc, name) -> None: ...

class UnusedVariable(Message):
    message: str
    message_args: Any
    def __init__(self, filename, loc, names) -> None: ...

class ReturnWithArgsInsideGenerator(Message):
    message: str

class ReturnOutsideFunction(Message):
    message: str

class YieldOutsideFunction(Message):
    message: str

class ContinueOutsideLoop(Message):
    message: str

class BreakOutsideLoop(Message):
    message: str

class ContinueInFinally(Message):
    message: str

class DefaultExceptNotLast(Message):
    message: str

class TwoStarredExpressions(Message):
    message: str

class TooManyExpressionsInStarredAssignment(Message):
    message: str

class IfTuple(Message):
    message: str

class AssertTuple(Message):
    message: str

class ForwardAnnotationSyntaxError(Message):
    message: str
    message_args: Any
    def __init__(self, filename, loc, annotation) -> None: ...

class CommentAnnotationSyntaxError(Message):
    message: str
    message_args: Any
    def __init__(self, filename, loc, annotation) -> None: ...

class RaiseNotImplemented(Message):
    message: str

class InvalidPrintSyntax(Message):
    message: str

class IsLiteral(Message):
    message: str

class FStringMissingPlaceholders(Message):
    message: str

class StringDotFormatExtraPositionalArguments(Message):
    message: str
    message_args: Any
    def __init__(self, filename, loc, extra_positions) -> None: ...

class StringDotFormatExtraNamedArguments(Message):
    message: str
    message_args: Any
    def __init__(self, filename, loc, extra_keywords) -> None: ...

class StringDotFormatMissingArgument(Message):
    message: str
    message_args: Any
    def __init__(self, filename, loc, missing_arguments) -> None: ...

class StringDotFormatMixingAutomatic(Message):
    message: str

class StringDotFormatInvalidFormat(Message):
    message: str
    message_args: Any
    def __init__(self, filename, loc, error) -> None: ...

class PercentFormatInvalidFormat(Message):
    message: str
    message_args: Any
    def __init__(self, filename, loc, error) -> None: ...

class PercentFormatMixedPositionalAndNamed(Message):
    message: str

class PercentFormatUnsupportedFormatCharacter(Message):
    message: str
    message_args: Any
    def __init__(self, filename, loc, c) -> None: ...

class PercentFormatPositionalCountMismatch(Message):
    message: str
    message_args: Any
    def __init__(self, filename, loc, n_placeholders, n_substitutions) -> None: ...

class PercentFormatExtraNamedArguments(Message):
    message: str
    message_args: Any
    def __init__(self, filename, loc, extra_keywords) -> None: ...

class PercentFormatMissingArgument(Message):
    message: str
    message_args: Any
    def __init__(self, filename, loc, missing_arguments) -> None: ...

class PercentFormatExpectedMapping(Message):
    message: str

class PercentFormatExpectedSequence(Message):
    message: str

class PercentFormatStarRequiresSequence(Message):
    message: str
