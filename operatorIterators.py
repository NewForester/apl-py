"""
    iterator objects and functions for APL operators

    UNDER DEVELOPMENT

    The objects in this module implement APL operators in conjunction with map
    functions defined in operatorMaps.

    This module is being implemented by analogy with the dyadic and monadic
    iterator modules.  It is experimental and may be replaced.
"""

from aplQuantity import aplQuantity, makeScalar
from aplError import aplException

# ------------------------------

def reduceVector(Fn, A, B):
    """
    the iterator for the reduce operator applied to a vector
    """
    I = B.__iter__()

    try:
        while True:
            Y = I.__next__()

            if isinstance(Y, aplQuantity):
                A = Fn(A, Y)
            else:
                A = Fn(A, makeScalar(Y))

    except StopIteration:
        return A.scalarToPy() if A.isScalar() else (A,)

    except aplException as error:
        if error.expr is None:
            error.expr = B.expressionToGo
        raise error

# EOF
