"""
    iterator functions for monadic APL functions

    UNDER DEVELOPMENT

    This module contains functions that implement vector versions of monadic
    APL non-mathematical functions.  Each takes two Python quantities and
    returns a third.

    WIP - the implementation of lazy evaluation means all functions in this
    module are under review.
"""

from functools import reduce

from systemVariables import confirmInteger, indexOrigin

from aplQuantity import aplQuantity
from aplError import assertError

# ------------------------------

class   maths(object):
    """
    the recursive iterator for monadic mathematical functions
    """
    def __init__(self, Map, Fn, B):
        self._map = Map
        self._fn = Fn
        self._B = B.__iter__()

    def __iter__(self):
        return self

    def __next__(self):
        Y = self._B.__next__()

        if isinstance(Y, aplQuantity):
            return self._map(self._fn, Y)

        try:
            return self._fn(Y)
        except TypeError:
            assertError("DOMAIN ERROR")

# ------------------------------

def     iota(B):
    """
    the iterator for monadic ⍳
    """
    IO = indexOrigin()

    return range(IO, B + IO)

# ------------------------------

def     depth(B):
    """
    implement monadic ≡ recursively
    """
    return reduce(
        lambda A, Y: max(A, depth(Y.vectorToPy()) + 1 if isinstance(Y, aplQuantity) else 0), B, 0)

# ------------------------------

def     transpose(B):
    """
    implement monadic ⍉ (for arrays - TBD)
    """
    return B

# ------------------------------

class   reverse(object):
    """
    the iterator for monadic ⌽
    """
    def __init__(self, B):
        self._B = B.__iter__()
        self._T = None

    def __iter__(self):
        return self

    def __next__(self):
        if self._T is None:
            self._T = reverse._stack(self._B)

        if self._T != []:
            return self._T.pop(0)

        return self._B.__next__()

    @staticmethod
    def _stack(B):
        """
        stack the all elements in reverse order
        """
        T = []

        try:
            while True:
                T.insert(0, B.__next__())

        except StopIteration:
            pass

        return T

# ------------------------------
# OLD IMPLEMENTATIONS TO BE REPLACED
# ------------------------------

def     head(B):
    """
    return the first element of B
    """
    return list(B)[0]

# --------------

def     tail(B):
    """
    return everything but the first element of B
    """
    return list(B)[1:]

# --------------

def     unique(B):
    """
    return B with duplicate values removed
    """
    V = []

    for X in B:
        if X not in V:
            V.append(X)

    return V

# EOF
