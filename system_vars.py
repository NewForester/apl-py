"""
    APL System Variables

    UNDER DEVELOPMENT

    This is an initial version:  there is much still to be done

    APL scalar/vector aware
"""

import  math
import  operator

from apl_quantity import eval_monadic, APL_scalar as apl_scalar
from apl_error import apl_error

# ------------------------------

class   APL_system_variable(object):
    """
    an APL system variable is represented by a pair; the is no behaviour
        - a value (represented by an instance of APL_quantity)
        - a confirm function (used during assignment to confirm the quantity falls in the approrpriate domain)
    """
    def __init__(self,value,confirm):
        self.value = value
        self.confirm = confirm

# ------------------------------

_indexOrigin =           APL_system_variable(apl_scalar(1),      lambda B: eval_monadic(confirm_bool,B))
_comparisonTolerance =   APL_system_variable(apl_scalar(1e-13),  lambda B: eval_monadic(confirm_real,B))

_system_variables = {
    "IO":       _indexOrigin,
    "CT":       _comparisonTolerance,
}

# ------------------------------

def     system_variable (name,value=None):
    """
    set or get the value of a system variable (from the shell)

    throws UNKNOWN SYSTEM VARIABLE if the name is not recognised
    """
    try:
        sys_var = _system_variables[name.upper()]
    except KeyError:
        apl_error("UNKNOWN SYSTEM VARIABLE", name)

    if not value is None:
        sys_var.value = sys_var.confirm(value)

    return sys_var.value

# ------------------------------

def     indexOrigin ():
    """
    the current index origin (0 or 1)
    """
    return _indexOrigin.value.python()

# --------------

def     equalCT (A,B):
    """
    true if A = B within the current comparison tolerance
    """
    return operator.le(math.fabs(A-B),_comparisonTolerance.value.python() * max(math.fabs(A), math.fabs(B)))

# --------------

def     integerCT (B):
    """
    returns B but if B is withhin comparison toleranace of an integer, returns the integer
    """
    if not type(B) is int:
        if B > 0:
            integer = int(B+0.5)
        elif B < 0:
            integer = int(B-0.5)
        else:
            integer = 0

        if equalCT(integer,B):
            return integer

    return B

# --------------

def     confirm_bool (B):
    """
    return the Boolean-domain value of B (within comparison tolerance) - else throw DOMAIN ERROR
    """
    B = integerCT(B)

    if B == 0:  return 0
    if B == 1:  return 1

    apl_error("DOMAIN ERROR")

# --------------

def     confirm_int (B):
    """
    return the integer-domain value of B (within comparison tolerance) - else throw DOMAIN ERROR
    """
    B = integerCT(B)

    if not type(B) is int:
        apl_error("DOMAIN ERROR")

    return B

# --------------

def     confirm_real (B):
    """
    return the real-domain value of B
    """
    return float(B)

# EOF
