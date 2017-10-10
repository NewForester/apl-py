"""
    a Python type that can hold APL scalar and vector quantities, numeric, string and mixed

    UNDER DEVELOPMENT

    APL quantities have:
        - prototype - rank and dimensions
        - type - numeric, string, mixed
        - depth - degree of nesting
        - empty - an APL quantity may have no values but may still have the other properties

    The current version of this module supports:
        - numeric and string scalars
            - scalars comprise a single value and have neither rank nor dimension
        - numeric, string and mixed vectors
            - vectors comprise a (Python) sequence of values and have no rank but a single dimension

    Strings are represented by a sequence of single characters, each of which has Python type str.

    Scalars are stored as a sequence of length 1 for computational convenience.

    Empty vector is also stored as a sequence of length 1.  This is a provisional representation
    for 'array prototypes'.

    APL quantities may be recursive.  Several methods are therefore recursive.

    Under eager evaluation rules, sequences are tuples containing concrete values.  Under lazy
    evaluation rules, the sequence are more likely to be an iterator type.   Think of the Python
    map() function and then think of special purpose, custom built, map-like functions.

    Such iterator types can yield concrete values only once.  This is usually done implicitly in
    calling code after a call to the python(), scalarToPy(), vectorToPy() or scalarIterator()
    methods.

    The comments below speak of 'promises' and of 'realising a promise'.  Apologies in advance.

    A lazy, iterable, APL quantity may be explicitly converted (in-place) to an eager, concrete,
    quantity by calling the resolve() method.  Again, apologies for the inconsistent terminology.

    In general terms, under lazy evaluation, an ordinary APL expression is parsed producing a
    sequence of promises and the sequence is then evaluated.  Most APL quantities live and die
    as promises.  Only when the quantity is needed more than once is it explicitly realised.
    For example, when an expression is assigned to a workspace variable.

    To support Python set operations, the APL quantity class implements the __hash__ method.
    Python hash() values for sequences only make sense for immutable sequences therefore the
    __hash__ method implicitly realises the quantity, converting promises to concrete values.

    Other than the APL quantity class itself, this module contains the implementation of a couple
    of iterators (implemented here to avoid circular module references) and four helper routines
    for the creation of APL quantities.  The class constructor should never be invoked directly by
    code outside this module.  The iterator classes are.

    The four helper functions and many of the class methods are designed to keep calling code (in
    monadicMaps and dyadicMaps, for example) simple and hopefully self-documenting.  A further
    group of assert routines are implemented in aplError (to avoid circular module references).

    The module has been complicated with the introduction of the lookAhead iterator.  The aim was
    to avoid the principle of lazy evaluation being compromised by the implementation.
"""

import operator
from functools import reduce

from aplError import assertError, assertNotArray

# ------------------------------

