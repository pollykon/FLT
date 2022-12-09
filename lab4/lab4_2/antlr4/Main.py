# (bb(b|c)*|aa*)*
from RegParser import RegParser
from RegLexer import RegLexer
from antlr4 import *

# Чтобы порождать исключение, если строка не распозналась
class my_listener(DiagnosticErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise AssertionError

if __name__ == "__main__":
    listener = my_listener()
    inputStream = InputStream("bbbcaaabbabbbbcccaac")
    lexer = RegLexer(inputStream)
    lexer.addErrorListener(listener)
    stream = CommonTokenStream(lexer)
    parser = RegParser(stream)
    parser.addErrorListener(listener)
    try:
        parser.start()
        print('ok')
    except AssertionError as a:
        print('not ok')

