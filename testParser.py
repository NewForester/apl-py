#!/usr/bin/python3
"""
    doctest style unit tests for the APL parser

    WIP - grows as evaluate.py is extended

    Each test passes a APL expression to the evaluate function.

    Tests include recognition of:
      - recognition of numbers
      - recognition of names
      - zilde as a result
      - scalar invocation of monadic and dyadic functions
      - parsing of vector quantities
      - parentheses to alter order of execution
      - system variables
      - system commands
"""

from evaluate import evaluate, evaluate_and_print

from apl_cio import APL_cio as apl_cio
from apl_error import APL_exception as apl_exception

# ------------------------------

def     test (expr):
    """
    test both positive and negative outcomes
    """
    try:
        cio = apl_cio()
        cio.printResult(evaluate(expr,cio))
    except apl_exception as error:
        print(error.message)

# ------------------------------

def     test_number (expr):
    """
    >>> test('0')
    0
    >>> test('¯1')
    ¯1
    >>> test('3.142')
    3.142
    >>> test('.5')
    0.5
    >>> test('1e3')
    1000
    >>> test('1E3')
    1000
    >>> test('1e-3')
    0.001
    >>> test('1e+3')
    1000
    >>> test('1e¯3')
    0.001
    >>> test('3.142e-0')
    3.142
    """
    pass

# ------------------------------

def     test_name (expr):
    """
    >>> test('A')
    UNKNOWN VARIABLE
    >>> test('A←2.5')
    2.5
    >>> test('A')
    2.5

    >>> test('Banana←3.5')
    3.5
    >>> test('M27←4.5')
    4.5
    >>> test('27M←5.5')
    INVALID TOKEN

    >>> test('A')
    2.5
    >>> test('A-1')
    1.5
    >>> test('1-A')
    ¯1.5
    >>> test('÷A')
    0.4

    >>> test('name←"Heather"')
    Heather
    """
    pass

# ------------------------------

def     test_zilde (expr):
    """
    zilde - empty numeric vector

    >>> test('⍬')
    ⍬
    >>> test('⍴ ⍬')
    0
    >>> test('⍴ ⍳0')
    0
    >>> test('⍴ 1 ~ 1')
    0
    >>> test('⍴ 1 2 3 ~ 1 2 3')
    0
    >>> test('⍴ ⍴0')
    0
    >>> test('⍴ 0 ⍴ 1 2 3 4 5')
    0
    >>> test('⍴ 0 ↑ 1 2 3 4 5')
    0
    >>> test('⍴ 10 ↓ 1 2 3 4 5')
    0
    >>> test('↓ 1')
    ⍬
    >>> test('↓ ,1')
    ⍬
    >>> test('↓ ⍬')
    ⍬
    >>> test('⍴ ⌽ 1')
    ⍬
    >>> test('⍴ ⊖ 1')
    ⍬
    >>> test('⍴ 6 ⌽ 1')
    ⍬
    >>> test('⍴ 1 ∩ 1')
    1
    >>> test('⍴ 6 ∩ 1')
    0
    >>> test('⍴ 1 ∪ 1')
    1
    >>> test('⍴ ⍉ 1')
    ⍬
    >>> test('⍴ ⍉ ⍬')
    0
    >>> test('⍴ ⍉ ,1')
    1
    >>> test('0 0 0 / 1 2 3')
    ⍬
    >>> test('⍴ 0 / ⍬')
    0
    >>> test('⍴ 0 \ ⍬')
    1
    >>> test('⍬ ≡ ⍳ 0')
    1
    >>> test('⍬ ≡ 0 ⍴ ⍳ 3')
    1
    >>> test('⍬ ⊤ 17')
    ⍬
    >>> test('16 16 ⊤ ⍬')
    RANK ERROR
    >>> test('⍬ ⊥ 1 1')
    0
    >>> test('16 16 ⊥ ⍬')
    0
    """
    pass

# ------------------------------

def     test_scalar (expr):
    """
    >>> test('+2')
    2
    >>> test('-¯2')
    2
    >>> test('×2')
    1
    >>> test('÷2')
    0.5
    >>> test('+-×÷2')
    ¯1

    >>> test('1 + 2')
    3
    >>> test('1 - 2')
    ¯1
    >>> test('1 × 2')
    2
    >>> test('1 ÷ 2')
    0.5
    >>> test('1 + 2 - 3 ÷ 4')
    2.25
    """
    pass

# ------------------------------

