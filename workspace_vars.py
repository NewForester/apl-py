"""
    APL System Variables

    UNDER DEVELOPMENT

    This is an initial version:  there is much still to be done
"""

from apl_error import apl_error

# ------------------------------

class   apl_variable(object):
    """
    a simple value, not even a checker
    """
    def __init__(self,value):
        self.value = value

# ------------------------------

workspace_variables = {}

# ------------------------------

def     workspace_variable (name,value=None):
    """
    return the value of a workspace variable

    if a value is passed in, it is assigned to the variable and the value is returned

    a new variable is created if necessary
    """
    try:
        apl_var = workspace_variables[name]

        if not value is None:
            apl_var.value = value
    except KeyError:
        if value is None:
            apl_error("UNKNOWN VARIABLE")

        apl_var = apl_variable(value)

        workspace_variables[name] = apl_var

    return apl_var.value

# EOF
