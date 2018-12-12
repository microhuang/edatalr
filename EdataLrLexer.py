# Generated from EdataLr.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2")
        buf.write(u"\t\60\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\3\2\3\2\3\3\3\3\3\4\6\4\27\n\4\r\4\16\4")
        buf.write(u"\30\3\4\3\4\3\4\6\4\36\n\4\r\4\16\4\37\5\4\"\n\4\3\5")
        buf.write(u"\3\5\3\6\3\6\3\7\3\7\3\b\6\b+\n\b\r\b\16\b,\3\b\3\b\2")
        buf.write(u"\2\t\3\3\5\4\7\5\t\6\13\7\r\b\17\t\3\2\6\4\2C\\c|\5\2")
        buf.write(u"eevv~~\3\2<<\5\2\13\f\17\17\"\"\2\63\2\3\3\2\2\2\2\5")
        buf.write(u"\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write(u"\2\2\2\17\3\2\2\2\3\21\3\2\2\2\5\23\3\2\2\2\7!\3\2\2")
        buf.write(u"\2\t#\3\2\2\2\13%\3\2\2\2\r\'\3\2\2\2\17*\3\2\2\2\21")
        buf.write(u"\22\7*\2\2\22\4\3\2\2\2\23\24\7+\2\2\24\6\3\2\2\2\25")
        buf.write(u"\27\t\2\2\2\26\25\3\2\2\2\27\30\3\2\2\2\30\26\3\2\2\2")
        buf.write(u"\30\31\3\2\2\2\31\"\3\2\2\2\32\33\t\3\2\2\33\35\t\4\2")
        buf.write(u"\2\34\36\t\2\2\2\35\34\3\2\2\2\36\37\3\2\2\2\37\35\3")
        buf.write(u"\2\2\2\37 \3\2\2\2 \"\3\2\2\2!\26\3\2\2\2!\32\3\2\2\2")
        buf.write(u"\"\b\3\2\2\2#$\7-\2\2$\n\3\2\2\2%&\7~\2\2&\f\3\2\2\2")
        buf.write(u"\'(\7/\2\2(\16\3\2\2\2)+\t\5\2\2*)\3\2\2\2+,\3\2\2\2")
        buf.write(u",*\3\2\2\2,-\3\2\2\2-.\3\2\2\2./\b\b\2\2/\20\3\2\2\2")
        buf.write(u"\7\2\30\37!,\3\b\2\2")
        return buf.getvalue()


class EdataLrLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    WORD = 3
    AND = 4
    OR = 5
    NOT = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'('", u"')'", u"'+'", u"'|'", u"'-'" ]

    symbolicNames = [ u"<INVALID>",
            u"WORD", u"AND", u"OR", u"NOT", u"WS" ]

    ruleNames = [ u"T__0", u"T__1", u"WORD", u"AND", u"OR", u"NOT", u"WS" ]

    grammarFileName = u"EdataLr.g4"

    def __init__(self, input=None, output=sys.stdout):
        super(EdataLrLexer, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


