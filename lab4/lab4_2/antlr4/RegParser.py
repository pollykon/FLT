# Generated from Reg.g4 by ANTLR 4.11.1
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
        4,1,3,35,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,0,1,0,3,0,
        14,8,0,1,1,1,1,1,1,1,1,1,1,3,1,21,8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,3,3,33,8,3,1,3,0,0,4,0,2,4,6,0,0,37,0,13,1,0,0,0,2,
        20,1,0,0,0,4,22,1,0,0,0,6,32,1,0,0,0,8,9,5,1,0,0,9,14,3,2,1,0,10,
        11,5,2,0,0,11,14,3,4,2,0,12,14,5,0,0,1,13,8,1,0,0,0,13,10,1,0,0,
        0,13,12,1,0,0,0,14,1,1,0,0,0,15,16,5,1,0,0,16,21,3,2,1,0,17,18,5,
        2,0,0,18,21,3,4,2,0,19,21,5,0,0,1,20,15,1,0,0,0,20,17,1,0,0,0,20,
        19,1,0,0,0,21,3,1,0,0,0,22,23,5,2,0,0,23,24,3,6,3,0,24,5,1,0,0,0,
        25,26,5,1,0,0,26,33,3,2,1,0,27,28,5,2,0,0,28,33,3,6,3,0,29,30,5,
        3,0,0,30,33,3,6,3,0,31,33,5,0,0,1,32,25,1,0,0,0,32,27,1,0,0,0,32,
        29,1,0,0,0,32,31,1,0,0,0,33,7,1,0,0,0,3,13,20,32
    ]

class RegParser ( Parser ):

    grammarFileName = "Reg.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'a'", "'b'", "'c'" ]

    symbolicNames = [  ]

    RULE_start = 0
    RULE_a = 1
    RULE_b = 2
    RULE_c = 3

    ruleNames =  [ "start", "a", "b", "c" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def a(self):
            return self.getTypedRuleContext(RegParser.AContext,0)


        def b(self):
            return self.getTypedRuleContext(RegParser.BContext,0)


        def EOF(self):
            return self.getToken(RegParser.EOF, 0)

        def getRuleIndex(self):
            return RegParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = RegParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.state = 13
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.match(RegParser.T__0)
                self.state = 9
                self.a()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 10
                self.match(RegParser.T__1)
                self.state = 11
                self.b()
                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 12
                self.match(RegParser.EOF)
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


    class AContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def a(self):
            return self.getTypedRuleContext(RegParser.AContext,0)


        def b(self):
            return self.getTypedRuleContext(RegParser.BContext,0)


        def EOF(self):
            return self.getToken(RegParser.EOF, 0)

        def getRuleIndex(self):
            return RegParser.RULE_a

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterA" ):
                listener.enterA(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitA" ):
                listener.exitA(self)




    def a(self):

        localctx = RegParser.AContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_a)
        try:
            self.state = 20
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.match(RegParser.T__0)
                self.state = 16
                self.a()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 17
                self.match(RegParser.T__1)
                self.state = 18
                self.b()
                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 19
                self.match(RegParser.EOF)
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


    class BContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def c(self):
            return self.getTypedRuleContext(RegParser.CContext,0)


        def getRuleIndex(self):
            return RegParser.RULE_b

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterB" ):
                listener.enterB(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitB" ):
                listener.exitB(self)




    def b(self):

        localctx = RegParser.BContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_b)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(RegParser.T__1)
            self.state = 23
            self.c()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def a(self):
            return self.getTypedRuleContext(RegParser.AContext,0)


        def c(self):
            return self.getTypedRuleContext(RegParser.CContext,0)


        def EOF(self):
            return self.getToken(RegParser.EOF, 0)

        def getRuleIndex(self):
            return RegParser.RULE_c

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterC" ):
                listener.enterC(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitC" ):
                listener.exitC(self)




    def c(self):

        localctx = RegParser.CContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_c)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.match(RegParser.T__0)
                self.state = 26
                self.a()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.match(RegParser.T__1)
                self.state = 28
                self.c()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.match(RegParser.T__2)
                self.state = 30
                self.c()
                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 4)
                self.state = 31
                self.match(RegParser.EOF)
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





