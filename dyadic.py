"""
    dyadic APL functions

    WIP - This module supports mixed scalar/vector expressions.  Arrays are not supported.

    The base functions are private Python functions.  They take two and return one Python number.

    Here a Python number is typically float:  complex numbers are not supported.

    Some functions may raise the APL 'DOMAIN ERROR' but none should raise a Python exception.

    WIP - Many base functions still to implement.
"""

import operator
import math
import random
import mpmath

from systemVariables import fuzzyEquals, fuzzyInteger, confirmBoolean, confirmInteger, indexOrigin

from dyadicMaps import ss2s, ss2v, sv_rho, vv_comma, vv2v, vv2s, sv2vr, sv2vl, sv_transpose, ce2v
from dyadicMaps import vv_match, vv2s_decode, vs2v_encode

from aplQuantity import aplQuantity
from aplError import aplError, aplException

# ------------------------------

def     add(A, B):
    """
    A plus B
    """
    return operator.add(A, B)

# --------------

def     subtract(A, B):
    """
    A minus B
    """
    return operator.sub(A, B)

# --------------

def     multiply(A, B):
    """
    A times B
    """
    return operator.mul(A, B)

# --------------

def     divide(A, B):
    """
    A divided by B - may raise DOMAIN ERROR
    """
    try:
        return operator.truediv(A, B)
    except ZeroDivisionError:
        if fuzzyEquals(A, 0) and fuzzyEquals(B, 0):
            return 1

        aplError("DOMAIN ERROR")

# --------------

def     maximum(A, B):
    """
    A maximum B
    """
    return max(A, B)

# --------------

def     minimum(A, B):
    """
    A minimum B
    """
    return min(A, B)

# --------------

def     residue(A, B):
    """
    B modulo A with comparison tolerance
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
    A to the power B - may raise DOMAIN ERROR
    """
    try:
        return math.pow(A, B)
    except ValueError:
        aplError("DOMAIN ERROR")

# --------------

