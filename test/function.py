#!/usr/bin/python3
"""
    template for test cases for one APL function pulled from other test modules

    Tests both the monadic and dyadic forms of the function.  For example:

        test/function iota

    The preamble allows the tests to be run with either eager or lazy evaluation.
"""

from test.base import preamble, testResult as test
from test.base import saveIndexOrigin, setIndexOrigin, restoreIndexOrigin

import testMonadic    as monadic
import testDyadic     as dyadic
import testString     as string
import testZilde      as zilde
import testMixed      as mixed
import testNested     as nested
import testPrototypes as prototypes

# ------------------------------

if __name__ == "__main__":
    preamble()

    __test__ = {}
    __test__["monadic"]     = monadic.function
    __test__["dyadic"]      = dyadic.function
    __test__["string"]      = string.function
    __test__["zilde"]       = zilde.function
    __test__["mixed"]       = mixed.function
    __test__["nested"]      = nested.function
    __test__["prototypes"]  = prototypes.function

    import doctest
    doctest.testmod()

# EOF
