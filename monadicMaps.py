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

import monadicIterators as iterator

from systemVariables import confirmInteger

from aplQuantity import aplQuantity, makeScalar, makeVector, makeEmptyVector
from aplError import aplError, assertNumeric
from aplError import aplError, assertNumeric, assertNotArray

# ------------------------------

def     maths(Fn, B):
    """
    the basic recursive map for monadic mathematical functions
    """
    if B.isScalar():
        return makeScalar(iterator.maths(maths, Fn, B))

    if B.isEmptyVector():
        return B

    if B.isVector():
        return makeVector(iterator.maths(maths, Fn, B), B.dimension())

    assertNotArray(B, "WIP - RANK ERROR")

# ------------------------------

def     depth(Fn, B):
    """
    implement monadic ≡
    """
    if B.isScalar():
        Rpy = Fn(B.vectorToPy())

        Rpy += 1 if Rpy != 0 else 0

    if B.isVector():
        Rpy = Fn(B.vectorToPy())

        Rpy += 1

    assertNotArray(B, "WIP - RANK ERROR")

    return makeScalar(Rpy)

# ------------------------------

def     tally(_, B):
    """
    implement monadic ≢
    """
    if B.isScalar():
        return makeScalar(1)

    if B.isVector():
        return makeScalar(B.tally())

    assertNotArray(B, "WIP - RANK ERROR")

# ------------------------------

def     rho(_, B):
    """
    implement monadic ⍴
    """
    if B.isScalar():
        return makeEmptyVector()

    if B.isVector():
        return makeVector((B.tally(),), 1)

    assertNotArray(B, "WIP - RANK ERROR")

# ------------------------------

def     unravel(_, B):
    """
    implement monadic ,
    """
    if B.isScalar():
        return makeVector(B.vectorToPy(), 1, B.prototype())

    if B.isVector():
        return B

    assertNotArray(B, "WIP - RANK ERROR")

# ------------------------------

def     transpose(_, B):
    """
    implement monadic ⍉
    """
    if B.isScalar():
        return B

    if B.isVector():
        return B

    assertNotArray(B, "WIP - RANK ERROR")

# ------------------------------

def     reverse(Fn, B):
    """
    implement monadic ⌽
    """
    if B.isScalarLike() or B.isEmptyVector():
        return B

    if B.isVector():
        return makeVector(Fn(B.vectorToPy()), B.dimension(), None)

    assertNotArray(B, "WIP - RANK ERROR")

# ------------------------------
# OLD IMPLEMENTATIONS TO BE REPLACED
# ------------------------------

def     s2v(Fn, B):
    """
    evaluate a numeric monadic function that, given a scalar argument, returns a vector
    """
    assertNumeric(B)

    Bpy = confirmInteger(B.scalarToPy())

    return aplQuantity(Fn(Bpy), int(Bpy))

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

# EOF
