"""
    map functions for dyadic APL functions

    UNDER DEVELOPMENT

    This module contains functions that map mathematical scalar functions over
    vectors and higher order arrays with the help of iterators functions.  It
    also contains functions that map non-mathematical vector functions.

    The external view is a map function but internally the functions delegate.
    Their task is a validate parameters and handle degenerate cases.

    WIP - the implementation of lazy evaluation means all functions in this
    module are under review.
"""

import operator

import dyadicIterators as iterator

from systemVariables import confirmInteger, indexOrigin

from aplQuantity import aplQuantity, makeScalar, makeVector, makeEmptyVector, scalarIterator
from aplError import aplError, assertTrue, assertNumeric, assertNotArray, assertScalarLike, assertEmptyVector

# ------------------------------

def     maths(Fn, A, B):
    """
    the basic recursive map for dyadic mathematical functions
    """
    if A.isScalar() and B.isScalar():
        return makeScalar(iterator.maths(maths, Fn, A, B))

    if A.isScalar():
        if B.isEmptyVector():
            return B

        return makeVector(
            iterator.maths(maths, Fn, A.scalarIterator(), B), B.dimension(), B.prototype())

    if B.isScalar():
        if A.isEmptyVector():
            return A

        return makeVector(
            iterator.maths(maths, Fn, A, B.scalarIterator()), A.dimension(), A.prototype())

    if A.isVector() and B.isVector():
        if B.isEmptyVector():
            assertTrue(A.isEmptyVector(), "LENGTH ERROR")

        return makeVector(iterator.maths(maths, Fn, A, B), B.dimension(), B.prototype())

    assertNotArray(A, "WIP - RANK ERROR")
    assertNotArray(B, "WIP - RANK ERROR")

# ------------------------------

def     deal(Fn, A, B):
    """
    implement deal (dyadic ?)
    """
    assertScalarLike(A, "RANK ERROR")
    assertScalarLike(B, "RANK ERROR")

    Apy = confirmInteger(A.scalarToPy())

    return makeVector(Fn(Apy, B.scalarToPy()), Apy)

# ------------------------------

def     _matchMap(Fn, A, B):
    """
    the recursive map for dyadic ≡ and ≢

    returns a Boolean
    """
    if A.padFill() != B.padFill():
        return False

    elif A.isScalar():
        if B.isScalar():
            return bool(Fn(A.scalarToPy(), B.scalarToPy()))

    elif A.isVector():
        if B.isVector():
            try:
                filter(lambda X: not X, iterator.match(_matchMap, Fn, A, B)).__next__()

            except StopIteration:
                return True

    else:
        assertNotArray(A, "WIP - RANK ERROR")

    return False

# --------------

def     match(Fn, A, B):
    """
    recursive implementation of dyadic ≢
    """
    return makeScalar(int(_matchMap(Fn, A, B)))

# --------------

def     noMatch(Fn, A, B):
    """
    recursive implementation of dyadic ≢
    """
    return makeScalar(int(not _matchMap(Fn, A, B)))

# ------------------------------

def     reshape(Fn, A, B):
    """
    implement dyadic ⍴
    """
    assertNotArray(A)

    if B.isVectorLike():
        if A.isEmptyVector():
            Apy = 1

        else:
            assertScalarLike(A, "WIP - LENGTH ERROR")

            Apy = confirmInteger(A.scalarToPy())

        assertTrue(Apy >= 0, "DOMAIN ERROR")

        if Apy == 0:
            return makeEmptyVector(B.prototype())

        Bpy = B.promoteScalarToVectorPy(B.isEmptyVector())

        return makeVector(Fn(Apy, Bpy), Apy, B.prototype())

    assertNotArray(B, "WIP - RANK ERROR")

# ------------------------------

def     concatenate(Fn, A, B):
    """
    implement dyadic ,
    """
    assertNotArray(A, "WIP - RANK ERROR")
    assertNotArray(B, "WIP - RANK ERROR")

    prototype = B.prototype() if A.isEmptyVector() else A.prototype()

    Apy = 1 if A.isScalar() else A.dimension()
    Bpy = 1 if B.isScalar() else B.dimension()

    dimension = -1 if (Apy < 0 or Bpy < 0) else (Apy + Bpy)

    Rpy = Fn(A.vectorToPy(), B.vectorToPy())

    return makeVector(Rpy, dimension, prototype)

# ------------------------------

def     transpose(_, A, B):
    """
    implement dyadic ⍉
    """
    assertNotArray(A)

    if B.isScalar():
        assertEmptyVector(A)

        return B

    if B.isVector():
        assertScalarLike(A)

        Apy = confirmInteger(A.scalarToPy())

        assertTrue(Apy == 1, "DOMAIN ERROR")

        return B

    assertNotArray(B, "WIP - RANK ERROR")

# ------------------------------

def     rotate(Fn, A, B):
    """
    implement dyadic ⌽
    """
    assertNotArray(A)

    if B.isVectorLike():
        assertScalarLike(A, "RANK ERROR")

        Apy = confirmInteger(A.scalarToPy())

        if B.isEmptyVector():
            return B

        Apy = operator.mod(Apy, B.tally())

        if Apy == 0:
            return B

        return makeVector(Fn(Apy, B.vectorToPy()), B.dimension(), None)

    assertNotArray(B, "WIP - RANK ERROR")

