from _typeshed import Incomplete

from pyqtgraph.Qt import QtCore, QtWidgets

app: Incomplete
path: Incomplete
QRegularExpression: Incomplete
QFont: Incomplete
QColor: Incomplete
QTextCharFormat: Incomplete
QSyntaxHighlighter: Incomplete

def charFormat(color, style: str = "", background=None): ...

class LightThemeColors:
    Red: str
    Pink: str
    Purple: str
    DeepPurple: str
    Indigo: str
    Blue: str
    LightBlue: str
    Cyan: str
    Teal: str
    Green: str
    LightGreen: str
    Lime: str
    Yellow: str
    Amber: str
    Orange: str
    DeepOrange: str
    Brown: str
    Grey: str
    BlueGrey: str

class DarkThemeColors:
    Red: str
    Pink: str
    Purple: str
    DeepPurple: str
    Indigo: str
    Blue: str
    LightBlue: str
    Cyan: str
    Teal: str
    Green: str
    LightGreen: str
    Lime: str
    Yellow: str
    Amber: str
    Orange: str
    DeepOrange: str
    Brown: str
    Grey: str
    BlueGrey: str

LIGHT_STYLES: Incomplete
DARK_STYLES: Incomplete

class PythonHighlighter(QSyntaxHighlighter):
    keywords: Incomplete
    operators: Incomplete
    braces: Incomplete
    tri_single: Incomplete
    tri_double: Incomplete
    rules: Incomplete
    searchText: Incomplete
    def __init__(self, document) -> None: ...
    @property
    def styles(self): ...
    def highlightBlock(self, text) -> None: ...
    def match_multiline(self, text, delimiter, in_state, style): ...
    def applySearchHighlight(self, text) -> None: ...

def unnestedDict(exDict): ...

class ExampleLoader(QtWidgets.QMainWindow):
    bindings: Incomplete
    modules: Incomplete
    ui: Incomplete
    cw: Incomplete
    codeBtn: Incomplete
    codeLayout: Incomplete
    hl: Incomplete
    curListener: Incomplete
    itemCache: Incomplete
    oldText: Incomplete
    def __init__(self) -> None: ...
    def event(self, event: QtCore.QEvent | None): ...
    def updateCodeViewTabWidth(self, font) -> None: ...
    def showEvent(self, event) -> None: ...
    def onTextChange(self) -> None: ...
    def filterByTitle(self, text) -> None: ...
    def filterByContent(self, text=None) -> None: ...
    def getMatchingTitles(self, text, exDict=None, acceptAll: bool = False): ...
    def showExamplesByTitle(self, titles) -> None: ...
    def simulate_black_mode(self) -> None: ...
    def populateTree(self, root, examples) -> None: ...
    def currentFile(self): ...
    def loadFile(self, *, edited: bool = False) -> None: ...
    def showFile(self) -> None: ...
    def getExampleContent(self, filename): ...
    def codeEdited(self) -> None: ...
    def runEditedCode(self) -> None: ...
    def keyPressEvent(self, event) -> None: ...

def main() -> None: ...
