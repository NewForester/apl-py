"""
    APL System Variables

    UNDER DEVELOPMENT

    This is an initial version:  there is much still to be done
"""

from apl_exception import APL_Exception as apl_exception

# ------------------------------

class   apl_system_variable(object):
    """
    a simple pair: (value, confirm function)
    """
    def __init__(self,value,confirm):
        self.value = value
        self.confirm = confirm

# ------------------------------

def     confirm_bool (value):
    value = confirm_int (value)

    if value == 0:  return 0
    if value == 1:  return 1

    raise (apl_exception("DOMAIN ERROR"))

# ------------------------------

def     confirm_int (value):
    integer = int(value)

    if integer == value:    return integer

    raise (apl_exception("DOMAIN ERROR"))

# ------------------------------

system_variables = {
    "IO":       apl_system_variable(1, confirm_bool),
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
        raise (apl_exception("UNKNOWN SYSTEM VARIABLE", name))

    if not value is None:
        sys_var.value = sys_var.confirm(value)

    return sys_var.value

# EOF
