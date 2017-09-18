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

class   index(object):
    """
    the iterator for dyadic ⍳
    """
    def __init__(self, A, B):
        self._A = A.__iter__()
        self._B = B.__iter__()
        self._L = -1
        self._V = []
        self._IO = indexOrigin()

    def __iter__(self):
        return self

    def __next__(self):
        Y = self._B.__next__()

        try:
            return self._V.index(Y) + self._IO
        except ValueError:
            pass

        while not self._A is None:
            try:
                X = self._A.__next__()
                if isinstance(X, aplQuantity):
                    X.__hash__()

                self._L += 1
                self._V.append(X)

                if X == Y:
                    return self._L + self._IO
            except StopIteration:
                self._A = None
                self._L += 1

        return self._L + self._IO

# ------------------------------

class   without(object):
    """
    the iterator for dyadic ~
    """
    def __init__(self, A, B):
        self._A = A.__iter__()
        self._B = B.__iter__()
        self._S = set()

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            X = self._A.__next__()
            if X in self._S:
                continue

            while not self._B is None:
                try:
                    Y = self._B.__next__()
                    self._S.add(Y)

                    if X == Y:
                        break

                except StopIteration:
                    self._B = None

            if self._B is None:
                return X

# ------------------------------

class   union(object):
    """
    the iterator for dyadic ∪
    """
    def __init__(self, A, B):
        self._A = A.__iter__()
        self._B = B.__iter__()
        self._S = set()

    def __iter__(self):
        return self

    def __next__(self):
        if not self._A is None:
            try:
                X = self._A.__next__()
                self._S.add(X)
                return X

            except StopIteration:
                self._A = None

        while True:
            Y = self._B.__next__()
            if Y not in self._S:
                return Y

# ------------------------------

class   intersection(object):
    """
    the iterator for dyadic ∩
    """
    def __init__(self, A, B):
        self._A = A.__iter__()
        self._B = B.__iter__()
        self._S = set()

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            X = self._A.__next__()
            if X in self._S:
                return X

            while not self._B is None:
                try:
                    Y = self._B.__next__()
                    self._S.add(Y)

                    if X == Y:
                        return X

                except StopIteration:
                    self._B = None

# ------------------------------

class   drop(object):
    """
    the iterator for dyadic ↓
    """
    def __init__(self, A, B):
        self._A = A
        self._B = B.__iter__() if A >= 0 else lookAhead(B, -A)

    def __iter__(self):
        return self

    def __next__(self):
        if self._A < 0:
            return self._B.pushThenPop()

        while self._A > 0:
            self._A -= 1
            self._B.__next__()

        return self._B.__next__()

# ------------------------------

class   take(object):
    """
    the iterator for dyadic ↑
    """
    def __init__(self, A, B, P):
        self._A = A
        self._B = B.__iter__() if A >= 0 else lookAhead(B, -A, P)
        self._P = P

        if A < 0:
            try:
                while True:
                    self._B.pushThenPop()
            except StopIteration:
                pass

    def __iter__(self):
        return self

    def __next__(self):
        if self._A < 0:
            return self._B.__next__()

        if self._A == 0:
            raise StopIteration

        self._A -= 1

        if not self._B is None:
            try:
                return self._B.__next__()
            except StopIteration:
                self._B = None

        return self._P

# ------------------------------
# OLD IMPLEMENTATIONS TO BE REPLACED
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
