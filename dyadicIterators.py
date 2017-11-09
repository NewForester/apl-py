"""
    iterator objects and functions for dyadic APL functions

    UNDER DEVELOPMENT

    The objects in this module implement dyadic APL functions for vectors in
    conjunction with map functions defined in dyadicMaps

    Each object takes two Python 'iterables' and logically returns a third but
    the implementation uses the Python iterator protocol to return the vector
    one scalar at a time so implementing lazy evaluation.

    Nested vectors are handled by lazy recursion with the iterator calling the
    map function, which returns a nested iterator.  The map function is the
    first parameter to the object's __init__ method.

    For a few functions, an iterator object is not appropriate.  A Python
    function is used instead but the calling map function in unaware of this.
"""

import operator
from functools import reduce

from systemVariables import confirmInteger, indexOrigin

from makeQuantity import makeScalar, makeVector, makePrototype

from aplQuantity import aplQuantity
from aplIterators import aplIterator, lookAhead, stack
from aplError import aplException, assertError, assertTrue

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
        if isinstance(B, aplIterator):
            raise StopIteration

    try:
        Y = B.__next__()
        OK += 1
    except StopIteration:
        if isinstance(A, aplIterator):
            raise StopIteration

    if OK == 2:
        return X, Y

    if OK == 0:
        raise StopIteration

    assertError("LENGTH ERROR")

# --------------

def _nextPairWithInteger(A, B):
    """
    utility routine to fetch the next pair of values from the iterators

    The first of the pair must be an integer
    """
    OK = 0

    try:
        X = confirmInteger(A.__next__())
        OK += 1
    except StopIteration:
        if isinstance(B, aplIterator):
            raise StopIteration

    try:
        Y = B.__next__()
        OK += 1
    except StopIteration:
        if isinstance(A, aplIterator):
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
        self._expresso = B.expressionToGo

    def __iter__(self):
        return self

    def __next__(self):
        try:
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

        except aplException as error:
            if error.expr is None:
                error.expr = self._expresso
            raise error

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
        self._expresso = B.expressionToGo

    def __iter__(self):
        return self

    def __next__(self):
        try:
            X, Y = _nextPair(self._A, self._B)

            if isinstance(X, aplQuantity) and isinstance(Y, aplQuantity):
                return self._map(self._fn, X, Y)

            if isinstance(X, aplQuantity):
                return False

            if isinstance(Y, aplQuantity):
                return False

            return self._fn(X, Y)

        except aplException as error:
            if error.message == "LENGTH ERROR":
                return False

            if error.expr is None:
                error.expr = self._expresso
            raise error

# ------------------------------

class   reshape(object):
    """
    the iterator for dyadic ⍴
    """
    def __init__(self, A, B):
        if isinstance(A, tuple):
            self._A = reduce(operator.mul, A, 1)
        else:
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

class   partition(object):
    """
    the iterator for dyadic ⊂
    """
    def __init__(self, A, B):
        self._A = A.__iter__()
        self._B = B.__iter__()
        self._V = []
        self._I = 0

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                X, Y = _nextPairWithInteger(self._A, self._B)
            except StopIteration:
                return self._aplVector(None)

            if X > self._I:
                self._I = X
                try:
                    return self._aplVector(Y)
                except StopIteration:
                    pass

            if X > 0:
                self._V.append(Y)
            elif X < 0:
                assertError("DOMAIN ERROR")

            self._I = X

    def _aplVector(self, Y):
        """
        create, for return, a non-empty APL vector quantity else raise StopIteration)
        """
        V = self._V

        if V == []:
            raise StopIteration

        self._V = [] if Y is None else [Y]

        return makeVector(tuple(V), len(V), (makePrototype(V[0]),))

# ------------------------------

class   membership(object):
    """
    the iterator for dyadic ∊
    """
    def __init__(self, A, B):
        self._A = A.__iter__()
        self._B = B.__iter__()
        self._S = set()

    def __iter__(self):
        return self

    def __next__(self):
        X = self._A.__next__()

        if X in self._S:
            return 1

        while not self._B is None:
            try:
                Y = self._B.__next__()
                self._S.add(Y)

                if X == Y:
                    return 1

            except StopIteration:
                self._B = None

        return 0

