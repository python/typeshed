from _typeshed import Incomplete

from reportlab.lib.colors import black
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus.flowables import Flowable

debug: int
DUMPPROGRAM: int
TOOSMALLSPACE: float

class paragraphEngine:
    lineOpHandlers: Incomplete
    program: Incomplete
    indent: float
    baseindent: float
    fontName: str
    fontSize: int
    leading: int
    fontColor: Incomplete
    x: float
    alignment: Incomplete
    textStateStack: Incomplete
    def __init__(self, program: Incomplete | None = None) -> None: ...
    TEXT_STATE_VARIABLES: Incomplete
    def pushTextState(self): ...
    def popTextState(self) -> None: ...
    def format(self, maxwidth, maxheight, program, leading: int = 0): ...
    def getState(self): ...
    def resetState(self, state) -> None: ...
    rightIndent: Incomplete
    def fitLine(self, program, totalLength): ...
    def centerAlign(self, line, lineLength, maxLength): ...
    def rightAlign(self, line, lineLength, maxLength): ...
    def insertShift(self, line, shift): ...
    def justifyAlign(self, line, lineLength, maxLength): ...
    def shrinkWrap(self, line): ...
    def cleanProgram(self, line): ...
    def runOpCodes(self, program, canvas, textobject): ...

def stringLine(line, length): ...
def simpleJustifyAlign(line, currentLength, maxLength): ...
def readBool(text): ...
def readAlignment(text): ...
def readLength(text): ...
def lengthSequence(s, converter=...): ...
def readColor(text): ...

class StyleAttributeConverters:
    fontSize: Incomplete
    leading: Incomplete
    leftIndent: Incomplete
    rightIndent: Incomplete
    firstLineIndent: Incomplete
    alignment: Incomplete
    spaceBefore: Incomplete
    spaceAfter: Incomplete
    bulletFontSize: Incomplete
    bulletIndent: Incomplete
    textColor: Incomplete
    backColor: Incomplete

class SimpleStyle:
    name: str
    fontName: Incomplete
    fontSize: int
    leading: int
    leftIndent: int
    rightIndent: int
    firstLineIndent: int
    alignment = TA_LEFT
    spaceBefore: int
    spaceAfter: int
    bulletFontName: Incomplete
    bulletFontSize: int
    bulletIndent: int
    textColor = black
    backColor: Incomplete
    def __init__(self, name, parent: Incomplete | None = None, **kw) -> None: ...
    def addAttributes(self, dictionary) -> None: ...

DEFAULT_ALIASES: Incomplete

class FastPara(Flowable):
    style: Incomplete
    simpletext: Incomplete
    lines: Incomplete
    def __init__(self, style, simpletext) -> None: ...
    availableWidth: Incomplete
    height: Incomplete
    def wrap(self, availableWidth, availableHeight): ...
    def split(self, availableWidth, availableHeight): ...
    def draw(self) -> None: ...
    def getSpaceBefore(self): ...
    def getSpaceAfter(self): ...

def defaultContext(): ...
def buildContext(stylesheet: Incomplete | None = None): ...

