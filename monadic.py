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

from apl_quantity import s2s
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

# --------------

def     _ceil (B):
    """
    ceil of B with comparison tolerance
    """
    B = integerCT(B)

    if type(B) is int:  return B

    return math.ceil(B)

# --------------

def     _floor (B):
    """
    floor of B with comparison tolerance
    """
    B = integerCT(B)

    if type(B) is int:  return B

    return math.floor(B)

# --------------

def     _magnitude (B):
    """
    absolute value of B
    """
    return math.fabs(B)

# ------------------------------

def     _exp (B):
    """
    e raised to the power B - may raise DOMAIN ERROR
    """
    return math.exp(B)

# --------------

def     _log (B):
    """
    natural logarithm of B
    """
    try:
        return math.log(B)
    except ValueError:
        apl_error("DOMAIN ERROR")

# --------------

def     _roll (B):
    """
    random selection of a number from the range [1,B] - may raise DOMAIN ERROR
    """

    try:
        return random.randint(1,B)
    except ValueError:
        apl_error("DOMAIN ERROR")

# --------------

def     _factorial (B):
    """
    factorial B (also valid for floating point numbers) - may raise DOMAIN ERROR
    """
    B = integerCT(B)

    try:
        if type(B) is int:
            return int(mpmath.factorial(B))
        else:
            return float(mpmath.factorial(B))
    except ValueError:
        apl_error("DOMAIN ERROR")

# ------------------------------

def     _pi (B):
    """
    pi times B (for conversion between Radians and degrees)
    """
    return math.pi * B

# ------------------------------

def     _logical_negation (B):
    """
    Boolean integer inverse of B - may raise DOMAIN ERROR
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

_monadic_functions = {
    # Mathematical
    '+':        lambda B: s2s(_identity,B),
    '-':        lambda B: s2s(_negation,B),
    '×':        lambda B: s2s(_signum,B),
    '÷':        lambda B: s2s(_reciprocal,B),
    '⌈':        lambda B: s2s(_ceil,B),
    '⌊':        lambda B: s2s(_floor,B),
    '|':        lambda B: s2s(_magnitude,B),

    # Algebraic
    '*':        lambda B: s2s(_exp,B),
    '⍟':        lambda B: s2s(_log,B),
    '?':        lambda B: s2s(_roll,B),
    '!':        lambda B: s2s(_factorial,B),
    '⌹':        to_be_implemented,      # matrix inverse

    # Trigonometric
    '○':        lambda B: s2s(_pi,B),

    # Logical
    '~':        lambda B: s2s(_logical_negation,B),

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
    };

# ------------------------------

def     monadic_function (symbol):
    """
    return the monadic function given its APL symbol

    raises INVALID TOKEN if the symbol is not recognised
    """
    try:
        return _monadic_functions[symbol[0]]
    except KeyError:
        apl_error("INVALID TOKEN", symbol)

# EOF