class   aplQuantity(object):
    """
    class that holds an APL quantity

    There a many query methods (most of them trivial) and very few behavioural methods.

    Methods may also alter the internal state.  This is because the state is lazy.
    """
    def __init__(self, value, dimension=0, prototype=(0,)):
        self._value = value
        self._dimension = dimension
        self._prototype = prototype
        self._resolved = False
        self._hash = None
        self.expressionToGo = None

    def __iter__(self):
        """
        required by the Python sort operation
        """
        return self._value.__iter__()

    def __eq__(self, other):
        """
        required by the Python sequence operations 'in' and 'not in'
        """
        if isinstance(other, aplQuantity):
            return self.__hash__() == other.__hash__()
        return False

    def __lt__(self, other):
        """
        required by the Python sort() method for sequences
        """
        return self._compare(other) < 0

    def __hash__(self):
        """
        required by the Python 'set' type
        """
        if self._hash is None:
            if self._resolved:
                for value in self._value:
                    if isinstance(value, aplQuantity):
                        value.__hash__()

            else:
                accumulator = []
                for value in self._value:
                    if isinstance(value, aplQuantity):
                        value.__hash__()
                    accumulator.append(value)

                if not isinstance(self._value, tuple):
                    self._value = tuple(accumulator)
                self._resolved = True

            self._hash = hash(self._value)
        return self._hash

    def _clone(self, other):
        """
        take on the attributes of some othe APL quantity (without realising any promises)
        """
        if isinstance(other, aplQuantity):
            self._value = other._value
            self._dimension = other._dimension
            self._prototype = other._prototype
            self._resolved = other._resolved
            self._hash = other._hash
        else:
            assertError("ASSERTION ERROR: aplQuantity._clone()")

        return self

    def _compare(self, other):
        """
        < 0, 0 or > 0 sor the self and other sort correctly
        """
        if not isinstance(other, aplQuantity):
            return 1

        delta = self.resolve().tally() - other.resolve().tally()

        if delta != 0:
            return delta

        A = self.__iter__()
        B = other.__iter__()
        try:
            while True:
                X = A.__next__()
                Y = B.__next__()

                if isinstance(X, aplQuantity):
                    delta = X.compare(Y)

                elif isinstance(Y, aplQuantity):
                    delta = -1

                elif isinstance(X, str) and isinstance(Y, str):
                    delta = ord(X) - ord(Y)

                elif isinstance(X, str):
                    delta = -1

                elif isinstance(Y, str):
                    delta = 1

                else:
                    delta = X - Y

                if delta != 0:
                    return delta

        except StopIteration:
            return 0

    def _lookAheadDimension(self, lowerBound):
        """
        return a good enough lower bound for the length of a vector
        """
        dimension = self._dimension

        if dimension < 0:
            if isinstance(self._value, tuple):
                self._dimension = self.tally()

                dimension = self._dimension
            else:
                dimension = self._value.buffer(lowerBound)
        return dimension

    def elementCount(self):
        """
        the dimension(s) of the quantity
        """
        if isinstance(self._dimension, tuple):
            return reduce(operator.mul, self._dimension, 1)

        elif isinstance(self._dimension, int):
            return self._dimension

        return 1

    def tally(self):
        """
        1 if a scalar, its length if a vector
        """
        if self._dimension is None:
            return 1

        if isinstance(self._dimension, int):
            if self._dimension < 0:
                if not isinstance(self._value, tuple):
                    self._value = tuple(self._value)
                self._dimension = len(self._value)

                if self._dimension == 0:
                    self._value = self._prototype
            return self._dimension

        assertError("ASSERTION ERROR: aplQuantity.tally()")

    def dimension(self):
        """
        the dimension(s) of the quantity
        """
        return self._dimension

    def rank(self):
        """
        the rank of the quantity
        """
        if isinstance(self._dimension, tuple):
            return len(self._dimension)
        return None

    def prototype(self):
        """
        the quantity's array prototype used for padding/filling
        """
        if self._prototype is None:
            if isinstance(self._value, tuple):
                initial = self._value[0]
            else:
                initial = self._value.peek()

            self._prototype = (makePrototype(initial),)
        return self._prototype

    def makePrototype(self):
        """
        the quantity's array prototype used for padding/filling
        """
        if self.isVectorLike():
            if isinstance(self._value, tuple):
                prototype = []
                for element in self._value:
                    prototype.append(makePrototype(element))
            else:
                prototype = self._value.makePrototype()

            return tuple(prototype)

        assertNotArray(self, "WIP - makePrototype PROTOTYPE RANK ERROR")

    def padFill(self):
        """
        the pad (aka fill) character/number for a vector quantity
        """
        if self.isVectorLike():
            prototype = self.prototype()

            if isinstance(prototype, aplQuantity):
                return prototype
            return prototype[0]

        assertNotArray(self, "WIP - pad PROTOTYPE RANK ERROR")

    def isString(self):
        """
        true if quantity really is a string
        """
        if self.padFill() == 0:
            return False

        if isinstance(self._value, tuple):
            for element in self._value:
                if not isinstance(element, str):
                    return False
            return True

        if not isinstance(self._value, lookAhead):
            self._value = lookAhead(self._value)

        return self._value.isString()

    def isScalar(self):
        """
        true if quantity is scalar
        """
        return self._dimension is None

    def isVector(self):
        """
        true if quantity is a vector
        """
        return isinstance(self._dimension, int)

    def isArray(self):
        """
        true if quantity is a higher order array
        """
        return isinstance(self._dimension, tuple)

    def isScalarLike(self):
        """
        true if quantity is scalar or a vector of length 1
        """
        if isinstance(self._dimension, int):
            return self._lookAheadDimension(2) == 1
        return self._dimension is None

    def isVectorLike(self):
        """
        true if quantity is scalar or a vector
        """
        if isinstance(self._dimension, int):
            return True
        return self._dimension is None

    def isEmptyVector(self):
        """
        true if quantity is a vector of length 0
        """
        if isinstance(self._dimension, int):
            return self._lookAheadDimension(1) == 0
        return False

    def scalarToPy(self):
        """
        return Python scalar (a single number or character)
        """
        if self.isArray():
            assertError("ASSERTION ERROR: aplQuantity.scalarToPy()")

        return self._value.__iter__().__next__()

    def vectorToPy(self):
        """
        return Python sequence (or a promise thereof)
        """
        if self.isArray():
            assertError("ASSERTION ERROR: aplQuantity.vectorToPy()")

        if self.isEmptyVector():
            return ()

        return self._value

    def arrayToPy(self):
        """
        return the Python sequence (or a promise thereof) that represents an array
        """
        if self.isArray():
            return self._value

        assertError("ASSERTION ERROR: aplQuantity.arrayToPy()")

    def promoteScalarToVectorPy(self, specialEmpty=False):
        """
        return a scalar as a scalar iterator but a vector as a sequence (promise)
        """
        if self.isScalar():
            return self.scalarIterator()

        if specialEmpty and self.isEmptyVector():
            return self.scalarIterator()

        if self.isVector():
            return self.vectorToPy()

        assertError("ASSERTION ERROR: aplQuantity.promoteScalarToVectorPy()")

    def python(self):
        """
        return the Python value (which could be a promise)
        """
        if self.isScalar():
            return self.scalarToPy()

        if self.isVector():
            return self.vectorToPy()

        assertError("ASSERTION ERROR: aplQuantity.python()")

    def safeScalar(self):
        """
        return the value of a scalar if safe and appropriate to do so

        We are just waiting for this one to blow up
        """
        if self.isScalar():
            value = self.scalarToPy()
            if not isinstance(value, aplQuantity):
                return value
            self._value = (value,)
        return self

    def scalarIterator(self):
        """
        infinite iterator for scalars so they may be used with arrays
        """
        return scalarIterator(self.scalarToPy(), -1, self.expressionToGo)

    def vectorIterator(self):
        """
        infinite iterator for vectors so they may be used with arrays
        """
        return vectorIterator(self.vectorToPy(), -1, self.expressionToGo)

    def resolve(self):
        """
        realise a promise (essentially a deep copy of a lazy APL quantity)
        """
        if not self._resolved:
            accumulator = []
            for value in self._value:
                if isinstance(value, aplQuantity):
                    value.resolve()
                accumulator.append(value)

            if not isinstance(self._value, tuple):
                self._value = tuple(accumulator)
            self._resolved = True
        return self

