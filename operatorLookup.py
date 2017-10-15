"""
    APL operator lookup

    UNDER DEVELOPMENT

    WIP - there are more operators to be implemented

    This module provides a single callable routine. The routine is passed an
    APL symbol and returns a Python function that implements the APL operator
    function represented by the symbol.

    This module is being implemented by analogy with the dyadic and monadic
    lookup modules.  It is experimental and may be replaced.
"""

import operatorMaps as mapper

from aplError import assertError

# ------------------------------

_OperatorFunctions = {
    # scan and reduce
    '/':        mapper.reduceLast,
    '⌿':        mapper.reduceFirst,
    '\\':       mapper.scanLast,
    '⍀':        mapper.scanFirst,
}

# ------------------------------

def     operatorFunction(symbol):
    """
    return the Python function that handles an APL operator given the operator's symbol

    return none if the symbol is not that of an operator
    """
    try:
        return _OperatorFunctions[symbol[0]]
    except KeyError:
        return None

# EOF
