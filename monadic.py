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

from systemVariables import fuzzyInteger, confirmInteger, indexOrigin

from monadicMaps import s2s, s2v, s_rho, s_comma, v_head, v_tail, v2v, v_nest, v_tally

from aplQuantity import makeScalar
from aplError import aplError

# ------------------------------

def     identity(B):
    """
    identity
    """
    return operator.pos(B)

# --------------

def     negation(B):
    """
    change sign of B
    """
    return operator.neg(B)

# --------------

def     signum(B):
    """
    sign of B
    """
    if B > 0:
        return 1
    if B < 0:
        return -1

    return 0

# --------------

def     reciprocal(B):
    """
    reciprocal of B - may raise DOMAIN ERROR
    """
    try:
        return operator.truediv(1.0, B)
    except ZeroDivisionError:
        aplError("DOMAIN ERROR")

# --------------

def     ceil(B):
    """
    ceil of B with comparison tolerance
    """
    B = fuzzyInteger(B)

    if isinstance(B, int):
        return B

    return math.ceil(B)

# --------------

def     floor(B):
    """
    floor of B with comparison tolerance
    """
    B = fuzzyInteger(B)

    if isinstance(B, int):
        return B

    return math.floor(B)

# --------------

def     magnitude(B):
    """
    absolute value of B
    """
    return math.fabs(B)

# ------------------------------

def     exp(B):
    """
    e raised to the power B - may raise DOMAIN ERROR
    """
    return math.exp(B)

# --------------

def     log(B):
    """
    natural logarithm of B
    """
    try:
        return math.log(B)
    except ValueError:
        aplError("DOMAIN ERROR")

# --------------

def     roll(B):
    """
    random selection of a number from the range [1, B] - may raise DOMAIN ERROR
    """

    try:
        return random.randint(1, B)
    except ValueError:
        aplError("DOMAIN ERROR")

# --------------

def     factorial(B):
    """
    factorial B (also valid for floating point numbers) - may raise DOMAIN ERROR
    """
    B = fuzzyInteger(B)

    try:
        if isinstance(B, int):
            return int(mpmath.factorial(B))

        return float(mpmath.factorial(B))
    except ValueError:
        aplError("DOMAIN ERROR")

# ------------------------------

def     pi(B):
    """
    pi times B (for conversion between Radians and degrees)
    """
    return math.pi * B

# ------------------------------

def     logicalNegation(B):
    """
    Boolean integer inverse of B - may raise DOMAIN ERROR
    """
    B = fuzzyInteger(B)

    if B == 1:
        return 0
    if B == 0:
        return 1

    aplError("DOMAIN ERROR")

# ------------------------------

def     iota(B):
    """
    [1, B] or [0, B) depending on ⎕IO
    """
    B = confirmInteger(B)

    IO = indexOrigin()

    return range(IO, B + IO)

# ------------------------------

def     head(B):
    """
    return the first element of B
    """
    return B[0]

# ------------------------------

def     tail(B):
    """
    return everything but the first element of B
    """
    return B[1:]

# ------------------------------

def     reverseLast(B):
    """
    return B reversed along its last axis
    """
    V = []

    for X in B:
        V = [X] + V

    return V

# ------------------------------

def     reverseFirst(B):
    """
    return B reversed along its first axis
    """
    V = []

    for X in B:
        V = [X] + V

    return V

# ------------------------------

def     unique(B):
    """
    return B with duplicate values removed
    """
    V = []

    for X in B:
        if X not in V:
            V.append(X)

    return V

# ------------------------------

def     transpose(B):
    """
    transpose B about its major axis
    """
    return B

# ------------------------------

def     _toBeImplemented(_):
    """
    placeholder for functions not yet implemented

    raises FUNCTION NOT YET IMPLEMENTED
    """
    aplError("FUNCTION NOT YET IMPLEMENTED")

# ------------------------------

