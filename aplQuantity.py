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
        self._string = string
        self._dim = dimension

        try:
            if self._dim == None:
                iter(value)
            self._value = value

        except TypeError:
            self._value = tuple([value])

        self.expressionToGo = None

    def __iter__(self):
        return self._value.__iter__()

    def scalarIter(self):
        """
        infinite iterator for scalars so they may be used with arrays
        """
        if not self.isScalar():
            aplError("RANK ASSERTION ERROR")

        return aplScalarIter(next(iter(self._value)))

    def clone(self, quantity):
        """
        clone without realishcing promises
        """
        self._string = quantity._string
        self._dim = quantity._dim
        self._value = quantity._value

    def deepClone(self, quantity):
        """
        clone converting promises
        """
        self.clone(quantity.resolve())      # quick and dirty

    def python(self):
        """
        return the Python value (could be a promise)
        """
        if self.isScalar():
            return next(iter(self._value))
        else:
            return self._value

    def resolve(self):
        """
        realise a promise
        """
        return aplQuantity(list(self._value), self._dim, self._string)

    def noStringConfirm(self):
        """
        ensure quantity is not a string quantity
        """
        if self.isString():
            aplError("DOMAIN ERROR")

    def scalarToPy(self, error=None):
        """
        return Python numeric
        """
        if self._dim is None or self._dim == 1:
            return next(iter(self._value))

        aplError(error if error else "RANK ERROR")

    def vectorToPy(self):
        """
        return Python list
        """
        return self._value

    def dimension(self):
        """
        the dimensions of the quantity
        """
        return self._dim

    def isString(self):
        """
        true is quantity is a string
        """
        return self._string

    def isScalar(self):
        """
        true if quantity is scalar
        """
        return self._dim is None

    def isVector(self):
        """
        true if quantity is a vector
        """
        return self._dim is not None

# ------------------------------

class   aplScalarIter(object):
    """
    trival class that supports mixed scalar/vector arithmetic

    the iterable returns the same value ad infinitum
    """
    def __init__(self, value):
        self._value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self._value

# ------------------------------

def     makeScalar(value):
    """
    make an APL scalar quantity from a numeric Python value
    """
    return aplQuantity([value], None)

# ------------------------------

def     makeVector(value, string=False):
    """
    make an APL vector quantity from a numeric Python list
    """
    return aplQuantity(value, len(value), string)

# ------------------------------

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
