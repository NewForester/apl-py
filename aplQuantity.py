"""
    a Python type that can hold APL scalar and vector quantities, both numeric and string

    UNDER DEVELOPMENT

    APL quantities have:
        - prototype - rank and dimensions
        - type - numeric, string, nested
        - depth - degree of nesting
        - empty - an APL quantity may have no values but may still have the other properties

    The current version supports
        - numeric and string scalars
            - scalars comprise a single value and have neither rank nor dimension
        - numeric, string and mixed vectors
            - vectors comprise a (Python) list of values and have no rank but a single dimension

    Strings are represented by a tuple of single characters, each of which has Python type str.

    Scalars are stored as a list of length 1 for computational convenience.
"""

from aplError import aplError

# ------------------------------

class   aplQuantity(object):
    """
    trivial class that holds an APL quantity
    """
    def __init__(self, value, dimension=0, string=False):
        try:
            if dimension is None:
                iter(value)
            self._value = value

        except TypeError:
            self._value = tuple([value])

        self._dimension = dimension
        self._string = string
        self._resolved = False
        self._hash = None
        self.expressionToGo = None

    def __iter__(self):
        return self._value.__iter__()

    def __eq__(self, other):
        if isinstance(other, aplQuantity):
            return self.__hash__() == other.__hash__()

        return False

    def __hash__(self):
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
        clone (without realising any promises)
        """
        if isinstance(other, aplQuantity):
            self._value = other._value
            self._dimension = other._dimension
            self._string = other._string
            self._resolved = other._resolved
            self._hash = other._hash

    def tally(self):
        """
        1 if a scalar, its length if a vector
        """
        if self._dimension is None:
            return 1

        if isinstance(self._dimension, int):
            return self.dimension()

        aplError("RANK ERROR ASSERTION")

    def dimension(self):
        """
        the dimension(s) of the quantity
        """
        if isinstance(self._dimension, int):
            if self._dimension == -1:
                if not isinstance(self._value, tuple):
                    self._value = tuple(self._value)
                self._dimension = len(self._value)
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
        return ' ' if self.isString() else 0

    def isString(self):
        """
        true if quantity is a string
        """
        if self._string is None:
            if not isinstance(self._value, tuple):
                self._value = tuple(self._value)
            self._string = isinstance(self._value[0], str)
        return self._string

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
        true if quantity is scalar or a vector length 1
        """
        return self._dimension is None or (isinstance(self._dimension, int) and self.dimension() == 1)

    def isVectorLike(self):
        """
        true if quantity is scalar or a vector
        """
        return self._dimension is None or isinstance(self._dimension, int)

    def isEmptyVector(self):
        """
        true if quantity is a vector length 0
        """
        return isinstance(self._dimension, int) and self.dimension() == 0

    def scalarToPy(self, error=None):
        """
        return Python numeric
        """
        self.isString()

        if self._dimension is None or self.dimension() == 1:
            return next(iter(self._value))

        aplError(error if error else "RANK ERROR")

    def vectorToPy(self):
        """
        return Python list
        """
        self.isString()

        return self._value

    def promoteScalarToVectorPy(self, specialEmpty=False):
        """
        return a scalar as a scalar iterator but a vector as a sequence (promise)
        """
        if self.isScalar():
            return self.scalarIterator()

        if specialEmpty and self.isEmptyVector():
            return scalarIterator(self.prototype())

        if self.isVector():
            return self.vectorToPy()

        aplError("RANK ASSERTION ERROR")

    def python(self):
        """
        return the Python value (which could be a promise)
        """
        if self.isScalar():
            return self.scalarToPy()

        if self.isVector():
            return self.vectorToPy()

        aplError("RANK ERROR")

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
        return scalarIterator(self.scalarToPy(), self.expressionToGo)

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

class   scalarIterator(object):
    """
    trival iterator for mapping scalar quantities with vector quantities

    the iterator returns the scalar value ad infinitum
    """
    def __init__(self, value, expressionToGo=None):
        self._value = value
        self.expressionToGo = expressionToGo

    def __iter__(self):
        return self

    def __next__(self):
        return self._value

# ------------------------------

def     makeScalar(value, string=False):
    """
    make an APL scalar quantity from a numeric Python value
    """
    try:
        value.__iter__()
    except AttributeError:
        value = (value,)

    return aplQuantity(value, None, string)

# --------------

def     makeVector(value, length=-1, string=False):
    """
    make an APL vector quantity from a numeric Python list
    """
    return aplQuantity(value, length, string)

# --------------

def     makeEmptyVector(string=False):
    """
    make an empty APL vector quantity (⍬ or '')
    """
    return aplQuantity((), 0, string)

# --------------

def     makeString(value, withDelimiter):
    """
    make an APL string quantity from a Python string
    """
    if withDelimiter:
        delimiter = value[0]
        value = value.replace(delimiter*2, delimiter)[1:-1]

    length = len(value)

    if withDelimiter:
        if length == 1 and delimiter == "'":
            length = None

    return aplQuantity(tuple(value), length, True)

# EOF
