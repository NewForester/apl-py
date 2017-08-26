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

    Strings have a lazy representation - a promise of a list of the ordinal representation of the
    characters in the Python string.  A scalar string is a single character.

    Scalars are stored as a list of length 1 for computational convenience.

    Mixed vectors comprised numeric and string values and are, by definition, nested.

    Strings and hence mixed/nested vectors are a product of the parser: support for these is adhoc.
"""

from aplError import aplError

# ------------------------------

class   aplQuantity(object):
    """
    trivial class that holds an APL quantity
    """
    def __init__(self, value, dimension=0, string=False):
        try:
            if dimension == None:
                iter(value)
            self._value = value

        except TypeError:
            self._value = tuple([value])

        self._dimension = dimension
        self._string = string
        self._resolved = False
        self.expressionToGo = None

    def __iter__(self):
        return self._value.__iter__()

    def _clone(self, quantity):
        """
        clone (without realising any promises)
        """
        self._value = quantity._value
        self._dimension = quantity._dimension
        self._string = quantity._string
        self._resolved = quantity._resolved

    def tally(self):
        """
        1 if a scalar, its length if a vector
        """
        if self._dimension is None:
            return 1

        if isinstance(self._dimension, int):
            return self._dimension

        aplError("RANK ERROR ASSERTION")

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
        the padding/filling value
        """
        return ord(' ') if self.isString() else 0

    def isString(self):
        """
        true is quantity is a string
        """
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
        return self._dimension is not None

    def isArray(self):
        """
        true if quantity is a higher order array
        """
        return isinstance(self._dimension, tuple)

    def isScalarLike(self):
        """
        true if quantity is scalar or a vector length 1
        """
        return self._dimension is None or (isinstance(self._dimension, int) and self._dimension == 1)

    def isVectorLike(self):
        """
        true if quantity is scalar or a vector
        """
        return self._dimension is None or isinstance(self._dimension, int)

    def isEmptyVector(self):
        """
        true if quantity is a vector length 0
        """
        return isinstance(self._dimension, int) and self._dimension == 0

    def scalarToPy(self, error=None):
        """
        return Python numeric
        """
        if self._dimension is None or self._dimension == 1:
            return next(iter(self._value))

        aplError(error if error else "RANK ERROR")

    def vectorToPy(self):
        """
        return Python list
        """
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
            return next(iter(self._value))
        else:
            return self._value

    def scalarIterator(self):
        """
        infinite iterator for scalars so they may be used with arrays
        """
        return scalarIterator(self.scalarToPy(), self.expressionToGo)

    def resolve(self):
        """
        realise a promise
        """
        if self._resolved:
            return self

        return _resolveMap(self)

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

class   _resolveIterator(object):
    """
    recursive iterator for eager evaluation of a lazy APL quantity B
    """
    def __init__(self, B):
        self._B = B.__iter__()

    def __iter__(self):
        return self

    def __next__(self):
        Y = self._B.__next__()

        if isinstance(Y, aplQuantity):
            if not Y._resolved:
                return _resolveMap(Y)

        return Y

# --------------

def     _resolveMap(B):
    """
    map for eager evaluation of a lazy APL quantity B
    """
    if B.isScalar():
        R = aplQuantity(tuple(_resolveIterator(B)), None, B.isString())

    elif B.isVector():
        R = aplQuantity(tuple(_resolveIterator(B)), B.dimension(), B.isString())

    else:
        aplError("RANK ERROR")

    R.expressionToGo = B.expressionToGo
    R._resolved = True
    return R

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

    return aplQuantity(map(ord, value), length, True)

# EOF
