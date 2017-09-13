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

from aplQuantity import aplQuantity, lookAhead, makeScalar, scalarIterator
from aplError import aplError, aplException, assertError

# ------------------------------

def _nextPair(A, B):
    """
    utility routine to fetch the next pair of values from the iterators
    """
    OK = 0

    try:
        X = A.__next__()
        OK += 1
    except StopIteration:
        if isinstance(B, scalarIterator):
            raise StopIteration

    try:
        Y = B.__next__()
        OK += 1
    except StopIteration:
        if isinstance(A, scalarIterator):
            raise StopIteration

    if OK == 2:
        return X, Y

    if OK == 0:
        raise StopIteration

    assertError("LENGTH ERROR")

# ------------------------------

class   maths(object):
    """
    the recursive iterator for dyadic mathematical functions
    """
    def __init__(self, Map, Fn, A, B):
        self._map = Map
        self._fn = Fn
        self._A = A.__iter__()
        self._B = B.__iter__()

    def __iter__(self):
        return self

    def __next__(self):
        X, Y = _nextPair(self._A, self._B)

        if isinstance(X, aplQuantity) and isinstance(Y, aplQuantity):
            return self._map(self._fn, X, Y)

        if isinstance(X, aplQuantity):
            return self._map(self._fn, X, makeScalar(Y))

        if isinstance(Y, aplQuantity):
            return self._map(self._fn, makeScalar(X), Y)

        try:
            return self._fn(X, Y)
        except TypeError:
            assertError("DOMAIN ERROR")

# ------------------------------

class   match(object):
    """
    the recursive iterator for dyadic ≡
    """
    def __init__(self, Map, Fn, A, B):
        self._map = Map
        self._fn = Fn
        self._A = A.__iter__()
        self._B = B.__iter__()

    def __iter__(self):
        return self

    def __next__(self):
        try:
            X, Y = _nextPair(self._A, self._B)
        except aplException as error:
            if error.message == "LENGTH ERROR":
                return False

        if isinstance(X, aplQuantity) and isinstance(Y, aplQuantity):
            return self._map(self._fn, X, Y)

        if isinstance(X, aplQuantity):
            return False

        if isinstance(Y, aplQuantity):
            return False

        return self._fn(X, Y)

# ------------------------------

class   reshape(object):
    """
    the iterator for dyadic ⍴
    """
    def __init__(self, A, B):
        self._A = A
        if isinstance(B, tuple):
            self._B = None
            self._R = B
        else:
            self._B = B.__iter__()
            self._T = []
            self._R = self._T
        self._I = self._R.__iter__()

    def __iter__(self):
        return self

    def __next__(self):
        if self._A <= 0:
            raise StopIteration

        if not self._B is None:
            try:
                Y = self._B.__next__()
                self._A -= 1
                self._T.append(Y)
                return Y
            except StopIteration:
                self._B = None

        try:
            self._A -= 1
            return self._I.__next__()

        except StopIteration:
            self._I = self._R.__iter__()
            return self._I.__next__()

# ------------------------------

class   concatenate(object):
    """
    the iterator for dyadic ,
    """
    def __init__(self, A, B):
        self._A = A.__iter__()
        self._B = B.__iter__()

    def __iter__(self):
        return self

    def __next__(self):
        if not self._A is None:
            try:
                return self._A.__next__()

            except StopIteration:
                self._A = None

        return self._B.__next__()

# ------------------------------

def     transpose(_, B):
    """
    implement dyadic ⍉ (for arrays - TBD)
    """
    return B

# ------------------------------

class   rotate(object):
    """
    the iterator for dyadic ⌽
    """
    def __init__(self, A, B):
        self._B = B.__iter__()
        self._L = lookAhead(self._B, A)

    def __iter__(self):
        return self

    def __next__(self):
        if self._B is None:
            return self._L.__next__()

        try:
            return self._B.__next__()

        except StopIteration:
            self._B = None

        return self.__next__()

# ------------------------------
# OLD IMPLEMENTATIONS TO BE REPLACED
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
