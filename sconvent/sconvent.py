import sys
import json
from pathlib import Path
from pprint import pprint
from sly import Lexer, Parser

'''
derectives ::= derective derectives | empty
derective ::= "(" + datas + ")"
datas ::= data datas | empty
data ::= WORD | DIGITS | STR | derective
'''

class SLexer(Lexer):
    tokens = {STCH, ENDCH, WORD, DIGITS, STR}
   
    ignore = r' \t'
    ignore_comment = r'\#.*'
    ignore_newline = r'\n+'

    STCH = r'\('
    DIGITS = r'[0-9][^ \(\)\t\n\.\$]+'
    WORD = r'[^ A-Z\(\)0-9\.\t\n\_\$]+'
    STR = r'[^ \(\)\t]+'
    ENDCH = r'\)' 

class SParser(Parser):
    tokens = SLexer.tokens

    @_('derective derectives')
    def derectives(self, p):
        return [p.derective] + p.derectives

    @_('empty')
    def derectives(self, p):
        return []

    @_('STCH datas ENDCH')
    def derective(self, p):
        return dict(type='der', args=[p.datas], ctx = [])
        #return [p.STCH] + [p.datas] + [p.ENDCH]

    @_('data datas')
    def datas(self, p):
        return [p.data] + p.datas

    @_('derective')
    def data(self, p):
        return p.derective

    @_('WORD')
    def data(self, p):
        return [p.WORD]

    @_('STR')
    def data(self, p):
        return [p.STR]

    @_('DIGITS')
    def data(self, p):
        return [p.DIGITS]

    @_('empty')
    def datas(self, p):
        return []

    @_('')
    def empty(self, p):
        pass


if __name__ == '__main__':
    try:
        file = open(sys.argv[1], 'r')
    except IOError:
        print("Ошибка открытия файла " + sys.argv[1])
        raise SystemExit(1)

    file_inside = file.read()

    lex = SLexer()

    #for token in lex.tokenize(file_inside):
    #    print(token)

    pars = SParser()
    
    pprint(pars.parse(lex.tokenize(file_inside)))
    Path("output.json").write_text(json.dumps(pars.parse(lex.tokenize(file_inside)), indent=2))

    raise SystemExit(1)