class Para(Flowable):
    spaceBefore: int
    spaceAfter: int
    baseindent: Incomplete
    context: Incomplete
    parsedText: Incomplete
    bulletText: Incomplete
    style1: Incomplete
    program: Incomplete
    formattedProgram: Incomplete
    remainder: Incomplete
    state: Incomplete
    bold: int
    italic: int
    face: Incomplete
    size: Incomplete
    def __init__(
        self,
        style,
        parsedText: Incomplete | None = None,
        bulletText: Incomplete | None = None,
        state: Incomplete | None = None,
        context: Incomplete | None = None,
        baseindent: int = 0,
    ) -> None: ...
    def getSpaceBefore(self): ...
    def getSpaceAfter(self): ...
    availableHeight: Incomplete
    myengine: Incomplete
    cansplit: int
    height: Incomplete
    laststate: Incomplete
    remainderProgram: Incomplete
    def wrap(self, availableWidth, availableHeight): ...
    def split(self, availableWidth, availableHeight): ...
    def draw(self) -> None: ...
    def compileProgram(self, parsedText, program: Incomplete | None = None): ...
    def linearize(self, program: Incomplete | None = None, parsedText: Incomplete | None = None) -> None: ...
    def compileComponent(self, parsedText, program) -> None: ...
    def shiftfont(
        self, program, face: Incomplete | None = None, bold: Incomplete | None = None, italic: Incomplete | None = None
    ): ...
    def compile_(self, attdict, content, extra, program) -> None: ...
    def compile_pageNumber(self, attdict, content, extra, program) -> None: ...
    def compile_b(self, attdict, content, extra, program) -> None: ...
    def compile_i(self, attdict, content, extra, program) -> None: ...
    def compile_u(self, attdict, content, extra, program) -> None: ...
    def compile_sub(self, attdict, content, extra, program) -> None: ...
    def compile_ul(self, attdict, content, extra, program, tagname: str = "ul") -> None: ...
    def compile_ol(self, attdict, content, extra, program): ...
    def compile_dl(self, attdict, content, extra, program) -> None: ...
    def compile_super(self, attdict, content, extra, program) -> None: ...
    def compile_font(self, attdict, content, extra, program) -> None: ...
    def compile_a(self, attdict, content, extra, program) -> None: ...
    def compile_link(self, attdict, content, extra, program) -> None: ...
    def compile_setLink(self, attdict, content, extra, program) -> None: ...
    def compile_bullet(self, attdict, content, extra, program) -> None: ...
    def do_bullet(self, text, program) -> None: ...
    def compile_tt(self, attdict, content, extra, program) -> None: ...
    def compile_greek(self, attdict, content, extra, program) -> None: ...
    def compile_evalString(self, attdict, content, extra, program) -> None: ...
    def compile_name(self, attdict, content, extra, program) -> None: ...
    def compile_getName(self, attdict, content, extra, program) -> None: ...
    def compile_seq(self, attdict, content, extra, program) -> None: ...
    def compile_seqReset(self, attdict, content, extra, program) -> None: ...
    def compile_seqDefault(self, attdict, content, extra, program) -> None: ...
    def compile_para(self, attdict, content, extra, program, stylename: str = "para.defaultStyle") -> None: ...

class bulletMaker:
    tagname: Incomplete
    style: Incomplete
    typ: Incomplete
    count: int
    def __init__(self, tagname, atts, context) -> None: ...
    def makeBullet(self, atts, bl: Incomplete | None = None) -> None: ...

class EvalStringObject:
    tagname: str
    attdict: Incomplete
    content: Incomplete
    context: Incomplete
    extra: Incomplete
    def __init__(self, attdict, content, extra, context) -> None: ...
    def getOp(self, tuple, engine): ...
    def width(self, engine): ...
    def execute(self, engine, textobject, canvas) -> None: ...

class SeqObject(EvalStringObject):
    def getOp(self, tuple, engine): ...

class NameObject(EvalStringObject):
    tagname: str
    def execute(self, engine, textobject, canvas) -> None: ...

class SeqDefaultObject(NameObject):
    op: str
    def getOp(self, tuple, engine): ...

class SeqResetObject(NameObject):
    op: str
    def getOp(self, tuple, engine): ...

class GetNameObject(EvalStringObject):
    tagname: str

class PageNumberObject:
    example: Incomplete
    def __init__(self, example: str = "XXX") -> None: ...
    def width(self, engine): ...
    def execute(self, engine, textobject, canvas) -> None: ...

def EmbedInRml2pdf(): ...
def handleSpecialCharacters(engine, text, program: Incomplete | None = None): ...
def Paragraph(
    text, style, bulletText: Incomplete | None = None, frags: Incomplete | None = None, context: Incomplete | None = None
): ...

class UnderLineHandler:
    color: Incomplete
    def __init__(self, color: Incomplete | None = None) -> None: ...
    xStart: Incomplete
    yStart: Incomplete
    def start_at(self, x, y, para, canvas, textobject) -> None: ...
    def end_at(self, x, y, para, canvas, textobject) -> None: ...

UNDERLINE: Incomplete

class HotLink(UnderLineHandler):
    url: Incomplete
    def __init__(self, url) -> None: ...
    def end_at(self, x, y, para, canvas, textobject) -> None: ...
    def link(self, rect, canvas) -> None: ...

class InternalLink(HotLink):
    def link(self, rect, canvas) -> None: ...

class DefDestination(HotLink):
    defined: int
    def link(self, rect, canvas) -> None: ...

def splitspace(text): ...

testparagraph: str
testparagraph1: str

def test2(canv, testpara) -> None: ...

testlink: Incomplete
test_program: Incomplete

def test() -> None: ...
