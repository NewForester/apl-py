"""
    an APL Interpreter implemented in Python 3

    The interpreter comprises the following modules:

    - apl.py                    the command line interpreter - run this to run the interpreter

    - aplCio.py                 the console I/O module - not my finest hour

    - aplError.py               routines that raise DOMAIN ERROR and so forth

    - aplQuantity.py            an abstraction to model APL scalars, vectors and arrays

    - dyadicFunctions.py        scalar implementations of APL's dyadic mathematical functions

    - dyadicIterators.py        'lazy evaluation' implementations of dyadic functions

    - dyadicLookup.py           convert an APL symbol into a callable dyadic function

    - dyadicMaps.py             vector implementations of APL's dyadic functions

    - evaluate.py               the evaluate part of the interpreter's read-evaluate-print loop

    - monadicFunctions.py       scalar implementations of APL's monadic mathematical functions

    - monadicIterators.py       'lazy evaluation' implementations of monadic functions

    - monadicLookup.py          convert an APL symbol into a callable monadic function

    - monadicMaps.py            vector implementations of APL's monadic functions

    - systemCommands.py         implementations of a subset of APL system commands such as )OFF

    - systemVariables.py        implementations of a subset of APL system variables such as ⌷IO

    - workspaceVariables.py     support for APL workspace variables
"""
