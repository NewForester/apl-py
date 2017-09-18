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

from monadicMaps import *
from monadicFunctions import *
from monadicIterators import *

from aplQuantity import makeScalar
from aplError import aplError

# ------------------------------

def     _toBeImplemented(_):
    """
    placeholder for functions not yet implemented

    raises FUNCTION NOT YET IMPLEMENTED
    """
    aplError("FUNCTION NOT YET IMPLEMENTED")

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
    '∨':        lambda B: aplError("VALENCE ERROR"),
    '∧':        lambda B: aplError("VALENCE ERROR"),
    '⍱':        lambda B: aplError("VALENCE ERROR"),
    '⍲':        lambda B: aplError("VALENCE ERROR"),

    # Comparison
    '<':        lambda B: aplError("VALENCE ERROR"),
    '≤':        lambda B: aplError("VALENCE ERROR"),
    '=':        lambda B: aplError("VALENCE ERROR"),
    '≥':        lambda B: aplError("VALENCE ERROR"),
    '>':        lambda B: aplError("VALENCE ERROR"),
    '≠':        lambda B: aplError("VALENCE ERROR"),

    # Structural (aka manipulative)
    '⍳':        lambda B: mapper.iota(iterator.iota, B),
    '≡':        lambda B: mapper.depth(iterator.depth, B),
    '≢':        lambda B: mapper.tally(None, B),
    '⍴':        lambda B: mapper.rho(None, B),
    ',':        lambda B: mapper.unravel(None, B),
    '⍪':        lambda B: aplError("VALENCE ERROR"),
    '∊':        _toBeImplemented,       # enlist - as comma but also nested arrays
    '⍉':        lambda B: mapper.transpose(iterator.transpose, B),
    '⌽':        lambda B: mapper.reverse(iterator.reverse, B),
    '⊖':        lambda B: mapper.reverse(iterator.reverse, B),
    '⊃':        _toBeImplemented,       # (disclose) - turn nested scalar into vector (?!?) - mix ?
    '⊂':        _toBeImplemented,       # (enclose) - turn array into nested scalar (?!?)

    # Selection and Set Operations
    '∪':        lambda B: mapper.unique(iterator.unique, B),
    '∩':        lambda B: aplError("VALENCE ERROR"),
    '↓':        lambda B: mapper.tail(iterator.tail, B),
    '↑':        lambda B: v_head(head, B),
    '⌷':        lambda B: aplError("VALENCE ERROR"),
    '/':        lambda B: aplError("VALENCE ERROR"),
    '⌿':        lambda B: aplError("VALENCE ERROR"),
    '\\':       lambda B: aplError("VALENCE ERROR"),
    '⍀':        lambda B: aplError("VALENCE ERROR"),

    # Miscellaneous
    '⍷':        lambda B: aplError("VALENCE ERROR"),
    '⍋':        _toBeImplemented,       # grade up (ascending sort indicies)
    '⍒':        _toBeImplemented,       # grade down (descending sort indicies)
    '⍺':        lambda B: aplError("VALENCE ERROR"),
    '⍕':        _toBeImplemented,       # monadic format
    '⍎':        _toBeImplemented,       # execute
    '⊤':        lambda B: aplError("VALENCE ERROR"),
    '⊥':        lambda B: aplError("VALENCE ERROR"),
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
        aplError("INVALID TOKEN", symbol)

# EOF
