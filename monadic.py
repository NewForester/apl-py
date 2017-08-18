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
    '+':        lambda B: s2s(identity, B),
    '-':        lambda B: s2s(negation, B),
    '×':        lambda B: s2s(signum, B),
    '÷':        lambda B: s2s(reciprocal, B),
    '⌈':        lambda B: s2s(ceil, B),
    '⌊':        lambda B: s2s(floor, B),
    '|':        lambda B: s2s(magnitude, B),

    # Algebraic
    '*':        lambda B: s2s(exp, B),
    '⍟':        lambda B: s2s(log, B),
    '!':        lambda B: s2s(factorial, B),
    '?':        lambda B: s2s(roll, B),
    '⌹':        _toBeImplemented,       # matrix inverse

    # Trigonometric
    '○':        lambda B: s2s(pi, B),

    # Logical
    '~':        lambda B: s2s(logicalNegation, B),
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
    '⍳':        lambda B: s2v(iota, B),
    '≡':        lambda B: v_nest(B),
    '≢':        lambda B: v_tally(B),
    '⍴':        lambda B: s_rho(None, B),
    ',':        lambda B: s_comma(None, B),
    '⍪':        lambda B: aplError("VALENCE ERROR"),
    '∊':        _toBeImplemented,       # enlist - as comma but also nested arrays
    '⌽':        lambda B: v2v(reverseLast, B),
    '⊖':        lambda B: v2v(reverseFirst, B),
    '⍉':        lambda B: v2v(transpose, B),
    '⊃':        _toBeImplemented,       # (disclose) - turn nested scalar into vector (?!?) - mix ?
    '⊂':        _toBeImplemented,       # (enclose) - turn array into nested scalar (?!?)

    # Selection and Set Operations
    '↑':        lambda B: v_head(head, B),
    '↓':        lambda B: v_tail(tail, B),
    '⌷':        lambda B: aplError("VALENCE ERROR"),
    '∪':        lambda B: v2v(unique, B),
    '∩':        lambda B: aplError("VALENCE ERROR"),
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
