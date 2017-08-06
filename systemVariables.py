"""
    APL System Variables

    UNDER DEVELOPMENT

    This initial version implements only ⎕CT and ⎕IO.
"""

import  math
import  operator

from apl_quantity import APL_quantity as apl_quantity, make_scalar
from apl_error import apl_error

# ------------------------------

class   _SystemVariable(apl_quantity):
    """
    an APL system variable is represented by a triplet;
        - a make function (used to make an APL quantity from a Python value)
        - a confirm function (used to validate the Python value)
        - an APL quantity
    """
    def __init__(self, makeFunction, confirmFunction, value):
        apl_quantity.__init__(self,None)
        self._make = makeFunction
        self._confirm = confirmFunction
        self.deepClone(self._make(value))

    def get(self):
        """
        return the APL quantity
        """
        return self

    def set(self, quantity):
        """
        validate and set the APL quantity
        """
        self.deepClone(self._make(self._confirm(quantity.python())))

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
    B = fuzzyInteger(B)

    if B == 0:
        return 0
    if B == 1:
        return 1

    apl_error("DOMAIN ERROR")

# --------------

def     confirmInteger(B):
    """
    the integer-domain value of B (if within comparison tolerance - else throw DOMAIN ERROR)
    """
    B = fuzzyInteger(B)

    if isinstance(B, int):
        return B

    apl_error("DOMAIN ERROR")

# --------------

def     confirmReal(B):
    """
    the real-domain value of B
    """
    return float(B)

# --------------

def     indexOrigin():
    """
    the current index origin (0 or 1)
    """
    return _IO.python()

# ------------------------------

_CT = _SystemVariable(make_scalar, confirmReal, 1e-13)
_IO = _SystemVariable(make_scalar, confirmBoolean, 1)

# a simple dictionary with (k, v) = (name, system-variable)

_SystemVariables = {
    "CT":       _CT,
    "IO":       _IO,
}

# ------------------------------

def     systemVariable(name, value=None):
    """
    set or get the value of a system variable (from the shell)
    """
    try:
        SV = _SystemVariables[name.upper()]
    except KeyError:
        apl_error("UNKNOWN SYSTEM VARIABLE", name)

    if not value is None:
        SV.set(value)

    return SV.get()

# EOF
