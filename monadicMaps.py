"""
    map functions for monadic APL functions

    UNDER DEVELOPMENT

    The functions in this module implement mathematical and non-mathematical
    monadic APL functions for vectors in conjunction with an iterator object
    defined in monadicIterators.

    Each function takes an APL quantity and returns another.  The quantity
    returned is generally an iterator so implementing lazy evaluation.

    The mathematical APL functions are handled by the generic map.  The
    pertinent scalar mathematical function is the first parameter.

    The non-mathematical APL functions the handled by special purpose map
    functions.  The pertinent iterator is the first parameter.

    Nested vectors are handled by recursion with the map function calling the
    iterator, which calls the map function.

    There are, of course, exceptions.  Scalar quantities are also handled as
    special cases.
"""

import monadicIterators as iterator

from systemVariables import confirmInteger

from aplQuantity import aplQuantity, makeScalar, makeVector, makeEmptyVector
from aplError import assertTrue, assertNotVector, assertNotArray

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

def     iota(Fn, B):
    """
    implement monadic ⍳

    the operand is scalar: there is no map as such
    """
    if B.isScalar():
        Bpy = confirmInteger(B.scalarToPy())

        assertTrue(Bpy >= 0, "DOMAIN ERROR")

        return makeVector(Fn(Bpy), Bpy)

    assertNotVector(B, "WIP - LENGTH ERROR")
    assertNotArray(B)

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

def     enclose(_, B):
    """
    implement monadic ⊂
    """
    if B.isScalar():
        return B

    if B.isVector():
        return makeScalar((B,), None)

    assertNotArray(B, "WIP - RANK ERROR")

# ------------------------------

def     unique(Fn, B):
    """
    implement monadic ∪
    """
    if B.isScalarLike() or B.isEmptyVector():
        return B

    if B.isVector():
        return makeVector(Fn(B.vectorToPy()), -1, B.prototype())

    assertNotArray(B, "WIP - RANK ERROR")

# ------------------------------

def     tail(Fn, B):
    """
    implement monadic ↓
    """
    if B.isScalarLike():
        return makeEmptyVector(B.prototype())

    if B.isEmptyVector():
        return B

    if B.isVector():
        return makeVector(Fn(B.vectorToPy()), B.dimension()-1, B.prototype())

    assertNotArray(B, "WIP - RANK ERROR")

# ------------------------------

def     head(Fn, B):
    """
    implement monadic ↑
    """
    if B.isScalar() or B.isEmptyVector():
        return B

    if B.isVector():
        return makeScalar(Fn(B.vectorToPy()), B.prototype())

    assertNotArray(B, "WIP - RANK ERROR")

# EOF
