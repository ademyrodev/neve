indentation = 0

def write(msg):
    print(" " * indentation + msg)    

def indent():
    indentation += 1

def unindent():
    indentation -= 1

class ClassNode:
    def __init__(self, name, fields, methods):
        self.name = name
        self.fields = fields
        self.methods = methods

    def __repr__(self):
        write(f"Class {self.name}") 
        indent()

        for f in self.fields:
            print(f)

        for m in self.methods:
            print(m)

        unindent()

class FunNode:
    def __init__(self, name, args, type, body):
        self.name = name
        self.args = args
        self.type = type
        self.body = body

    def __repr__(self):
        write(f"Fun {self.name}")
        indent()

        for a in self.args:
            print(a)
        
        write(self.type)
        print(self.body)
        
        unindent()

