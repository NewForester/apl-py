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

from apl_exception import APL_Exception as apl_exception, apl_quit, apl_exit

# ------------------------------

def     format_scalar (scalar):
    """
    format a scalar number for printing
    """
    try:
        return '{0:.10g}'.format(scalar).replace('-','¯')
    except Exception as e:
        print (scalar)
        raise(e)

# ------------------------------

def     format_result (result):
    """
    print the result of evaluating an APL expression
    """
    if type(result) == type(()):
        return '(' + ' '.join(map(format_result, result)) + ')'
    elif result is not None:
        return format_scalar(result)

# ------------------------------

def     print_result (result,prefix=""):
    """
    print the result of evaluating an APL expression
    """
    if prefix:
        print(prefix,end=' ')

    if type(result) == type(()):
        print (' '.join(map(format_result, result)))
    elif result is not None:
        print (format_scalar(result))

# ------------------------------

def     print_error (e,line,prompt=""):
    """
    print the error response when APL expression evaluation fails
    """
    print(' '*(len(prompt)+len(line)-len(e.line.lstrip())),end="^\n")
    print(e.message)

# ------------------------------

def     strip_comment (line):
    pos = line.find('⍝')

    if pos != -1:
        line = line[:pos]

    return line.rstrip()

# ------------------------------

def     read_evaluate_print (prompt):
    """
    Read input, evaluate it and output the result
    """
    while True:
        line = strip_comment(input(prompt))

        if line:
            try:
                print_result(evaluate(line),"⎕")
            except apl_exception as e:
                print_error (e,line,prompt)

# ------------------------------

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("APL Shell implemented in Python 3, Copyright 2017 NewForester")

        try:
            read_evaluate_print('       ')
        except EOFError:
            apl_exit(0,"")
        except KeyboardInterrupt:
            apl_quit(2)
    else:
        # evaluate parameters as an APL expresson

        line = strip_comment(' '.join(sys.argv[1:]))

        if line:
            try:
                print_result(evaluate(line))
                apl_exit(0)
            except apl_exception as e:
                print(line)
                print_error(e,line)
                apl_exit(1)

# EOF
