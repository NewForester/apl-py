"""
    iterator functions for dyadic APL functions

    UNDER DEVELOPMENT

    This module contains functions that implement vector versions of dyadic
    APL non-mathematical functions.  Each takes two Python quantities and
    returns a third.

    WIP - the implementation of lazy evaluation means all functions in this
    module are under review.
"""

import operator

from systemVariables import confirmInteger, indexOrigin

from aplError import aplError

# ------------------------------
# OLD IMPLEMENTATIONS TO BE REPLACED
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

# --------------

def     concatenate(A, B):
    """
    concatenate (list) B onto the end of (list) A
    """
    return list(A) + list(B)

# --------------

def     rotateLast(A, B):
    """
    rotate (vector) B by A elements
    """
    B = list(B)
    A = confirmInteger(A) % len(B)

    return B[A:] + B[:A]

# --------------

def     rotateFirst(A, B):
    """
    rotate (vector) B by A elements
    """
    B = list(B)
    A = confirmInteger(A) % len(B)

    return B[A:] + B[:A]

# --------------

def     transpose(_, B):
    """
    transpose B about A
    """
    return B

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

def     index(A, B, mixed):
    """
    index(es) of (elements of) B in (list) A
    """
    V = []
    IO = indexOrigin()

    A = list(A)

    for X in B:
        if mixed:
            V.append(len(A) + IO)
        else:
            try:
                V.append(A.index(X) + IO)
            except ValueError:
                V.append(len(A) + IO)

    return V

# --------------

def     drop(A, B, _):
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

def     take(A, B, pad):
    """
    take A elements from B
    """
    A = confirmInteger(A)

    B = list(B)
    LB = len(B)

    if A < 0:
        length = LB + A

        if length < 0:
            R = ([pad] * (0 - length)) + B
        else:
            R = B[length:]
    else:
        length = LB - A

        if length < 0:
            R = B + ([pad] * (0 - length))
        else:
            R = B[:A]

    return R

# --------------

def     union(A, B):
    """
    return union of B with A

    NB  only good for homogeneous operands
    """
    V = []

    A = list(A)

    for X in A:
        V.append(X)

    for X in B:
        if X not in A:
            V.append(X)

    return V

# --------------

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

# --------------

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

# --------------

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

# --------------

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

# EOF
