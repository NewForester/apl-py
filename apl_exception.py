"""
    A simple APL exception class

    ... and the simple routines apl_quit and apl_exit
"""

import sys

# ------------------------------

class   APL_Exception (Exception):
    """
    APL Exception Class
    """
    def __init__ (self,message,line=None):
        self.message = message
        self.line = line

# ------------------------------

def     apl_quit (status):
    """
    Quit without clean up
    """
    print()
    sys.exit(status)

# ------------------------------

def     apl_exit (status,message=None):
    """
    Clean up and exit
    """
    if not message is None:
        print(message)
    sys.exit(status)

# EOF
