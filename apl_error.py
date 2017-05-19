"""
    three useful abort routines and a simple exception class
"""

import sys

# ------------------------------

class   APL_exception (Exception):
    """
    An simple APL Exception Class
    """
    def __init__ (self,message,expr=None):
        self.message = message
        self.expr = expr

# ------------------------------

def     apl_error (message,expr=None):
    """
    raise an exception so aborting the current operation
    """
    raise (APL_exception(message,expr))

# ------------------------------

def     apl_exit (status,message=None):
    """
    clean up and exit session
    """
    if not message is None:
        print(message)
    sys.exit(status)

# ------------------------------

def     apl_quit (status,prompt=""):
    """
    quit session without clean up
    """
    print(prompt)
    sys.exit(status)

# EOF
