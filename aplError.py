"""
    a simple exception class for APL and wrappers for Python's sys.exit()
"""

import sys

# ------------------------------

class   aplException(Exception):
    """
    A simple APL Exception Class
    """
    def __init__(self, message, expr=None):
        Exception.__init__(self)
        self.message = message
        self.expr = expr

# ------------------------------

def     aplError(message, expr=None):
    """
    raise an exception so aborting the current operation
    """
    raise aplException(message, expr)

# ------------------------------

def     aplExit(status, message=None):
    """
    clean up and exit session
    """
    if not message is None:
        print(message)

    sys.exit(status)

# ------------------------------

def     aplQuit(status, message=""):
    """
    quit session without clean up
    """
    print(message)

    sys.exit(status)

# EOF
