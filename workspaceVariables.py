"""
    APL Workspace Variables

    UNDER DEVELOPMENT

    This is an initial version:  there is much still to be done
"""

from apl_quantity import APL_quantity as apl_quantity
from apl_error import apl_error

# ------------------------------

class   _WorkspaceVariable(apl_quantity):
    """
    a simple wrapper for an APL_quantity to ensure values are values, not promises
    """
    def __init__(self, quantity):
        apl_quantity.__init__(self,None)
        self.deepClone(quantity)

    def get(self):
        """
        return the APL quantity
        """
        return self

    def set(self, quantity):
        """
        set the APL quantity - ensure promises are made good
        """
        self.deepClone(quantity)

# ------------------------------

# a simple dictionary with (k, v) = (name, workspace-variable)

_WorkspaceVariables = {}

# ------------------------------

def     workspaceVariable(name, value=None):
    """
    set or get the value of a workspace variable by name lookup

    if a value is passed in, it is assigned to the variable and the value is returned

    a new variable is created if appropriate
    """
    if value is None:
        try:
            apl_var = _WorkspaceVariables[name]
        except KeyError:
            apl_error("UNKNOWN VARIABLE")
    else:
        try:
            apl_var = _WorkspaceVariables[name]

            apl_var.set(value)
        except KeyError:
            apl_var = _WorkspaceVariable(value)

            _WorkspaceVariables[name] = apl_var

    return apl_var.get()

# EOF
