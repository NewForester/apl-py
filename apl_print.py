"""
    the print class for handling the complexities of output

    UNDER DEVELOPMENT

    This is the third step of the transition.

    Boolean state variables have been added to the object in order to remove
    the boolean state parameters from the parse-evaluate call stack.

    The boolean state parameters were passed down several layers with being
    used or set.  This obscured the intent of the code.

    Passing an object with boolean state variables unclutters the code but
    does not by itself make the the effects of the object any clearer.  That
    is all in how the state is decomposed and its components named.

    The intention is that the complexities of output (and input) will be
    delegated to this module as and when it becomes advantageous to do so.
"""

# ------------------------------

class   APL_print (object):
    def __init__(self,silent=False):
        self.silent = silent
        self.hush = True
        self.eol = False
        self.newline = True

    def printResult (self,result,newline=True):
        print(str(result),end='\n' if newline else '')

    def printError (self,error,expr,prompt="",where=""):
        if error.message:
            print('\r'+' '*(len(prompt)+expr.rfind(error.expr)),end="^\n")
            print(error.message,where)

# EOF
