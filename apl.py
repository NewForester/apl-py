#!/usr/bin/python3
"""
    A simple wrapper script for the APL Read-Evaluate-Print loop

    Supports 'shell' and 'calculator' modes
"""

import sys

from functools import reduce

from rep import read_evaluate_print, apl_quit, evaluate

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

        print(evaluate(reduce(lambda x, y: x + ' ' + y, sys.argv[1:])))

# EOF
