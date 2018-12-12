# Generated from EdataLr.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\t\27\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\r\n")
        buf.write(u"\2\3\2\3\2\3\2\7\2\22\n\2\f\2\16\2\25\13\2\3\2\2\3\2")
        buf.write(u"\3\2\2\3\3\2\6\7\2\30\2\f\3\2\2\2\4\5\b\2\1\2\5\r\7\5")
        buf.write(u"\2\2\6\7\7\3\2\2\7\b\5\2\2\2\b\t\7\4\2\2\t\r\3\2\2\2")
        buf.write(u"\n\13\7\b\2\2\13\r\7\5\2\2\f\4\3\2\2\2\f\6\3\2\2\2\f")
        buf.write(u"\n\3\2\2\2\r\23\3\2\2\2\16\17\f\6\2\2\17\20\t\2\2\2\20")
        buf.write(u"\22\5\2\2\7\21\16\3\2\2\2\22\25\3\2\2\2\23\21\3\2\2\2")
        buf.write(u"\23\24\3\2\2\2\24\3\3\2\2\2\25\23\3\2\2\2\4\f\23")
        return buf.getvalue()


class EdataLrParser ( Parser ):

    grammarFileName = "EdataLr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'('", u"')'", u"<INVALID>", u"'+'", 
                     u"'|'", u"'-'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"WORD", 
                      u"AND", u"OR", u"NOT", u"WS" ]

    RULE_expr = 0

    ruleNames =  [ u"expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    WORD=3
    AND=4
    OR=5
    NOT=6
    WS=7

    def __init__(self, input, output=sys.stdout):
        super(EdataLrParser, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(EdataLrParser.ExprContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EdataLrParser.RULE_expr

     
        def copyFrom(self, ctx):
            super(EdataLrParser.ExprContext, self).copyFrom(ctx)


    class NotContext(ExprContext):

        def __init__(self, parser, ctx): # actually a EdataLrParser.ExprContext)
            super(EdataLrParser.NotContext, self).__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def WORD(self):
            return self.getToken(EdataLrParser.WORD, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterNot"):
                listener.enterNot(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNot"):
                listener.exitNot(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitNot"):
                return visitor.visitNot(self)
            else:
                return visitor.visitChildren(self)


    class WordContext(ExprContext):

        def __init__(self, parser, ctx): # actually a EdataLrParser.ExprContext)
            super(EdataLrParser.WordContext, self).__init__(parser)
            self.copyFrom(ctx)

        def WORD(self):
            return self.getToken(EdataLrParser.WORD, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterWord"):
                listener.enterWord(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWord"):
                listener.exitWord(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitWord"):
                return visitor.visitWord(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx): # actually a EdataLrParser.ExprContext)
            super(EdataLrParser.ParensContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(EdataLrParser.ExprContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterParens"):
                listener.enterParens(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitParens"):
                listener.exitParens(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitParens"):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class AndOrContext(ExprContext):

        def __init__(self, parser, ctx): # actually a EdataLrParser.ExprContext)
            super(EdataLrParser.AndOrContext, self).__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(EdataLrParser.ExprContext)
            else:
                return self.getTypedRuleContext(EdataLrParser.ExprContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterAndOr"):
                listener.enterAndOr(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAndOr"):
                listener.exitAndOr(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitAndOr"):
                return visitor.visitAndOr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EdataLrParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EdataLrParser.WORD]:
                localctx = EdataLrParser.WordContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 3
                self.match(EdataLrParser.WORD)
                pass
            elif token in [EdataLrParser.T__0]:
                localctx = EdataLrParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 4
                self.match(EdataLrParser.T__0)
                self.state = 5
                self.expr(0)
                self.state = 6
                self.match(EdataLrParser.T__1)
                pass
            elif token in [EdataLrParser.NOT]:
                localctx = EdataLrParser.NotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 8
                localctx.op = self.match(EdataLrParser.NOT)
                self.state = 9
                self.match(EdataLrParser.WORD)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 17
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = EdataLrParser.AndOrContext(self, EdataLrParser.ExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 12
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 13
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==EdataLrParser.AND or _la==EdataLrParser.OR):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 14
                    self.expr(5) 
                self.state = 19
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         




