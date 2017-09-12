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

import dyadicIterators as iterator

from systemVariables import confirmInteger

from aplQuantity import aplQuantity, makeScalar, makeVector, makeEmptyVector, scalarIterator
from aplError import aplError, assertTrue, assertNumeric, assertNotArray, assertScalarLike

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
# OLD IMPLEMENTATIONS TO BE REPLACED
# ------------------------------

def     vv2v(Fn, A, B):
    """
    evaluate a dyadic function that returns a vector
    """
    case = A.isString() + B.isString()

    if case == 1:
        return A

    Rpy = Fn(A.vectorToPy(), B.vectorToPy())

    return aplQuantity(Rpy, len(Rpy), A.prototype())

# ------------------------------

def     vv2s(Fn, A, B):
    """
    evaluate a dyadic function that returns a vector if B is a vector but a scalar if B is scalar
    """
    case = A.isString() + B.isString()

    Rpy = Fn(A.vectorToPy(), B.vectorToPy(), case == 1)

    if B.isScalar():
        return aplQuantity(Rpy[0], None)

    if B.isVector():
        return aplQuantity(Rpy, B.dimension())

    aplError("RANK ERROR")

# ------------------------------

def     sv_transpose(Fn, A, B):
    """
    evaluate dyadic transpose (a degenerate function for vectors)
    """
    assertNumeric(A)

    if A.dimension() == 0 and B.isScalar():
        return B

    if A.dimension() == 0 and B.dimension() == 0:
        aplError("LENGTH ERROR")

    Apy = A.scalarToPy("LENGTH ERROR")

    if Apy != 1:
        aplError("DOMAIN ERROR")

    if B.isScalar():
        aplError("LENGTH ERROR")

    Bpy = B.vectorToPy()

    return aplQuantity(Fn(Apy, Bpy), B.dimension(), B.prototype())

# ------------------------------

def     sv2vr(Fn, A, B):
    """
    evaluate a dyadic function that returns a vector if B is a vector but a scalar if B is scalar
    """
    assertNumeric(A)

    if A.dimension() == 0:
        aplError("RANK ERROR")

    if B.dimension() == 0:
        return B

    Rpy = Fn(A.scalarToPy("RANK ERROR"), B.vectorToPy())

    if B.isScalar():
        return aplQuantity(Rpy[0], None, B.prototype())

    if B.isVector():
        return aplQuantity(Rpy, B.dimension(), B.prototype())

    aplError("RANK ERROR")

# ------------------------------

def     sv2vl(Fn, A, B):
    """
    evaluate a dyadic function that returns a vector if B is a vector but a scalar if B is scalar
    """
    assertNumeric(A)

    if A.dimension() == 0:
        if B.isScalar():
            return B
        elif B.isVector():
            return aplQuantity([], 0, B.prototype())

        aplError("RANK ERROR")

    if B.isString():
        Rpy = Fn(A.scalarToPy("LENGTH ERROR"), B.vectorToPy(), ' ')
    else:
        Rpy = Fn(A.scalarToPy("LENGTH ERROR"), B.vectorToPy(), 0)

    if B.isScalar() and Rpy != []:
        return aplQuantity(Rpy[0], None, B.prototype())

    return aplQuantity(Rpy, len(Rpy), B.prototype())

# ------------------------------

def     ce2v(Fn, A, B):
    """
    compress or expand a vector yielding another
    """
    assertNumeric(A)

    if A.dimension() == 0 and B.isScalar():
        return aplQuantity([], 0, B.prototype())

    if B.isString():
        Rpy = Fn(A.vectorToPy(), B.vectorToPy(), ' ')
    else:
        Rpy = Fn(A.vectorToPy(), B.vectorToPy(), 0)

    return aplQuantity(Rpy, len(Rpy), B.prototype())

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
