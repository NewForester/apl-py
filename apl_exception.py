"""
    A simple APL exception class
"""

class   APL_Exception (BaseException):
    """
    APL Exception Class
    """
    def __init__ (self,message,line=None):
        self.message = message
        self.line = line

# EOF
