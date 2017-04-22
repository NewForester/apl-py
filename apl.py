#!/usr/bin/python3
"""
    a simple implementation of APL in Python 3

    UNDER DEVELOPMENT

    This module is the command-line script.

    The script, with arguments, evaluates them as an APL expression.

    The script, without arguments, enters a read-evaluate-print shell:
        * the read part is the Python input() function
        * the evaluate part is in evaluate.py
        * the print part is in this module.
"""

import sys

from evaluate import evaluate

from apl_exception import APL_Exception as apl_exception, apl_quit, apl_exit

# ------------------------------

def     print_result (result,prefix=""):
    """
    print the result of evaluating an APL expression
    """
    if result is not None:
        if prefix:
            print (prefix,end=" ")

        print('{0:g}'.format(result).replace('-','¯'))

# ------------------------------

def     print_error (e,line,prompt=""):
    """
    print the error response when APL expression evaluation fails
    """
    print(' '*(len(prompt)+len(line)-len(e.line.lstrip())),end="^\n")
    print(e.message)

# ------------------------------

def     read_evaluate_print (prompt):
    """
    Read input, evaluate it and output the result
    """
    try:
        while True:
            result = None

            print(end=prompt)
            line = input()

            if line.strip():
                try:
                    print_result(evaluate(line),"⎕")
                except apl_exception as e:
                    print_error (e,line,prompt)

    except EOFError:
        apl_exit(0,"")

# ------------------------------

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("APL Shell implemented in Python 3, Copyright 2017 NewForester")

        try:
            read_evaluate_print('       ')
        except KeyboardInterrupt:
            apl_quit(2)
    else:
        # evaluate parameters as an APL expresson

        line = ' '.join(sys.argv[1:])
        try:
            print_result(evaluate(line))
            apl_exit(0)
        except apl_exception as e:
            print(line)
            print_error(e,line)
            apl_exit(1)

# EOF
