"""
    a Python type that can hold APL scalar and vector quantities, both numeric and string

    UNDER DEVELOPMENT

    Routines to handle vector quantities are work-in-progress.  They will
    eventually all use lazy evaluation techniques.

    This version drops the derived classes APL_scalar etc and replaces them
    with the routines make_scalar() etc.  They are not used by this module.
    The intention is that these are external routines used by evaluate.py.
"""

from apl_error import apl_error

# ------------------------------

def _format_element (value):
    """
    format a single element of an APL quantity
    """
    if isinstance(value,APL_quantity):
        if value.isString():
            return "'{0}'".format(value)
        else:
            return "({0})".format(value)
    else:
        if type(value) == str:
            return "'{0}'".format(value)
        else:
            string = "{0:.10g}".format(value)

            if string == "-0":  return "0"

            return string.replace('-','¯')

# ------------------------------

class APL_quantity (object):
    """
    trivial class that holds an APL quantity
    """
    def __init__(self,value,dimension,string=False):
        self.value = value
        self.dim = dimension
        self.string = string

    def __iter__(self):
        if self.isScalar():
            return APL_scalar_iter(self.value)
        else:
            return self.value.__iter__()

    def __str__(self):
        if self.isString():
            return ''.join(self.value)

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
        if self.isString() or self.isScalar():
            return self
        else:
            return APL_quantity(list(self.value),self.dim,self.string)

    def noStringConfirm(self):
        if self.isString():
            apl_error("DOMAIN ERROR")

    def noString(self):
        if self.isString():
            if self.isScalar():
                return APL_quantity(ord(self.value),None)
            else:
                return APL_quantity(map(ord,self.value),self.dim)

        return self

    def scalarToPy(self,error=None):
        if self.dim is None:
            return self.value
        elif self.dim == 1:
            return self.value[0]

        apl_error(error if error else "RANK ERROR")

    def vectorToPy(self):
        if self.dim is None and not self.string:
            return [self.value]
        else:
            return self.value

    def dimension(self):
        return self.dim

    def isString(self):
        return self.string

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

def     make_scalar(value):
    """
    make an APL scalar quantity from a numeric Python value
    """
    return APL_quantity(value,None)

# ------------------------------

def     make_vector(value,string=False):
    """
    make an APL vector quantity from a numeric Python list
    """
    return APL_quantity(value,len(value),string)

# ------------------------------

def     make_string(value):
    """
    make an APL string quantity from a Python str
    """
    delim = value[0]
    value = value.replace(delim*2,delim)[1:-1]
    length = len(value)

    if length == 1 and delim == "'":
        return APL_quantity(value,None,True)
    else:
        return APL_quantity(value,length,True)

# ------------------------------

def eval_monadic(Fn,B):
    """
    evaluate an monadic Python function that does not understand APL quantitites
    """
    return make_scalar(Fn(B.scalarToPy("LENGTH ERROR")))

# ------------------------------

def s2s (Fn,B):
    """
    evaluate a numeric monadic function that, given a scalar argument, returns a scalar
    """
    B.noStringConfirm()

    if B.isScalar():
        return APL_quantity(Fn(B.python()),None)
    else:
        return APL_quantity(map(Fn,B),B.dimension())

# ------------------------------

def s2v (Fn,B):
    """
    evaluate a numeric monadic function that, given a scalar argument, returns a vector
    """
    B.noStringConfirm()

    Bpy = B.scalarToPy()

    return APL_quantity(Fn(Bpy),Bpy)

# ------------------------------

def v2s (Fn,B):
    """
    evaluate a numeric function that, given a vector argument, returns a scalar
    """
    return APL_quantity(Fn(B.vectorToPy()),None)

# ------------------------------

def v2v (Fn,B):
    """
    evaluate a function that, given a vector argument, returns a vector
    """
    Rpy = Fn(B.vectorToPy())

    if B.isScalar():
        return APL_quantity(Rpy[0],B.dimension(),B.isString())
    else:
        return APL_quantity(Rpy,B.dimension(),B.isString())

