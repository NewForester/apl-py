#!/usr/bin/python3
"""
    template for test cases for one APL function pulled from other test modules

    Tests both the monadic and dyadic forms of the function.  For example:

        test/function iota

    The preamble allows the tests to be run with either eager or lazy evaluation.
"""

from test.base import preamble, testResult as test
from test.base import saveIndexOrigin, setIndexOrigin, restoreIndexOrigin

import monadic
import dyadic
import strings
import zilde
import mixed
import nested
import prototypes

# ------------------------------

if __name__ == "__main__":
    preamble()

    __test__ = {}
    __test__["monadic"]     = monadic.function          # pylint: disable=no-member, bad-whitespace
    __test__["dyadic"]      = dyadic.function           # pylint: disable=no-member, bad-whitespace
    __test__["strings"]     = strings.function          # pylint: disable=no-member, bad-whitespace
    __test__["zilde"]       = zilde.function            # pylint: disable=no-member, bad-whitespace
    __test__["mixed"]       = mixed.function            # pylint: disable=no-member, bad-whitespace
    __test__["nested"]      = nested.function           # pylint: disable=no-member, bad-whitespace
    __test__["prototypes"]  = prototypes.function       # pylint: disable=no-member, bad-whitespace

    if test and __name__:
        import doctest
        doctest.testmod()
    else:
        IO = saveIndexOrigin()
        setIndexOrigin(0)
        restoreIndexOrigin(IO)

# EOF