def     log(A, B):
    """
    log to base A of B - may raise DOMAIN ERROR
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

    aplError("DOMAIN ERROR")

# --------------

def     deal(A, B):
    """
    random selection of A numbers from the range [1, B] without replacement - may raise DOMAIN ERROR
    """

    A = confirmInteger(A)
    B = confirmInteger(B)

    try:
        return random.sample(range(1, B+1), A)
    except ValueError:
        aplError("DOMAIN ERROR")

# --------------

def     combinations(A, B):
    """
    number of combinations of size A from a population of size B - may raise DOMAIN ERROR

    for floating point numbers this is binomial(B, A)

    rules for negative integers and floating point are interesting
    """

    try:
        if isinstance(A, int) and isinstance(B, int):
            return int(mpmath.binomial(B, A))

        return float(mpmath.binomial(B, A))
    except ValueError:
        aplError("DOMAIN ERROR")

# ------------------------------

_TrigonometricFunctions = (
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

def     trigonometric(A, B):
    """
    A(B) where A is a trignometic function and B is an angle in Radians

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
        aplError("DOMAIN ERROR")

    function = _TrigonometricFunctions[A+12]
    if function is None:
        return _toBeImplemented(A, B)

    try:
        return function(B)
    except ValueError:
        aplError("DOMAIN ERROR")


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
    A or B (Boolean); GCD(A, B) (otherwise)
    """
    try:
        return int(confirmBoolean(A) + confirmBoolean(B) != 0)
    except aplException:
        return _highestCommonFactor(A, B)

# --------------

def     andLCM(A, B):
    """
    A and B (Boolean); LCM(A, B) (otherwise)
    """
    try:
        return int(confirmBoolean(A) + confirmBoolean(B) == 2)
    except aplException:
        return A * B / _highestCommonFactor(A, B)

# --------------

def     nor(A, B):
    """
    A nor B - may raise DOMAIN ERROR
    """
    return int(confirmBoolean(A) + confirmBoolean(B) == 0)

# --------------

def     nand(A, B):
    """
    A nand B - may raise DOMAIN ERROR
    """
    return int(confirmBoolean(A) + confirmBoolean(B) != 2)

# ------------------------------

def     lt(A, B):
    """
    A < B with comparison tolerance
    """
    if isinstance(A, int) and isinstance(B, int):
        return int(operator.lt(A, B))

    if fuzzyEquals(A, B):
        return 0

    return int(operator.lt(A, B))

# --------------

def     le(A, B):
    """
    A <= B
    """
    if isinstance(A, int) and isinstance(B, int):
        return int(operator.le(A, B))

    if fuzzyEquals(A, B):
        return 1

    return int(operator.le(A, B))

# --------------

def     eq(A, B):
    """
    A == B with comparison tolerance
    """
    if isinstance(A, int) and isinstance(B, int):
        return int(operator.eq(A, B))

    return int(fuzzyEquals(A, B))

# --------------

def     ge(A, B):
    """
    A >= B with comparison tolerance
    """
    if isinstance(A, int) and isinstance(B, int):
        return int(operator.ge(A, B))

    if fuzzyEquals(A, B):
        return 1

    return int(operator.ge(A, B))

# --------------

def     gt(A, B):
    """
    A > B with comparison tolerance
    """
    if isinstance(A, int) and isinstance(B, int):
        return int(operator.gt(A, B))

    if fuzzyEquals(A, B):
        return 0

    return int(operator.gt(A, B))

# --------------

def     ne(A, B):
    """
    A != B with comparison tolerance
    """
    if isinstance(A, int) and isinstance(B, int):
        return int(operator.ne(A, B))

    if isinstance(A, aplQuantity) or isinstance(B, aplQuantity):
        return True

    return int(not fuzzyEquals(A, B))

# ------------------------------

def     without(A, B):
    """
    remove (elements of B) from (list) A
    """
    A = list(A)

    for X in B:
        try:
            while True:
                A.remove(X)
        except ValueError:
            pass

    return A

# --------------

def     index(A, B):
    """
    index(es) of (elements of) B in (list) A
    """
    V = []
    IO = indexOrigin()

    A = list(A)

    for X in B:
        try:
            V.append(A.index(X) + IO)
        except ValueError:
            V.append(len(A) + IO)

    return V

# --------------

def     take(A, B):
    """
    take A elements from B
    """
    A = confirmInteger(A)

    if isinstance(B, str):
        pad = ' '
    else:
        pad = [0]
        B = list(B)

    LB = len(B)

    if A < 0:
        length = LB + A

        if length < 0:
            R = (pad * (0 - length)) + B
        else:
            R = B[length:]
    else:
        length = LB - A

        if length < 0:
            R = B + (pad * (0 - length))
        else:
            R = B[:A]

    return R

# --------------

def     drop(A, B):
    """
    drop A elements from B
    """
    A = confirmInteger(A)
    if not isinstance(B, str):
        B = list(B)
    LB = len(B)

    if A >= 0:
        return B[A:]

    if LB + A >= 0:
        return B[:LB + A]

    return []

# --------------

def     rotateLast(A, B):
    """
    rotate (vector) B by A elements
    """
    A = confirmInteger(A) % len(B)

    return B[A:] + B[:A]

# --------------

def     rotateFirst(A, B):
    """
    rotate (vector) B by A elements
    """
    A = confirmInteger(A) % len(B)

    return B[A:] + B[:A]

# ------------------------------

def     reshape(A, B):
    """
    reshape (list) B to have length A by replication and/or truncation
    """
    A = confirmInteger(A)

    if A < 0:
        aplError("DOMAIN ERROR")

    B = list(B)

    length = len(B)

    tail = A % length

    count = int((A - tail) / length)

    return B * count + B [:tail]

# ------------------------------

def     concatenation(A, B):
    """
    concatenate (list) B onto the end of (list) A
    """
    return A + B

# ------------------------------

def     union(A, B):
    """
    return union of B with A

    NB  only good for homogeneous operands
    """
    V = list(A)

    for X in B:
        if X not in A:
            V.append(X)

    return V

# ------------------------------

def     intersection(A, B):
    """
    return intersection of of B with A

    NB  only good for homogeneous operands
    """
    V = []

    for X in A:
        if X in B:
            V.append(X)

    return V

# ------------------------------

def     transpose(_, B):
    """
    transpose B about A
    """
    return B

# ------------------------------

def     compress(A, B, pad):
    """
    compress/replicate B using A as the template
    """

    R = []

    I = B.__iter__()

    try:
        for X in A:
            X = confirmInteger(X)

            V = I.__next__()

            if X > 0:
                for _ in range(X):
                    R.append(V)
            elif X < 0:
                for _ in range(-X):
                    R.append(pad)
            else:
                pass

    except StopIteration:
        if len(A) > 1:
            aplError("LENGTH ERROR")

    try:
        V = I.__next__()
    except StopIteration:
        pass
    else:
        aplError("LENGTH ERROR")

    return R

# ------------------------------

def     expand(A, B, pad):
    """
    expand B using A as the template
    """
    V = []

    I = B.__iter__()

    try:
        for X in A:
            X = confirmInteger(X)

            if X > 0:
                S = I.__next__()
                for _ in range(X):
                    V.append(S)
            elif X < 0:
                for _ in range(-X):
                    V.append(pad)
            else:
                V.append(pad)

    except StopIteration:
        aplError("LENGTH ERROR")

    try:
        S = I.__next__()
    except StopIteration:
        pass
    else:
        aplError("LENGTH ERROR")

    return V

# ------------------------------

def     encode(A, B):
    """
    encode (scalar) B using (vector) A as base
    """
    V = []

    for X in reversed(A):
        if X != 0:
            V = [operator.mod(B, X)] + V
            B = operator.floordiv(B, X)
        else:
            V = [B] + V
            B = 0

    return V

# ------------------------------

def     decode(A, B):
    """
    decode (vector) B using (vector) A as base
    """
    S = 0

    I = B.__iter__()

    try:
        for X in A:
            S = S * X + I.__next__()
    except StopIteration:
        pass

    return S

# ------------------------------

def     _toBeImplemented(_, __):
    """
    placeholder for functions not yet implemented

    raises FUNCTION NOT YET IMPLEMENTED
    """
    aplError("FUNCTION NOT YET IMPLEMENTED")

# ------------------------------

_DyadicFunctions = {
    # Arithmetic
    '+':        lambda A, B: ss2s(add, A, B, True),
    '-':        lambda A, B: ss2s(subtract, A, B, True),
    '×':        lambda A, B: ss2s(multiply, A, B, True),
    '÷':        lambda A, B: ss2s(divide, A, B, True),
    '⌈':        lambda A, B: ss2s(maximum, A, B, True),
    '⌊':        lambda A, B: ss2s(minimum, A, B, True),
    '|':        lambda A, B: ss2s(residue, A, B, True),

    # Algebraic
    '*':        lambda A, B: ss2s(exp, A, B, True),
    '⍟':        lambda A, B: ss2s(log, A, B, True),
    '?':        lambda A, B: ss2v(deal, A, B),
    '!':        lambda A, B: ss2s(combinations, A, B, True),
    '⌹':        _toBeImplemented,       # matrix divide

    # Trigonometric
    '○':        lambda A, B: ss2s(trigonometric, A, B, True),

    # Logical
    '∨':        lambda A, B: ss2s(orGCD, A, B, True),
    '∧':        lambda A, B: ss2s(andLCM, A, B, True),
    '⍱':        lambda A, B: ss2s(nor, A, B, True),
    '⍲':        lambda A, B: ss2s(nand, A, B, True),

    # Comparison
    '<':        lambda A, B: ss2s(lt, A, B, True),
    '≤':        lambda A, B: ss2s(le, A, B, True),
    '=':        lambda A, B: ss2s(eq, A, B, False),
    '≥':        lambda A, B: ss2s(ge, A, B, True),
    '>':        lambda A, B: ss2s(gt, A, B, True),
    '≠':        lambda A, B: ss2s(ne, A, B, False),
    '≡':        lambda A, B: vv_match(ne, A, B, False),
    '≢':        lambda A, B: vv_match(ne, A, B, True),

    # Structural (aka manipulative)
    '⍴':        lambda A, B: sv_rho(reshape, A, B),
    ',':        lambda A, B: vv_comma(concatenation, A, B),
    '⍪':        lambda A, B: vv_comma(concatenation, A, B),
    '⌽':        lambda A, B: sv2vr(rotateLast, A, B),
    '⊖':        lambda A, B: sv2vr(rotateFirst, A, B),
    '⍉':        lambda A, B: sv_transpose(transpose, A, B),
    '⊃':        _toBeImplemented,       # pick (disclose) = picks from an array (?!?)
    '⊂':        _toBeImplemented,       # partitioned enclose - creates an array of vectors (?!?)

    # Selection and Set Operations
    '~':        lambda A, B: vv2v(without, A, B),
    '⍳':        lambda A, B: vv2s(index, A, B),
    '↓':        lambda A, B: sv2vl(drop, A, B),
    '↑':        lambda A, B: sv2vl(take, A, B),
    '⌷':        _toBeImplemented,       # index
    '∪':        lambda A, B: vv2v(union, A, B),
    '∩':        lambda A, B: vv2v(intersection, A, B),
    '/':        lambda A, B: ce2v(compress, A, B),
    '⌿':        lambda A, B: ce2v(compress, A, B),
    '\\':       lambda A, B: ce2v(expand, A, B),
    '⍀':        lambda A, B: ce2v(expand, A, B),

    # Miscellaneous
    '∊':        _toBeImplemented,       # membership - is A in B (also characters)
    '⍷':        _toBeImplemented,       # find (look for a substring)
    '⍋':        _toBeImplemented,       # sort ascending with specified collating sequence
    '⍒':        _toBeImplemented,       # sort descending with specified collating sequence
    '⍺':        _toBeImplemented,       # picture format
    '⍕':        _toBeImplemented,       # dyadic (specification) format
    '⍎':        _toBeImplemented,       # dyadic execute
    '⊤':        lambda A, B: vs2v_encode(encode, A, B),
    '⊥':        lambda A, B: vv2s_decode(decode, A, B),
    '⊣':        lambda A, B: A,
    '⊢':        lambda A, B: B,
}

# ------------------------------

def     dyadicFunction(symbol):
    """
    return the dyadic function given its APL symbol

    raises INVALID TOKEN if the symbol is not recognised
    """
    try:
        return _DyadicFunctions[symbol[0]]
    except KeyError:
        aplError("INVALID TOKEN", symbol)

# EOF
