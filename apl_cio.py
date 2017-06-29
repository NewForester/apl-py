"""
    APL console input/output helper class

    UNDER DEVELOPMENT

    This is the fifth step of the transition.

    This step is an incrementation improvement.  The interactive prompt and
    prefix strings are added to the object during construction.  The print
    methods are altered to use them allowing a little simplification of the
    calling code.

    The intention is that the complexities of console input and output will be
    delegated to the apl_cio module as and when it becomes advantageous to do so.
"""

# ------------------------------

class   APL_cio (object):
    def __init__(self,prompt="",prefix="",silent=False):
        self.prompt = prompt
        self.prefix = prefix
        self.silent = silent
        self.hush = True
        self.newline = True
        self.prefixDone = False

    def printResult (self,result):
        if result is None:
            print(None)
        else:
            if not self.prefixDone and not self.silent:
                print(self.prefix,end="")
                self.prefixDone = True
            print(str(result),end='\n' if self.newline else '')

    def printError (self,error,expr,where=""):
        if error.message:
            print('\r'+' '*(len(self.prompt)+expr.rfind(error.expr)),end="^\n")
            print(error.message,where)

# EOF