# ------------------------------

class   aplIterator(object):
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
            P.append(makePrototype(Y))

        try:
            while True:
                Y = self._pushBuffer(self._B.__next__())

                P.append(makePrototype(Y))
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

# ------------------------------

def     makeScalar(value, prototype=(0,)):
    """
    make an APL scalar quantity from a scalar Python value
    """
    if isinstance(value, aplQuantity):
        assertError("makeScalar: needs more thought")

    try:
        value = value.__iter__().__next__()
    except AttributeError:
        pass

    return aplQuantity((value,), None, prototype)

# --------------

def     makeVector(value, length=-1, prototype=(0,)):
    """
    make an APL vector quantity from a Python list
    """
    if length is None:
        length = 1

    if not isinstance(value, (tuple, lookAhead)):
        if length < 0 or prototype is None:
            value = lookAhead(value, 1)

    if isinstance(value, lookAhead):
        if length < 0:
            if value.buffered() == 0:
                length = 0

        if prototype is None:
            if value.buffered() == 0:
                assertError("ASSERTION ERROR: makeVector()")
            prototype = (makePrototype(value.peek()),)

    if length == 0:
        return makeEmptyVector(prototype)

    return aplQuantity(value, length, prototype)

# --------------

def     makeArray(value, dimensions, prototype=(0,)):
    return aplQuantity(value, dimensions, prototype)

# --------------

def     makeEmptyVector(prototype=(0,)):
    """
    make an empty APL vector quantity (⍬ or '')
    """
    return aplQuantity(prototype, 0, prototype)

# --------------

def     makeString(value, withDelimiter):
    """
    make an APL string quantity from a Python string
    """
    if withDelimiter:
        delimiter = value[0]
        value = value.replace(delimiter*2, delimiter)[1:-1]

    length = len(value)

    if length == 0:
        value = ' '

    if withDelimiter:
        if length == 1 and delimiter == "'":
            length = None

    return aplQuantity(tuple(value), length, (' ',))

# --------------

def     makePrototype(value):
    """
    the 'array prototype' for this value
    """
    if isinstance(value, aplQuantity):
        prototype = value.makePrototype()

        return aplQuantity(prototype, len(prototype), prototype)

    return ' ' if isinstance(value, str) else 0

# EOF
