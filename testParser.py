#!/usr/bin/python3
"""
    doctest style unit tests for the APL parser

    WIP - grows as evaluate.py is extended

    The tests in this module exercise the functions in evaluate.py:
      - recognition of numbers
      - recognition of strings
      - recognition of names
      - scalar invocation of monadic and dyadic functions
      - parentheses to alter order of execution
      - tack functions (⊢ and ⊣)
      - parsing of vector quantities - including mixed vectors
      - parsing of output operators (⎕ ⍞) - but not input operators
      - system variables
      - system commands

    All but the system commnd tests pass an APL expression to the evaluate function.
    Almost all tests are positive.
"""

from evaluate import evaluate, evaluate_and_print

from aplCio import aplCio
from aplError import aplException

# ------------------------------

def     test(expr):
    """
    test both positive and negative outcomes
    """
    try:
        cio = aplCio()
        cio.printResult(evaluate(expr, cio))
    except aplException as error:
        print(error.message)

# ------------------------------

def     parseNumbers():
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

def     parseStrings(expr):
    """
    >>> test(r"'Hello'")
    Hello
    >>> test("'Hello\\"Jello'")
    Hello"Jello
    >>> test(r"'Hello''Jello'")
    Hello'Jello
    >>> test(r"'H'")
    H
    >>> test(r"''")
    <BLANKLINE>

    >>> test(r'"Hello"')
    Hello
    >>> test('"Hello\\'Jello"')
    Hello'Jello
    >>> test(r'"Hello""Jello"')
    Hello"Jello
    >>> test(r'"H"')
    H
    >>> test(r'""')
    <BLANKLINE>
    """
    try:
        cio = aplCio()
        cio.printResult(evaluate(expr, cio))
    except aplException as error:
        print(error.message)

# ------------------------------

def     parseNames():
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

def     parseScalars():
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

def     parseVectors():
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

    >>> test(r"'Hello' 'Paul'")
    'Hello' 'Paul'
    >>> test(r"1 'Hello' 2")
    1 'Hello' 2
    >>> test(r"'Hello' (19 20) 'Paul'")
    'Hello' (19 20) 'Paul'
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
        cio = aplCio()
        evaluate_and_print(expr, cio)
    except aplException as error:
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

    >>> systemVariable(r"⎕CT")
    1e¯13
    """
    try:
        cio = aplCio()
        cio.printResult(evaluate(expr, cio))
    except aplException as error:
        print(error.message)

# ------------------------------

def     systemCommand(expr):
    """
    >>> systemCommand(")dummy")
    UNKNOWN SYSTEM COMMAND
    """
    try:
        evaluate(expr, aplCio())
    except aplException as error:
        print(error.message)

# ------------------------------

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# EOF
