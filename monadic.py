"""
    monadic APL functions

    WIP - This module supports mixed scalar/vector expressions.  Arrays are not supported.

    The base functions are private Python functions.  They take and return one Python number.

    Here a Python number is typically float:  complex numbers are not supported.

    Some functions may raise the APL 'DOMAIN ERROR' but none should raise a Python exception.

    WIP - Many base functions still to implement.
"""

import operator
import math
import random
import mpmath

from system_vars import integerCT

from apl_quantity import monadic2scalar, monadic2vector
from apl_error import apl_error

# ------------------------------

def     _identity (B):
    """
    identity
    """
    return operator.pos(B)

# --------------

def     _negation (B):
    """
    change sign of B
    """
    return operator.neg(B)

# --------------

def     _signum (B):
    """
    sign of B
    """
    if B > 0:   return 1
    if B < 0:   return -1

    return 0

# --------------

def     _reciprocal (B):
    """
    reciprocal of B - may raise DOMAIN ERROR
    """
    try:
        return operator.truediv(1.0,B)
    except:
        apl_error("DOMAIN ERROR")

# ------------------------------

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

    raises FUNCTION NOT YET IMPLEMENTED
    """
    apl_error("FUNCTION NOT YET IMPLEMENTED")

# ------------------------------

monadic_functions = {
    # Mathematical
    '+':        lambda B: monadic2scalar(_identity,B),
    '-':        lambda B: monadic2scalar(_negation,B),
    '×':        lambda B: monadic2scalar(_signum,B),
    '÷':        lambda B: monadic2scalar(_reciprocal,B),
    '⌈':        lambda B: monadic2scalar(ceil,B),
    '⌊':        lambda B: monadic2scalar(floor,B),
    '|':        lambda B: monadic2scalar(magnitude,B),

    # Algebraic
    '*':        lambda B: monadic2scalar(exp,B),
    '⍟':        lambda B: monadic2scalar(log,B),
    '?':        lambda B: monadic2scalar(roll,B),
    '!':        lambda B: monadic2scalar(factorial,B),
    '○':        lambda B: monadic2scalar(pi,B),
    '⌹':        to_be_implemented,      # matrix inverse

    # Logical
    '~':        lambda B: monadic2scalar(logical_negation,B),

# Structural (aka manipulative)
    '⍳':        to_be_implemented,      # index generator
    '≡':        to_be_implemented,      # depth - reports on nesting
    '⍴':        to_be_implemented,      # shape - reports dimensions
    ',':        to_be_implemented,      # unravel - reshape into a vector
    '∊':        to_be_implemented,      # enlist - ditto but also nested arrays
    '⌽':        to_be_implemented,      # reversal, last axis
    '⊖':        to_be_implemented,      # reversal, first axis
    '⍉':        to_be_implemented,      # transpose
    '⊂':        to_be_implemented,      # (enclose) - turn array into nested scalar (?!?)
    '⊃':        to_be_implemented,      # (disclose) - the inverse

# Selection
    '↑':        to_be_implemented,      # take - first element of an array

# Sort
    '⍋':        to_be_implemented,      # grade up (ascending sort indicies)
    '⍒':        to_be_implemented,      # grade down (descending sort indicies)

# Miscellaneous
    '⍕':        to_be_implemented,      # monadic format
    '⍎':        to_be_implemented,      # execute
    '⍬':        to_be_implemented,      # zilde - empty numeric vector - same as ⍳0 or 0⍴0
    };

# ------------------------------

def     monadic_function (symbol):
    """
    return the monadic function given its APL symbol

    raises INVALID TOKEN if the symbol is not recognised
    """
    try:
        return monadic_functions[symbol[0]]
    except KeyError:
        apl_error("INVALID TOKEN", symbol)

# EOF
