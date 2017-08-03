#!/usr/bin/python3
"""
    doctest style unit tests for the APL parser

    WIP - grows as evaluate.py is extended

    Each test passes a APL expression to the evaluate function.

    Tests include recognition of:
      - recognition of numbers
      - recognition of names
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

def     test(expr):
    """
    test both positive and negative outcomes
    """
    try:
        cio = apl_cio()
        cio.printResult(evaluate(expr,cio))
    except apl_exception as error:
        print(error.message)

# ------------------------------

def     parseNumber():
    """
    >>> test(r"0")
    0
    >>> test(r"¯1")
    ¯1
    >>> test(r"3.142")
    3.142
    >>> test(r".5")
    0.5
    >>> test(r"1e3")
    1000
    >>> test(r"1E3")
    1000
    >>> test(r"1e-3")
    0.001
    >>> test(r"1e+3")
    1000
    >>> test(r"1e¯3")
    0.001
    >>> test(r"3.142e-0")
    3.142
    """
    pass

# ------------------------------

def     parseName():
    """
    >>> test(r"A")
    UNKNOWN VARIABLE
    >>> test(r"A←2.5")
    2.5
    >>> test(r"A")
    2.5

    >>> test(r"Banana←3.5")
    3.5
    >>> test(r"M27←4.5")
    4.5
    >>> test(r"27M←5.5")
    INVALID TOKEN

    >>> test(r"A")
    2.5
    >>> test(r"A-1")
    1.5
    >>> test(r"1-A")
    ¯1.5
    >>> test(r"÷A")
    0.4

    >>> test(r"name←'Heather'")
    Heather
    """
    pass

# ------------------------------

def     parseScalar():
    """
    >>> test(r"+2")
    2
    >>> test(r"-¯2")
    2
    >>> test(r"×2")
    1
    >>> test(r"÷2")
    0.5
    >>> test(r"+-×÷2")
    ¯1

    >>> test(r"1 + 2")
    3
    >>> test(r"1 - 2")
    ¯1
    >>> test(r"1 × 2")
    2
    >>> test(r"1 ÷ 2")
    0.5
    >>> test(r"1 + 2 - 3 ÷ 4")
    2.25
    """
    pass

# ------------------------------

def     parseVector():
    """
    >>> test(r"1 2 3")
    1 2 3
    >>> test(r"¯1 ¯2 ¯3")
    ¯1 ¯2 ¯3
    >>> test(r"0.5 (1.5+2.5) 3.5")
    0.5 4 3.5
    >>> test(r"0.5 (1.5+2.5) 3.5")
    0.5 4 3.5

    >>> test(r"1 2 3 4")
    1 2 3 4
    >>> test(r"1 (2 3) 4")
    1 (2 3) 4
    >>> test(r"(1 2 3) 4")
    (1 2 3) 4
    >>> test(r"1 (2 3 4)")
    1 (2 3 4)

    >>> test(r"1 2 + 3 4")
    4 6
    >>> test(r"(1 2) + 3 4")
    4 6
    >>> test(r"1 2 + (3 4)")
    4 6
    >>> test(r"(1 2) + (3 4)")
    4 6
    >>> test(r"1 (2 + 3) 4")
    1 5 4
    >>> test(r"1 2 + 3")
    4 5
    >>> test(r"1 + 2 3")
    3 4

    >>> test(r"A ← 10")
    10
    >>> test(r"1 A 3")
    1 10 3
    >>> test(r"1 (A÷2) 3")
    1 5 3
    >>> test(r"1 ⎕IO 3")
    1 1 3

    >>> test(r"A ← 10 20")
    10 20
    >>> test(r"1 A 3")
    1 (10 20) 3
    """
    pass

# ------------------------------

def     parseParentheses():
    """
    >>> test(r"(0)")
    0
    >>> test(r"1 + 2 × 2 + 1")
    7
    >>> test(r"(1 + 2) × (2 + 1)")
    9
    >>> test(r"(1 + 2) × 2 + 1")
    9
    >>> test(r"1 - 2 - 3 - 4")
    ¯2
    >>> test(r"((1 - 2) - 3) - 4")
    ¯8
    >>> test(r"1 - (2 - 3) - 4")
    6
    >>> test(r"1 - (2 - 3 - 4")
    SYNTAX ERROR
    """
    pass

# ------------------------------

def     parseTacks():
    """
    >>> test(r"⊣ 2")
    0
    >>> test(r"⊢ 2")
    2

    >>> test(r"6 ⊣ 2")
    6
    >>> test(r"6 ⊢ 2")
    2
    """
    pass

# ------------------------------

def     parseOutput(expr):
    """
    >>> parseOutput(r"'Hello' ⍝ end of line comments are ignored")
    Hello

    >>> parseOutput(r"'Hello ⍝ in a string is not a comment' ⍝ end of line comments are ignored")
    Hello ⍝ in a string is not a comment

    >>> parseOutput(r"'Hello' ⋄ 'Paul'")
    Hello
    Paul
    >>> parseOutput(r"'Hello ⋄ Paul'")
    Hello ⋄ Paul

    >>> parseOutput(r"1 + 2 ⋄ 3 + 4 ⋄ 5 + 6")
    3
    7
    11
    >>> parseOutput(r"1 + 2 ⋄ 3 + 4 ⋄")
    3
    7
    >>> parseOutput(r"⋄ 3 + 4")
    7

    >>> parseOutput(r"⎕ ← 1 + 2")
    3
    >>> parseOutput(r"⍞ ← 1 + 2")
    3

    >>> parseOutput(r"6 + ⎕ ← 1 + 2")
    3
    9
    >>> parseOutput(r"6 + ⍞ ← 1 + 2")
    39

    >>> parseOutput(r"⎕ ← 'Hello' ⋄ 'Paul'")
    Hello
    Paul
    >>> parseOutput(r"⍞ ← 'Hello ' ⋄ 'Paul'")
    Hello Paul

    >>> parseOutput(r"1 + 2 ⋄ ⎕ ← 3 + 4 ⋄ 5 + 6")
    3
    7
    11
    >>> parseOutput(r"1 + 2 ⋄ ⍞ ← 3 + 4 ⋄ 5 + 6")
    3
    711

    >>> parseOutput(r"1 2 3")
    1 2 3
    >>> parseOutput(r"1 ⎕ ← 2 3")
    2 3
    1 (2 3)
    >>> parseOutput(r"'Hello' 2 3")
    'Hello' 2 3
    >>> parseOutput(r"'Hello' ⎕ ← 2 3")
    2 3
    'Hello' (2 3)

    >>> parseOutput(r"1 ⍞ ← 2 3")
    (2 3)1 (2 3)
    """
    try:
        cio = apl_cio()
        evaluate_and_print(expr,cio)
    except apl_exception as error:
        print(error.message)

# ------------------------------

def     systemVariable(expr):
    """
    >>> systemVariable(r"⎕dummy")
    UNKNOWN SYSTEM VARIABLE

    >>> systemVariable(r"⎕IO")
    1
    >>> systemVariable(r"⎕Io←0")
    0
    >>> systemVariable(r"⎕io")
    0
    >>> systemVariable(r"⎕iO←0")
    0
    >>> systemVariable(r"⎕IO←2")
    DOMAIN ERROR
    >>> systemVariable(r"⎕io")
    0
    >>> systemVariable(r"⎕IO←1")
    1
    >>> systemVariable(r"⎕io")
    1
    """
    try:
        cio = apl_cio()
        cio.printResult(evaluate(expr,cio))
    except apl_exception as error:
        print(error.message)

# ------------------------------

def     systemCommand(expr):
    """
    >>> systemCommand(")dummy")
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
