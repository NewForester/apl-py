"""
    APL Workspace Variables

    UNDER DEVELOPMENT

    This is an initial version:  there is much still to be done
"""

from aplQuantity import aplQuantity
from aplError import assertError

# ------------------------------

class   _workspaceVariable(aplQuantity):
    """
    a simple wrapper for an aplQuantity to ensure values are values, not promises
    """
    def __init__(self, quantity):
        aplQuantity.__init__(self, [])
        self.set(quantity)

    def get(self):
        """
        return the APL quantity
        """
        return self

    def set(self, quantity):
        """
        set the APL quantity
        """
        self._clone(quantity)

# ------------------------------

# a simple dictionary with (k, v) = (name, workspace-variable)

_WorkspaceVariables = {}

# ------------------------------

def     workspaceVariable(name, quantity=None):
    """
    set or get the value of a workspace variable by name lookup

    if a value is passed in, it is assigned to the variable and the value is returned

    a new variable is created if appropriate
    """
    if quantity is None:
        try:
            WV = _WorkspaceVariables[name]
        except KeyError:
            assertError("UNKNOWN VARIABLE")
    else:
        quantity = quantity.resolve()
        try:
            WV = _WorkspaceVariables[name]

            WV.set(quantity)
        except KeyError:
            WV = _workspaceVariable(quantity)

            _WorkspaceVariables[name] = WV

    return WV.get()

# EOF
