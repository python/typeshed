import types
from typing import Any, Optional

def find_lexer_class(name: Any): ...
def get_lexer_by_name(_alias: Any, **options: Any): ...
def load_lexer_from_file(filename: Any, lexername: str = ..., **options: Any): ...
def get_lexer_for_filename(_fn: Any, code: Optional[Any] = ..., **options: Any): ...
def guess_lexer(_text: Any, **options: Any): ...

class _automodule(types.ModuleType):
    def __getattr__(self, name: Any): ...

# Names in __all__ with no definition:
#   ABAPLexer
#   AMDGPULexer
#   APLLexer
#   AbnfLexer
#   ActionScript3Lexer
#   ActionScriptLexer
#   AdaLexer
#   AdlLexer
#   AgdaLexer
#   AheuiLexer
#   AlloyLexer
#   AmbientTalkLexer
#   AmplLexer
#   Angular2HtmlLexer
#   Angular2Lexer
#   AntlrActionScriptLexer
#   AntlrCSharpLexer
#   AntlrCppLexer
#   AntlrJavaLexer
#   AntlrLexer
#   AntlrObjectiveCLexer
#   AntlrPerlLexer
#   AntlrPythonLexer
#   AntlrRubyLexer
#   ApacheConfLexer
#   AppleScriptLexer
#   ArduinoLexer
#   ArrowLexer
#   AspectJLexer
#   AsymptoteLexer
#   AugeasLexer
#   AutoItLexer
#   AutohotkeyLexer
#   AwkLexer
#   BBCBasicLexer
#   BBCodeLexer
#   BCLexer
#   BSTLexer
#   BareLexer
#   BaseMakefileLexer
#   BashLexer
#   BashSessionLexer
#   BatchLexer
#   BefungeLexer
#   BibTeXLexer
#   BlitzBasicLexer
#   BlitzMaxLexer
#   BnfLexer
#   BoaLexer
#   BooLexer
#   BoogieLexer
#   BrainfuckLexer
#   BugsLexer
#   CAmkESLexer
#   CLexer
#   CMakeLexer
#   CObjdumpLexer
#   CPSALexer
#   CSharpAspxLexer
#   CSharpLexer
#   Ca65Lexer
#   CadlLexer
#   CapDLLexer
#   CapnProtoLexer
#   CbmBasicV2Lexer
#   CddlLexer
#   CeylonLexer
#   Cfengine3Lexer
#   ChaiscriptLexer
#   ChapelLexer
#   CharmciLexer
#   CheetahHtmlLexer
#   CheetahJavascriptLexer
#   CheetahLexer
#   CheetahXmlLexer
#   CirruLexer
#   ClayLexer
#   CleanLexer
#   ClojureLexer
#   ClojureScriptLexer
#   CobolFreeformatLexer
#   CobolLexer
#   CoffeeScriptLexer
#   ColdfusionCFCLexer
#   ColdfusionHtmlLexer
#   ColdfusionLexer
#   CommonLispLexer
#   ComponentPascalLexer
#   CoqLexer
#   CppLexer
#   CppObjdumpLexer
#   CrmshLexer
#   CrocLexer
#   CryptolLexer
#   CrystalLexer
#   CsoundDocumentLexer
#   CsoundOrchestraLexer
#   CsoundScoreLexer
#   CssDjangoLexer
#   CssErbLexer
#   CssGenshiLexer
#   CssLexer
#   CssPhpLexer
#   CssSmartyLexer
#   CudaLexer
#   CypherLexer
#   CythonLexer
#   DLexer
#   DObjdumpLexer
#   DarcsPatchLexer
#   DartLexer
#   Dasm16Lexer
#   DebianControlLexer
#   DelphiLexer
#   DevicetreeLexer
#   DgLexer
#   DiffLexer
#   DjangoLexer
#   DockerLexer
#   DtdLexer
#   DuelLexer
#   DylanConsoleLexer
#   DylanLexer
#   DylanLidLexer
#   ECLLexer
#   ECLexer
#   EarlGreyLexer
#   EasytrieveLexer
#   EbnfLexer
#   EiffelLexer
#   ElixirConsoleLexer
#   ElixirLexer
#   ElmLexer
#   EmacsLispLexer
#   EmailLexer
#   ErbLexer
#   ErlangLexer
#   ErlangShellLexer
#   EvoqueHtmlLexer
#   EvoqueLexer
#   EvoqueXmlLexer
#   ExeclineLexer
#   EzhilLexer
#   FSharpLexer
#   FStarLexer
#   FactorLexer
#   FancyLexer
#   FantomLexer
#   FelixLexer
#   FennelLexer
#   FishShellLexer
#   FlatlineLexer
#   FloScriptLexer
#   ForthLexer
#   FortranFixedLexer
#   FortranLexer
#   FoxProLexer
#   FreeFemLexer
#   FutharkLexer
#   GAPLexer
#   GDScriptLexer
#   GLShaderLexer
#   GasLexer
#   GcodeLexer
#   GenshiLexer
#   GenshiTextLexer
#   GettextLexer
#   GherkinLexer
#   GnuplotLexer
#   GoLexer
#   GoloLexer
#   GoodDataCLLexer
#   GosuLexer
#   GosuTemplateLexer
#   GraphvizLexer
#   GroffLexer
#   GroovyLexer
#   HLSLShaderLexer
#   HamlLexer
#   HandlebarsHtmlLexer
#   HandlebarsLexer
#   HaskellLexer
#   HaxeLexer
#   HexdumpLexer
#   HsailLexer
#   HspecLexer
#   HtmlDjangoLexer
#   HtmlGenshiLexer
#   HtmlLexer
#   HtmlPhpLexer
#   HtmlSmartyLexer
#   HttpLexer
#   HxmlLexer
#   HyLexer
#   HybrisLexer
#   IDLLexer
#   IconLexer
#   IdrisLexer
#   IgorLexer
#   Inform6Lexer
#   Inform6TemplateLexer
#   Inform7Lexer
#   IniLexer
#   IoLexer
#   IokeLexer
#   IrcLogsLexer
#   IsabelleLexer
#   JLexer
#   JagsLexer
#   JasminLexer
#   JavaLexer
#   JavascriptDjangoLexer
#   JavascriptErbLexer
#   JavascriptGenshiLexer
#   JavascriptLexer
#   JavascriptPhpLexer
#   JavascriptSmartyLexer
#   JclLexer
#   JsgfLexer
#   JsonBareObjectLexer
#   JsonLdLexer
#   JsonLexer
#   JspLexer
#   JuliaConsoleLexer
#   JuliaLexer
#   JuttleLexer
#   KalLexer
#   KconfigLexer
#   KernelLogLexer
#   KokaLexer
#   KotlinLexer
#   KuinLexer
#   LSLLexer
#   LassoCssLexer
#   LassoHtmlLexer
#   LassoJavascriptLexer
#   LassoLexer
#   LassoXmlLexer
#   LeanLexer
#   LessCssLexer
#   LighttpdConfLexer
#   LimboLexer
#   LiquidLexer
#   LiterateAgdaLexer
#   LiterateCryptolLexer
#   LiterateHaskellLexer
#   LiterateIdrisLexer
#   LiveScriptLexer
#   LlvmLexer
#   LlvmMirBodyLexer
#   LlvmMirLexer
#   LogosLexer
#   LogtalkLexer
#   LuaLexer
#   MIMELexer
#   MOOCodeLexer
#   MSDOSSessionLexer
#   MakefileLexer
#   MakoCssLexer
#   MakoHtmlLexer
#   MakoJavascriptLexer
#   MakoLexer
#   MakoXmlLexer
#   MaqlLexer
#   MarkdownLexer
#   MaskLexer
#   MasonLexer
#   MathematicaLexer
#   MatlabLexer
#   MatlabSessionLexer
#   MiniDLexer
#   MiniScriptLexer
#   ModelicaLexer
#   Modula2Lexer
#   MoinWikiLexer
#   MonkeyLexer
#   MonteLexer
#   MoonScriptLexer
#   MoselLexer
#   MozPreprocCssLexer
#   MozPreprocHashLexer
#   MozPreprocJavascriptLexer
#   MozPreprocPercentLexer
#   MozPreprocXulLexer
#   MqlLexer
#   MscgenLexer
#   MuPADLexer
#   MxmlLexer
#   MySqlLexer
#   MyghtyCssLexer
#   MyghtyHtmlLexer
#   MyghtyJavascriptLexer
#   MyghtyLexer
#   MyghtyXmlLexer
#   NCLLexer
#   NSISLexer
#   NasmLexer
#   NasmObjdumpLexer
#   NemerleLexer
#   NesCLexer
#   NestedTextLexer
#   NewLispLexer
#   NewspeakLexer
#   NginxConfLexer
#   NimrodLexer
#   NitLexer
#   NixLexer
#   NotmuchLexer
#   NuSMVLexer
#   NumPyLexer
#   ObjdumpLexer
#   ObjectiveCLexer
#   ObjectiveCppLexer
#   ObjectiveJLexer
#   OcamlLexer
#   OctaveLexer
#   OdinLexer
#   OmgIdlLexer
#   OocLexer
#   OpaLexer
#   OpenEdgeLexer
#   PacmanConfLexer
#   PanLexer
#   ParaSailLexer
#   PawnLexer
#   PegLexer
#   Perl6Lexer
#   PerlLexer
#   PhpLexer
#   PigLexer
#   PikeLexer
#   PkgConfigLexer
#   PlPgsqlLexer
#   PointlessLexer
#   PonyLexer
#   PostScriptLexer
#   PostgresConsoleLexer
#   PostgresLexer
#   PovrayLexer
#   PowerShellLexer
#   PowerShellSessionLexer
#   PraatLexer
#   PrologLexer
#   PromQLLexer
#   PropertiesLexer
#   ProtoBufLexer
#   PsyshConsoleLexer
#   PugLexer
#   PuppetLexer
#   PyPyLogLexer
#   Python2Lexer
#   Python2TracebackLexer
#   Python3Lexer
#   Python3TracebackLexer
#   PythonConsoleLexer
#   PythonLexer
#   PythonTracebackLexer
#   QBasicLexer
#   QVToLexer
#   QmlLexer
#   RConsoleLexer
#   RNCCompactLexer
#   RPMSpecLexer
#   RacketLexer
#   RagelCLexer
#   RagelCppLexer
#   RagelDLexer
#   RagelEmbeddedLexer
#   RagelJavaLexer
#   RagelLexer
#   RagelObjectiveCLexer
#   RagelRubyLexer
#   RawTokenLexer
#   RdLexer
#   ReasonLexer
#   RebolLexer
#   RedLexer
#   RedcodeLexer
#   RegeditLexer
#   ResourceLexer
#   RexxLexer
#   RhtmlLexer
#   RideLexer
#   RoboconfGraphLexer
#   RoboconfInstancesLexer
#   RobotFrameworkLexer
#   RqlLexer
#   RslLexer
#   RstLexer
#   RtsLexer
#   RubyConsoleLexer
#   RubyLexer
#   RustLexer
#   SASLexer
#   SLexer
#   SMLLexer
#   SarlLexer
#   SassLexer
#   ScalaLexer
#   ScamlLexer
#   ScdocLexer
#   SchemeLexer
#   ScilabLexer
#   ScssLexer
#   ShExCLexer
#   ShenLexer
#   SieveLexer
#   SilverLexer
#   SingularityLexer
#   SlashLexer
#   SlimLexer
#   SlurmBashLexer
#   SmaliLexer
#   SmalltalkLexer
#   SmartGameFormatLexer
#   SmartyLexer
#   SnobolLexer
#   SnowballLexer
#   SolidityLexer
#   SourcePawnLexer
#   SourcesListLexer
#   SparqlLexer
#   SqlLexer
#   SqliteConsoleLexer
#   SquidConfLexer
#   SspLexer
#   StanLexer
#   StataLexer
#   SuperColliderLexer
#   SwiftLexer
#   SwigLexer
#   SystemVerilogLexer
#   TAPLexer
#   TNTLexer
#   TOMLLexer
#   Tads3Lexer
#   TasmLexer
#   TclLexer
#   TcshLexer
#   TcshSessionLexer
#   TeaTemplateLexer
#   TealLexer
#   TeraTermLexer
#   TermcapLexer
#   TerminfoLexer
#   TerraformLexer
#   TexLexer
#   TextLexer
#   ThingsDBLexer
#   ThriftLexer
#   TiddlyWiki5Lexer
#   TodotxtLexer
#   TransactSqlLexer
#   TreetopLexer
#   TurtleLexer
#   TwigHtmlLexer
#   TwigLexer
#   TypeScriptLexer
#   TypoScriptCssDataLexer
#   TypoScriptHtmlDataLexer
#   TypoScriptLexer
#   UcodeLexer
#   UniconLexer
#   UrbiscriptLexer
#   UsdLexer
#   VBScriptLexer
#   VCLLexer
#   VCLSnippetLexer
#   VCTreeStatusLexer
#   VGLLexer
#   ValaLexer
#   VbNetAspxLexer
#   VbNetLexer
#   VelocityHtmlLexer
#   VelocityLexer
#   VelocityXmlLexer
#   VerilogLexer
#   VhdlLexer
#   VimLexer
#   WDiffLexer
#   WatLexer
#   WebIDLLexer
#   WhileyLexer
#   X10Lexer
#   XQueryLexer
#   XmlDjangoLexer
#   XmlErbLexer
#   XmlLexer
#   XmlPhpLexer
#   XmlSmartyLexer
#   XorgLexer
#   XsltLexer
#   XtendLexer
#   XtlangLexer
#   YamlJinjaLexer
#   YamlLexer
#   YangLexer
#   ZeekLexer
#   ZephirLexer
#   ZigLexer
#   apdlexer
