"""
    a simple exception class for APL and wrappers for Python's sys.exit()

    An exception is raised explicity by calling the routine aplError() or
    calling one of a small number of conditional assert routines.
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

# ------------------------------

def     assertError(message):
    """
    raise an exception so aborting the current operation
    """
    raise aplException(message)

# ------------------------------

def     assertTrue(condition, error):
    """
    raise error if condition is not true
    """
    if not condition:
        raise aplException(error)

# ------------------------------

def     assertNotTrue(condition, error):
    """
    raise error if condition is true
    """
    if condition:
        raise aplException(error)

# ------------------------------

def     assertNumeric(X, error="DOMAIN ERROR"):
    """
    throw if quantity is not a number
    """
    if X.prototype() != 0:
        raise aplException(error)

# --------------

def     assertEmptyVector(X, error="LENGTH ERROR"):
    """
    throw if quantity is a not a vector length 0
    """
    if not X.isEmptyVector():
        raise aplException(error)

# --------------

def     assertScalarLike(X, error="LENGTH ERROR"):
    """
    throw if quantity is not scalar nor a vector length 1
    """
    if not X.isScalarLike():
        raise aplException(error)

# --------------

def     assertNotScalar(X, error="RANK ERROR"):
    """
    throw if quantity is a scalar
    """
    if X.isScalar():
        raise aplException(error)

# --------------

def     assertNotVector(X, error="RANK ERROR"):
    """
    throw if quantity is a vector
    """
    if X.isVector():
        raise aplException(error)

# --------------

def     assertNotArray(X, error="RANK ERROR"):
    """
    throw if quantity is a higher order array
    """
    if X.isArray():
        raise aplException(error)

# EOF