def     test_parse_vector (expr):
    """
    >>> test('1 2 3')
    1 2 3
    >>> test('¯1 ¯2 ¯3')
    ¯1 ¯2 ¯3
    >>> test('0.5 (1.5+2.5) 3.5')
    0.5 4 3.5
    >>> test('0.5 (1.5+2.5) 3.5')
    0.5 4 3.5

    >>> test('1 2 3 4')
    1 2 3 4
    >>> test('1 (2 3) 4')
    1 (2 3) 4
    >>> test('(1 2 3) 4')
    (1 2 3) 4
    >>> test('1 (2 3 4)')
    1 (2 3 4)

    >>> test('1 2 + 3 4')
    4 6
    >>> test('(1 2) + 3 4')
    4 6
    >>> test('1 2 + (3 4)')
    4 6
    >>> test('(1 2) + (3 4)')
    4 6
    >>> test('1 (2 + 3) 4')
    1 5 4
    >>> test('1 2 + 3')
    4 5
    >>> test('1 + 2 3')
    3 4

    >>> test('A ← 10')
    10
    >>> test('1 A 3')
    1 10 3
    >>> test('1 (A÷2) 3')
    1 5 3
    >>> test('1 ⎕IO 3')
    1 1 3

    >>> test('A ← 10 20')
    10 20
    >>> test('1 A 3')
    1 (10 20) 3
    """
    pass

# ------------------------------

def     test_parentheses (expr):
    """
    >>> test('(0)')
    0
    >>> test('1 + 2 × 2 + 1')
    7
    >>> test('(1 + 2) × (2 + 1)')
    9
    >>> test('(1 + 2) × 2 + 1')
    9
    >>> test('1 - 2 - 3 - 4')
    ¯2
    >>> test('((1 - 2) - 3) - 4')
    ¯8
    >>> test('1 - (2 - 3) - 4')
    6
    >>> test('1 - (2 - 3 - 4')
    SYNTAX ERROR
    """
    pass

# ------------------------------

def     test_tacks (expr):
    """
    >>> test('⊣ 2')
    0
    >>> test('⊢ 2')
    2

    >>> test('6 ⊣ 2')
    6
    >>> test('6 ⊢ 2')
    2
    """
    pass

# ------------------------------

def     test_output (expr):
    """
    >>> test_output('"Hello" ⍝ end of line comments are ignored')
    Hello

    >>> test_output('"Hello ⍝ in a string is not a comment" ⍝ end of line comments are ignored')
    Hello ⍝ in a string is not a comment

    >>> test_output('"Hello" ⋄ "Paul"')
    Hello
    Paul
    >>> test_output('"Hello ⋄ Paul"')
    Hello ⋄ Paul

    >>> test_output('1 + 2 ⋄ 3 + 4 ⋄ 5 + 6')
    3
    7
    11
    >>> test_output('1 + 2 ⋄ 3 + 4 ⋄')
    3
    7
    >>> test_output('⋄ 3 + 4')
    7

    >>> test_output('⎕ ← 1 + 2')
    3
    >>> test_output('⍞ ← 1 + 2')
    3

    >>> test_output('6 + ⎕ ← 1 + 2')
    3
    9
    >>> test_output('6 + ⍞ ← 1 + 2')
    39

    >>> test_output('⎕ ← "Hello" ⋄ "Paul"')
    Hello
    Paul
    >>> test_output('⍞ ← "Hello " ⋄ "Paul"')
    Hello Paul

    >>> test_output('1 + 2 ⋄ ⎕ ← 3 + 4 ⋄ 5 + 6')
    3
    7
    11
    >>> test_output('1 + 2 ⋄ ⍞ ← 3 + 4 ⋄ 5 + 6')
    3
    711

    >>> test_output('1 2 3')
    1 2 3
    >>> test_output('1 ⎕ ← 2 3')
    2 3
    1 (2 3)
    >>> test_output('"Hello" 2 3')
    'Hello' 2 3
    >>> test_output('"Hello" ⎕ ← 2 3')
    2 3
    'Hello' (2 3)

    >>> test_output('1 ⍞ ← 2 3')
    (2 3)1 (2 3)
    """
    try:
        cio = apl_cio()
        evaluate_and_print(expr,cio)
    except apl_exception as error:
        print(error.message)

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
        cio = apl_cio()
        cio.printResult(evaluate(expr,cio))
    except apl_exception as error:
        print(error.message)

# ------------------------------

def     test_sys_cmds (expr):
    """
    >>> test_sys_cmds(')dummy')
    UNKNOWN SYSTEM COMMAND
    """
    try:
        evaluate(expr,apl_cio())
    except apl_exception as error:
        print(error.message)

# ------------------------------

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# EOF
