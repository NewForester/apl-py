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

from makeQuantity import makeScalar, makeVector, makeEmptyVector, makeArray

from aplQuantity import aplQuantity
from aplIterators import monadicTranspose
from aplError import assertTrue, assertNotScalar, assertNotVector, assertNotArray

# ------------------------------

def     maths(Fn, B):
    """
    the basic recursive map for monadic mathematical functions
    """
    if B.isArray():
        return makeArray(iterator.maths(maths, Fn, B), B.dimension())

    if B.isVector():
        return makeVector(iterator.maths(maths, Fn, B), B.dimension(), B.prototype())

    return makeScalar(iterator.maths(maths, Fn, B))

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

def     depth(_, B):
    """
    implement monadic ≡
    """
    return makeScalar(B.depth())

# ------------------------------

def     tally(_, B):
    """
    implement monadic ≢
    """
    return makeScalar(B.tally())

# ------------------------------

def     rho(_, B):
    """
    implement monadic ⍴
    """
    if B.isArray():
        return makeVector(B.dimension(), B.rank())

    if B.isVector():
        return makeVector((B.tally(),), 1)

    return makeEmptyVector()

# ------------------------------

def     unravel(_, B):
    """
    implement monadic ,
    """
    if B.isArray():
        return makeVector(B.arrayToPy(), B.elementCount(), B.prototype())

    if B.isVector():
        return B

    return makeVector(B.vectorToPy(), 1, B.prototype())

# ------------------------------

def     enlist(Fn, B):
    """
    implement monadic ∊
    """
    if B.isEmptyVector():
        return B

    if B.isVectorLike():
        return makeVector(Fn(B.vectorToPy()), -1, B.prototype())

    return makeVector(Fn(B.arrayToPy()), -1, B.prototype())

# ------------------------------

def     transpose(_, B):
    """
    implement monadic ⍉
    """
    if B.isArray():
        assertTrue(B.dimension() == (2, 2), "WIP - MATRIX ERROR")

        Rpy = monadicTranspose(B.arrayToPy(), B.dimension())

        return makeArray(Rpy, B.dimension(), None)

    return B

# ------------------------------

def     reverselast(Fn, B):
    """
    implement monadic ⌽
    """
    if B.isArray():
        assertTrue(B.dimension() == (2, 2), "WIP - MATRIX ERROR")

        Rpy = []
        for Bit in B.arrayByLastAxis():
            Rpy += Fn(Bit.vectorToPy())

        return makeArray(Rpy, B.dimension(), None)

    if B.isVector() and not B.isEmptyVector():
        return makeVector(Fn(B.vectorToPy()), B.dimension(), None)

    return B

# ------------------------------

def     reversefirst(Fn, B):
    """
    implement monadic ⊖
    """
    if B.isArray():
        assertTrue(B.dimension() == (2, 2), "WIP - MATRIX ERROR")

        Rpy = []
        for Bit in B.arrayByFirstAxis():
            Rpy += Fn(Bit.vectorToPy())

        Rpy = monadicTranspose(Rpy, B.dimension())

        return makeArray(Rpy, B.dimension(), None)

    if B.isVector() and not B.isEmptyVector():
        return makeVector(Fn(B.vectorToPy()), B.dimension(), None)

    return B

# ------------------------------

def     enclose(_, B):
    """
    implement monadic ⊂
    """
    if B.isScalar():
        return B

    return makeScalar((B,), None)

# ------------------------------

def     disclose(Fn, B):
    """
    implement monadic ⊃
    """
    if B.isArray():
        return makeArray(Fn(B.arrayToPy()), B.dimension(), B.prototype())

    if B.isVector():
        if B.isEmptyVector():
            return B

        return makeVector(Fn(B.vectorToPy()), B.dimension(), B.prototype())

    if B.isScalar():
        Bpy = B.scalarToPy()

        if isinstance(Bpy, aplQuantity):
            return Bpy

        return makeScalar(Bpy, None)

# ------------------------------

def     unique(Fn, B):
    """
    implement monadic ∪
    """
    assertNotArray(B, "RANK ERROR")

    if B.isScalarLike() or B.isEmptyVector():
        return B

    return makeVector(Fn(B.vectorToPy()), -1, B.prototype())

# ------------------------------

def     tail(Fn, B):
    """
    implement monadic ↓
    """
    assertNotArray(B, "RANK ERROR")

    if B.isScalarLike():
        return makeEmptyVector(B.prototype())

    if B.isEmptyVector():
        return B

    return makeVector(Fn(B.vectorToPy()), B.dimension()-1, B.prototype())

# ------------------------------

def     head(Fn, B):
    """
    implement monadic ↑
    """
    if B.isScalar() or B.isEmptyVector():
        return B

    if B.isVector():
        return makeScalar(Fn(B.vectorToPy()), Fn(B.prototype()))

    return makeScalar(Fn(B.arrayToPy()), Fn(B.prototype()))

# ------------------------------

def     grade(descending, B):
    """
    implement monadic ⍒ and ⍋
    """
    def _sortKey(Y):
        """
        sort key depends on type as well value
        """
        if isinstance(Y, aplQuantity):
            return 2 * Y.tally(), Y

        if isinstance(Y, str):
            return 0, ord(Y)

        return 1, Y

    assertNotScalar(B, "DOMAIN ERROR")

    if B.isArray():
        assertTrue(B.dimension() == (2, 2), "WIP - MATRIX ERROR")

        Bpy = [Bit.vectorToPy() for Bit in B.arrayByLastAxis()]
        Key = lambda X: [_sortKey(Y) for Y in Bpy[X]]

    if B.isVector():
        B.resolve()
        Bpy = B.vectorToPy()
        Key = lambda X: _sortKey(Bpy[X])

    Len = B.tally()
    S = list(range(Len))
    S.sort(key=Key, reverse=descending)

    return makeVector(iterator.grade(S), Len)

# EOF
