"""
    dyadic APL function lookup

    UNDER DEVELOPMENT

    WIP - there are a number of functions yet to be implemented

    This module provides a single callable routine. The routine is passed an
    APL symbol and returns a Python function that implements the APL dyadic
    function represented by the symbol.

    The Python function returned is typically a lambda function that invokes
    a higher order map function and passes it the scalar version of the function
    (mathematical APL functions) or an iterator (other APL functions).

    The routine also returns a value indicating how to evaluate the reduce
    operator when applied to an empty vector.  For most functions, the value is
    None, indicating that a DOMAIN ERROR should be thrown.  Any other value is
    taken to be the result of the reduction.
"""

import dyadicMaps as mapper
import dyadicFunctions as dyadic
import dyadicIterators as iterator

from aplError import assertError

# ------------------------------

def     _toBeImplemented(_, __):
    """
    placeholder for functions not yet implemented

    raises FUNCTION NOT YET IMPLEMENTED
    """
    assertError("FUNCTION NOT YET IMPLEMENTED")

# ------------------------------

_DyadicFunctions = {
    # Arithmetic
    '+':        (0, lambda A, B: mapper.maths(dyadic.add, A, B)),
    '-':        (0, lambda A, B: mapper.maths(dyadic.subtract, A, B)),
    '×':        (1, lambda A, B: mapper.maths(dyadic.multiply, A, B)),
    '÷':        (1, lambda A, B: mapper.maths(dyadic.divide, A, B)),
    '⌈':        (float('-inf'), lambda A, B: mapper.maths(dyadic.maximum, A, B)),
    '⌊':        (float('inf'),  lambda A, B: mapper.maths(dyadic.minimum, A, B)),
    '|':        (0, lambda A, B: mapper.maths(dyadic.residue, A, B)),

    # Algebraic
    '*':        (1, lambda A, B: mapper.maths(dyadic.exp, A, B)),
    '⍟':        (None, lambda A, B: mapper.maths(dyadic.log, A, B)),
    '!':        (1, lambda A, B: mapper.maths(dyadic.binomial, A, B)),
    '?':        (None, lambda A, B: mapper.deal(dyadic.deal, A, B)),
    '⌹':        (None, _toBeImplemented),  # matrix divide

    # Trigonometric
    '○':        (0, lambda A, B: mapper.maths(dyadic.circular, A, B)),

    # Logical
    '∨':        (0, lambda A, B: mapper.maths(dyadic.orGCD, A, B)),
    '∧':        (1, lambda A, B: mapper.maths(dyadic.andLCM, A, B)),
    '⍱':        (None, lambda A, B: mapper.maths(dyadic.nor, A, B)),
    '⍲':        (None, lambda A, B: mapper.maths(dyadic.nand, A, B)),

    # Comparison
    '<':        (0, lambda A, B: mapper.maths(dyadic.lt, A, B)),
    '≤':        (1, lambda A, B: mapper.maths(dyadic.le, A, B)),
    '≥':        (1, lambda A, B: mapper.maths(dyadic.ge, A, B)),
    '>':        (0, lambda A, B: mapper.maths(dyadic.gt, A, B)),
    '=':        (1, lambda A, B: mapper.maths(dyadic.eq, A, B)),
    '≠':        (0, lambda A, B: mapper.maths(dyadic.ne, A, B)),
    '≡':        (None, lambda A, B: mapper.match(dyadic.eq, A, B)),
    '≢':        (None, lambda A, B: mapper.noMatch(dyadic.eq, A, B)),

    # Structural (aka manipulative)
    '⍴':        (None, lambda A, B: mapper.reshape(iterator.reshape, A, B)),
    ',':        (None, lambda A, B: mapper.concatenate(iterator.concatenate, A, B)),
    '⍪':        (None, lambda A, B: mapper.concatenate(iterator.concatenate, A, B)),
    '⍉':        (None, lambda A, B: mapper.transpose(iterator.transpose, A, B)),
    '⌽':        (None, lambda A, B: mapper.rotateLast(iterator.rotate, A, B)),
    '⊖':        (None, lambda A, B: mapper.rotateFirst(iterator.rotate, A, B)),
    '⊂':        (None, lambda A, B: mapper.partition(iterator.partition, A, B)),
    '⊃':        (None, lambda A, B: mapper.pick(None, A, B)),

    # Selection and Set Operations
    '∊':        (None, lambda A, B: mapper.membership(iterator.membership, A, B)),
    '⍷':        (None, lambda A, B: mapper.find(iterator.find, A, B)),
    '⍳':        (None, lambda A, B: mapper.index(iterator.index, A, B)),
    '~':        (None, lambda A, B: mapper.without(iterator.without, A, B)),
    '∪':        (None, lambda A, B: mapper.set2set(iterator.union, A, B)),
    '∩':        (None, lambda A, B: mapper.set2set(iterator.intersection, A, B)),
    '↓':        (None, lambda A, B: mapper.drop(iterator.drop, A, B)),
    '↑':        (None, lambda A, B: mapper.take(iterator.take, A, B)),
    '/':        (None, lambda A, B: mapper.compressLast(iterator.compress, A, B)),
    '⌿':        (None, lambda A, B: mapper.compressFirst(iterator.compress, A, B)),
    '\\':       (None, lambda A, B: mapper.expandLast(iterator.expand, A, B)),
    '⍀':        (None, lambda A, B: mapper.expandFirst(iterator.expand, A, B)),
    '⍋':        (None, lambda A, B: mapper.grade(False, A, B)),
    '⍒':        (None, lambda A, B: mapper.grade(True, A, B)),
    '⌷':        (None, _toBeImplemented),  # index

    # Miscellaneous
    '⍺':        (None, _toBeImplemented),  # picture format
    '⍕':        (None, _toBeImplemented),  # dyadic (specification) format
    '⍎':        (None, _toBeImplemented),  # dyadic execute
    '⊤':        (None, lambda A, B: mapper.encode(iterator.encode, A, B)),
    '⊥':        (None, lambda A, B: mapper.decode(iterator.decode, A, B)),
    '⊣':        (None, lambda A, B: A),
    '⊢':        (None, lambda A, B: B),
}

# ------------------------------

def     dyadicFunction(symbol):
    """
    return the dyadic function given its APL symbol

    raises INVALID TOKEN if the symbol is not recognised
    """

    try:
        return _DyadicFunctions[symbol[0]]
    except ZeroDivisionError:
        assertError("DOMAIN ERROR")
    except KeyError:
        assertError("INVALID TOKEN")

# EOF
