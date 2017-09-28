"""
    map functions for dyadic APL functions

    UNDER DEVELOPMENT

    The functions in this module implement mathematical and non-mathematical
    dyadic APL functions for vectors in conjunction with an iterator object
    defined in dyadicIterators.

    Each function takes two APL quantities and returns a third.  The quantity
    returned is generally an iterator so implementing lazy evaluation.

    The mathematical APL functions are handled by the generic dyadicMap.  The
    pertinent scalar mathematical function is the first parameter.

    The non-mathematical APL functions the handled by special purpose map
    functions.  The pertinent iterator is the first parameter.

    Nested vectors are handled by recursion with the map function calling the
    iterator, which calls the map function.

    There are, of course, exceptions.  Scalar quantities are also handled as
    special cases.
"""

import operator

import dyadicIterators as iterator

from systemVariables import confirmInteger, indexOrigin

from aplQuantity import aplQuantity, scalarIterator, makeScalar, makeVector, makeEmptyVector
from aplError import assertError, assertTrue, assertNotTrue
from aplError import assertNotScalar, assertNotVector, assertNotArray
from aplError import assertNumeric, assertScalarLike, assertEmptyVector

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

def     partition(Fn, A, B):
    """
    implement dyadic ⊂
    """
    assertNotArray(A)

    assertNotTrue(B.isScalar(), "RANK ERROR")

    if B.isEmptyVector() and A.isEmptyVector():
        return B

    if B.isVector():
        if A.isScalar():
            Apy = confirmInteger(A.scalarToPy())

            if Apy == 0:
                return makeEmptyVector()

            return makeScalar((B,), B.prototype())

        return makeVector(Fn(A.vectorToPy(), B.vectorToPy()), -1, B.prototype())

    assertNotArray(B, "WIP - RANK ERROR")

# ------------------------------

def     pick(_, A, B):
    """
    implement dyadic ⊃
    """
    assertNotArray(A)

    if A.isEmptyVector():
        return B

    assertNotScalar(B)

    if B.isVector():
        IO = indexOrigin()

        try:
            for X in A.vectorToPy():
                X = confirmInteger(X)

                assertTrue(X >= IO, "INDEX ERROR")

                if isinstance(B, aplQuantity):
                    B = B.vectorToPy()[X-IO]
                else:
                    assertError("RANK ERROR")

        except IndexError:
            assertError("INDEX ERROR")

        if isinstance(B, aplQuantity):
            return B

        return makeScalar((B,), None)

    assertNotArray(B, "WIP - RANK ERROR")

# ------------------------------

def     membership(Fn, A, B):
    """
    implement dyadic ∊
    """
    if A.isEmptyVector():
        return A

    if A.isVectorLike() and B.isVectorLike():
        Rpy = Fn(A.vectorToPy(), B.vectorToPy())

        if A.isScalar():
            return makeScalar(Rpy, A.prototype())

        return makeVector(Rpy, A.dimension(), A.prototype())

    assertNotArray(A, "WIP - RANK ERROR")
    assertNotArray(B, "WIP - RANK ERROR")

# ------------------------------

def     find(Fn, A, B):
    """
    implement dyadic ∊
    """
    A.resolve()

    if B.isVectorLike() and A.isVectorLike():
        Rpy = Fn(A.vectorToPy(), B.vectorToPy())

        if B.isScalar():
            return makeScalar(Rpy, B.prototype())

        return makeVector(Rpy, B.dimension(), B.prototype())

    assertNotArray(A, "WIP - RANK ERROR")
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

def     encode(Fn, A, B):
    """
    implement dyadic ⊤
    """
    assertNotArray(A)

    if B.isEmptyVector():
        return makeEmptyVector()

    assertNotArray(B)

    if A.isEmptyVector():
        return makeEmptyVector()

    if B.isScalarLike():
        Rpy = Fn(A.vectorToPy(), B.scalarToPy())

        return makeVector(Rpy, A.dimension())

    assertNotVector(B, "WIP - LENGTH ERROR")

# ------------------------------

def     decode(Fn, A, B):
    """
    implement dyadic ⊥
    """
    assertNotArray(A)

    if B.isScalar():
        assertNumeric(B)

        if A.isScalar():
            assertNumeric(A)

            return B

        return makeScalar(Fn(A.vectorToPy(), B.scalarIterator()))

    if B.isVector():
        if A.isEmptyVector() or B.isEmptyVector():
            return makeScalar(0)

        return makeScalar(Fn(A.promoteScalarToVectorPy(), B.vectorToPy()))

    assertNotArray(B, "WIP - RANK ERROR")

# EOF
