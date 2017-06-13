#!/usr/bin/python3
"""
    Unit test for evaluate.py - doctest style

    WIP - grows as evaluate is extended

    Test recognition of:
      - numbers
      - invocation of monadic and dyadic functions
      - parentheses to alter order of execution
      - strings in apostrophes or quotes
"""

from evaluate import evaluate

from apl import print_result

from apl_error import APL_exception as apl_exception

# ------------------------------

def     test_number (expr):
    """
    >>> test_number('0')
    0
    >>> test_number('¯1')
    ¯1
    >>> test_number('3.142')
    3.142
    >>> test_number('.5')
    0.5
    >>> test_number('1e3')
    1000
    >>> test_number('1E3')
    1000
    >>> test_number('1e-3')
    0.001
    >>> test_number('1e+3')
    1000
    >>> test_number('1e¯3')
    0.001
    >>> test_number('3.142e-0')
    3.142
    """
    try:
        print_result(evaluate(expr))
    except apl_exception as error:
        print (error.message)

# ------------------------------

def     test_zilde (expr):
    """
    zilde - empty numeric vector - same as 0⍴0

    >>> test_zilde('⍬')
    Quantity has dimension 0
    ⍬
    >>> test_zilde('⍳0')
    Quantity has dimension 0
    ⍬
    """
    try:
        quantity = evaluate(expr)

        print("Quantity has dimension {0}".format(quantity.dimension()))

        print_result(quantity)
    except apl_exception as error:
        print (error.message)

# ------------------------------

def     test_scalar (expr):
    """
    >>> test_scalar('+2')
    2
    >>> test_scalar('-¯2')
    2
    >>> test_scalar('×2')
    1
    >>> test_scalar('÷2')
    0.5
    >>> test_scalar('+-×÷2')
    ¯1

    >>> test_scalar('1 + 2')
    3
    >>> test_scalar('1 - 2')
    ¯1
    >>> test_scalar('1 × 2')
    2
    >>> test_scalar('1 ÷ 2')
    0.5
    >>> test_scalar('1 + 2 - 3 ÷ 4')
    2.25
    """
    try:
        print_result(evaluate(expr))
    except apl_exception as error:
        print (error.message)

# ------------------------------

def     test_parentheses (expr):
    """
    >>> test_parentheses('(0)')
    0
    >>> test_parentheses('1 + 2 × 2 + 1')
    7
    >>> test_parentheses('(1 + 2) × (2 + 1)')
    9
    >>> test_parentheses('(1 + 2) × 2 + 1')
    9
    >>> test_parentheses('1 - 2 - 3 - 4')
    ¯2
    >>> test_parentheses('((1 - 2) - 3) - 4')
    ¯8
    >>> test_parentheses('1 - (2 - 3) - 4')
    6
    >>> test_parentheses('1 - (2 - 3 - 4')
    SYNTAX ERROR
    """
    try:
        print_result(evaluate(expr))
    except apl_exception as error:
        print (error.message)

# ------------------------------

def     test_string (expr):
    """
    Implementation of string handling incomplete - parser test only

    >>> test_string("'Hello'")
    Hello
    >>> test_string("'Hello\\"Jello'")
    Hello"Jello
    >>> test_string("'Hello''Jello'")
    Hello'Jello
    >>> test_string("'H'")
    H
    >>> test_string("''")
    <BLANKLINE>

    >>> test_string('"Hello"')
    Hello
    >>> test_string('"Hello\\'Jello"')
    Hello'Jello
    >>> test_string('"Hello""Jello"')
    Hello"Jello
    >>> test_string('"H"')
    H
    >>> test_string('""')
    <BLANKLINE>

    >>> test_string("'Hello'")
    Hello
    >>> test_string("'Hello' 'Paul'")
    'Hello' 'Paul'
    >>> test_string("1 'Hello' 2")
    1 'Hello' 2
    >>> test_string("'Hello' (19 20) 'Paul'")
    'Hello' (19 20) 'Paul'
    """
    try:
        print_result(evaluate(expr))
    except apl_exception as error:
        print (error.message)

# ------------------------------

def     test_sys_vars (expr):
    """
    >>> test_sys_vars('⎕dummy')
    UNKNOWN SYSTEM VARIABLE

    >>> test_sys_vars('⎕IO')
    1
    >>> test_sys_vars('⎕Io←0')
    0
    >>> test_sys_vars('⎕io')
    0
    >>> test_sys_vars('⎕iO←0')
    0
    >>> test_sys_vars('⎕IO←2')
    DOMAIN ERROR
    >>> test_sys_vars('⎕io')
    0
    >>> test_sys_vars('⎕IO←1')
    1
    >>> test_sys_vars('⎕io')
    1
    """
    try:
        print_result(evaluate(expr))
    except apl_exception as error:
        print (error.message)

# ------------------------------

def     test_sys_cmds (expr):
    """
    >>> test_sys_cmds(')dummy')
    UNKNOWN SYSTEM COMMAND
    """
    try:
        return evaluate(expr)
    except apl_exception as error:
        print (error.message)

# ------------------------------

def     test_name (expr):
    """
    >>> test_name('A')
    UNKNOWN VARIABLE
    >>> test_name('A←2.5')
    2.5
    >>> test_name('A')
    2.5

    >>> test_name('Banana←3.5')
    3.5
    >>> test_name('M27←4.5')
    4.5
    >>> test_name('27M←5.5')
    INVALID TOKEN

    >>> test_name('A')
    2.5
    >>> test_name('A-1')
    1.5
    >>> test_name('1-A')
    ¯1.5
    >>> test_name('÷A')
    0.4
    """
    try:
        print_result(evaluate(expr))
    except apl_exception as error:
        print (error.message)

# ------------------------------

def     test_parse_vector (expr):
    """
    >>> test_parse_vector('1 2 3')
    1 2 3
    >>> test_parse_vector('¯1 ¯2 ¯3')
    ¯1 ¯2 ¯3
    >>> test_parse_vector('0.5 (1.5+2.5) 3.5')
    0.5 4 3.5
    >>> test_parse_vector('0.5 (1.5+2.5) 3.5')
    0.5 4 3.5

    >>> test_parse_vector('1 2 3 4')
    1 2 3 4
    >>> test_parse_vector('1 (2 3) 4')
    1 (2 3) 4
    >>> test_parse_vector('(1 2 3) 4')
    (1 2 3) 4
    >>> test_parse_vector('1 (2 3 4)')
    1 (2 3 4)

    >>> test_parse_vector('1 2 + 3 4')
    4 6
    >>> test_parse_vector('(1 2) + 3 4')
    4 6
    >>> test_parse_vector('1 2 + (3 4)')
    4 6
    >>> test_parse_vector('(1 2) + (3 4)')
    4 6
    >>> test_parse_vector('1 (2 + 3) 4')
    1 5 4
    >>> test_parse_vector('1 2 + 3')
    4 5
    >>> test_parse_vector('1 + 2 3')
    3 4

    >>> test_parse_vector('A ← 10')
    10
    >>> test_parse_vector('1 A 3')
    1 10 3
    >>> test_parse_vector('1 (A÷2) 3')
    1 5 3
    >>> test_parse_vector('1 ⎕IO 3')
    1 1 3

    >>> test_parse_vector('A ← 10 20')
    10 20
    >>> test_parse_vector('1 A 3')
    1 (10 20) 3
    """
    try:
        print_result(evaluate(expr))
    except apl_exception as error:
        print (error.message)

# ------------------------------

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# EOF
