#!/usr/bin/python3
"""
    monadic APL functions

    WIP - limited set

    WIP - scalar parameters only
"""

import operator

from apl_exception import APL_Exception as apl_exception

# ------------------------------

def     identity (B):
    """
    identity

    scalar argument only
    """
    return operator.pos(B)

def     negation (B):
    """
    change sign of B

    scalar argument only
    """
    return operator.neg(B)

def     signum (B):
    """
    sign of B

    scalar argument only
    """
    if B:
        if B > 0:
            return 1
        else:
            return -1
    else:
        return 0

def     reciprocal (B):
    """
    1 divided by B

    scalar argument only

    throws RANGE ERROR (B == 0)
    """
    try:
        return operator.truediv(1.0,B)
    except:
        raise (apl_exception("RANGE ERROR"))

def     to_be_implemented (B):
    """
    placeholder for functions not yet implemented

    throws FUNCTION NOT YET IMPLEMENTED
    """
    raise (apl_exception("FUNCTION NOT YET IMPLEMENTED"))

# ------------------------------

monadic_functions = {
    '+':        identity,
    '-':        negation,
    '×':        signum,
    '÷':        reciprocal,
    '*':        to_be_implemented,
    };

def     monadic_function (symbol):
    """
    return the monadic function given its APL symbol

    throws INVALID TOKEN if the symbol is not recognised
    """
    try:
        return monadic_functions[symbol[0]]
    except KeyError:
        raise (apl_exception("INVALID TOKEN", symbol))

# EOF
