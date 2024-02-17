import sys
import colors
import file_info

class SrcSnippet:
    def __init__(self, origin, from, tint=colors.RESET, until=None):
        self.origin = origin
        self.from = from
        self.tint = tint
        self.until = until

    def write(self):
        for c in origin[from:until]:
            write(c)

    def tinted_in(self, tint):
        self.tint = tint
        return self
        
    def until(self, until):
        self.until = until
        self.write()

line_digits = 0

def set_line(line):
    global line_digits
    # could’ve used floor(log10(abs(line)) + 1), but laziness 
    # speaks louder
    line_digits = len(str(line))

def write(*msg):
    print(*msg, end="", sep="", file=sys.stderr)

def write_from(origin, from):
    return SrcSnippet(origin, from)

def margin(length):
    return " " * length

def write_locus(msg, pos):
    write(colors.RED, margin(line_digits), " error", 
          colors.WHITE, ": ", msg)

    end_fmt()
    write(colors.BLUE, margin(line_digits), "    at",
          colors.WHITE, f": {file_info.fname}:{pos.line}:{pos.col}")
    end_fmt()

def write_empty_pipe():
    write(margin(line_digits), " |")

def write_pipes(line):
    write(colors.BLUE)
    write_empty_pipe()
    write(line, " | ")

def write_line(pos, exposing_tint):
    line_number = pos.line
    set_line(line_number)

    line = file_info.lines[line_number - 1]
    line_end = len(line)
    write_pipes(line_number) 
    
    write_from(line, 0)
        .until(pos.col)
    write_from(line, pos.col)
        .tinted_in(exposing_tint)
        .until(pos.col + pos.length))
    write_from(line, pos.col + pos.length)
        .until(line_end)

def highlight(pos, color, highlighter):
    write(margin(pos.col))
    write(color, highlighter * pos.length)

def write_err(pos, msg):
    write_line(pos, color.RED)
    write_empty_pipe() 

    highlight(pos, colors.RED, "^")
    write(" ", msg)

def write_hint(msg):
    write(margin(line_digits))
    write(colors.BLUE, "-> 💡 ")
    write(msg)

def write_note(pos, msg):
    write_line(pos, colors.BLUE) 
    
    write_empty_pipe()
    highlight(pos, colors.BLUE, "-")    
    write(" ", msg)

def write_change(pos, change, msg):
    line_number = pos.line
    set_line(line_number)

    line = file_info.lines[line_number]
    line_end = len(line)
    write_pipes(line_number)
    
    write_from(line, 0)
        .until(pos.col)
    write(colors.GREEN, change, colors.RESET)
    write_from(line, pos.col)
        .until(line_end)

    write_empty_pipe()
    highlight(pos, colors.GREEN, "+")
    write(" ", msg)

def end_fmt():
    write(colors.RESET, "\n") 

