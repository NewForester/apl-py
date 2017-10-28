"""
    iterator objects and functions for monadic APL functions

    UNDER DEVELOPMENT

    The objects in this module implement monadic APL functions for vectors in
    conjunction with map functions defined in monadicMaps

    Each object takes a Python 'iterable' and logically returns another but
    the implementation uses the Python iterator protocol to return the vector
    one scalar at a time so implementing lazy evaluation.

    Nested vectors are handled by lazy recursion with the iterator calling the
    map function, which returns a nested iterator.  The map function is the
    first parameter to the object's __init__ method.

    For several functions, an iterator object is not appropriate.  A Python
    function is used instead but the calling map function in unaware of this.
"""

# pylint: disable=too-few-public-methods

from systemVariables import indexOrigin

from aplQuantity import aplQuantity, lookAhead
from aplError import aplException, assertError

# ------------------------------

class   maths(object):
    """
    the recursive iterator for monadic mathematical functions
    """
    def __init__(self, Map, Fn, B):
        self._map = Map
        self._fn = Fn
        self._B = B.__iter__()
        self._expresso = B.expressionToGo

    def __iter__(self):
        return self

    def __next__(self):
        try:
            Y = self._B.__next__()

            if isinstance(Y, aplQuantity):
                return self._map(self._fn, Y)

            try:
                return self._fn(Y)
            except TypeError:
                assertError("DOMAIN ERROR")

        except aplException as error:
            if error.expr is None:
                error.expr = self._expresso
            raise error

# ------------------------------

def     iota(B):
    """
    the iterator for monadic ⍳
    """
    IO = indexOrigin()

    return range(IO, B + IO)

# ------------------------------

class   enlist(object):
    """
    the iterator for monadic ∊
    """
    def __init__(self, B):
        self._B = B.__iter__()
        self._Y = None

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self._Y is None:
                Y = self._B.__next__()

                if not isinstance(Y, aplQuantity):
                    return Y

                self._Y = enlist(Y)

            try:
                return self._Y.__next__()
            except StopIteration:
                self._Y = None

# ------------------------------

def     transpose(B):
    """
    implement monadic ⍉ (for arrays - TBD)
    """
    return B

# ------------------------------

class   reverse(object):
    """
    the iterator for monadic ⌽
    """
    def __init__(self, B):
        self._B = B.__iter__()
        self._T = None

    def __iter__(self):
        return self

    def __next__(self):
        if self._T is None:
            self._T = reverse._stack(self._B)

        if self._T != []:
            return self._T.pop(0)

        return self._B.__next__()

    @staticmethod
    def _stack(B):
        """
        stack the all elements in reverse order
        """
        T = []

        try:
            while True:
                T.insert(0, B.__next__())

        except StopIteration:
            pass

        return T

# ------------------------------

class   disclose(object):
    """
    the iterator for monadic ⊃
    """
    def __init__(self, B):
        self._B = B.__iter__()

    def __iter__(self):
        return self

    def __next__(self):
        Y = self._B.__next__()

        if isinstance(Y, aplQuantity):
            assertError("WIP - LENGTH ERROR")

        return Y

# ------------------------------

class   unique(object):
    """
    the iterator for monadic ∪
    """
    def __init__(self, B):
        self._B = B.__iter__()
        self._S = set()

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            Y = self._B.__next__()

            if Y not in self._S:
                self._S.add(Y)
                return Y

# ------------------------------

class   tail(object):
    """
    the iterator for monadic ↓

    Everything but the first element of B
    """
    def __init__(self, B):
        self._B = B.__iter__()
        self._B.__next__()

    def __iter__(self):
        return self

    def __next__(self):
        return self._B.__next__()

# ------------------------------

def     head(B):
    """
    the iterator for monadic ↑

    The first element of B
    """
    return B.__iter__().__next__()

# ------------------------------

class   grade(object):
    """
    the iterator for monadic ⍒ and ⍋
    """
    def __init__(self, B):
        self._B = B.__iter__()
        self._IO = indexOrigin()

    def __iter__(self):
        return self

    def __next__(self):
        return self._B.__next__() + self._IO

 # EOF