# ------------------------------

def s_rho (Fn,B):
    """
    scalar rho - return dimension/rank of B - does not operate on B
    """
    if B.isScalar():    return APL_quantity([],0)

    if B.isVector():    return APL_quantity([B.dimension()],1)

    apl_error("RANK ERROR")

# ------------------------------

def s_comma (Fn,B):
    """
    scalar comma - unravel B and return a vector
    """

    if B.isScalar():    return APL_quantity(B.vectorToPy(),1,B.isString())

    if B.isVector():    return B

    apl_error("RANK ERROR")

# ------------------------------

def ss2s (Fn,A,B,numbersOnly):
    """
    evaluate a dyadic function that, given scalar arguments, returns a scalar
    """
    if (numbersOnly):
        A.noStringConfirm()
        B.noStringConfirm()
    else:
        A = A.noString()
        B = B.noString()

    dims = tuple(filter(lambda X: X is not None, (A.dimension(), B.dimension())))
    case = len(dims)

    if case == 0:
        return APL_quantity(Fn(A.python(),B.python()),None)

    if case == 2:
        if dims[0] != dims[1]:
            apl_error("LENGTH ERROR")

    return APL_quantity(map(Fn,A,B),dims[0])

# ------------------------------

def ss2v (Fn,A,B):
    """
    evaluate a numeric dyadic function that, given scalar arguments, returns a vector
    """
    return APL_quantity(Fn(A.scalarToPy(),B.scalarToPy()),A)

# ------------------------------

def vv2v (Fn,A,B):
    """
    evaluate a dyadic function that returns a vector
    """
    case = A.isString() + B.isString()

    if case == 1:   return A

    Rpy = Fn(A.vectorToPy(),B.vectorToPy())

    return APL_quantity(Rpy,len(Rpy),case == 2)

# ------------------------------

def vv2s (Fn,A,B):
    """
    evaluate a dyadic function that returns a vector if B is a vector but a scalar if B is scalar
    """
    Rpy = Fn(A.vectorToPy(),B.vectorToPy())

    if B.isScalar():
        return APL_quantity(Rpy[0],None)
    else:
        return APL_quantity(Rpy,B.dimension())

# ------------------------------

def sv_rho (Fn,A,B):
    """
    evaluate a dyadic function that may take a scalar/vector and a vector and return a vector

    well, this is for ⍴ and probably will not work for anything else
    """
    A.noStringConfirm()

    Rpy = Fn(A.scalarToPy(),B.vectorToPy())

    return APL_quantity(Rpy,A.scalarToPy(),B.isString())

# ------------------------------

def vv_comma (Fn,A,B):
    """
    evaluate a dyadic function that returns a vector
    """
    case = A.isString() + B.isString()

    Apy = [A] if A.isString() and case == 1 else A.vectorToPy()
    Bpy = [B] if B.isString() and case == 1 else B.vectorToPy()

    Rpy = Fn(Apy,Bpy)

    return APL_quantity(Rpy,len(Rpy),case == 2)

# ------------------------------

def sv2vr (Fn,A,B):
    """
    evaluate a dyadic function that returns a vector if B is a vector but a scalar if B is scalar
    """
    A.noStringConfirm()

    Rpy = Fn(A.scalarToPy("RANK ERROR"),B.vectorToPy())

    if B.isScalar():
        return APL_quantity(Rpy[0],None,B.isString())
    else:
        return APL_quantity(Rpy,B.dimension(),B.isString())

# ------------------------------

def sv2vl (Fn,A,B):
    """
    evaluate a dyadic function that returns a vector if B is a vector but a scalar if B is scalar
    """
    A.noStringConfirm()

    Rpy = Fn(A.scalarToPy("LENGTH ERROR"),B.vectorToPy())

    if B.isScalar():
        return APL_quantity(Rpy[0],B.dimension(),B.isString())
    else:
        return APL_quantity(Rpy,len(Rpy),B.isString())

# EOF
