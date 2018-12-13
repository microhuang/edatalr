# -*- coding: utf-8 -*-

# Generated from EdataLr.g4 by ANTLR 4.7.1
from antlr4 import *
from EdataLrLexer import EdataLrLexer

# This class defines a complete generic visitor for a parse tree produced by EdataLrParser.

#用于预览语法解析
class EdataLrVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by EdataLrParser#Not.
    # Not
    def visitNot(self, ctx):
        return '-' + ctx.getText()


    # Visit a parse tree produced by EdataLrParser#Word.
    # Word
    def visitWord(self, ctx):
        return ctx.getText()


    # Visit a parse tree produced by EdataLrParser#Parens.
    # Parens
    def visitParens(self, ctx):
        return self.visit(ctx.expr())


    # Visit a parse tree produced by EdataLrParser#AddOr.
    # AndOr
    def visitAndOr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == EdataLrLexer.AND:
            return left + '+' + right
        else:
            return left + '|' + right


