"""
    map functions for APL operators

    UNDER DEVELOPMENT

    The functions in this module implement APL operators.  Typically, they use
    an iterator object or function defined in operatorIterators.

    Operators are APL's equivalent of higher order functions:  they operate
    on APL functions and quantities.  Typically, the functions are the lambda
    functions defined in dyadicLookup.

    This module is being implemented by analogy with the dyadic and monadic
    map modules.  It is experimental and may be replaced.

    Currently, the operators acts on vector and scalar, not arrays.
"""

import operatorIterators as iterator

from makeQuantity import makeScalar, makeVector, makePrototype

from aplError import assertNotTrue, assertNotArray

# ------------------------------

def     reduceLast(Fn, A, B):
    """
    the map for the / (reduce along last axis) operator
    """
    if B.isScalar():
        return B

    if B.isVector():
        if B.isEmptyVector():
            assertNotTrue(A is None, "DOMAIN ERROR")

            return makeScalar(A)

        Rpy = iterator.reduceVector(Fn, B)

        if Rpy.isScalar():
            return Rpy

        return makeScalar((Rpy,), makePrototype(Rpy))

    assertNotArray(B, "WIP - RANK ERROR")

# ------------------------------

def     reduceFirst(Fn, A, B):
    """
    the map for the ⌿ (reduce along first axis) operator
    """
    if B.isScalar():
        return B

    if B.isVector():
        if B.isEmptyVector():
            assertNotTrue(A is None, "DOMAIN ERROR")

            return makeScalar(A)

        Rpy = iterator.reduceVector(Fn, B)

        if Rpy.isScalar():
            return Rpy

        return makeScalar((Rpy,), makePrototype(Rpy))

    assertNotArray(B, "WIP - RANK ERROR")

# ------------------------------

def     scanLast(Fn, _, B):
    """
    the map for the \ (scan along last axis) operator
    """
    if B.isScalar():
        return B

    if B.isVector():
        if B.isEmptyVector():
            return B

        if B.isScalarLike():
            return makeScalar(B.scalarToPy())

        Rpy = iterator.scanVector(Fn, B)

        return makeVector(Rpy, B.dimension(), B.prototype())

    assertNotArray(B, "WIP - RANK ERROR")

# ------------------------------

def     scanFirst(Fn, _, B):
    """
    the map for the ⍀ (scan along first axis) operator
    """
    if B.isScalar():
        return B

    if B.isVector():
        if B.isEmptyVector():
            return B

        if B.isScalarLike():
            return makeScalar(B.scalarToPy())

        Rpy = iterator.scanVector(Fn, B)

        return makeVector(Rpy, B.dimension(), B.prototype())

    assertNotArray(B, "WIP - RANK ERROR")

# EOF
