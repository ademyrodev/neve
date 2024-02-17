import sys
import lex
import file_info

fname = "?"
src_lines = ["?"]

def usage():
    print("Usage: neve <filename>")  

if __name__ == "__main__":
    args = sys.argv 
    if len(args) < 2:
        usage()
        exit(1)

    file = args[1]
    file_info.fname = file
    with open(file) as f:
        file_info.lines = [lines for lines in f]
        f.seek(0)
        contents = f.read()

        lexer = lex.Lexer(contents)
        toks = lexer.lex()
        
        print(toks)
