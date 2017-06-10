"""
    a Python type that can hold APL scalar and vector quantities

    UNDER DEVELOPMENT
"""

from apl_error import apl_error

# ------------------------------

def _format_element (value):
    """
    format a single element of an APL quantity
    """
    if isinstance(value,APL_quantity):
        string = '({0})'.format(value)
    else:
        string = '{0:.10g}'.format(value)

    if string == '-0':  return '0'

    return string

# ------------------------------

class APL_quantity (object):
    """
    trivial class that holds an APL quantity
    """
    def __init__(self,value,dimension):
        self.value = value
        self.dim = dimension

    def __iter__(self):
        if self.isScalar():
            return APL_scalar_iter(self.value)
        else:
            return self.value.__iter__()

    def __str__(self):
        if self.isScalar():
            return _format_element(self.value)
        else:
            if self.dimension() == 0:
                return '⍬'
            else:
                return ' '.join(map(_format_element, self.value))

    def python(self):
        return self.value

    def resolve(self):
        if self.isScalar():
            return APL_scalar(self.value)
        else:
            return APL_vector(list(self.value))

    def scalarToPy(self,error=None):
        if self.dim is None:
            return self.value
        elif self.dim == 1:
            return self.value[0]

        apl_error(error if error else "RANK ERROR")

    def vectorToPy(self):
        if self.dim is None:
            return [self.value]
        else:
            return self.value

    def dimension(self):
        return self.dim

    def isScalar(self):
        return self.dim is None

    def isVector(self):
        return self.dim is not None

# ------------------------------

class APL_scalar_iter (object):
    """
    trival class that supports mixed scalar/vector arithmetic

    the iterable returns the same value ad infinitum
    """
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value

# ------------------------------

class APL_scalar (APL_quantity):
    """
    trivial class that holds an APL scalar quantity
    """
    def __init__(self,value):
        APL_quantity.__init__(self,value,None)

    def resolve(self):
        return self

# ------------------------------

class APL_vector (APL_quantity):
    """
    trivial class that holds an APL vector quantity
    """
    def __init__(self,value):
        APL_quantity.__init__(self,value,len(value))

    def resolve(self):
        return self

# ------------------------------

def eval_monadic(Fn,B):
    """
    evaluate an monadic Python function that does not understand APL quantitites
    """
    return APL_scalar(Fn(B.scalarToPy("LENGTH ERROR")))

# ------------------------------

def s2s (Fn,B):
    """
    evaluate a numeric monadic function that, given a scalar argument, returns a scalar
    """
    if B.isScalar():
        return APL_scalar(Fn(B.python()))

    return APL_quantity(map(Fn,B),B.dimension())

# ------------------------------

def s2v (Fn,B):
    """
    evaluate a numeric monadic function that, given a scalar argument, returns a vector
    """
    return APL_vector(Fn(B.scalarToPy()))

# ------------------------------

def ss2s (Fn,A,B):
    """
    evaluate a numeric dyadic function that, given scalar arguments, returns a scalar
    """

    dims = tuple(filter(lambda X: X is not None, (A.dimension(), B.dimension())))
    case = len(dims)

    if case == 0:
        return APL_scalar(Fn(A.python(),B.python()))

    if case == 2:
        if dims[0] != dims[1]:
            apl_error("LENGTH ERROR")

    return APL_quantity(map(Fn,A,B),dims[0])

# ------------------------------

def ss2v (Fn,A,B):
    """
    evaluate a numeric dyadic function that, given scalar arguments, returns a vector
    """
    return APL_vector(Fn(A.scalarToPy(),B.scalarToPy()))

# EOF
