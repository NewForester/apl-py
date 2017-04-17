#!/usr/bin/python3
"""
    Unit test for rep.evaluate - doctest style

    WIP - grows as evaluate is extended

    Test recognition of:
      - numbers
      - invocation of monadic and dyadic functions
      - parentheses to alter order of execution
      - strings in apostrophes or quotes
"""

from apl_exception import APL_Exception as apl_exception

from rep import evaluate

# ------------------------------

def     test_number (expr):
    """
    >>> test_number('0')
    0.0
    >>> test_number('¯1')
    -1.0
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
    >>> test_number('1e¯3')
    0.001
    >>> test_number('3.142e-0')
    3.142
    """
    try:
        return evaluate(expr)
    except apl_exception as e:
        print (e.message)

def     test_scalar (expr):
    """
    >>> test_scalar('+2')
    2.0
    >>> test_scalar('-¯2')
    2.0
    >>> test_scalar('×2')
    1
    >>> test_scalar('÷2')
    0.5
    >>> test_scalar('+-×÷2')
    -1

    >>> test_scalar('1 + 2')
    3.0
    >>> test_scalar('1 - 2')
    -1.0
    >>> test_scalar('1 × 2')
    2.0
    >>> test_scalar('1 ÷ 2')
    0.5
    >>> test_scalar('1 + 2 - 3 ÷ 4')
    2.25
    """
    try:
        return evaluate(expr)
    except apl_exception as e:
        print (e.message)

def     test_parentheses (expr):
    """
    >>> test_parentheses('(0)')
    0.0
    >>> test_parentheses('1 + 2 × 2 + 1')
    7.0
    >>> test_parentheses('(1 + 2) × (2 + 1)')
    9.0
    >>> test_parentheses('(1 + 2) × 2 + 1')
    9.0
    >>> test_parentheses('1 - 2 - 3 - 4')
    -2.0
    >>> test_parentheses('((1 - 2) - 3) - 4')
    -8.0
    >>> test_parentheses('1 - (2 - 3) - 4')
    6.0
    >>> test_parentheses('1 - (2 - 3 - 4')
    SYNTAX ERROR
    """
    try:
        return evaluate(expr)
    except apl_exception as e:
        print (e.message)

# ------------------------------

def     test_string (expr):
    """
    Implementation of string handling incomplete - parser test only

    >>> test_number("'Hello'")
    'Hello'
    0
    >>> test_number("'Hello\\"Jello'")
    'Hello"Jello'
    0
    >>> test_number("'Hello''Jello'")
    'Hello'Jello'
    0

    >>> test_number('"Hello"')
    "Hello"
    1
    >>> test_number('"Hello\\'Jello"')
    "Hello'Jello"
    1
    >>> test_number('"Hello""Jello"')
    "Hello"Jello"
    1
    """
    try:
        return evaluate(expr)
    except apl_exception as e:
        print (e.message)

# ------------------------------

def     test_name (expr):
    """
    Implementation of name handling incomplete - parser test only

    >>> test_number("Hello")
    Hello
    2
    >>> test_number("Hello_Paul")
    Hello_Paul
    2
    >>> test_number("arithmetic")
    arithmetic
    2

    >>> test_number('5+A')
    A
    7.0
    >>> test_number('a+6')
    a
    8.0
    >>> test_number('-banana')
    banana
    -2
    >>> test_number('ba2a2a2')
    ba2a2a2
    2

    >>> test_number('⎕three+1')
    three
    4.0

    >>> test_number(')FOUR+2')
    FOUR
    6.0
    """
    try:
        return evaluate(expr)
    except apl_exception as e:
        print (e.message)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# EOF
