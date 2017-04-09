#!/usr/bin/python3
"""
    A simple wrapper script for the APL Read-Evaluate-Print loop

    This version adds simple APL exception handling
"""

import sys

from functools import reduce

from rep import read_evaluate_print, apl_quit, evaluate, print_result

from apl_exception import APL_Exception as apl_exception

# ------------------------------

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("APL Shell")

        try:
            read_evaluate_print('       ')
        except KeyboardInterrupt:
            apl_quit()
    else:
        # evaluate parameters as an APL expresson

        line = reduce(lambda x, y: x + ' ' + y, sys.argv[1:]).strip()

        try:
            print_result(evaluate(line))
        except apl_exception as e:
            print(line)
            print(' '*(len(line)-len(e.line)),end="^\n")
            print(e.message)

# EOF
