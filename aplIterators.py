"""
    iterators not specific to any one function or operator map

    UNDER DEVELOPMENT

    It was found some time ago that some iterators could not go in the existing
    iterators without creating circular references.  There were temporarily
    given a home in aplQuantity but that module is already too large.

    So, the useful, common, iterators have been separated out before adding any
    new ones (to deal with arrays).

    The common iterators defined here are:

        - aplIterator - an empty base class
        - scalarIterator - that allows scalars to be added to vectors and arrays
        - vectorIterator - that allows vectors to be added to arrays
        - stack - a rewrite of the monadic reverse iterator
        - lookahead - temporary storage for 'promises'

    The vectorIterator may be withdrawn:  it seems the arithmetic it supports
    is not valid anyway.

    The lookAhead was first introduced to solve several generic problems - such
    as "Is a promise a vector length 1 or is it longer ?" without having to
    resolve the entire promise.

    It has since acquired a number of function specific methods.  A couple of
    these introduce incompatible use of the buffer.  The class is crying out
    for specialisation.

    In the immediate future, iterators are to be added to allow arrays to be treated
    as iterators.  Some of these may be complex.
"""

import makeQuantity ## makeVector, makePrototype

from aplError import assertError

# ------------------------------

class   aplIterator(object):
    """
    a base class to make it simpler to determine that an iterator is one of ours

    It is for now, and may always be, empty
    """
    pass

# ------------------------------

class   scalarIterator(aplIterator):
    """
    trivial iterator for mapping scalar quantities with vector and array quantities

    The iterator returns the scalar value ad infinitum
    """
    def __init__(self, value, count=-1, expressionToGo=None):
        self._value = value
        self._count = count
        self.expressionToGo = expressionToGo

    def __iter__(self):
        return self

    def __next__(self):
        if self._count == 0:
            raise StopIteration

        self._count -= 1

        return self._value

# ------------------------------

class   vectorIterator(aplIterator):
    """
    trivial iterator for mapping vector quantities with array quantities

    The iterator returns the vector elemment by element, over and over
    """
    def __init__(self, value, count=-1, expressionToGo=None):
        self._original = value
        self._iterator = value.__iter__()
        self._repeater = []
        self._count = count
        self.expressionToGo = expressionToGo

    def __iter__(self):
        return self

    def __next__(self):
        if self._count == 0:
            raise StopIteration

        self._count -= 1

        if not self._original is None:
            try:
                element = self._iterator.__next__()
                self._repeater.append(element)
                return element
            except StopIteration:
                self._original = None
                self._iterator = self._repeater.__iter__()

        try:
            return self._iterator.__next__()

        except StopIteration:
            self._iterator = self._repeater.__iter__()
            return self._iterator.__next__()

# ------------------------------

class   stack(object):
    """
    an iterator that allow a vector to be read backwards
    """
    def __init__(self, B):
        B = B.__iter__()

        T = []

        try:
            while True:
                T.insert(0, B.__next__())

        except StopIteration:
            pass

        self._B = T.__iter__()

    def __iter__(self):
        return self

    def __next__(self):
        return self._B.__next__()

# ------------------------------

class   lookAhead(object):
    """
    an iterator to allow peeking at the first few elements of some other iterator

    Extended to support other operations including buffering inside some other custom iterator
    """
    def __init__(self, B, N=0, F=None):
        self._B = B.__iter__()
        self._LA = []
        self._BL = 0

        if F is None:
            self.buffer(N)
        else:
            self.pushThisIn(F, N)

    def __iter__(self):
        return self

    def __next__(self):
        if self._BL == 0:
            return self._B.__next__()

        return self._popBuffer()

    def _popBuffer(self):
        """
        remove and return item from the front of the buffer
        """
        self._BL -= 1
        return self._LA.pop(0)

    def _pushBuffer(self, Y):
        """
        add item to the end of the buffer
        """
        self._LA.append(Y)
        self._BL += 1

        return Y

    def pushThisIn(self, F, N=1):
        """
        push F in at the end of buffer N times
        """
        while N > 0:
            N -= 1
            self._pushBuffer(F)

    def pushThenPop(self):
        """
        push another element into the end of the buffer, pop and return the element at the front

        When StopIteration is raised repeated calls do not drain the buffer.
        """
        if self._BL == 0:
            return self._B.__next__()

        self._pushBuffer(self._B.__next__())

        return self._popBuffer()

    def popThenPush(self):
        """
        pop (and return) the element at the front, push another element into the end of the buffer

        When StopIteration is raised repeated calls drain the buffer.
        """
        if self._BL == 0:
            return self._B.__next__()

        R = self._popBuffer()

        self._pushBuffer(self._B.__next__())

        return R

    def buffer(self, N):
        """
        if possible, ensure at least N elements are in the lookahead buffer
        """
        N -= self._BL

        try:
            while N > 0:
                N -= 1
                self._pushBuffer(self._B.__next__())
        except StopIteration:
            pass

        return self._BL

    def buffered(self):
        """
        how many elements are there in the lookahead buffer ?
        """
        return self._BL

    def peek(self):
        """
        return the first element in the lookahead buffer and leave the buffer unchanged
        """
        if self._BL == 0:
            try:
                return self._pushBuffer(self._B.__next__())
            except StopIteration:
                return None

        return self._LA[0]

    def makePrototype(self):
        """
        return the 'empty' array prototype for APL quantity enclosed in the buffer
        """
        P = []

        for Y in self._LA:
            P.append(makeQuantity.makePrototype(Y))

        try:
            while True:
                Y = self._pushBuffer(self._B.__next__())

                P.append(makeQuantity.makePrototype(Y))
        except StopIteration:
            pass

        return P

    def isString(self):
        """
        true if a real vector of characters, false if only a mixed vector
        """
        for Y in self._LA:
            if not isinstance(Y, str):
                return False

        try:
            while True:
                Y = self._pushBuffer(self._B.__next__())

                if not isinstance(Y, str):
                    return False
        except StopIteration:
            pass

        return True

    def isMatch(self, V):
        """
        true if V matches the contents of the buffer exactly, false otherwise
        """
        V = V.__iter__()

        try:
            for Y in self._LA:
                if Y != V.__next__():
                    return False
            V.__next__()
        except StopIteration:
            return True

        return False

# EOF
