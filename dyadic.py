#!/usr/bin/python3
"""
    dyadic APL functions

    WIP - limited set

    WIP - scalar parameters only
"""

import operator

from apl_exception import APL_Exception as apl_exception

# --------------

def     add (A,B):
    """
    A plus B

    scalar arguments only
    """
    return operator.add(A,B)

def     subtract (A,B):
    """
    A minus B

    scalar arguments only
    """
    return operator.sub(A,B)

def     multiply (A,B):
    """
    A multiplied by B

    scalar arguments only
    """
    return operator.mul(A,B)

def     divide (A,B):
    """
    A divided by B

    scalar arguments only

    throws RANGE ERROR (B == 0)
    """
    try:
        return operator.truediv(A,B)
    except:
        raise (apl_exception("RANGE ERROR"))

def     to_be_implemented (A,B):
    """
    placeholder for functions not yet implemented

    throws FUNCTION NOT YET IMPLEMENTED
    """
    raise (apl_exception("FUNCTION NOT YET IMPLEMENTED"))

# ------------------------------

dyadic_functions = {
    '+':        add,
    '-':        subtract,
    '×':        multiply,
    '÷':        divide,
    '*':        to_be_implemented,
    };

def     dyadic_function (symbol):
    """
    return the dyadic function given its APL symbol

    throws INVALID TOKEN if the symbol is not recognised
    """
    try:
        return dyadic_functions[symbol[0]]
    except KeyError:
        raise (apl_exception("INVALID TOKEN", symbol))

# EOF
