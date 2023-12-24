from _typeshed import Incomplete
from collections.abc import Generator

from antlr4.RuleContext import RuleContext as RuleContext
from antlr4.Token import Token as Token
from antlr4.tree.Tree import (
    INVALID_INTERVAL as INVALID_INTERVAL,
    ErrorNodeImpl as ErrorNodeImpl,
    ParseTree as ParseTree,
    ParseTreeListener as ParseTreeListener,
    TerminalNode as TerminalNode,
    TerminalNodeImpl as TerminalNodeImpl,
)

class ParserRuleContext(RuleContext):
    children: Incomplete
    start: Incomplete
    stop: Incomplete
    exception: Incomplete
    def __init__(self, parent: ParserRuleContext | None = None, invokingStateNumber: int | None = None) -> None: ...
    parentCtx: Incomplete
    invokingState: Incomplete
    def copyFrom(self, ctx: ParserRuleContext) -> Incomplete: ...
    def enterRule(self, listener: ParseTreeListener) -> Incomplete: ...
    def exitRule(self, listener: ParseTreeListener) -> Incomplete: ...
    def addChild(self, child: ParseTree) -> Incomplete: ...
    def removeLastChild(self) -> None: ...
    def addTokenNode(self, token: Token) -> Incomplete: ...
    def addErrorNode(self, badToken: Token) -> Incomplete: ...
    def getChild(self, i: int, ttype: type | None = None) -> Incomplete: ...
    def getChildren(self, predicate: Incomplete | None = ...) -> Generator[Incomplete, None, None]: ...
    def getToken(self, ttype: int, i: int) -> Incomplete: ...
    def getTokens(self, ttype: int) -> Incomplete: ...
    def getTypedRuleContext(self, ctxType: type, i: int) -> Incomplete: ...
    def getTypedRuleContexts(self, ctxType: type) -> Incomplete: ...
    def getChildCount(self) -> Incomplete: ...
    def getSourceInterval(self) -> Incomplete: ...

class InterpreterRuleContext(ParserRuleContext):
    ruleIndex: Incomplete
    def __init__(self, parent: ParserRuleContext, invokingStateNumber: int, ruleIndex: int) -> None: ...
