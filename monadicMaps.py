"""
    map functions for monadic APL functions

    UNDER DEVELOPMENT

    This module contains functions that map mathematical scalar functions over
    vectors and higher order arrays with the help of iterators functions.  It
    also contains functions that map non-mathematical vector functions.

    The external view is a map function but internally the functions delegate.
    Their task is a validate parameters and handle degenerate cases.

    WIP - the implementation of lazy evaluation means all functions in this
    module are under review.
"""

from systemVariables import confirmInteger

from aplQuantity import aplQuantity
from aplError import aplError, assertNumeric

# ------------------------------
# OLD IMPLEMENTATIONS TO BE REPLACED
# ------------------------------

def     s2s(Fn, B):
    """
    evaluate a numeric monadic function that, given a scalar argument, returns a scalar
    """
    assertNumeric(B)

    if B.isScalar():
        return aplQuantity(Fn(B.python()), None)

    if B.isVector():
        return aplQuantity(map(Fn, B), B.dimension())

    aplError("RANK ERROR")

# ------------------------------

def     s2v(Fn, B):
    """
    evaluate a numeric monadic function that, given a scalar argument, returns a vector
    """
    assertNumeric(B)

    Bpy = confirmInteger(B.scalarToPy())

    return aplQuantity(Fn(Bpy), Bpy)

# ------------------------------

def     v_head(Fn, B):
    """
    evaluate a numeric function that, given a vector argument, returns a scalar
    """
    if B.isScalar():
        return aplQuantity(B.scalarToPy(), None, B.prototype())

    if B.isVector():
        if B.dimension() < 1:
            return aplQuantity([], 0, B.prototype())

        if B.isString():
            return aplQuantity([Fn(B.vectorToPy())], None, B.prototype())

        return aplQuantity(Fn(B.vectorToPy()), None, B.prototype())

    aplError("RANK ERROR")

# ------------------------------

def     v_tail(Fn, B):
    """
    evaluate a function that, given a vector argument, returns a vector (probably)
    """
    if B.isScalar():
        return aplQuantity([], 0, B.prototype())

    if B.isVector():
        if B.dimension() <= 1:
            return aplQuantity([], 0, B.prototype())

        return aplQuantity(Fn(B.vectorToPy()), B.dimension()-1, B.prototype())

    aplError("RANK ERROR")

# ------------------------------

def     v2v(Fn, B):
    """
    evaluate a function that, given a vector argument, returns a vector
    """
    Rpy = Fn(B.vectorToPy())

    if B.isScalar():
        return aplQuantity(Rpy[0], B.dimension(), B.prototype())

    if B.isVector():
        return aplQuantity(Rpy, B.dimension(), B.prototype())

    aplError("RANK ERROR")

# ------------------------------

def     s_rho(_, B):
    """
    scalar rho - return dimension/rank of B - does not operate on B
    """
    if B.isScalar():
        return aplQuantity([], 0)

    if B.isVector():
        return aplQuantity([B.dimension()], 1)

    aplError("RANK ERROR")

# ------------------------------

def     s_comma(_, B):
    """
    scalar comma - unravel B and return a vector
    """

    if B.isScalar():
        return aplQuantity(B.vectorToPy(), 1, B.prototype())

    if B.isVector():
        return B

    aplError("RANK ERROR")

# ------------------------------

def     v_nest(B):
    """
    depth of nesting in B
    """
    Rpy = 0

    if B.isScalar():
        Rpy = 0

    elif B.isVector():
        Rpy = 1
        for X in B:
            if isinstance(X, aplQuantity):
                Rpy = max (Rpy, 1 + v_nest(X).python())
                break

    else:
        aplError("RANK ERROR")

    return aplQuantity(Rpy, None)

# ------------------------------

def     v_tally(B):
    """
    number of elements in last axis
    """
    Rpy = 0

    if B.isScalar():
        Rpy = 1

    elif B.isString():
        Rpy = B.dimension()

    elif B.isVector():
        Rpy = B.dimension()

    else:
        aplError("RANK ERROR")

    return aplQuantity(Rpy, None)

# EOF
