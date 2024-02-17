class Parser:
    def __init__(self, tokens):
        self.token_stream = reversed(tokens)
        self.curr = self.next()

    def next(self):
        try:
            return token_stream.pop()
        except IndexError:
            return None

    def parse(self):
        return self.decl()

    def decl(self):
        match self.curr.type:
            case CLASS:
                return self.class_decl()
            
            case FUN:
                return self.fun_decl()
            
            case LET:
                return self.let_decl()

            case VAR:
                return self.var_decl()

    def fun_decl(self):
         
