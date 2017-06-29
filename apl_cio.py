"""
    APL console input/output helper class

    UNDER DEVELOPMENT

    This is the sixth step of the transition.

    This step separates the printing of values that are:
        - implicit, as a result of evaluating an expression
        - explicit, thanks to ⎕← or ⍞←
        - testing

    The separation of the implicit and explicit cases allow for different
    rules:  --script suppress implicit, but not explicit, output.

    The testing case just leaves existing tests unaltered (for now).

    The intention is that the complexities of console input and output will be
    delegated to the apl_cio module as and when it becomes advantageous to do so.
"""

# ------------------------------

class   APL_cio (object):
    def __init__(self,prompt="",prefix="",silent=False):
        self.prompt = prompt
        self.prefix = prefix
        self.silent = silent
        self.newline = True
        self.prefixDone = False
        self.hushExplicit = True

    def printResult (self,value):
        if value is None:
            print(None)
        else:
            print(str(value))

    def printImplicit (self,value):
        if value is not None and not self.silent:
            if not self.prefixDone:
                print(self.prefix,end="")
                self.prefixDone = True

            print(str(value),end='\n' if self.newline else '')

    def printExplicit (self,value):
        if value is not None:
            if not self.prefixDone and not self.silent:
                print(self.prefix,end="")
                self.prefixDone = True

            print(str(value),end='\n' if self.newline else '')

    def printError (self,error,expr,where=""):
        if error.message:
            print('\r'+' '*(len(self.prompt)+expr.rfind(error.expr)),end="^\n")
            print(error.message,where)

# EOF
