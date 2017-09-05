"""
    scalar monadic APL functions

    This module contains the scalar versions of monadic APL mathematical
    functions.  Each takes a scalar numeric Python value and returns another.

    Matrix inverse (monadic ⌹) is not implemented here.

    Comparison tolerance (⎕CT) is used in functions involving a comparison
    (explicit or implicit) or integer rounding.

    Several functions may raise DOMAIN ERROR.  This is typically, but not
    exclusively, in response to Python raising an exception, typically, but
    not exclusively, ValueError

    All functions may raise TypeError, which the caller is expected to convert
    to DOMAIN ERROR.  This very often indicates the function has been passed
    a string value and is to be expected.
"""

import operator
import math
import random
import mpmath

from systemVariables import fuzzyInteger

from aplError import assertError

# ------------------------------

def     identity(B):
    """
    + B
    """
    return operator.pos(B)

# --------------

def     negation(B):
    """
    - B
    """
    return operator.neg(B)

# --------------

def     signum(B):
    """
    × B
    """
    if B > 0:
        return 1
    if B < 0:
        return -1

    return 0

# --------------

def     reciprocal(B):
    """
    ÷ B
    """
    try:
        return operator.truediv(1.0, B)
    except ZeroDivisionError:
        assertError("DOMAIN ERROR")

# --------------

def     ceil(B):
    """
    ⌈ B
    """
    B = fuzzyInteger(B)

    if isinstance(B, int):
        return B

    return math.ceil(B)

# --------------

def     floor(B):
    """
    ⌊ B
    """
    B = fuzzyInteger(B)

    if isinstance(B, int):
        return B

    return math.floor(B)

# --------------

def     magnitude(B):
    """
    | B
    """
    return math.fabs(B)

# ------------------------------

def     exp(B):
    """
    * B
    """
    return math.exp(B)

# --------------

def     log(B):
    """
    ⍟ B
    """
    try:
        return math.log(B)
    except ValueError:
        assertError("DOMAIN ERROR")

# --------------

def     factorial(B):
    """
    ! B
    """
    B = fuzzyInteger(B)

    try:
        if isinstance(B, int):
            return int(mpmath.factorial(B))

        return float(mpmath.factorial(B))
    except ValueError:
        assertError("DOMAIN ERROR")

# --------------

def     roll(B):
    """
    ? B
    """
    try:
        return random.randint(1, B)
    except ValueError:
        assertError("DOMAIN ERROR")

# ------------------------------

def     pi(B):
    """
    ○ B
    """
    return math.pi * B

# ------------------------------

def     logicalNegation(B):
    """
    ~ B
    """
    B = fuzzyInteger(B)

    if B == 1:
        return 0
    if B == 0:
        return 1

    assertError("DOMAIN ERROR")

# EOF
