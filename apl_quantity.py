"""
    a Python type that can hold APL scalar and vector quantities

    UNDER DEVELOPMENT
"""

from apl_exception import APL_Exception as apl_exception

# ------------------------------

class APL_quantity (object):
    """
    trivial class that holds an APL quantity
    """
    def __init__(self,value,dimension):
        self.value = value
        self.dim = dimension

    def __iter__(self):
        return self.value.__iter__()

    def python(self):
        return self.value

    def dimension(self):
        return self.dim

# ------------------------------

class APL_scalar (APL_quantity):
    """
    trivial class that holds an APL scalar quantity
    """
    def __init__(self,value):
        APL_quantity.__init__(self,value,None)

# ------------------------------

class APL_vector (APL_quantity):
    """
    trivial class that holds an APL vector quantity
    """
    def __init__(self,value):
        APL_quantity.__init__(self,value,len(value))

# EOF
