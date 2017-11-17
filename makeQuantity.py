"""
    factory methods for creating APL quantities

    UNDER DEVELOPMENT

    This module was factored out from aplQuantity when aplIterators was.  It
    was necessary to avoid circular references.

    Note the import of makePrototype from aplQuantity 'completes' the set and
    bears witness to the expediency of refactoring.

    Since subclassing of aplQuantity is expected during the next major
    refactoring and makePrototype may disappear then, the current not quite
    optimal situation will be tolerated until then.
"""

from aplQuantity import aplQuantity
from aplIterators import lookAhead
from aplError import assertError

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

    elif isinstance(value, list):
        value = tuple(value)

    if length == 0:
        return makeEmptyVector(prototype)

    if not isinstance(value, (tuple, lookAhead)):
        value = lookAhead(value, 1)

    return aplQuantity(value, length, None)

# --------------

def     makeArray(value, dimensions, prototype=(0,)):
    if isinstance(value, list):
        value = tuple(value)

    return aplQuantity(value, tuple(dimensions), prototype)

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
