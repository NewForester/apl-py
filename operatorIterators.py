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

# ------------------------------

class   scanVector(object):
    """
    the iterator for the scan operator applied to a vector
    """
    def __init__(self, Fn, A, B):
        self._Fn = Fn
        self._A = A
        self._B = B.__iter__()

    def __iter__(self):
        return self

    def __next__(self):
        try:
            Y = self._B.__next__()

            if isinstance(Y, aplQuantity):
                X = self._Fn(self._A, Y).resolve()
            else:
                X = self._Fn(self._A, makeScalar(Y))

            self._A = X

            return X.scalarToPy() if X.isScalar() else X

        except aplException as error:
            if error.expr is None:
                error.expr = B.expressionToGo
            raise error

# EOF
