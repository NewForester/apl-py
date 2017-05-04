#!/usr/bin/python3
"""
    monadic APL functions

    WIP - limited set

    WIP - scalar parameters only
"""

import operator
import math
import random
import mpmath

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
    if B > 0:   return 1
    if B < 0:   return -1

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
        raise (apl_exception("DOMAIN ERROR"))

def     ceil (B):
    """
    ceil

    scalar argument only
    """
    return math.ceil(B)

def     floor (B):
    """
    floor

    scalar argument only
    """
    return math.floor(B)

def     exp (B):
    """
    e raised to the power

    scalar argument only
    """
    return math.exp(B)

def     log (B):
    """
    natural logarithm

    scalar argument only
    """
    try:
        return math.log(B)
    except ValueError:
        raise (apl_exception("DOMAIN ERROR"))

def     magnitude (B):
    """
    absolute value of B

    scalar argument only
    """
    return math.fabs(B)

def     roll (B):
    """
    random selection of a number from the range [1,B]

    scalar argument only
    """

    try:
        return random.randint(1,B)
    except ValueError:
        raise (apl_exception("DOMAIN ERROR"))

def     factorial (B):
    """
    factorial B also valid for floating point numbers

    scalar argument only
    """

    try:
        if type(B) is int:
            return int(mpmath.factorial(B))
        else:
            return float(mpmath.factorial(B))
    except ValueError:
        raise (apl_exception("DOMAIN ERROR"))

def     pi (B):
    """
    identity

    scalar argument only
    """
    return math.pi * B

# ------------------------------

def     logical_negation (B):
    """
    Boolean integer inverse of B

    scalar argument only

    throws DOMAIN ERROR (B is not 0 or 1)
    """
    if B == 1:  return 0
    if B == 0:  return 1

    raise (apl_exception("DOMAIN ERROR"))

# ------------------------------

def     to_be_implemented (B):
    """
    placeholder for functions not yet implemented

    throws FUNCTION NOT YET IMPLEMENTED
    """
    raise (apl_exception("FUNCTION NOT YET IMPLEMENTED"))

# ------------------------------

monadic_functions = {
    # Mathematical
    '+':        identity,
    '-':        negation,
    '×':        signum,
    '÷':        reciprocal,

    '⌈':        ceil,
    '⌊':        floor,
    '*':        exp,
    '⍟':        log,

    '|':        magnitude,
    '?':        roll,
    '!':        factorial,
    '○':        pi,

    # Logical
    '~':        logical_negation,

# Mathematical
    '⌹':        to_be_implemented,      # matrix inverse
# Structural
    '⍴':        to_be_implemented,      # shape
    ',':        to_be_implemented,      # reshape into a vector
    '⌽':        to_be_implemented,      # reversal, last axis
    '⊖':        to_be_implemented,      # reversal, first axis
    '⍉':        to_be_implemented,      # transpose
# Seletion and Set Operations
# Search and Sort
    '⍳':        to_be_implemented,      # index generator
    '⍋':        to_be_implemented,      # grade up
    '⍒':        to_be_implemented,      # grade down
# Miscellaneous
    '⍕':        to_be_implemented,      # monadic format
    '⍎':        to_be_implemented,      # execute
# Operators
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
