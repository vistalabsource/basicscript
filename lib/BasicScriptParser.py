# Generated from grammar/BasicScript.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,45,227,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,5,0,40,8,0,
        10,0,12,0,43,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,70,8,1,1,
        2,1,2,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,86,8,4,
        1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,
        1,8,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,11,1,11,3,11,115,8,11,
        1,11,1,11,1,12,1,12,1,12,5,12,122,8,12,10,12,12,12,125,9,12,1,13,
        1,13,3,13,129,8,13,1,14,1,14,5,14,133,8,14,10,14,12,14,136,9,14,
        1,14,1,14,1,15,1,15,1,15,1,15,1,15,3,15,145,8,15,1,15,1,15,1,15,
        3,15,150,8,15,1,15,1,15,1,15,1,15,3,15,156,8,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,169,8,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,5,15,202,8,15,10,15,12,15,205,9,15,1,16,1,16,1,16,5,
        16,210,8,16,10,16,12,16,213,9,16,1,17,1,17,1,17,5,17,218,8,17,10,
        17,12,17,221,9,17,1,18,1,18,1,18,1,18,1,18,0,1,30,19,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,0,4,1,0,20,21,1,0,22,25,1,
        0,28,29,1,0,30,31,249,0,41,1,0,0,0,2,69,1,0,0,0,4,71,1,0,0,0,6,76,
        1,0,0,0,8,78,1,0,0,0,10,87,1,0,0,0,12,91,1,0,0,0,14,97,1,0,0,0,16,
        103,1,0,0,0,18,106,1,0,0,0,20,108,1,0,0,0,22,110,1,0,0,0,24,118,
        1,0,0,0,26,126,1,0,0,0,28,130,1,0,0,0,30,168,1,0,0,0,32,206,1,0,
        0,0,34,214,1,0,0,0,36,222,1,0,0,0,38,40,3,2,1,0,39,38,1,0,0,0,40,
        43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,44,1,0,0,0,43,41,1,0,0,
        0,44,45,5,0,0,1,45,1,1,0,0,0,46,47,3,4,2,0,47,48,5,1,0,0,48,70,1,
        0,0,0,49,50,3,6,3,0,50,51,5,1,0,0,51,70,1,0,0,0,52,70,3,8,4,0,53,
        70,3,10,5,0,54,70,3,12,6,0,55,70,3,14,7,0,56,57,3,16,8,0,57,58,5,
        1,0,0,58,70,1,0,0,0,59,60,3,18,9,0,60,61,5,1,0,0,61,70,1,0,0,0,62,
        63,3,20,10,0,63,64,5,1,0,0,64,70,1,0,0,0,65,70,3,22,11,0,66,67,3,
        26,13,0,67,68,5,1,0,0,68,70,1,0,0,0,69,46,1,0,0,0,69,49,1,0,0,0,
        69,52,1,0,0,0,69,53,1,0,0,0,69,54,1,0,0,0,69,55,1,0,0,0,69,56,1,
        0,0,0,69,59,1,0,0,0,69,62,1,0,0,0,69,65,1,0,0,0,69,66,1,0,0,0,70,
        3,1,0,0,0,71,72,5,2,0,0,72,73,5,39,0,0,73,74,5,3,0,0,74,75,3,30,
        15,0,75,5,1,0,0,0,76,77,3,30,15,0,77,7,1,0,0,0,78,79,5,4,0,0,79,
        80,3,30,15,0,80,85,3,28,14,0,81,82,5,38,0,0,82,86,3,28,14,0,83,84,
        5,38,0,0,84,86,3,8,4,0,85,81,1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,
        86,9,1,0,0,0,87,88,5,5,0,0,88,89,3,30,15,0,89,90,3,28,14,0,90,11,
        1,0,0,0,91,92,5,6,0,0,92,93,5,39,0,0,93,94,5,3,0,0,94,95,3,30,15,
        0,95,96,3,28,14,0,96,13,1,0,0,0,97,98,5,7,0,0,98,99,3,28,14,0,99,
        100,5,8,0,0,100,101,5,39,0,0,101,102,3,28,14,0,102,15,1,0,0,0,103,
        104,5,9,0,0,104,105,3,30,15,0,105,17,1,0,0,0,106,107,5,10,0,0,107,
        19,1,0,0,0,108,109,5,11,0,0,109,21,1,0,0,0,110,111,5,12,0,0,111,
        114,5,39,0,0,112,113,5,3,0,0,113,115,3,24,12,0,114,112,1,0,0,0,114,
        115,1,0,0,0,115,116,1,0,0,0,116,117,3,28,14,0,117,23,1,0,0,0,118,
        123,5,39,0,0,119,120,5,13,0,0,120,122,5,39,0,0,121,119,1,0,0,0,122,
        125,1,0,0,0,123,121,1,0,0,0,123,124,1,0,0,0,124,25,1,0,0,0,125,123,
        1,0,0,0,126,128,5,14,0,0,127,129,3,30,15,0,128,127,1,0,0,0,128,129,
        1,0,0,0,129,27,1,0,0,0,130,134,5,15,0,0,131,133,3,2,1,0,132,131,
        1,0,0,0,133,136,1,0,0,0,134,132,1,0,0,0,134,135,1,0,0,0,135,137,
        1,0,0,0,136,134,1,0,0,0,137,138,5,16,0,0,138,29,1,0,0,0,139,140,
        6,15,-1,0,140,141,5,19,0,0,141,169,3,30,15,19,142,144,5,26,0,0,143,
        145,3,32,16,0,144,143,1,0,0,0,144,145,1,0,0,0,145,146,1,0,0,0,146,
        169,5,27,0,0,147,149,5,15,0,0,148,150,3,34,17,0,149,148,1,0,0,0,
        149,150,1,0,0,0,150,151,1,0,0,0,151,169,5,16,0,0,152,153,5,39,0,
        0,153,155,5,34,0,0,154,156,3,32,16,0,155,154,1,0,0,0,155,156,1,0,
        0,0,156,157,1,0,0,0,157,169,5,35,0,0,158,169,5,42,0,0,159,169,5,
        40,0,0,160,169,5,41,0,0,161,169,5,36,0,0,162,169,5,37,0,0,163,169,
        5,39,0,0,164,165,5,34,0,0,165,166,3,30,15,0,166,167,5,35,0,0,167,
        169,1,0,0,0,168,139,1,0,0,0,168,142,1,0,0,0,168,147,1,0,0,0,168,
        152,1,0,0,0,168,158,1,0,0,0,168,159,1,0,0,0,168,160,1,0,0,0,168,
        161,1,0,0,0,168,162,1,0,0,0,168,163,1,0,0,0,168,164,1,0,0,0,169,
        203,1,0,0,0,170,171,10,21,0,0,171,172,5,17,0,0,172,202,3,30,15,22,
        173,174,10,20,0,0,174,175,5,18,0,0,175,202,3,30,15,21,176,177,10,
        18,0,0,177,178,7,0,0,0,178,202,3,30,15,19,179,180,10,17,0,0,180,
        181,7,1,0,0,181,202,3,30,15,18,182,183,10,13,0,0,183,184,7,2,0,0,
        184,202,3,30,15,14,185,186,10,12,0,0,186,187,7,3,0,0,187,202,3,30,
        15,13,188,189,10,11,0,0,189,190,5,32,0,0,190,202,3,30,15,12,191,
        192,10,10,0,0,192,193,5,33,0,0,193,202,3,30,15,11,194,195,10,16,
        0,0,195,196,5,26,0,0,196,197,3,30,15,0,197,198,5,27,0,0,198,202,
        1,0,0,0,199,200,10,9,0,0,200,202,5,39,0,0,201,170,1,0,0,0,201,173,
        1,0,0,0,201,176,1,0,0,0,201,179,1,0,0,0,201,182,1,0,0,0,201,185,
        1,0,0,0,201,188,1,0,0,0,201,191,1,0,0,0,201,194,1,0,0,0,201,199,
        1,0,0,0,202,205,1,0,0,0,203,201,1,0,0,0,203,204,1,0,0,0,204,31,1,
        0,0,0,205,203,1,0,0,0,206,211,3,30,15,0,207,208,5,13,0,0,208,210,
        3,30,15,0,209,207,1,0,0,0,210,213,1,0,0,0,211,209,1,0,0,0,211,212,
        1,0,0,0,212,33,1,0,0,0,213,211,1,0,0,0,214,219,3,36,18,0,215,216,
        5,13,0,0,216,218,3,36,18,0,217,215,1,0,0,0,218,221,1,0,0,0,219,217,
        1,0,0,0,219,220,1,0,0,0,220,35,1,0,0,0,221,219,1,0,0,0,222,223,5,
        41,0,0,223,224,5,3,0,0,224,225,3,30,15,0,225,37,1,0,0,0,15,41,69,
        85,114,123,128,134,144,149,155,168,201,203,211,219
    ]