# ------------------------------

class   find(object):
    """
    the iterator for dyadic ⍷
    """
    def __init__(self, A, B):
        self._A = A
        self._B = lookAhead(B)
        self._L = len(A)

    def __iter__(self):
        return self

    def __next__(self):
        if self._L == 0:
            self._B.__next__()
            return 0

        if self._B.buffered() == 0:
            self._B.buffer(self._L)
        else:
            try:
                self._B.popThenPush()
            except StopIteration:
                pass

        if self._B.buffered() == 0:
            raise StopIteration

        return int(self._B.isMatch(self._A))

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

class   compress(object):
    """
    the iterator for dyadic /
    """
    def __init__(self, A, B, P):
        self._A = A.__iter__()
        self._B = B.__iter__()
        self._P = P
        self._X = 0
        self._Y = None

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self._X == 0:
                self._X, self._Y = _nextPairWithInteger(self._A, self._B)

            if self._X > 0:
                self._X -= 1
                return self._Y

            if self._X < 0:
                self._X += 1
                return self._P

# ------------------------------

class   expand(object):
    """
    the iterator for dyadic \
    """
    def __init__(self, A, B, P):
        self._A = A.__iter__()
        self._B = B.__iter__()
        self._P = P
        self._T = 0
        self._X = 0
        self._Y = None

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self._X == 0:
                self._nextPair()

            if self._X > 0:
                self._X -= 1
                return self._Y

            if self._X < 0:
                self._X += 1
                return self._P

    def _nextPair(self):
        """
        fetch the next pair of values from the iterators
        """
        OK = 0
        try:
            self._X = confirmInteger(self._A.__next__())
            if self._X > 0:
                self._T += 1
                if self._T == 0:
                    return

            elif self._X == 0:
                self._X -= 1

            OK += 1
        except StopIteration:
            pass

        if self._X < 0 and self._T < 0:
            return

        try:
            self._Y = self._B.__next__()
            self._T -= 1

            OK += 1
        except StopIteration:
            pass

        if self._X < 0 and self._T == 0:
            return

        if OK != 2:
            if isinstance(self._A, aplIterator):
                assertTrue(self._T == 1, "LENGTH ERROR")
            else:
                assertTrue(self._T == 0, "LENGTH ERROR")

            raise StopIteration

# ------------------------------

class   encode(object):
    """
    the iterator for dyadic ⊤ - overkill
    """
    def __init__(self, A, B):
        self._A = A.__iter__()
        self._B = B
        self._I = None

    def __iter__(self):
        return self

    def __next__(self):
        if self._I is None:
            self._I = encode._encode(stack(self._A), self._B)

        return self._I.__next__()

    @staticmethod
    def _encode(I, B):
        """
        encode B to the base given by the values of the iterator I and return a new iterator
        """
        try:
            T = []
            while True:
                J = I.__next__()

                T = [operator.mod(B, J) if J != 0 else B] + T

                B = operator.floordiv(B, J) if J != 0 else 0

        except StopIteration:
            return T.__iter__()

        except TypeError:
            assertError("DOMAIN ERROR")

# --------------

def     decode(A, B):
    """
    the non-iterator for dyadic ⊥
    """
    A = A.__iter__()
    B = B.__iter__()
    S = 0

    try:
        while True:
            X, Y = _nextPair(A, B)

            S = operator.add(operator.mul(S, X), Y)

    except StopIteration:
        return S

    except TypeError:
        assertError("DOMAIN ERROR")

# ------------------------------

class   grade(object):
    """
    the iterator for dyadic ⍒ and ⍋
    """
    def __init__(self, B):
        self._B = B.__iter__()
        self._IO = indexOrigin()

    def __iter__(self):
        return self

    def __next__(self):
        return self._B.__next__() + self._IO

# EOF
