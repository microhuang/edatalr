import sys

from antlr4 import *
from EdataLrParser import EdataLrParser
from EdataLrLexer import EdataLrLexer
from EdataLrListener import EdataLrListener
from EdataLrVisitor import EdataLrVisitor


def main(argv):
    input = FileStream(argv[1])
    lexer = EdataLrLexer(input)
    stream = CommonTokenStream(lexer)
    parser = EdataLrParser(stream)
    tree = parser.expr()
    v = EdataLrVisitor()
    print (v.visit(tree))

if __name__ == '__main__':
    main(sys.argv)




