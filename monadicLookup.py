"""
    monadic APL function lookup

    UNDER DEVELOPMENT

    WIP - there are a number of functions yet to be implemented

    This module provides a single callable routine. The routine is passed an
    APL symbol and returns a Python function that implements the APL monadic
    function represented by the symbol.

    The Python function returned is typically a lambda function that invokes
    a higher order map function and passes it the scalar version of the function
    (mathematical APL functions) or an iterator (other APL functions).
"""

import monadicMaps as mapper
import monadicFunctions as monadic
import monadicIterators as iterator

from aplQuantity import makeScalar
from aplError import assertError

# ------------------------------

def     _toBeImplemented(_):
    """
    placeholder for functions not yet implemented

    raises FUNCTION NOT YET IMPLEMENTED
    """
    assertError("FUNCTION NOT YET IMPLEMENTED")

# ------------------------------

_MonadicFunctions = {
    # Arithmetic
    '+':        lambda B: mapper.maths(monadic.identity, B),
    '-':        lambda B: mapper.maths(monadic.negation, B),
    '×':        lambda B: mapper.maths(monadic.signum, B),
    '÷':        lambda B: mapper.maths(monadic.reciprocal, B),
    '⌈':        lambda B: mapper.maths(monadic.ceil, B),
    '⌊':        lambda B: mapper.maths(monadic.floor, B),
    '|':        lambda B: mapper.maths(monadic.magnitude, B),

    # Algebraic
    '*':        lambda B: mapper.maths(monadic.exp, B),
    '⍟':        lambda B: mapper.maths(monadic.log, B),
    '!':        lambda B: mapper.maths(monadic.factorial, B),
    '?':        lambda B: mapper.maths(monadic.roll, B),
    '⌹':        _toBeImplemented,       # matrix inverse

    # Trigonometric
    '○':        lambda B: mapper.maths(monadic.pi, B),

    # Logical
    '~':        lambda B: mapper.maths(monadic.logicalNegation, B),
    '∨':        lambda B: assertError("VALENCE ERROR"),
    '∧':        lambda B: assertError("VALENCE ERROR"),
    '⍱':        lambda B: assertError("VALENCE ERROR"),
    '⍲':        lambda B: assertError("VALENCE ERROR"),

    # Comparison
    '<':        lambda B: assertError("VALENCE ERROR"),
    '≤':        lambda B: assertError("VALENCE ERROR"),
    '=':        lambda B: assertError("VALENCE ERROR"),
    '≥':        lambda B: assertError("VALENCE ERROR"),
    '>':        lambda B: assertError("VALENCE ERROR"),
    '≠':        lambda B: assertError("VALENCE ERROR"),

    # Structural (aka manipulative)
    '⍳':        lambda B: mapper.iota(iterator.iota, B),
    '≡':        lambda B: mapper.depth(iterator.depth, B),
    '≢':        lambda B: mapper.tally(None, B),
    '⍴':        lambda B: mapper.rho(None, B),
    ',':        lambda B: mapper.unravel(None, B),
    '⍪':        lambda B: assertError("VALENCE ERROR"),
    '∊':        lambda B: mapper.enlist(iterator.enlist, B),
    '⍷':        lambda B: assertError("VALENCE ERROR"),
    '⍉':        lambda B: mapper.transpose(iterator.transpose, B),
    '⌽':        lambda B: mapper.reverse(iterator.reverse, B),
    '⊖':        lambda B: mapper.reverse(iterator.reverse, B),
    '⊂':        lambda B: mapper.enclose(None, B),
    '⊃':        lambda B: mapper.disclose(iterator.disclose, B),

    # Selection and Set Operations
    '∪':        lambda B: mapper.unique(iterator.unique, B),
    '∩':        lambda B: assertError("VALENCE ERROR"),
    '↓':        lambda B: mapper.tail(iterator.tail, B),
    '↑':        lambda B: mapper.head(iterator.head, B),
    '/':        lambda B: assertError("SYNTAX ERROR"),
    '⌿':        lambda B: assertError("SYNTAX ERROR"),
    '\\':       lambda B: assertError("SYNTAX ERROR"),
    '⍀':        lambda B: assertError("SYNTAX ERROR"),
    '⍋':        lambda B: mapper.grade(False, B),
    '⍒':        lambda B: mapper.grade(True, B),
    '⌷':        lambda B: assertError("VALENCE ERROR"),

    # Miscellaneous
    '⍺':        lambda B: assertError("VALENCE ERROR"),
    '⍕':        _toBeImplemented,       # monadic format
    '⍎':        _toBeImplemented,       # execute
    '⊤':        lambda B: assertError("VALENCE ERROR"),
    '⊥':        lambda B: assertError("VALENCE ERROR"),
    '⊣':        lambda B: makeScalar(0),
    '⊢':        lambda B: B,
}

# ------------------------------

def     monadicFunction(symbol):
    """
    return the monadic function given its APL symbol

    raises INVALID TOKEN if the symbol is not recognised
    """
    try:
        return _MonadicFunctions[symbol[0]]
    except KeyError:
        assertError("INVALID TOKEN")

# EOF
