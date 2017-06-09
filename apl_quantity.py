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
        if self.dim is None:
            return APL_scalar_iter(self.value)
        else:
            return self.value.__iter__()

    def __str__(self):
        if self.dim is None:
            return _format_element(self.value)
        elif self.dim == 0:
            return '⍬'
        else:
            return ' '.join(map(_format_element, self.value))

    def python(self):
        return self.value

    def resolve(self):
        if self.dim is None:
            return APL_scalar(self.value)
        else:
            return APL_vector(list(self.value))

    def dimension(self):
        return self.dim

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
        return (self)

# ------------------------------

class APL_vector (APL_quantity):
    """
    trivial class that holds an APL vector quantity
    """
    def __init__(self,value):
        APL_quantity.__init__(self,value,len(value))

    def resolve(self):
        return (self)

# ------------------------------

def eval_monadic(Fn,B):
    """
    evaluate an monadic Python function that does not understand APL quantitites
    """
    if B.dimension() == None:
        return APL_scalar(Fn(B.python()))
    else:
        apl_error("LENGTH ERROR")

# ------------------------------

def monadic2scalar (Fn,B):
    """
    evaluate a monadic function that, if given a scalar argument, returns a scalar
    """
    dim = B.dimension()

    if dim is None:
        return APL_scalar(Fn(B.python()))

    return APL_quantity(map(Fn,B),dim)

# ------------------------------

def monadic2vector (Fn,B):
    """
    evaluate a monadic function that, if given a scalar argument, returns a vector
    """
    dim = B.dimension()

    if dim is None:
        return APL_vector(Fn(B.python()))

    return APL_quantity(map(Fn,B),dim)

# ------------------------------

def dyadic2scalar (Fn,A,B):
    """
    evaluate a dyadic function that, if given scalar arguments, returns a scalar
    """
    aDim = A.dimension()
    bDim = B.dimension()

    if aDim is None:
        if bDim is None:
            return APL_scalar(Fn(A.python(),B.python()))
        dim = bDim
    else:
        if bDim is not None:
            if aDim != bDim:
                apl_error("LENGTH ERROR")
        dim = aDim

    return APL_quantity(map(Fn,A,B),dim)

# ------------------------------

def dyadic2vector (Fn,A,B):
    """
    evaluate a dyadic function that, given scalar arguments, returns a vector
    """
    if A.dimension() != None:
        apl_error("RANK ERROR")
    if B.dimension() != None:
        apl_error("RANK ERROR")

    return APL_vector(Fn(A.python(),B.python()))

# EOF