_MonadicFunctions = {
    # Arithmetic
    '+':        lambda B: s2s(identity, B),
    '-':        lambda B: s2s(negation, B),
    '×':        lambda B: s2s(signum, B),
    '÷':        lambda B: s2s(reciprocal, B),
    '⌈':        lambda B: s2s(ceil, B),
    '⌊':        lambda B: s2s(floor, B),
    '|':        lambda B: s2s(magnitude, B),

    # Algebraic
    '*':        lambda B: s2s(exp, B),
    '⍟':        lambda B: s2s(log, B),
    '?':        lambda B: s2s(roll, B),
    '!':        lambda B: s2s(factorial, B),
    '⌹':        _toBeImplemented,       # matrix inverse

    # Trigonometric
    '○':        lambda B: s2s(pi, B),

    # Logical
    '~':        lambda B: s2s(logicalNegation, B),
    '∨':        lambda B: aplError("VALENCE ERROR"),
    '∧':        lambda B: aplError("VALENCE ERROR"),
    '⍱':        lambda B: aplError("VALENCE ERROR"),
    '⍲':        lambda B: aplError("VALENCE ERROR"),

    # Comparison
    '<':        lambda B: aplError("VALENCE ERROR"),
    '≤':        lambda B: aplError("VALENCE ERROR"),
    '=':        lambda B: aplError("VALENCE ERROR"),
    '≥':        lambda B: aplError("VALENCE ERROR"),
    '>':        lambda B: aplError("VALENCE ERROR"),
    '≠':        lambda B: aplError("VALENCE ERROR"),

    # Structural (aka manipulative)
    '⍳':        lambda B: s2v(iota, B),
    '≡':        lambda B: v_nest(B),
    '≢':        lambda B: v_tally(B),
    '⍴':        lambda B: s_rho(None, B),
    ',':        lambda B: s_comma(None, B),
    '⍪':        lambda B: aplError("VALENCE ERROR"),
    '∊':        _toBeImplemented,       # enlist - as comma but also nested arrays
    '⌽':        lambda B: v2v(reverseLast, B),
    '⊖':        lambda B: v2v(reverseFirst, B),
    '⍉':        lambda B: v2v(transpose, B),
    '⊃':        _toBeImplemented,       # (disclose) - turn nested scalar into vector (?!?) - mix ?
    '⊂':        _toBeImplemented,       # (enclose) - turn array into nested scalar (?!?)

    # Selection and Set Operations
    '↑':        lambda B: v_head(head, B),
    '↓':        lambda B: v_tail(tail, B),
    '⌷':        lambda B: aplError("VALENCE ERROR"),
    '∪':        lambda B: v2v(unique, B),
    '∩':        lambda B: aplError("VALENCE ERROR"),
    '/':        lambda B: aplError("VALENCE ERROR"),
    '⌿':        lambda B: aplError("VALENCE ERROR"),
    '\\':       lambda B: aplError("VALENCE ERROR"),
    '⍀':        lambda B: aplError("VALENCE ERROR"),

    # Miscellaneous
    '⍷':        lambda B: aplError("VALENCE ERROR"),
    '⍋':        _toBeImplemented,       # grade up (ascending sort indicies)
    '⍒':        _toBeImplemented,       # grade down (descending sort indicies)
    '⍺':        lambda B: aplError("VALENCE ERROR"),
    '⍕':        _toBeImplemented,       # monadic format
    '⍎':        _toBeImplemented,       # execute
    '⊤':        lambda B: aplError("VALENCE ERROR"),
    '⊥':        lambda B: aplError("VALENCE ERROR"),
    '⊣':        lambda B: makeScalar(0),
    '⊢':        lambda B: B,
}

# ------------------------------

def     monadicFunction(symbol):
    """
    return the monadic function given its APL symbol

    raises INVALID TOKEN if the symbol is not recognised
    """
    try:
        return _MonadicFunctions[symbol[0]]
    except KeyError:
        aplError("INVALID TOKEN", symbol)

# EOF