class BasicScriptParser ( Parser ):

    grammarFileName = "BasicScript.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'let'", "':'", "'if'", "'while'", 
                     "'for'", "'try'", "'catch'", "'throw'", "'break'", 
                     "'continue'", "'function'", "','", "'return'", "'{'", 
                     "'}'", "'||'", "'&&'", "'!'", "'=='", "'!='", "'<'", 
                     "'<='", "'>'", "'>='", "'['", "']'", "'+'", "'-'", 
                     "'*'", "'/'", "'^'", "'%'", "'('", "')'", "'True'", 
                     "'False'", "'else'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ELSE", "ID", "FLOAT", "STRING", 
                      "INT", "WS", "COMMENT", "LINE_COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assign = 2
    RULE_expr_s = 3
    RULE_if = 4
    RULE_while = 5
    RULE_for = 6
    RULE_try_catch = 7
    RULE_throw = 8
    RULE_break = 9
    RULE_continue = 10
    RULE_function = 11
    RULE_param_list = 12
    RULE_return = 13
    RULE_block = 14
    RULE_expr = 15
    RULE_arg_list = 16
    RULE_pair_list = 17
    RULE_pair = 18

    ruleNames =  [ "program", "statement", "assign", "expr_s", "if", "while", 
                   "for", "try_catch", "throw", "break", "continue", "function", 
                   "param_list", "return", "block", "expr", "arg_list", 
                   "pair_list", "pair" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    ELSE=38
    ID=39
    FLOAT=40
    STRING=41
    INT=42
    WS=43
    COMMENT=44
    LINE_COMMENT=45

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BasicScriptParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicScriptParser.StatementContext)
            else:
                return self.getTypedRuleContext(BasicScriptParser.StatementContext,i)


        def getRuleIndex(self):
            return BasicScriptParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BasicScriptParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8469743197940) != 0):
                self.state = 38
                self.statement()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
            self.match(BasicScriptParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(BasicScriptParser.AssignContext,0)


        def expr_s(self):
            return self.getTypedRuleContext(BasicScriptParser.Expr_sContext,0)


        def if_(self):
            return self.getTypedRuleContext(BasicScriptParser.IfContext,0)


        def while_(self):
            return self.getTypedRuleContext(BasicScriptParser.WhileContext,0)


        def for_(self):
            return self.getTypedRuleContext(BasicScriptParser.ForContext,0)


        def try_catch(self):
            return self.getTypedRuleContext(BasicScriptParser.Try_catchContext,0)


        def throw(self):
            return self.getTypedRuleContext(BasicScriptParser.ThrowContext,0)


        def break_(self):
            return self.getTypedRuleContext(BasicScriptParser.BreakContext,0)


        def continue_(self):
            return self.getTypedRuleContext(BasicScriptParser.ContinueContext,0)


        def function(self):
            return self.getTypedRuleContext(BasicScriptParser.FunctionContext,0)


        def return_(self):
            return self.getTypedRuleContext(BasicScriptParser.ReturnContext,0)


        def getRuleIndex(self):
            return BasicScriptParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = BasicScriptParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.assign()
                self.state = 47
                self.match(BasicScriptParser.T__0)
                pass
            elif token in [15, 19, 26, 34, 36, 37, 39, 40, 41, 42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.expr_s()
                self.state = 50
                self.match(BasicScriptParser.T__0)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.if_()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 53
                self.while_()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 5)
                self.state = 54
                self.for_()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 6)
                self.state = 55
                self.try_catch()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 7)
                self.state = 56
                self.throw()
                self.state = 57
                self.match(BasicScriptParser.T__0)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 8)
                self.state = 59
                self.break_()
                self.state = 60
                self.match(BasicScriptParser.T__0)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 9)
                self.state = 62
                self.continue_()
                self.state = 63
                self.match(BasicScriptParser.T__0)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 10)
                self.state = 65
                self.function()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 11)
                self.state = 66
                self.return_()
                self.state = 67
                self.match(BasicScriptParser.T__0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BasicScriptParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(BasicScriptParser.ExprContext,0)


        def getRuleIndex(self):
            return BasicScriptParser.RULE_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = BasicScriptParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(BasicScriptParser.T__1)
            self.state = 72
            self.match(BasicScriptParser.ID)
            self.state = 73
            self.match(BasicScriptParser.T__2)
            self.state = 74
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_sContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BasicScriptParser.ExprContext,0)


        def getRuleIndex(self):
            return BasicScriptParser.RULE_expr_s

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_s" ):
                return visitor.visitExpr_s(self)
            else:
                return visitor.visitChildren(self)




    def expr_s(self):

        localctx = BasicScriptParser.Expr_sContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BasicScriptParser.ExprContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicScriptParser.BlockContext)
            else:
                return self.getTypedRuleContext(BasicScriptParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(BasicScriptParser.ELSE, 0)

        def if_(self):
            return self.getTypedRuleContext(BasicScriptParser.IfContext,0)


        def getRuleIndex(self):
            return BasicScriptParser.RULE_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)




    def if_(self):

        localctx = BasicScriptParser.IfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(BasicScriptParser.T__3)
            self.state = 79
            self.expr(0)
            self.state = 80
            self.block()
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 81
                self.match(BasicScriptParser.ELSE)
                self.state = 82
                self.block()

            elif la_ == 2:
                self.state = 83
                self.match(BasicScriptParser.ELSE)
                self.state = 84
                self.if_()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BasicScriptParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(BasicScriptParser.BlockContext,0)


        def getRuleIndex(self):
            return BasicScriptParser.RULE_while

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)




    def while_(self):

        localctx = BasicScriptParser.WhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(BasicScriptParser.T__4)
            self.state = 88
            self.expr(0)
            self.state = 89
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BasicScriptParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(BasicScriptParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(BasicScriptParser.BlockContext,0)


        def getRuleIndex(self):
            return BasicScriptParser.RULE_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor" ):
                return visitor.visitFor(self)
            else:
                return visitor.visitChildren(self)




    def for_(self):

        localctx = BasicScriptParser.ForContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(BasicScriptParser.T__5)
            self.state = 92
            self.match(BasicScriptParser.ID)
            self.state = 93
            self.match(BasicScriptParser.T__2)
            self.state = 94
            self.expr(0)
            self.state = 95
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Try_catchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicScriptParser.BlockContext)
            else:
                return self.getTypedRuleContext(BasicScriptParser.BlockContext,i)


        def ID(self):
            return self.getToken(BasicScriptParser.ID, 0)

        def getRuleIndex(self):
            return BasicScriptParser.RULE_try_catch

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTry_catch" ):
                return visitor.visitTry_catch(self)
            else:
                return visitor.visitChildren(self)




    def try_catch(self):

        localctx = BasicScriptParser.Try_catchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_try_catch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(BasicScriptParser.T__6)
            self.state = 98
            self.block()
            self.state = 99
            self.match(BasicScriptParser.T__7)
            self.state = 100
            self.match(BasicScriptParser.ID)
            self.state = 101
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ThrowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BasicScriptParser.ExprContext,0)


        def getRuleIndex(self):
            return BasicScriptParser.RULE_throw

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThrow" ):
                return visitor.visitThrow(self)
            else:
                return visitor.visitChildren(self)




    def throw(self):

        localctx = BasicScriptParser.ThrowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_throw)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(BasicScriptParser.T__8)
            self.state = 104
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BasicScriptParser.RULE_break

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak" ):
                return visitor.visitBreak(self)
            else:
                return visitor.visitChildren(self)




    def break_(self):

        localctx = BasicScriptParser.BreakContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(BasicScriptParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BasicScriptParser.RULE_continue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue" ):
                return visitor.visitContinue(self)
            else:
                return visitor.visitChildren(self)




    def continue_(self):

        localctx = BasicScriptParser.ContinueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(BasicScriptParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BasicScriptParser.ID, 0)

        def block(self):
            return self.getTypedRuleContext(BasicScriptParser.BlockContext,0)


        def param_list(self):
            return self.getTypedRuleContext(BasicScriptParser.Param_listContext,0)


        def getRuleIndex(self):
            return BasicScriptParser.RULE_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = BasicScriptParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(BasicScriptParser.T__11)
            self.state = 111
            self.match(BasicScriptParser.ID)
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 112
                self.match(BasicScriptParser.T__2)
                self.state = 113
                self.param_list()


            self.state = 116
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BasicScriptParser.ID)
            else:
                return self.getToken(BasicScriptParser.ID, i)

        def getRuleIndex(self):
            return BasicScriptParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = BasicScriptParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(BasicScriptParser.ID)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 119
                self.match(BasicScriptParser.T__12)
                self.state = 120
                self.match(BasicScriptParser.ID)
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BasicScriptParser.ExprContext,0)


        def getRuleIndex(self):
            return BasicScriptParser.RULE_return

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn" ):
                return visitor.visitReturn(self)
            else:
                return visitor.visitChildren(self)




    def return_(self):

        localctx = BasicScriptParser.ReturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_return)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(BasicScriptParser.T__13)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8469743173632) != 0):
                self.state = 127
                self.expr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicScriptParser.StatementContext)
            else:
                return self.getTypedRuleContext(BasicScriptParser.StatementContext,i)


        def getRuleIndex(self):
            return BasicScriptParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = BasicScriptParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(BasicScriptParser.T__14)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8469743197940) != 0):
                self.state = 131
                self.statement()
                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 137
            self.match(BasicScriptParser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BasicScriptParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class OrContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(BasicScriptParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr" ):
                return visitor.visitOr(self)
            else:
                return visitor.visitChildren(self)


    class ModContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(BasicScriptParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMod" ):
                return visitor.visitMod(self)
            else:
                return visitor.visitChildren(self)


    class MulImpliedContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(BasicScriptParser.ExprContext,0)

        def ID(self):
            return self.getToken(BasicScriptParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulImplied" ):
                return visitor.visitMulImplied(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicScriptParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(BasicScriptParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicScriptParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(BasicScriptParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(BasicScriptParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class TrueContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrue" ):
                return visitor.visitTrue(self)
            else:
                return visitor.visitChildren(self)


    class IndexContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(BasicScriptParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex" ):
                return visitor.visitIndex(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(BasicScriptParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class FalseContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFalse" ):
                return visitor.visitFalse(self)
            else:
                return visitor.visitChildren(self)


    class EqContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(BasicScriptParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEq" ):
                return visitor.visitEq(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(BasicScriptParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)


    class ArrayContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arg_list(self):
            return self.getTypedRuleContext(BasicScriptParser.Arg_listContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)


    class FuncCallContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(BasicScriptParser.ID, 0)
        def arg_list(self):
            return self.getTypedRuleContext(BasicScriptParser.Arg_listContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCall" ):
                return visitor.visitFuncCall(self)
            else:
                return visitor.visitChildren(self)


    class FloatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(BasicScriptParser.FLOAT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat" ):
                return visitor.visitFloat(self)
            else:
                return visitor.visitChildren(self)


    class NotContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(BasicScriptParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot" ):
                return visitor.visitNot(self)
            else:
                return visitor.visitChildren(self)


    class DictContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def pair_list(self):
            return self.getTypedRuleContext(BasicScriptParser.Pair_listContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDict" ):
                return visitor.visitDict(self)
            else:
                return visitor.visitChildren(self)


    class AndContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(BasicScriptParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd" ):
                return visitor.visitAnd(self)
            else:
                return visitor.visitChildren(self)


    class RelContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(BasicScriptParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRel" ):
                return visitor.visitRel(self)
            else:
                return visitor.visitChildren(self)


    class PowContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(BasicScriptParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPow" ):
                return visitor.visitPow(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicScriptParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(BasicScriptParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BasicScriptParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = BasicScriptParser.NotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 140
                self.match(BasicScriptParser.T__18)
                self.state = 141
                self.expr(19)
                pass

            elif la_ == 2:
                localctx = BasicScriptParser.ArrayContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 142
                self.match(BasicScriptParser.T__25)
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8469743173632) != 0):
                    self.state = 143
                    self.arg_list()


                self.state = 146
                self.match(BasicScriptParser.T__26)
                pass

            elif la_ == 3:
                localctx = BasicScriptParser.DictContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 147
                self.match(BasicScriptParser.T__14)
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==41:
                    self.state = 148
                    self.pair_list()


                self.state = 151
                self.match(BasicScriptParser.T__15)
                pass

            elif la_ == 4:
                localctx = BasicScriptParser.FuncCallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 152
                self.match(BasicScriptParser.ID)
                self.state = 153
                self.match(BasicScriptParser.T__33)
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8469743173632) != 0):
                    self.state = 154
                    self.arg_list()


                self.state = 157
                self.match(BasicScriptParser.T__34)
                pass

            elif la_ == 5:
                localctx = BasicScriptParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 158
                self.match(BasicScriptParser.INT)
                pass

            elif la_ == 6:
                localctx = BasicScriptParser.FloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 159
                self.match(BasicScriptParser.FLOAT)
                pass

            elif la_ == 7:
                localctx = BasicScriptParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 160
                self.match(BasicScriptParser.STRING)
                pass

            elif la_ == 8:
                localctx = BasicScriptParser.TrueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 161
                self.match(BasicScriptParser.T__35)
                pass

            elif la_ == 9:
                localctx = BasicScriptParser.FalseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 162
                self.match(BasicScriptParser.T__36)
                pass

            elif la_ == 10:
                localctx = BasicScriptParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 163
                self.match(BasicScriptParser.ID)
                pass

            elif la_ == 11:
                localctx = BasicScriptParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 164
                self.match(BasicScriptParser.T__33)
                self.state = 165
                self.expr(0)
                self.state = 166
                self.match(BasicScriptParser.T__34)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 203
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 201
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = BasicScriptParser.OrContext(self, BasicScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 170
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 171
                        self.match(BasicScriptParser.T__16)
                        self.state = 172
                        self.expr(22)
                        pass

                    elif la_ == 2:
                        localctx = BasicScriptParser.AndContext(self, BasicScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 173
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 174
                        self.match(BasicScriptParser.T__17)
                        self.state = 175
                        self.expr(21)
                        pass

                    elif la_ == 3:
                        localctx = BasicScriptParser.EqContext(self, BasicScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 176
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 177
                        _la = self._input.LA(1)
                        if not(_la==20 or _la==21):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 178
                        self.expr(19)
                        pass

                    elif la_ == 4:
                        localctx = BasicScriptParser.RelContext(self, BasicScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 179
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 180
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 62914560) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 181
                        self.expr(18)
                        pass

                    elif la_ == 5:
                        localctx = BasicScriptParser.AddSubContext(self, BasicScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 182
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 183
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==28 or _la==29):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 184
                        self.expr(14)
                        pass

                    elif la_ == 6:
                        localctx = BasicScriptParser.MulDivContext(self, BasicScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 185
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 186
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==30 or _la==31):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 187
                        self.expr(13)
                        pass

                    elif la_ == 7:
                        localctx = BasicScriptParser.PowContext(self, BasicScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 188
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 189
                        self.match(BasicScriptParser.T__31)
                        self.state = 190
                        self.expr(12)
                        pass

                    elif la_ == 8:
                        localctx = BasicScriptParser.ModContext(self, BasicScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 191
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 192
                        self.match(BasicScriptParser.T__32)
                        self.state = 193
                        self.expr(11)
                        pass

                    elif la_ == 9:
                        localctx = BasicScriptParser.IndexContext(self, BasicScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 194
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 195
                        self.match(BasicScriptParser.T__25)
                        self.state = 196
                        self.expr(0)
                        self.state = 197
                        self.match(BasicScriptParser.T__26)
                        pass

                    elif la_ == 10:
                        localctx = BasicScriptParser.MulImpliedContext(self, BasicScriptParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 199
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 200
                        self.match(BasicScriptParser.ID)
                        pass

             
                self.state = 205
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Arg_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicScriptParser.ExprContext)
            else:
                return self.getTypedRuleContext(BasicScriptParser.ExprContext,i)


        def getRuleIndex(self):
            return BasicScriptParser.RULE_arg_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg_list" ):
                return visitor.visitArg_list(self)
            else:
                return visitor.visitChildren(self)




    def arg_list(self):

        localctx = BasicScriptParser.Arg_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_arg_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.expr(0)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 207
                self.match(BasicScriptParser.T__12)
                self.state = 208
                self.expr(0)
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pair_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicScriptParser.PairContext)
            else:
                return self.getTypedRuleContext(BasicScriptParser.PairContext,i)


        def getRuleIndex(self):
            return BasicScriptParser.RULE_pair_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPair_list" ):
                return visitor.visitPair_list(self)
            else:
                return visitor.visitChildren(self)




    def pair_list(self):

        localctx = BasicScriptParser.Pair_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_pair_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.pair()
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 215
                self.match(BasicScriptParser.T__12)
                self.state = 216
                self.pair()
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(BasicScriptParser.STRING, 0)

        def expr(self):
            return self.getTypedRuleContext(BasicScriptParser.ExprContext,0)


        def getRuleIndex(self):
            return BasicScriptParser.RULE_pair

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPair" ):
                return visitor.visitPair(self)
            else:
                return visitor.visitChildren(self)




    def pair(self):

        localctx = BasicScriptParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(BasicScriptParser.STRING)
            self.state = 223
            self.match(BasicScriptParser.T__2)
            self.state = 224
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[15] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 9)
         




