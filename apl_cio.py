"""
    APL console input/output helper class

    UNDER DEVELOPMENT

    This second version refactors the print routines as print methods.

    The intention is that the complexities of console input and output will be
    delegated to the apl_cio module as and when it becomes advantageous to do so.
"""

# ------------------------------

class   APL_cio (object):
    def __init__(self):
        pass

    def printResult (self,result,newline=True):
        print(str(result),end='\n' if newline else '')

    def printError (self,error,expr,prompt="",where=""):
        if error.message:
            print('\r'+' '*(len(prompt)+expr.rfind(error.expr)),end="^\n")
            print(error.message,where)

# EOF
