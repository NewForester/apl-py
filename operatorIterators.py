"""
    iterator objects and functions for APL operators

    UNDER DEVELOPMENT

    The objects in this module implement APL operators in conjunction with map
    functions defined in operatorMaps.

    This module is being implemented by analogy with the dyadic and monadic
    iterator modules.  It is experimental and may be replaced.
"""

from monadicIterators import reverse

from makeQuantity import makeScalar

from aplQuantity import aplQuantity
from aplError import aplException

# ------------------------------

def reduceVector(Fn, B):
    """
    the iterator for the reduce operator when applied to a vector
    """
    I = reverse(B).__iter__()
    Y = I.__next__()

    if not isinstance(Y, aplQuantity):
        Y = makeScalar(Y)

    try:
        while True:
            X = I.__next__()

            if not isinstance(X, aplQuantity):
                X = makeScalar(X)

            Y = Fn(X, Y).resolve()

    except StopIteration:
        pass

    return Y

# ------------------------------

class   scanVector(object):
    """
    the iterator for the scan operator when applied to a vector
    """
    def __init__(self, Fn, B):
        self._Fn = Fn
        self._B = B.__iter__()
        self._expresso = B.expressionToGo

        self._A = []

    def __iter__(self):
        return self

    def __next__(self):
        Y = self._B.__next__()

        if self._A == []:
            self._A.append(Y)
            return (Y)

        self._A.append(Y)

        try:
            Y = reduceVector(self._Fn, self._A)
        except aplException as error:
            if error.expr is None:
                error.expr = self._expresso
            raise error

        return Y.scalarToPy() if Y.isScalar() else Y

# EOF
