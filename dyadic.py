#!/usr/bin/python3
"""
    dyadic APL functions

    WIP - limited set

    WIP - scalar parameters only
"""

import operator

from apl_exception import APL_Exception as apl_exception

# --------------

def     add (A,B):
    """
    A plus B

    scalar arguments only
    """
    return operator.add(A,B)

def     subtract (A,B):
    """
    A minus B

    scalar arguments only
    """
    return operator.sub(A,B)

def     multiply (A,B):
    """
    A multiplied by B

    scalar arguments only
    """
    return operator.mul(A,B)

def     divide (A,B):
    """
    A divided by B

    scalar arguments only

    throws RANGE ERROR (B == 0)
    """
    try:
        return operator.truediv(A,B)
    except:
        raise (apl_exception("RANGE ERROR"))

# ------------------------------

def     _Boolean (B):
    """
    Boolean integer value of B

    scalar argument only

    throws DOMAIN ERROR (B is not 0 or 1)
    """
    if B == 1:  return 1
    if B == 0:  return 0

    raise (apl_exception("DOMAIN ERROR"))

def     _highest_common_factor (A,B):
    """
    Highest Common Factor by the Euclid method

    scalar argument only
    """
    if B == 0:
        return abs(A)

    return _highest_common_factor(B, A % B)

def     or_gcd (A,B):
    """
    A or B (Boolean); GCD(A,B) otherwise

    scalar arguments only
    """
    try:
        return int(_Boolean(A) + _Boolean(B) != 0)
    except:
        return _highest_common_factor(A,B)

def     and_lcm (A,B):
    """
    A and B (Boolean); LCM(A,B) otherwise

    scalar arguments only
    """
    try:
        return int(_Boolean(A) + _Boolean(B) == 2)
    except:
        return A * B / _highest_common_factor(A,B)

def     nor (A,B):
    """
    A nor B

    scalar arguments only

    throws DOMAIN ERROR (B is not 0 or 1)
    """
    return int(_Boolean(A) + _Boolean(B) == 0)

def     nand (A,B):
    """
    A nand B

    scalar arguments only

    throws DOMAIN ERROR (B is not 0 or 1)
    """
    return int(_Boolean(A) + _Boolean(B) != 2)

# ------------------------------

def     lt (A,B):
    """
    A < B

    scalar arguments only
    """

    return int(operator.lt(A,B))

def     le (A,B):
    """
    A <= B

    scalar arguments only
    """

    return int(operator.le(A,B))

def     eq (A,B):
    """
    A == B

    scalar arguments only
    """

    return int(operator.eq(A,B))

def     ge (A,B):
    """
    A >= B

    scalar arguments only
    """

    return int(operator.ge(A,B))

def     gt (A,B):
    """
    A > B

    scalar arguments only
    """

    return int(operator.gt(A,B))

def     ne (A,B):
    """
    A != B

    scalar arguments only
    """

    return int(operator.ne(A,B))

# ------------------------------

def     to_be_implemented (A,B):
    """
    placeholder for functions not yet implemented

    throws FUNCTION NOT YET IMPLEMENTED
    """
    raise (apl_exception("FUNCTION NOT YET IMPLEMENTED"))

# ------------------------------

dyadic_functions = {
    '+':        add,
    '-':        subtract,
    '×':        multiply,
    '÷':        divide,

    '∨':        or_gcd,
    '∧':        and_lcm,
    '⍱':        nor,
    '⍲':        nand,

    '<':        lt,
    '≤':        le,
    '=':        eq,
    '≥':        ge,
    '>':        gt,
    '≠':        ne,

    '*':        to_be_implemented,      # exponentiation
    '○':        to_be_implemented,      # trigonometric function
    '?':        to_be_implemented,      # deal
    '∈':        to_be_implemented,      # membership
    '⌈':        to_be_implemented,      # maximum
    '⌊':        to_be_implemented,      # minimum
    '⍴':        to_be_implemented,      # reshape
    '↑':        to_be_implemented,      # take
    '↓':        to_be_implemented,      # drop
    '⊥':        to_be_implemented,      # decode
    '⊤':        to_be_implemented,      # encode
    '∣':        to_be_implemented,      # residue
    ',':        to_be_implemented,      # catenation
    '\\':       to_be_implemented,      # expansion
    '/':        to_be_implemented,      # compression
    '⍳':        to_be_implemented,      # index
    '⌹':        to_be_implemented,      # matrix divide
    '⌽':        to_be_implemented,      # rotation, last axis
    '⊖':        to_be_implemented,      # rotation, first axis
    '⍟':        to_be_implemented,      # logarithm
    '⍕':        to_be_implemented,      # format
    '⍉':        to_be_implemented,      # transpose
    '!':        to_be_implemented,      # combinations
    '¨':        to_be_implemented,      # diaeresis
    };

def     dyadic_function (symbol):
    """
    return the dyadic function given its APL symbol

    throws INVALID TOKEN if the symbol is not recognised
    """
    try:
        return dyadic_functions[symbol[0]]
    except KeyError:
        raise (apl_exception("INVALID TOKEN", symbol))

# EOF
