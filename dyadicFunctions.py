"""
    scalar dyadic APL functions

    This module contains the scalar versions of dyadic APL mathematical
    functions.  Generally speaking, each takes two scalar numeric Python
    values and returns a third.

    The equality (=) and inequality (≠) functions are exceptions to the
    numeric rule for they also used to compare string types.

    The deal (?) function is another exception for it returns not a simple
    scalar value but a tuple of scalar values.

    Matrix divide (dyadic ⌹) is not implemented here.

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

from systemVariables import fuzzyEquals, fuzzyInteger, confirmBoolean, confirmInteger

from aplError import aplException, assertError

# ------------------------------

def     add(A, B):
    """
    A + B
    """
    if isinstance(A, str) or isinstance(B, str):
        raise TypeError

    return operator.add(A, B)

# --------------

def     subtract(A, B):
    """
    A - B
    """
    return operator.sub(A, B)

# --------------

def     multiply(A, B):
    """
    A × B
    """
    if isinstance(A, str) or isinstance(B, str):
        raise TypeError

    return operator.mul(A, B)

# --------------

def     divide(A, B):
    """
    A ÷ B
    """
    try:
        return operator.truediv(A, B)
    except ZeroDivisionError:
        if fuzzyEquals(A, 0) and fuzzyEquals(B, 0):
            return 1

        assertError("DOMAIN ERROR")

# --------------

def     maximum(A, B):
    """
    A ⌈ B
    """
    if isinstance(A, str) or isinstance(B, str):
        raise TypeError

    return max(A, B)

# --------------

def     minimum(A, B):
    """
    A ⌊ B
    """
    if isinstance(A, str) or isinstance(B, str):
        raise TypeError

    return min(A, B)

# --------------

def     residue(A, B):
    """
    A | B
    """
    if isinstance(A, int):
        if A == 0:
            return B
    else:
        if fuzzyEquals(A, 0):
            return B

    if isinstance(fuzzyInteger(operator.truediv(B, A)), int):
        return 0

    R = math.fmod(B, A)

    if (R < 0) != (A < 0):
        R += A

    if isinstance(A, int) and isinstance(B, int):
        R = int(R)

    return R

# ------------------------------

def     exp(A, B):
    """
    A * B
    """
    try:
        return math.pow(A, B)
    except ValueError:
        assertError("DOMAIN ERROR")

# --------------

def     log(A, B):
    """
    A ⍟ B
    """
    try:
        if A == 10:
            return math.log10(B)

        # Python 3.3 and later # if A == 2:  return math.log2(B)

        return math.log(B, A)

    except ValueError:
        if fuzzyEquals(A, B):
            return 1.0
        if fuzzyEquals(A, 0):
            return 0.0
        if fuzzyEquals(B, 1):
            return 0.0

    except ZeroDivisionError:
        if fuzzyEquals(A, B):
            return 1.0

    assertError("DOMAIN ERROR")

# --------------

def     binomial(A, B):
    """
    A ! B
    """
    try:
        if isinstance(A, int) and isinstance(B, int):
            return int(mpmath.binomial(B, A))

        return float(mpmath.binomial(B, A))
    except ValueError:
        assertError("DOMAIN ERROR")

# --------------

def     deal(A, B):
    """
    A ? B
    """
    A = confirmInteger(A)
    B = confirmInteger(B)

    try:
        return tuple(random.sample(range(1, B+1), A))
    except ValueError:
        assertError("DOMAIN ERROR")

# ------------------------------

_CircularFunctions = (
    None,               # -12
    None,
    None,
    None,
    None,               # -8
    math.atanh,
    math.acosh,
    math.asinh,
    lambda x: math.sqrt(x*x-1), # -4
    math.atan,
    math.acos,
    math.asin,
    lambda x: math.sqrt(1-x*x), # 0
    math.sin,
    math.cos,
    math.tan,
    lambda x: math.sqrt(x*x+1), # +4
    math.sinh,
    math.cosh,
    math.tanh,
    None,               # +8
    None,
    None,
    None,
    None,               # +12
)

# --------------

def     circular(A, B):
    """
    A ○ B

    A is valid in the range [-12, +12].  The following are implemented:

    ¯7  atanh(B)
    ¯6  acosh(B)
    ¯5  asinh(B)
    ¯4  sqrt(B**2-1)
    ¯3  atan(B)
    ¯2  acos(B)
    ¯1  asin(B)
     0  sqrt(1-B**2)
     1  sin(B)
     2  cos(B)
     3  tan(B)
     4  sqrt(B**2+1)
     5  sinh(B)
     6  cosh(B)
     7  tanh(B)
    """
    A = confirmInteger(A)

    if A <= -12 or A >= 12:
        assertError("DOMAIN ERROR")

    function = _CircularFunctions[A+12]
    if function is None:
        assertError("FUNCTION NOT YET IMPLEMENTED")

    try:
        return function(B)
    except ValueError:
        assertError("DOMAIN ERROR")

# ------------------------------

def     _highestCommonFactor(A, B):
    """
    Highest Common Factor by the Euclid method

    Note: math.gcd() is Python 3.5 and later
    """
    if B == 0:
        return abs(A)

    return _highestCommonFactor(B, A % B)

# --------------

def     orGCD(A, B):
    """
    A ∨ B
    """
    try:
        return int(confirmBoolean(A) + confirmBoolean(B) != 0)
    except aplException:
        return _highestCommonFactor(A, B)

# --------------

def     andLCM(A, B):
    """
    A ∧ B
    """
    try:
        return int(confirmBoolean(A) + confirmBoolean(B) == 2)
    except aplException:
        return A * B / _highestCommonFactor(A, B)

# --------------

def     nor(A, B):
    """
    A ⍱ B
    """
    return int(confirmBoolean(A) + confirmBoolean(B) == 0)

# --------------

def     nand(A, B):
    """
    A ⍲ B
    """
    return int(confirmBoolean(A) + confirmBoolean(B) != 2)

# ------------------------------

def     lt(A, B):
    """
    A < B
    """
    if isinstance(A, int) and isinstance(B, int):
        return int(operator.lt(A, B))

    if fuzzyEquals(A, B):
        return 0

    return int(operator.lt(A, B))

# --------------

def     le(A, B):
    """
    A ≤ B
    """
    if isinstance(A, int) and isinstance(B, int):
        return int(operator.le(A, B))

    if fuzzyEquals(A, B):
        return 1

    return int(operator.le(A, B))

# --------------

def     ge(A, B):
    """
    A ≥ B
    """
    if isinstance(A, int) and isinstance(B, int):
        return int(operator.ge(A, B))

    if fuzzyEquals(A, B):
        return 1

    return int(operator.ge(A, B))

# --------------

def     gt(A, B):
    """
    A > B
    """
    if isinstance(A, int) and isinstance(B, int):
        return int(operator.gt(A, B))

    if fuzzyEquals(A, B):
        return 0

    return int(operator.gt(A, B))

# --------------

def     eq(A, B):
    """
    A = B
    """
    if isinstance(A, int) and isinstance(B, int):
        return int(operator.eq(A, B))

    if isinstance(A, str) and isinstance(B, str):
        return int(operator.eq(ord(A), ord(B)))

    try:
        return int(fuzzyEquals(A, B))
    except TypeError:
        return 0

# --------------

def     ne(A, B):
    """
    A ≠ B
    """
    if isinstance(A, int) and isinstance(B, int):
        return int(operator.ne(A, B))

    if isinstance(A, str) and isinstance(B, str):
        return int(operator.ne(ord(A), ord(B)))

    try:
        return int(not fuzzyEquals(A, B))
    except TypeError:
        return 1

# EOF
