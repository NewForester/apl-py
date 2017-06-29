"""
    APL console input/output helper class

    UNDER DEVELOPMENT

    This is the fourth step of the transition.

    This step simplified calling code by removing the optional parameter to
    printResult() and using the self.newline state instead.

    Refactor of calling code also led to the elimination of the self.eol state.

    The intention is that the complexities of console input and output will be
    delegated to the apl_cio module as and when it becomes advantageous to do so.
"""

# ------------------------------

class   APL_cio (object):
    def __init__(self,silent=False):
        self.silent = silent
        self.hush = True
        self.newline = True

    def printResult (self,result):
        if result is None:
            print(None)
        else:
            print(str(result),end='\n' if self.newline else '')

    def printError (self,error,expr,prompt="",where=""):
        if error.message:
            print('\r'+' '*(len(prompt)+expr.rfind(error.expr)),end="^\n")
            print(error.message,where)

# EOF
