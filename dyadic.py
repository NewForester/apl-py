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

from system_vars import confirm_bool, confirm_int, equalCT, integerCT

from apl_quantity import dyadic2scalar, dyadic2vector
from apl_error import apl_error

# ------------------------------

trigonometric_functions = (
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

# ------------------------------

def     _add (A,B):
    """
    A plus B
    """
    return operator.add(A,B)

# --------------

def     _subtract (A,B):
    """
    A minus B
    """
    return operator.sub(A,B)

# --------------

def     _multiply (A,B):
    """
    A times B
    """
    return operator.mul(A,B)

# --------------

def     _divide (A,B):
    """
    A divided by B - may raise DOMAIN ERROR
    """
    try:
        return operator.truediv(A,B)
    except:
        if equalCT(A,0) and equalCT(B,0):   return 1

        apl_error("DOMAIN ERROR")

# --------------

def     _maximum (A,B):
    """
    A maximum B
    """
    return max(A,B)

# --------------

def     _minimum (A,B):
    """
    A minimum B
    """
    return min(A,B)

# --------------

def     _residue (A,B):
    """
    B modulo A with comparison tolerance
    """
    if type(A) is int:
        if A == 0:          return B
    else:
        if equalCT(A,0):    return B

    if type(integerCT(operator.truediv(B,A))) is int:
        return 0

    result = math.fmod(B,A)

    if result < 0:
        if A > 0:       result += A
    elif result > 0:
        if A < 0:       result += A
    else:
        result = 0.0

    if type(A) is int and type(B) is int:
        return int(result)
    else:
        return result

# ------------------------------

def     _exp (A,B):
    """
    A to the power B - may raise DOMAIN ERROR
    """
    try:
        return math.pow(A,B)
    except ValueError:
        apl_error("DOMAIN ERROR")

# --------------

def     _log (A,B):
    """
    log to base A of B - may raise DOMAIN ERROR
    """
    try:
        if A == 10: return math.log10(B)
        # Python 3.3 and later # if A == 2:  return math.log2(B)

        return math.log(B,A)

    except ValueError:
        if equalCT(A,B):  return 1.0
        if equalCT(A,0):  return 0.0
        if equalCT(B,1):  return 0.0

    except ZeroDivisionError:
        if equalCT(A,B):  return 1.0

    apl_error("DOMAIN ERROR")

# --------------

def     _deal (A,B):
    """
    random selection of A numbers from the range [1,B] without replacement - may raise DOMAIN ERROR
    """

    A = confirm_int(A)
    B = confirm_int(B)

    try:
        return random.sample(range(1,B+1),A)
    except ValueError:
        apl_error("DOMAIN ERROR")

# --------------

def     _combinations (A,B):
    """
    number of combinations of size A from a population of size B - may raise DOMAIN ERROR

    for floating point numbers this is binomial(B,A)

    rules for negative integers and floating point are interesting
    """

    try:
        if type(A) is int and type(B) is int:
            return int(mpmath.binomial(B,A))
        else:
            return float(mpmath.binomial(B,A))
    except ValueError:
        apl_error("DOMAIN ERROR")

# ------------------------------

def     trigonometric (A,B):
    """
    A plus B

    scalar arguments only
    """
    if type(A) is int:
        if abs(A) <= 12:
            function = trigonometric_functions[A+12]
            if function is None:
                return to_be_implemented (A,B)
            else:
                return function(B)

    apl_error("DOMAIN ERROR")

# ------------------------------

def     _highest_common_factor (A,B):
    """
    Highest Common Factor by the Euclid method

    Note: math.gcd() is Python 3.5 and later
    """
    if B == 0:
        return abs(A)

    return _highest_common_factor(B, A % B)

# --------------

def     _or_gcd (A,B):
    """
    A or B (Boolean); GCD(A,B) (otherwise)
    """
    try:
        return int(confirm_bool(A) + confirm_bool(B) != 0)
    except:
        return _highest_common_factor(A,B)

# --------------

def     _and_lcm (A,B):
    """
    A and B (Boolean); LCM(A,B) (otherwise)
    """
    try:
        return int(confirm_bool(A) + confirm_bool(B) == 2)
    except:
        return A * B / _highest_common_factor(A,B)

# --------------

def     _nor (A,B):
    """
    A nor B - may raise DOMAIN ERROR
    """
    return int(confirm_bool(A) + confirm_bool(B) == 0)

# --------------

def     _nand (A,B):
    """
    A nand B - may raise DOMAIN ERROR
    """
    return int(confirm_bool(A) + confirm_bool(B) != 2)

# ------------------------------

def     _lt (A,B):
    """
    A < B with comparison tolerance
    """
    if type(A) is int and type(B) is int:
        return int(operator.lt(A,B))

    if equalCT(A,B):
        return 0

    return int(operator.lt(A,B))

# --------------

def     _le (A,B):
    """
    A <= B
    """
    if type(A) is int and type(B) is int:
        return int(operator.le(A,B))

    if equalCT(A,B):
        return 1

    return int(operator.le(A,B))

# --------------

def     _eq (A,B):
    """
    A == B with comparison tolerance
    """
    if type(A) is int and type(B) is int:
        return int(operator.eq(A,B))

    return int(equalCT(A,B))

# --------------

def     _ge (A,B):
    """
    A >= B with comparison tolerance
    """
    if type(A) is int and type(B) is int:
        return int(operator.ge(A,B))

    if equalCT(A,B):
        return 1

    return int(operator.ge(A,B))

# --------------

def     _gt (A,B):
    """
    A > B with comparison tolerance
    """
    if type(A) is int and type(B) is int:
        return int(operator.gt(A,B))

    if equalCT(A,B):
        return 0

    return int(operator.gt(A,B))

# --------------

def     _ne (A,B):
    """
    A != B with comparison tolerance
    """
    if type(A) is int and type(B) is int:
        return int(operator.ne(A,B))

    return int(not equalCT(A,B))

# ------------------------------

def     to_be_implemented (A,B):
    """
    placeholder for functions not yet implemented

    raises FUNCTION NOT YET IMPLEMENTED
    """
    apl_error("FUNCTION NOT YET IMPLEMENTED")

# ------------------------------

dyadic_functions = {
    # Mathematical
    '+':        lambda A,B: dyadic2scalar(_add,A,B),
    '-':        lambda A,B: dyadic2scalar(_subtract,A,B),
    '×':        lambda A,B: dyadic2scalar(_multiply,A,B),
    '÷':        lambda A,B: dyadic2scalar(_divide,A,B),
    '⌈':        lambda A,B: dyadic2scalar(_maximum,A,B),
    '⌊':        lambda A,B: dyadic2scalar(_minimum,A,B),
    '|':        lambda A,B: dyadic2scalar(_residue,A,B),

    # Algebraic
    '*':        lambda A,B: dyadic2scalar(_exp,A,B),
    '⍟':        lambda A,B: dyadic2scalar(_log,A,B),
    '?':        lambda A,B: dyadic2vector(_deal,A,B),
    '!':        lambda A,B: dyadic2scalar(_combinations,A,B),
    '○':        lambda A,B: dyadic2scalar(trigonometric,A,B),
    '⌹':        to_be_implemented,      # matrix divide

    # Logical
    '∨':        lambda A,B: dyadic2scalar(_or_gcd,A,B),
    '∧':        lambda A,B: dyadic2scalar(_and_lcm,A,B),
    '⍱':        lambda A,B: dyadic2scalar(_nor,A,B),
    '⍲':        lambda A,B: dyadic2scalar(_nand,A,B),

    # Comparison
    '<':        lambda A,B: dyadic2scalar(_lt,A,B),
    '≤':        lambda A,B: dyadic2scalar(_le,A,B),
    '=':        lambda A,B: dyadic2scalar(_eq,A,B),
    '≥':        lambda A,B: dyadic2scalar(_ge,A,B),
    '>':        lambda A,B: dyadic2scalar(_gt,A,B),
    '≠':        lambda A,B: dyadic2scalar(_ne,A,B),
    '≡':        to_be_implemented,      # match (return 0/1 irrespective of rank etc)

# Structural (aka manipulative)
    '⍴':        to_be_implemented,      # (rho) reshape
    ',':        to_be_implemented,      # (comma) concatenation
    '⍪':        to_be_implemented,      #
    '⌽':        to_be_implemented,      # rotation, last axis
    '⊖':        to_be_implemented,      # rotation, first axis
    '⍉':        to_be_implemented,      # transpose
    '⊂':        to_be_implemented,      # (enclose) - creates an array of vectors (?!?)
    '⊃':        to_be_implemented,      # (disclose) = picks from an array (?!?)

# Selection and Set Operations
    '\\':       to_be_implemented,      # expansion
    '/':        to_be_implemented,      # compression
    '↑':        to_be_implemented,      # take
    '↓':        to_be_implemented,      # drop
    '⌷':        to_be_implemented,      # index
    '~':        to_be_implemented,      # without - removes items
    '⌿':        to_be_implemented,      #
    '⍀':        to_be_implemented,      #
    '∪':        to_be_implemented,      #
    '∩':        to_be_implemented,      #
    '⊣':        to_be_implemented,      #
    '⊢':        to_be_implemented,      #

# Search
    '⍳':        to_be_implemented,      # index of B in A
    '∈':        to_be_implemented,      # membership ... same as ?
    '∊':        to_be_implemented,      # membership - is A in B (also characters) - return a boolean
    '⍷':        to_be_implemented,      # find (look for a substring)

# Sorting
    '⍋':        to_be_implemented,      # Sort ascending with specified collating sequence
    '⍒':        to_be_implemented,      # Sort descending with specified collating sequence

# Encode/decode
    '⊤':        to_be_implemented,      # (encode) Convert to a new number system
    '⊥':        to_be_implemented,      # (decode) Convert back to units

# Formatting
    '⍕':        to_be_implemented,      # Format data for display
    '⍺':        to_be_implemented,      # Use picture to format data for display
};

# ------------------------------

def     dyadic_function (symbol):
    """
    return the dyadic function given its APL symbol

    raises INVALID TOKEN if the symbol is not recognised
    """
    try:
        return dyadic_functions[symbol[0]]
    except KeyError:
        apl_error("INVALID TOKEN", symbol)

# EOF
