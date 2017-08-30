"""
    APL System Variables

    UNDER DEVELOPMENT

    This initial version implements only ⎕CT and ⎕IO.

    The non-standard ⎕EE was added to ease switching between lazy and eager
    evaluation modes for debugging purposes and may be withdrawn.
"""

import math
import operator

from aplQuantity import aplQuantity, makeScalar
from aplError import assertError

# ------------------------------

class   _systemVariable(aplQuantity):
    """
    an APL system variable is represented by a triplet;
        - a make function (used to make an APL quantity from a Python value)
        - a confirm function (used to validate the Python value)
        - an APL quantity
    """
    def __init__(self, makeFunction, confirmFunction, value):
        aplQuantity.__init__(self, [])
        self._make = makeFunction
        self._confirm = confirmFunction
        self._clone(self._make(self._confirm(value)))
        self._resolved = True

    def get(self):
        """
        return the APL quantity
        """
        return self

    def set(self, quantity):
        """
        validate and set the APL quantity
        """
        self._clone(self._make(self._confirm(quantity.python())))
        self._resolved = True

# ------------------------------

def     fuzzyEquals(A, B):
    """
    true if A = B to within the current comparison tolerance
    """
    return operator.le(math.fabs(operator.sub(A, B)),
                       operator.mul(_CT.python(), max(math.fabs(A), math.fabs(B))))

# --------------

def     fuzzyInteger(B):
    """
    B but, if B is within comparison toleranace of an integer, the integer
    """
    if isinstance(B, int):
        return B

    if B > 0:
        I = int(B+0.5)
    elif B < 0:
        I = int(B-0.5)
    else:
        I = 0

    if fuzzyEquals(I, B):
        return I

    return B

# --------------

def     confirmBoolean(B):
    """
    the Boolean-domain value of B (if within comparison tolerance - else throw DOMAIN ERROR)
    """
    try:
        B = fuzzyInteger(B)

        if B == 0:
            return 0
        if B == 1:
            return 1
    except TypeError:
        pass

    assertError("DOMAIN ERROR")

# --------------

def     confirmInteger(B):
    """
    the integer-domain value of B (if within comparison tolerance - else throw DOMAIN ERROR)
    """
    try:
        B = fuzzyInteger(B)

        if isinstance(B, int):
            return B
    except TypeError:
        pass

    assertError("DOMAIN ERROR")

# --------------

def     confirmReal(B):
    """
    the real-domain value of B
    """
    try:
        return float(B)
    except TypeError:
        pass

    assertError("DOMAIN ERROR")

# --------------

def     indexOrigin():
    """
    the current index origin (0 or 1)
    """
    return _IO.python()

# --------------

def     eagerEvaluation():
    """
    true is evaluation mode is set to eager
    """
    return _EE.python() == 1

# --------------

def     setEvaluationMode(mode):
    """
    set the eager/lazy evaluation mode (from command line flags)
    """
    return _EE.set(makeScalar(mode))

# ------------------------------

_CT = _systemVariable(makeScalar, confirmReal, 1e-13)
_EE = _systemVariable(makeScalar, confirmBoolean, 0)
_IO = _systemVariable(makeScalar, confirmBoolean, 1)

# a simple dictionary with (k, v) = (name, system-variable)

_SystemVariables = {
    "CT":       _CT,
    "EE":       _EE,
    "IO":       _IO,
}

# ------------------------------

def     systemVariable(name, quantity=None):
    """
    set or get the value of a system variable (from the shell)
    """
    try:
        SV = _SystemVariables[name.upper()]
    except KeyError:
        assertError("UNKNOWN SYSTEM VARIABLE")

    if not quantity is None:
        SV.set(quantity.resolve())

    return SV.get()

# EOF
