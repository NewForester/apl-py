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

from aplQuantity import makeScalar
from aplError import assertError, assertNotArray

# ------------------------------

def     reduceLast(Fn, A, B):
    """
    the map for the / (reduce along last axis) operator
    """
    if B.isVectorLike():
        Rpy = iterator.reduceVector(Fn, makeScalar(A), B)

        return makeScalar(Rpy)

    assertNotArray(B, "WIP - RANK ERROR")

# ------------------------------

def     reduceFirst(Fn, A, B):
    """
    the map for the ⌿ (reduce along first axis) operator
    """
    if B.isVectorLike():
        Rpy = iterator.reduceVector(Fn, makeScalar(A), B)

        return makeScalar(Rpy)

    assertNotArray(B, "WIP - RANK ERROR")

# EOF
