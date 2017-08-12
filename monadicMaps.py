"""
    maps used to apply a monadic function to an APL quantitity

    UNDER DEVELOPMENT

    A monadic APL function that can be applied to a single numeric value
    can be extended to operator over a large APL quantity by means of a
    higher order function known as a map.

    Python provides a standard map that is good for APL mathematical functions
    but functions that do not map one-to-one need special purpose maps.

    The Python map is an example of lazy evaluation.  The special purpose maps
    also implement lazy evaluation where possible.

    That is a statement of intent:  the old implementations are to be replaced.
"""

from aplQuantity import aplQuantity
from aplError import aplError

# ------------------------------
# OLD IMPLEMENTATIONS TO BE REPLACED
# ------------------------------

def     s2s(Fn, B):
    """
    evaluate a numeric monadic function that, given a scalar argument, returns a scalar
    """
    B.noStringConfirm()

    if B.isScalar():
        return aplQuantity(Fn(B.python()), None)

    if B.isVector():
        return aplQuantity(map(Fn, B), B.dimension())

    aplError("RANK ERROR")

# ------------------------------

def     s2v(Fn, B):
    """
    evaluate a numeric monadic function that, given a scalar argument, returns a vector
    """
    B.noStringConfirm()

    Bpy = B.scalarToPy()

    return aplQuantity(Fn(Bpy), Bpy)

# ------------------------------

def     v_head(Fn, B):
    """
    evaluate a numeric function that, given a vector argument, returns a scalar
    """
    if B.isScalar():
        return aplQuantity(B.scalarToPy(), None, B.isString())

    if B.isVector():
        if B.dimension() < 1:
            return aplQuantity([], 0, B.isString())

        return aplQuantity(Fn(B.vectorToPy()), None, B.isString())

    aplError("RANK ERROR")

# ------------------------------

def     v_tail(Fn, B):
    """
    evaluate a function that, given a vector argument, returns a vector (probably)
    """
    if B.isScalar():
        return aplQuantity([], 0, B.isString())

    if B.isVector():
        if B.dimension() <= 1:
            return aplQuantity([], 0, B.isString())

        return aplQuantity(Fn(B.vectorToPy()), B.dimension()-1, B.isString())

    aplError("RANK ERROR")

# ------------------------------

def     v2v(Fn, B):
    """
    evaluate a function that, given a vector argument, returns a vector
    """
    Rpy = Fn(B.vectorToPy())

    if B.isScalar():
        return aplQuantity(Rpy[0], B.dimension(), B.isString())

    if B.isVector():
        return aplQuantity(Rpy, B.dimension(), B.isString())

    aplError("RANK ERROR")

# ------------------------------

def     s_rho(_, B):
    """
    scalar rho - return dimension/rank of B - does not operate on B
    """
    if B.isScalar():
        return aplQuantity([], 0)

    if B.isVector():
        return aplQuantity([B.dimension()], 1)

    aplError("RANK ERROR")

# ------------------------------

def     s_comma(_, B):
    """
    scalar comma - unravel B and return a vector
    """

    if B.isScalar():
        return aplQuantity(B.vectorToPy(), 1, B.isString())

    if B.isVector():
        return B

    aplError("RANK ERROR")

# ------------------------------

def     v_nest(B):
    """
    depth of nesting in B
    """
    Rpy = 0

    if B.isScalar():
        Rpy = 0

    elif B.isString():
        Rpy = 1

    elif B.isVector():
        Rpy = 1
        for X in B:
            if isinstance(X, aplQuantity):
                Rpy = 2
                break

    else:
        aplError("RANK ERROR")

    return aplQuantity(Rpy, None)

# ------------------------------

def     v_tally(B):
    """
    number of elements in last axis
    """
    Rpy = 0

    if B.isScalar():
        Rpy = 1

    elif B.isString():
        Rpy = B.dimension()

    elif B.isVector():
        Rpy = B.dimension()

    else:
        aplError("RANK ERROR")

    return aplQuantity(Rpy, None)

# EOF
