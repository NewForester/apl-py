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
import readline

from evaluate import evaluate

from apl_quantity import APL_scalar as apl_scalar, APL_vector as apl_vector
from apl_error import APL_exception as apl_exception, apl_exit, apl_quit

# ------------------------------

def     print_result (result,prefix=""):
    """
    print the result when APL expression evaluation succeeds
    """
    print("{0}{1}".format(prefix,result).replace('-','¯'))

# ------------------------------

def     print_error (error,expr,prompt=""):
    """
    print the error response when APL expression evaluation fails
    """
    print(' '*(len(prompt)+len(expr)-len(error.expr.lstrip())),end="^\n")
    print(error.message)

# ------------------------------

def     _strip_comment (line):
    """
    strip end-of-line comment
    """
    pos = line.find('⍝')

    if pos != -1:
        line = line[:pos]

    return line.rstrip()

# ------------------------------

def     read_evaluate_print (prompt):
    """
    read input, evaluate it and print the result
    """
    while True:
        line = input(prompt)

        expr = _strip_comment(line)
        if expr:
            try:
                print_result(evaluate(expr),"⎕")
            except apl_exception as e:
                print_error (e,expr,prompt)

# ------------------------------

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("APL Shell implemented in Python 3, Copyright 2017 NewForester")

        try:
            read_evaluate_print('       ')
        except EOFError:
            apl_exit(0,"")
        except KeyboardInterrupt:
            apl_quit(2,"^C")
    else:
        # evaluate parameters as an APL expresson

        line = ' '.join(sys.argv[1:])

        expr = _strip_comment(line)
        if expr:
            try:
                print_result(evaluate(expr))
                apl_exit(0)
            except apl_exception as error:
                print(line)
                print_error(error,expr)
                apl_exit(1)

# EOF