# ------------------------------

def     index(Fn, A, B):
    """
    implement dyadic ⍳
    """
    assertNotArray(A)

    if B.isEmptyVector():
        return makeEmptyVector(B.prototype())

    if B.isVectorLike():
        if A.isEmptyVector():
            Rpy = scalarIterator(indexOrigin(), B.tally(), B.expressionToGo)
        else:
            Rpy = Fn(A.vectorToPy(), B.vectorToPy())

        if B.isScalar():
            return makeScalar(Rpy)

        return makeVector(Rpy, B.dimension())

    assertNotArray(B, "WIP - RANK ERROR")

# ------------------------------

def     without(Fn, A, B):
    """
    implement dyadic ~
    """
    assertNotArray(A)

    if B.isVectorLike():
        Rpy = Fn(A.vectorToPy(), B.vectorToPy())

        return makeVector(Rpy, -1, A.prototype())

    assertNotArray(B, "WIP - RANK ERROR")

# ------------------------------

def     set2set(Fn, A, B):
    """
    implement dyadic ∪ and ∩
    """
    assertNotArray(A)
    assertNotArray(B)

    if A.isEmptyVector() and B.isEmptyVector():
        return B

    Rpy = Fn(A.vectorToPy(), B.vectorToPy())

    return makeVector(Rpy, -1, A.prototype())

# ------------------------------

def     drop(Fn, A, B):
    """
    implement dyadic ↓
    """
    assertNotArray(A)

    if B.isScalar():
        if A.isEmptyVector():
            return B

        assertScalarLike(A)

        Apy = confirmInteger(A.scalarToPy())

        if Apy == 0:
            return makeVector(B.vectorToPy(), 1, B.prototype())

        return makeEmptyVector(B.prototype())

    if B.isVector():
        if A.isEmptyVector():
            Apy = 1

        else:
            assertScalarLike(A)

            Apy = confirmInteger(A.scalarToPy())

            if Apy == 0:
                return B

        Rpy = Fn(Apy, B.vectorToPy())

        return makeVector(Rpy, -1, B.prototype())

    assertNotArray(B, "WIP - RANK ERROR")

# ------------------------------

def     take(Fn, A, B):
    """
    implement dyadic ↑
    """
    assertNotArray(A)

    if B.isScalar() or B.isEmptyVector():
        if A.isEmptyVector():
            return B

    if B.isVectorLike():
        assertScalarLike(A)

        Apy = confirmInteger(A.scalarToPy())

        if Apy == 0:
            return makeEmptyVector(B.prototype())

        Rpy = Fn(Apy, B.vectorToPy(), B.padFill())

        return makeVector(Rpy, abs(Apy), B.prototype())

    assertNotArray(B, "WIP - RANK ERROR")

# ------------------------------

def     compress(Fn, A, B):
    """
    implement dyadic / and \
    """
    assertNotArray(A)

    if B.isScalar() and A.isEmptyVector():
        return makeEmptyVector(B.prototype())

    if B.isVectorLike():
        Rpy = Fn(A.promoteScalarToVectorPy(), B.vectorToPy(), B.padFill())

        return makeVector(Rpy, -1, B.prototype())

    assertNotArray(B, "WIP - RANK ERROR")

# ------------------------------

def     expand(Fn, A, B):
    """
    implement dyadic / and \
    """
    assertNotArray(A)

    if B.isScalar() and A.isEmptyVector():
        return makeEmptyVector(B.prototype())

    if B.isVectorLike():
        if A.isScalar():
            Apy = confirmInteger(A.scalarToPy())

            assertTrue(Apy >= 0, "LENGTH ERROR")

            if Apy == 0:
                return makeVector(B.prototype(), 1, B.prototype())

        Rpy = Fn(A.promoteScalarToVectorPy(), B.vectorToPy(), B.padFill())

        return makeVector(Rpy, -1, B.prototype())

    assertNotArray(B, "WIP - RANK ERROR")

# ------------------------------
# OLD IMPLEMENTATIONS TO BE REPLACED
# ------------------------------

def     vs2v_encode(Fn, A, B):
    """
    encode B to base A
    """
    assertNumeric(A)
    assertNumeric(B)

    if B.dimension() == 0:
        return aplQuantity([])

    Rpy = Fn(A.vectorToPy(), B.scalarToPy())

    if A.isScalar():
        return aplQuantity(Rpy[0], None, False)

    if A.isEmptyVector():
        return A

    if A.isVector():
        return aplQuantity(Rpy, A.dimension(), False)

    aplError("RANK ERROR")

# ------------------------------

def     vv2s_decode(Fn, A, B):
    """
    decode B from base A
    """
    assertNumeric(A)
    assertNumeric(B)

    if A.isScalar():
        Rpy = Fn(A.scalarIterator(), B.vectorToPy())
    else:
        Rpy = Fn(A.vectorToPy()[-B.dimension():], B.vectorToPy())

    return aplQuantity(Rpy, None, False)

# EOF
