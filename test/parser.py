#!/usr/bin/python3
"""
    doctest style unit tests for the APL parser

    WIP - grows as evaluate.py is extended.

    The tests in this module exercise the functions in evaluate.py:
      - recognition of numbers
      - recognition of strings
      - recognition of names
      - tack functions (⊢ and ⊣)
      - scalar invocation of monadic and dyadic functions
      - parentheses to alter order of execution
      - parsing of vector quantities - including mixed/nested vectors
      - printing of array quantities
      - array prototypes
      - parsing of output operators (⎕ ⍞) - but not input operators
      - system variables
      - system commands

    All but the system commnd tests pass an APL expression to the evaluate function.
    Almost all tests are positive.

    Note:
        testDyadic --eager      # run with eager evaluation
        testDyadic --lazy       # run with lazy evaluation
"""

from test.base import preamble, testOutput, testCommand, testResult as test
from test.base import saveIndexOrigin, setIndexOrigin, restoreIndexOrigin

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

def     parseStrings():
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
    ''

    >>> test(r'"Hello"')
    Hello
    >>> test('"Hello\\'Jello"')
    Hello'Jello
    >>> test(r'"Hello""Jello"')
    Hello"Jello
    >>> test(r'"H"')
    H
    >>> test(r'""')
    ''
    """
    pass

# ------------------------------

def     parseNames():
    """
    >>> test(r"B")
    UNKNOWN VARIABLE
    >>> test(r"B←2.5")
    2.5
    >>> test(r"B")
    2.5

    >>> test(r"Banana←3.5")
    3.5
    >>> test(r"M27←4.5")
    4.5
    >>> test(r"27M←5.5")
    INVALID TOKEN

    >>> test(r"B")
    2.5
    >>> test(r"B-1")
    1.5
    >>> test(r"1-B")
    ¯1.5
    >>> test(r"÷B")
    0.4

    >>> test(r"name←'Heather'")
    Heather
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

    >>> IO = saveIndexOrigin()
    >>> setIndexOrigin(1)

    >>> test(r"A ← 10")
    10
    >>> test(r"1 A 3")
    1 10 3
    >>> test(r"1 (A÷2) 3")
    1 5 3
    >>> test(r"1 ⎕IO 3")
    1 1 3

    >>> restoreIndexOrigin(IO)

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

def     arkMatrices():
    """
    >>> test(r"⍳ 4")
    1 2 3 4
    >>> test(r"2 2 ⍴ ⍳ 4")
    1 2
    3 4
    >>> test(r", 2 2 ⍴ ⍳ 4")
    1 2 3 4

    >>> test(r"⍴ ⍳ 4")
    4
    >>> test(r"⍴ 2 2 ⍴ ⍳ 4")
    2 2
    >>> test(r"⍴ , 2 2 ⍴ ⍳ 4")
    4

    >>> test(r"A ← 2 2 ⍴ ⍳ 4")
    1 2
    3 4
    >>> test(r"A")
    1 2
    3 4
    >>> test(r"+ A")
    1 2
    3 4

    >>> test(r"A + A")
    2 4
    6 8
    >>> test(r"A + 0 1")
    1 3
    3 5
    >>> test(r"(1 0) + A")
    2 2
    4 4
    >>> test(r"A + 3")
    4 5
    6 7
    >>> test(r"2 + A")
    3 4
    5 6
    """
    pass

# ------------------------------

def     parseMixed():
    """
    >>> test(r"N ← 1 2 3 'a' 'b' 'c'")
    1 2 3 abc
    >>> test(r"≢ N")
    6
    >>> test(r"≡ N")
    1
    >>> test(r"N ≡ 1 2 3, 'abc'")
    1
    >>> test(r"1 ↑ 0 ⍴ N")
    0

    >>> test(r"N ← 'c' 'b' 'a' 3 2 1")
    cba 3 2 1
    >>> test(r"≢ N")
    6
    >>> test(r"≡ N")
    1
    >>> test(r"N ≡ 'cba', 3 2 1")
    1
    >>> test(r"'«', (1 ↑ 0 ⍴ N), '»'")
    « »
    """
    pass

# ------------------------------

def     parseNested():
    """
    >>> test(r"N ← 1 2 3 'abc' 4 5 6")
    1 2 3 'abc' 4 5 6
    >>> test(r"≢ N")
    7
    >>> test(r"≡ N")
    2

    >>> test(r"N ← 1 2 3 ('abc') 4 5 6")
    1 2 3 'abc' 4 5 6
    >>> test(r"≢ N")
    7
    >>> test(r"≡ N")
    2

    >>> test(r"N ← 1 2 3, 'abc', 4 5 6")
    1 2 3 abc 4 5 6
    >>> test(r"≢ N")
    9
    >>> test(r"≡ N")
    1

    >>> test(r'N ← 1 2 3 "a" "b" "c" 4 5 6')
    1 2 3 'a' 'b' 'c' 4 5 6
    >>> test(r"≢ N")
    9
    >>> test(r"≡ N")
    2

    >>> test(r'N ← 1 2 3 ("a" "b" "c") 4 5 6')
    1 2 3 ('a' 'b' 'c') 4 5 6
    >>> test(r"≢ N")
    7
    >>> test(r"≡ N")
    3

    >>> test(r"N ← 1 2 3 'a' 'b' 'c' 4 5 6")
    1 2 3 abc 4 5 6
    >>> test(r"≢ N")
    9
    >>> test(r"≡ N")
    1

    >>> test(r"N ← 1 2 3 ('a' 'b' 'c') 4 5 6")
    1 2 3 'abc' 4 5 6
    >>> test(r"≢ N")
    7
    >>> test(r"≡ N")
    2

    >>> test(r"N ← 'H' 'ello'")
    H 'ello'
    >>> test(r"≢ N")
    2
    >>> test(r"≡ N")
    2

    >>> test(r'N ← "H" "ello"')
    'H' 'ello'
    >>> test(r"≢ N")
    2
    >>> test(r"≡ N")
    2

    >>> test(r"N ← 'Hell' 'o'")
    'Hell' o
    >>> test(r"≢ N")
    2
    >>> test(r"≡ N")
    2

    >>> test(r'N ← "Hell" "o"')
    'Hell' 'o'
    >>> test(r"≢ N")
    2
    >>> test(r"≡ N")
    2
    """
    pass

# ------------------------------

def     parsePrototypes():
    """
    >>> test(r"'«', (1 ⍴ ⍬), '»'")
    « 0 »
    >>> test(r"'«', (1 ⍴ ''), '»'")
    « »

    >>> test(r"'«', (1 ↑ 0 ⍴ 1 2 3), '»'")
    « 0 »
    >>> test(r"'«', (1 ↑ 0 ⍴ 'Hello'), '»'")
    « »

    >>> test(r"'«', (1 ↑ 0 ⍴ 1 'a'), '»'")
    « 0 »
    >>> test(r"'«', (1 ↑ 0 ⍴ 'a' 1), '»'")
    « »

    >>> test(r"(0 ⍴ (1 2) (3 4))")
    (⍬ ⍬)
    >>> test(r"(0 ⍴ (1 2) '??')")
    (⍬ ⍬)
    >>> test(r"(0 ⍴ '!!' (3 4))")
    ('' '')

    >>> test(r"'«', (1 ↑ 0 ⍴ (1 2) (3 4)), '»'")
    « (0 0) »
    >>> test(r"'«', (1 ↑ 0 ⍴ (1 2) '??'), '»'")
    « (0 0) »
    >>> test(r"'«', (1 ↑ 0 ⍴ '!!' (3 4)), '»'")
    « '  ' »
    """
    pass

# ------------------------------

def     parseOutput():
    """
    >>> testOutput(r"'Hello' ⍝ end of line comments are ignored")
    Hello

    >>> testOutput(r"'Hello ⍝ in a string is not a comment' ⍝ end of line comments are ignored")
    Hello ⍝ in a string is not a comment

    >>> testOutput(r"'Hello' ⋄ 'Paul'")
    Hello
    Paul
    >>> testOutput(r"'Hello ⋄ Paul'")
    Hello ⋄ Paul

    >>> testOutput(r"1 + 2 ⋄ 3 + 4 ⋄ 5 + 6")
    3
    7
    11
    >>> testOutput(r"1 + 2 ⋄ 3 + 4 ⋄")
    3
    7
    >>> testOutput(r"⋄ 3 + 4")
    7

    >>> testOutput(r"⎕ ← 1 + 2")
    3
    >>> testOutput(r"⍞ ← 1 + 2")
    3

    >>> testOutput(r"6 + ⎕ ← 1 + 2")
    3
    9
    >>> testOutput(r"6 + ⍞ ← 1 + 2")
    39

    >>> testOutput(r"⎕ ← 'Hello' ⋄ 'Paul'")
    Hello
    Paul
    >>> testOutput(r"⍞ ← 'Hello ' ⋄ 'Paul'")
    Hello Paul

    >>> testOutput(r"1 + 2 ⋄ ⎕ ← 3 + 4 ⋄ 5 + 6")
    3
    7
    11
    >>> testOutput(r"1 + 2 ⋄ ⍞ ← 3 + 4 ⋄ 5 + 6")
    3
    711

    >>> testOutput(r"1 2 3")
    1 2 3
    >>> testOutput(r"1 ⎕ ← 2 3")
    2 3
    1 (2 3)
    >>> testOutput(r"'Hello' 2 3")
    'Hello' 2 3
    >>> testOutput(r"'Hello' ⎕ ← 2 3")
    2 3
    'Hello' (2 3)

    >>> testOutput(r"1 ⍞ ← 2 3")
    (2 3)1 (2 3)
    """
    pass

# ------------------------------

def     systemVariable():
    """
    >>> test(r"⎕dummy")
    UNKNOWN SYSTEM VARIABLE

    >>> IO = saveIndexOrigin()
    >>> setIndexOrigin(1)

    >>> test(r"⎕IO")
    1
    >>> test(r"⎕Io←0")
    0
    >>> test(r"⎕io")
    0
    >>> test(r"⎕iO←0")
    0
    >>> test(r"⎕IO←2")
    DOMAIN ERROR
    >>> test(r"⎕io")
    0
    >>> test(r"⎕IO←1")
    1
    >>> test(r"⎕io")
    1

    >>> restoreIndexOrigin(IO)

    >>> test(r"⊣ EE←⎕EE")
    0
    >>> test(r"⎕EE←0")
    0
    >>> test(r"⎕EE")
    0
    >>> test(r"⎕EE←1")
    1
    >>> test(r"⎕EE←2")
    DOMAIN ERROR
    >>> test(r"⎕EE")
    1
    >>> test(r"⊣ ⎕EE←EE")
    0

    >>> test(r"⎕CT")
    1e¯13
    """
    pass

# ------------------------------

def     systemCommand():
    """
    >>> testCommand(")dummy")
    UNKNOWN SYSTEM COMMAND
    """
    pass

# ------------------------------

if __name__ == "__main__":
    preamble()
    if test and testOutput and testCommand:
        import doctest
        doctest.testmod()
    else:
        IO = saveIndexOrigin()
        setIndexOrigin(0)
        restoreIndexOrigin(IO)

# EOF
