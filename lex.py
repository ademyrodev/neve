import chars
import toks

class Lexer:
    def __init__(self, src):
        self.pos = toks.Pos(1, 0, 0)
        self.char_stack = list(src[::-1])
        self.curr = self.char_stack.pop()

    def advance(self):
        if self.curr == '\n':
            self.pos.newline()

        self.pos.advance()

        try:
            self.curr = self.char_stack.pop()
        except IndexError:
            self.curr = None

        return self.curr

    def peek_next(self):
        return self.char_stack[1]

    def sync(self):
        self.pos.sync()

    def lex(self):
        tokens = []

        while self.curr:
            self.skip_whitespace()
            self.sync()

            if chars.is_digit(self.curr):
                tokens.append(self.lex_number())
            elif chars.is_ascii(self.curr):
                tokens.append(self.lex_ascii())
            else:
                tokens.append(self.lex_tok())

        return tokens

    def skip_whitespace(self):
        while chars.is_whitespace(self.curr):
            self.advance()

    def lex_number(self):
        as_str = ''
        is_float = False

        while chars.is_digit(self.curr) or self.curr == '.':
            if self.curr == '.':
                if not chars.is_digit(self.peek_next()):
                    break

                is_float = True
    
            as_str += self.curr
            self.advance()

        if is_float:
            return toks.Tok(self.pos.cpy(), toks.FLOAT, float(as_str))
        else:
            return toks.Tok(self.pos.cpy(), toks.INT, int(as_str))

    def lex_ascii(self):
        id = ''

        while chars.is_ascii(self.curr):
            id += self.curr
            self.advance()

        try:
            keyword = toks.MATCH_KEYWORD[id]
            return toks.Tok(self.pos.cpy(), keyword)
        except KeyError:
            return toks.Tok(self.pos.cpy(), toks.ID, id)

    def lex_tok(self):
        if not self.curr:
            return toks.Tok(self.pos.cpy(), toks.EOF)

        while self.curr == '\n':
            self.advance()
            return toks.Tok(self.pos.cpy(), toks.NEWLINE)

        previous = self.curr
        self.advance()
        double_chars = previous + self.curr

        try:
            tok_type = toks.MATCH_TOK[double_chars]    
            return toks.Tok(self.pos.cpy(), tok_type)
        except KeyError:
            tok_type = toks.MATCH_TOK[previous]
            return toks.Tok(self.pos.cpy(), tok_type)
