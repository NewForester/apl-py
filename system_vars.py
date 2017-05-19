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

class   apl_system_variable(object):
    """
    a simple pair: (value, confirm function)
    """
    def __init__(self,value,confirm):
        self.value = value
        self.confirm = confirm

# ------------------------------

def     equalCT (A,B):
    return operator.le(math.fabs(A-B),comparisonTolerance.value.python() * max(math.fabs(A), math.fabs(B)))

# ------------------------------

def     integerCT (B):
    if not type(B) is int:
        integer = int(B+0.5)

        if equalCT(integer,B):
            return integer

    return B

# ------------------------------

def     confirm_bool (B):
    B = integerCT(B)

    if B == 0:  return 0
    if B == 1:  return 1

    apl_error("DOMAIN ERROR")

# ------------------------------

def     confirm_int (B):
    B = integerCT(B)

    if not type(B) is int:
        apl_error("DOMAIN ERROR")

    return B

# ------------------------------

def     confirm_real (B):
    return float(B)

# ------------------------------

indexOrigin =           apl_system_variable(apl_scalar(1),      lambda B: eval_monadic(confirm_bool,B))
comparisonTolerance =   apl_system_variable(apl_scalar(1e-13),  lambda B: eval_monadic(confirm_real,B))

system_variables = {
    "IO":       indexOrigin,
    "CT":       comparisonTolerance,
}

# ------------------------------

def     system_variable (name,value=None):
    """
    return the value of a system variable

    if a value is passed in, it is assigned to the system variable and the value is returned

    throws UNKNOWN SYSTEM VARIABLE if the name is not recognised
    """
    try:
        sys_var = system_variables[name.upper()]
    except KeyError:
        apl_error("UNKNOWN SYSTEM VARIABLE", name)

    if not value is None:
        sys_var.value = sys_var.confirm(value)

    return sys_var.value

# EOF
