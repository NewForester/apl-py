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

def     print_error (error,expr,prompt="",where=""):
    """
    print the error response when APL expression evaluation fails
    """
    print(' '*(len(prompt)+len(expr)-len(error.expr.lstrip())),end="^\n")
    print(error.message,where)

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

def     rep_from_file (prompt,path,inputFile,silent):
    """
    read input, evaluate it and print the result
    """
    if silent:
        prefix = ""
    else:
        prefix = "⎕"

    lineCount = 0
    for line in inputFile:
        lineCount += 1

        if lineCount == 1:
            if line.startswith("#!"):
                continue

        if not silent:
            print("{0}{1}".format(prompt,line),end="")

        expr = _strip_comment(line)
        if expr:
            try:
                print_result(evaluate(expr),prefix)
            except apl_exception as error:
                if silent:
                    print("{0}{1}".format(prompt,line),end="")
                print_error(error,expr,prompt,"in {0} on line {1}".format(path,lineCount))
                apl_exit(1)

# ------------------------------

def     rep_from_tty (prompt):
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
    try:
        if len(sys.argv) == 1:
            flags, args = [], []
        elif '--' in sys.argv:
            ii = sys.argv.index("--")
            flags, args = sys.argv[1:ii], sys.argv[ii + 1:]
        elif sys.argv[1][0] == '-':
            flags, args = sys.argv[1:], []
        else:
            flags, args = [], sys.argv[1:]

        if len(flags):
            flags = ' '.join(flags).replace(' -',':-').split(':')

        silent = False

        for flag in flags:
            if flag in ("-h", "--help"):
                print("{0} coming soon".format(flag))

            elif flag in ("-s", "--silent", "--script"):
                silent = True

            elif flag in ("-v", "--verbose"):
                silent = False

            elif flag.startswith(("-f ", "--file ")):
                path = flag.split()[1];
                inputFile = open(path, "r")
                rep_from_file('       ',path,inputFile,silent)
                inputFile.close()

            else:
                print("{0} not recognised: perhaps try --help".format(flag))

        if sys.stdin.isatty():
            # enter interactive shell iff there are is no command line expression

            if not len(args):
                print("APL Shell implemented in Python 3, Copyright 2017 NewForester")

                try:
                    rep_from_tty('       ')
                except EOFError:
                    apl_exit(0,"")
        else:
            # stdin redirected

            rep_from_file('       ',"<stdin>",sys.stdin,silent)

        if len(args):
            # evaluate command line expression

            line = ' '.join(args)

            expr = _strip_comment(line)
            if expr:
                try:
                    print_result(evaluate(expr))
                    apl_exit(0)
                except apl_exception as error:
                    print(line)
                    print_error(error,expr)
                    apl_exit(1)

    except KeyboardInterrupt:
        apl_quit(2,"^C")

# EOF
