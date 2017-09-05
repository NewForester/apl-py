"""
    iterator functions for monadic APL functions

    UNDER DEVELOPMENT

    This module contains functions that implement vector versions of monadic
    APL non-mathematical functions.  Each takes two Python quantities and
    returns a third.

    WIP - the implementation of lazy evaluation means all functions in this
    module are under review.
"""

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
# OLD IMPLEMENTATIONS TO BE REPLACED
# ------------------------------

def     iota(B):
    """
    [1, B] or [0, B) depending on ⎕IO
    """
    B = confirmInteger(B)

    IO = indexOrigin()

    return range(IO, B + IO)

# --------------

def     reverseLast(B):
    """
    return B reversed along its last axis
    """
    V = []

    for X in B:
        V = [X] + V

    return V

# --------------

def     reverseFirst(B):
    """
    return B reversed along its first axis
    """
    V = []

    for X in B:
        V = [X] + V

    return V

# --------------

def     transpose(B):
    """
    transpose B about its major axis
    """
    return B

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
