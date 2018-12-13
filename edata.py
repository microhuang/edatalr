# -*- coding:utf-8 -*-


import sys

from antlr4 import *
from EdataLrParser import EdataLrParser
from EdataLrLexer import EdataLrLexer
from EdataLrListener import EdataLrListener
from EdataLrVisitor import EdataLrVisitor
from EdataLrSearch import EdataLrSearch
from EdataLrSpider import EdataLrSpider


def main(argv):
    #input = FileStream(argv[1], encoding='utf8')
    input = InputStream('(zhangsan) | (((c:linke) | (t:wangwu)) + (lisi))')
    lexer = EdataLrLexer(input)
    stream = CommonTokenStream(lexer)
    parser = EdataLrParser(stream)
    tree = parser.expr()

    v = EdataLrVisitor()
    print (v.visit(tree))

    v = EdataLrSearch()
    print (v.visit(tree))

    v = EdataLrSpider()
    print (v.visit(tree))

if __name__ == '__main__':
    main(sys.argv)




