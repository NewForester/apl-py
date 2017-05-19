"""
    monadic APL functions

    WIP - limited set

    WIP - extended to handle APL scalars and vectors
"""

import operator
import math
import random
import mpmath

from system_vars import integerCT

from apl_quantity import monadic2scalar, monadic2vector
from apl_error import apl_error

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
        apl_error("DOMAIN ERROR")

def     ceil (B):
    """
    ceil with comparison tolerance

    scalar argument only
    """
    B = integerCT(B)

    if type(B) is int:  return B

    return math.ceil(B)

def     floor (B):
    """
    floor with comparison tolerance

    scalar argument only
    """
    B = integerCT(B)

    if type(B) is int:  return B

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
        apl_error("DOMAIN ERROR")

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
        apl_error("DOMAIN ERROR")

def     factorial (B):
    """
    factorial B also valid for floating point numbers

    scalar argument only
    """
    B = integerCT(B)

    try:
        if type(B) is int:
            return int(mpmath.factorial(B))
        else:
            return float(mpmath.factorial(B))
    except ValueError:
        apl_error("DOMAIN ERROR")

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
    B = integerCT(B)

    if B == 1:  return 0
    if B == 0:  return 1

    apl_error("DOMAIN ERROR")

# ------------------------------

def     to_be_implemented (B):
    """
    placeholder for functions not yet implemented

    throws FUNCTION NOT YET IMPLEMENTED
    """
    apl_error("FUNCTION NOT YET IMPLEMENTED")

# ------------------------------

monadic_functions = {
    # Mathematical
    '+':        lambda B: monadic2scalar(identity,B),
    '-':        lambda B: monadic2scalar(negation,B),
    '×':        lambda B: monadic2scalar(signum,B),
    '÷':        lambda B: monadic2scalar(reciprocal,B),

    '⌈':        lambda B: monadic2scalar(ceil,B),
    '⌊':        lambda B: monadic2scalar(floor,B),
    '*':        lambda B: monadic2scalar(exp,B),
    '⍟':        lambda B: monadic2scalar(log,B),

    '|':        lambda B: monadic2scalar(magnitude,B),
    '?':        lambda B: monadic2scalar(roll,B),
    '!':        lambda B: monadic2scalar(factorial,B),
    '○':        lambda B: monadic2scalar(pi,B),

    # Logical
    '~':        lambda B: monadic2scalar(logical_negation,B),

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

# ------------------------------

def     monadic_function (symbol):
    """
    return the monadic function given its APL symbol

    throws INVALID TOKEN if the symbol is not recognised
    """
    try:
        return monadic_functions[symbol[0]]
    except KeyError:
        apl_error("INVALID TOKEN", symbol)

# EOF
