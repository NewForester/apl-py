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

from system_vars import integerCT, confirm_int, indexOrigin

from apl_quantity import APL_quantity as apl_quantity, s2s, s2v, s_rho, s_comma, v_head, v_tail, v2v, v_nest, v_tally
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

def     _range (B):
    """
    [1, B] or [0, B) depending on ⎕IO
    """
    B = confirm_int(B)

    IO = indexOrigin()

    return range (IO, B + IO)

# ------------------------------

def     _head (B):
    """
    return the first element of B
    """
    return B[0]

# ------------------------------

def     _tail (B):
    """
    return everything but the first element of B
    """
    return B[1:]

# ------------------------------

def     _reverselast (B):
    """
    return B reversed along its last axis
    """
    V = []

    for X in B:
        V = [X] + V

    return V

# ------------------------------

def     _reversefirst (B):
    """
    return B reversed along its first axis
    """
    V = []

    for X in B:
        V = [X] + V

    return V

# ------------------------------

def     _unique (B):
    """
    return B with duplicate values removed
    """
    V = []

    for X in B:
        if X not in V:
            V.append(X)

    return V

# ------------------------------

def     _transpose (B):
    """
    transpose B about its major axis
    """
    return B

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
    '∨':        lambda B: apl_error("VALENCE ERROR"),
    '∧':        lambda B: apl_error("VALENCE ERROR"),
    '⍱':        lambda B: apl_error("VALENCE ERROR"),
    '⍲':        lambda B: apl_error("VALENCE ERROR"),

    # Comparison
    '<':        lambda B: apl_error("VALENCE ERROR"),
    '≤':        lambda B: apl_error("VALENCE ERROR"),
    '=':        lambda B: apl_error("VALENCE ERROR"),
    '≥':        lambda B: apl_error("VALENCE ERROR"),
    '>':        lambda B: apl_error("VALENCE ERROR"),
    '≠':        lambda B: apl_error("VALENCE ERROR"),

    # Structural (aka manipulative)
    '⍳':        lambda B: s2v(_range,B),
    '⍴':        lambda B: s_rho(None,B),
    '≡':        lambda B: v_nest(B),
    '≢':        lambda B: v_tally(B),
    ',':        lambda B: s_comma(None,B),
    '⍪':        lambda B: apl_error("VALENCE ERROR"),
    '⌽':        lambda B: v2v(_reverselast,B),
    '⊖':        lambda B: v2v(_reversefirst,B),
    '⍉':        lambda B: v2v(_transpose,B),
    '∊':        to_be_implemented,      # enlist - ditto but also nested arrays
    '⍷':        lambda B: apl_error("VALENCE ERROR"),
    '⊃':        to_be_implemented,      # (disclose) - turn nested scalar into vector (?!?) - mix ?
    '⊂':        to_be_implemented,      # (enclose) - turn array into nested scalar (?!?)

    # Selection and Set Operations
    '↑':        lambda B: v_head(_head,B),
    '↓':        lambda B: v_tail(_tail,B),
    '∪':        lambda B: v2v(_unique,B),
    '∩':        lambda B: apl_error("VALENCE ERROR"),
    '\\':       lambda B: apl_error("VALENCE ERROR"),
    '/':        lambda B: apl_error("VALENCE ERROR"),
    '⍀':        lambda B: apl_error("VALENCE ERROR"),
    '⌿':        lambda B: apl_error("VALENCE ERROR"),

# Sort
    '⍋':        to_be_implemented,      # grade up (ascending sort indicies)
    '⍒':        to_be_implemented,      # grade down (descending sort indicies)

    # Miscellaneous
    '⊣':        lambda B: apl_quantity(0,None),
    '⊢':        lambda B: B,
    '⊤':        lambda B: apl_error("VALENCE ERROR"),
    '⊥':        lambda B: apl_error("VALENCE ERROR"),
    '⌷':        to_be_implemented,      # materialise
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
