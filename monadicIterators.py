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
    return B[0]

# --------------

def     tail(B):
    """
    return everything but the first element of B
    """
    return B[1:]

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
