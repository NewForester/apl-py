#!/usr/bin/python3
"""
    Unit test for rep.evaluate - doctest style

    WIP - grows as evaluate is extended

    Test recognition of numbers
"""

from apl_exception import APL_Exception as apl_exception

from rep import evaluate

# ------------------------------

def     test_number (expr):
    """
    >>> test_number('0')
    0.0
    >>> test_number('3.142')
    3.142
    >>> test_number('.5')
    0.5
    >>> test_number('1e3')
    1000.0
    >>> test_number('1E3')
    1000.0
    >>> test_number('1e-3')
    0.001
    >>> test_number('1e+3')
    1000.0
    >>> test_number('3.142e-0')
    3.142
    """
    try:
        return evaluate(expr)
    except apl_exception as e:
        print (e.message)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# EOF
