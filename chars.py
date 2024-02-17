import string

DIGITS = '0123456789'
ASCII  = string.ascii_letters + '_'
WHITESPACE = ' \t\r;'

def is_digit(c):
    return c and c in DIGITS

def is_ascii(c):
    return c and c in ASCII

def is_whitespace(c):
    return c and c in WHITESPACE
