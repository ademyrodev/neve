INT                 = 'int'
FLOAT               = 'float'
STR                 = 'str'
ID                  = 'id'
TRUE                = 'true'
FALSE               = 'false'
NIL                 = 'nil'
COMMA               = ','
PLUS                = '+'
MINUS               = '-'
MULTI               = '*'
DIVIS               = '/'
DOT                 = '.'
DOUBLE_DOT          = '..'
QUESTION            = '?'
EXCLAM              = '!'
ASSIGN              = '='
EQ                  = '=='
NOT_EQ              = '!='
GREATER             = '>'
GREATER_EQ          = '>='
LESS                = '<'
LESS_EQ             = '<='
LPAREN              = '(' 
RPAREN              = ')'
LBRACKET            = '['
RBRACKET            = ']'
PIPE                = '|'
LET                 = 'let'
VAR                 = 'var'
IF                  = 'if'
ELSE                = 'else'
AND                 = 'and'
OR                  = 'or'
NOT                 = 'not'
WHILE               = 'while'
WITH                = 'with'
FOR                 = 'for'
MATCH               = 'match'
FUN                 = 'fun'
RETURN              = 'return'
CLASS               = 'class'
IN                  = 'in'
CONTINUE            = 'continue'
BREAK               = 'break'
DO                  = 'do'
END                 = 'end'
NEWLINE             = 'NEWLINE'
EOF                 = 'EOF'

MATCH_TOK = {
    ',': COMMA,
    '+': PLUS,
    '-': MINUS,
    '*': MULTI,
    '/': DIVIS,
    '.': DOT,
    '..': DOUBLE_DOT, 
    '?': QUESTION,
    '!': EXCLAM,
    '=': ASSIGN,
    '==': EQ,
    '!=': NOT_EQ,
    '>': GREATER,
    '>=': GREATER_EQ,
    '<': LESS,
    '<=': LESS_EQ,
    '(': LPAREN,
    ')': RPAREN,
    '[': LBRACKET,
    ']': RBRACKET,
    '|': PIPE
}

MATCH_KEYWORD = {
    'let': LET,
    'var': VAR,
    'if': IF,
    'else': ELSE,
    'and': AND,
    'or': OR,
    'not': NOT,
    'while': WHILE,
    'with': WITH,
    'for': FOR,
    'match': MATCH,
    'fun': FUN,
    'return': RETURN,
    'class': CLASS,
    'in': IN,
    'continue': CONTINUE,
    'break': BREAK,
    'do': DO,
    'end': END
}

class Pos:
    def __init__(self, line, col, length):
        self.line = line
        self.col = col
        self.length = length

    def advance(self):
        self.length += 1

    def newline(self):
        self.line += 1
        self.col = 0
        self.length = 0

    def sync(self):
        self.col += self.length
        self.length = 0

    def cpy(self):
        return Pos(self.line, self.col, self.length)

    def __repr__(self):
        return f'({self.line}:{self.col}:{self.length})'

class Tok:
    def __init__(self, pos, type, value=None):
        self.pos = pos
        self.type = type
        self.value = value

    def __repr__(self):
        if self.value:
            return f'{self.type}:{self.value} {self.pos}'
        else:
            return f'{self.type} {self.pos}'

        return f'{self.pos}'
