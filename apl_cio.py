"""
    APL console input/output helper class

    UNDER DEVELOPMENT

    This initial version is the first step of a transition.

    It holds the existing print routines (print_result and print_error) and a
    dummy APL_cio class so that the calling sequences of other routines can be
    adjusted.  An APL_cio object will be passed down the calling sequence of
    most parser routines without them doing anything with the object other than
    pass it on.

    The intention is that the complexities of console input and output will be
    delegated to the apl_cio module as and when it becomes advantageous to do so.
"""

# ------------------------------

def     print_result (result,newline=True):
    """
    print the result when APL expression evaluation succeeds
    """
    print(str(result),end='\n' if newline else '')

# ------------------------------

def     print_error (error,expr,prompt="",where=""):
    """
    print the error response when APL expression evaluation fails
    """
    if error.message:
        print('\r'+' '*(len(prompt)+expr.rfind(error.expr)),end="^\n")
        print(error.message,where)

# ------------------------------

class   APL_cio (object):
    def __init__(self):
        pass

# EOF
