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
    '+':        lambda A, B: mapper.maths(dyadic.add, A, B),
    '-':        lambda A, B: mapper.maths(dyadic.subtract, A, B),
    '×':        lambda A, B: mapper.maths(dyadic.multiply, A, B),
    '÷':        lambda A, B: mapper.maths(dyadic.divide, A, B),
    '⌈':        lambda A, B: mapper.maths(dyadic.maximum, A, B),
    '⌊':        lambda A, B: mapper.maths(dyadic.minimum, A, B),
    '|':        lambda A, B: mapper.maths(dyadic.residue, A, B),

    # Algebraic
    '*':        lambda A, B: mapper.maths(dyadic.exp, A, B),
    '⍟':        lambda A, B: mapper.maths(dyadic.log, A, B),
    '!':        lambda A, B: mapper.maths(dyadic.binomial, A, B),
    '?':        lambda A, B: mapper.deal(dyadic.deal, A, B),
    '⌹':        _toBeImplemented,       # matrix divide

    # Trigonometric
    '○':        lambda A, B: mapper.maths(dyadic.circular, A, B),

    # Logical
    '∨':        lambda A, B: mapper.maths(dyadic.orGCD, A, B),
    '∧':        lambda A, B: mapper.maths(dyadic.andLCM, A, B),
    '⍱':        lambda A, B: mapper.maths(dyadic.nor, A, B),
    '⍲':        lambda A, B: mapper.maths(dyadic.nand, A, B),

    # Comparison
    '<':        lambda A, B: mapper.maths(dyadic.lt, A, B),
    '≤':        lambda A, B: mapper.maths(dyadic.le, A, B),
    '≥':        lambda A, B: mapper.maths(dyadic.ge, A, B),
    '>':        lambda A, B: mapper.maths(dyadic.gt, A, B),
    '=':        lambda A, B: mapper.maths(dyadic.eq, A, B),
    '≠':        lambda A, B: mapper.maths(dyadic.ne, A, B),
    '≡':        lambda A, B: mapper.match(dyadic.eq, A, B),
    '≢':        lambda A, B: mapper.noMatch(dyadic.eq, A, B),

    # Structural (aka manipulative)
    '⍴':        lambda A, B: mapper.reshape(iterator.reshape, A, B),
    ',':        lambda A, B: mapper.concatenate(iterator.concatenate, A, B),
    '⍪':        lambda A, B: mapper.concatenate(iterator.concatenate, A, B),
    '⍉':        lambda A, B: mapper.transpose(iterator.transpose, A, B),
    '⌽':        lambda A, B: mapper.rotate(iterator.rotate, A, B),
    '⊖':        lambda A, B: mapper.rotate(iterator.rotate, A, B),
    '⊂':        lambda A, B: mapper.partition(iterator.partition, A, B),
    '⊃':        lambda A, B: mapper.pick(None, A, B),

    # Selection and Set Operations
    '∊':        lambda A, B: mapper.membership(iterator.membership, A, B),
    '⍷':        lambda A, B: mapper.find(iterator.find, A, B),
    '⍳':        lambda A, B: mapper.index(iterator.index, A, B),
    '~':        lambda A, B: mapper.without(iterator.without, A, B),
    '∪':        lambda A, B: mapper.set2set(iterator.union, A, B),
    '∩':        lambda A, B: mapper.set2set(iterator.intersection, A, B),
    '↓':        lambda A, B: mapper.drop(iterator.drop, A, B),
    '↑':        lambda A, B: mapper.take(iterator.take, A, B),
    '/':        lambda A, B: mapper.compress(iterator.compress, A, B),
    '⌿':        lambda A, B: mapper.compress(iterator.compress, A, B),
    '\\':       lambda A, B: mapper.expand(iterator.expand, A, B),
    '⍀':        lambda A, B: mapper.expand(iterator.expand, A, B),
    '⍋':        lambda A, B: mapper.grade(False, A, B),
    '⍒':        lambda A, B: mapper.grade(True, A, B),
    '⌷':        _toBeImplemented,       # index

    # Miscellaneous
    '⍺':        _toBeImplemented,       # picture format
    '⍕':        _toBeImplemented,       # dyadic (specification) format
    '⍎':        _toBeImplemented,       # dyadic execute
    '⊤':        lambda A, B: mapper.encode(iterator.encode, A, B),
    '⊥':        lambda A, B: mapper.decode(iterator.decode, A, B),
    '⊣':        lambda A, B: A,
    '⊢':        lambda A, B: B,
}

# ------------------------------

def     dyadicFunction(symbol):
    """
    return the dyadic function given its APL symbol

    raises INVALID TOKEN if the symbol is not recognised
    """

# // need identity for ⍬ - so prepend it to the table and return it
# // what follows is a temporary hack

    try:
        return 0, _DyadicFunctions[symbol[0]]
    except KeyError:
        assertError("INVALID TOKEN")

# EOF
