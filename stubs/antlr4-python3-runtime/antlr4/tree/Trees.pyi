from _typeshed import Incomplete

from antlr4.Token import Token as Token
from antlr4.tree.Tree import (
    ErrorNode as ErrorNode,
    ParseTree as ParseTree,
    RuleNode as RuleNode,
    TerminalNode as TerminalNode,
    Tree as Tree,
)
from antlr4.Utils import escapeWhitespace as escapeWhitespace

Parser: Incomplete

class Trees:
    @classmethod
    def toStringTree(cls, t: Tree, ruleNames: list[str] | None = None, recog: Parser | None = None) -> Incomplete: ...
    @classmethod
    def getNodeText(cls, t: Tree, ruleNames: list[str] | None = None, recog: Parser | None = None) -> Incomplete: ...
    @classmethod
    def getChildren(cls, t: Tree) -> Incomplete: ...
    @classmethod
    def getAncestors(cls, t: Tree) -> Incomplete: ...
    @classmethod
    def findAllTokenNodes(cls, t: ParseTree, ttype: int) -> Incomplete: ...
    @classmethod
    def findAllRuleNodes(cls, t: ParseTree, ruleIndex: int) -> Incomplete: ...
    @classmethod
    def findAllNodes(cls, t: ParseTree, index: int, findTokens: bool) -> Incomplete: ...
    @classmethod
    def descendants(cls, t: ParseTree) -> Incomplete: ...
