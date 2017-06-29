#!/usr/bin/python3
"""
    a simple implementation of APL in Python 3

    UNDER DEVELOPMENT

    This Python module is the command-line executable.

    With no flags/arguments, the module enters a read-evaluate-print loop.
    Each line of input read from the terminal is interpreted as an APL
    expression.  The expression is evaluated and the result printed to the
    terminal.

    With flags, the interpreter may be directed to read input from a file
    (scripting) before or instead of entering the read-evaluate-print loop.

    The interpreter will treat arguments as a single APL expression.  It will
    evaluate the expression, print the result and then exit without entering
    the read-evaluate-print loop.

    When flags and arguments are both used, -- (the end-of-flags flag) must
    also be used.  Flags and arguments must appear on the command line to the
    left and of the end-of-flags flag.

    For more information try:

                    apl.py --help
"""

import sys
import readline

from functools import reduce

from evaluate import evaluate_and_print_line

from apl_quantity import APL_scalar as apl_scalar, APL_vector as apl_vector
from apl_print import APL_print as apl_print, print_error
from apl_error import APL_exception as apl_exception, apl_error, apl_exit, apl_quit

# ------------------------------

_banner = "APL Shell implemented in Python 3, Copyright 2017 NewForester"
_version = "Version 0.1.++, developed on Python 3.2.3"
_milestone = "Scalar calculator complete, vector calculator in progress"

_helpText = """
Invocation without any flags or arguments will enter an interactive APL shell.
Use an APL command such as )OFF to exit.

Invocation without flags but with arguments will intepret the arguments as
an APL expression, print the result and exit.  Eg:

    $ apl.py 4 8 16 ÷ 2
    2 4 8

Non-interactive (or scripted) use is supported:

    $ apl.py < script_file
    $ cat script_file | apl-py
    $ apl.py -f script_file

will all interpret script_file as a sequence of APL expressions.  Interactive
output may be suppressed using the --script flag.  In response to an error,
the interpreter will print the offending line (and line number) and then exit.

To be able to run a script directly from a Linux command line, the file must
be executable and its first line should read something like:

    # !/usr/bin/apl.py --script -f

Use the path appropriate for your installation.  The -f flag must appear to the
right of any other flags.

There is no flag to redirect output to a file.  Should you need this it is
suggested you try:

    $ apl.py -f script_file |& tee -i log_file

This will record output to both stdout and stderr in log_file and print it to
the terminal.  It is also record the Python stack in the event of a crash.

There is no mechanism for script files to include other script files but they
may be chained together:

   $ apl.py -f file_1 -f file_2 ...

A standalone script file is expected to use )OFF or equivalent to terminate.
Otherwise script files are assumed to be rc files that set up a particular
environment (such as loading a workspace).

If the interpreter is still running after executing the last line of the final
script file, then it will consider entering the interactive shell or
interpreting command line arguments.

When working with scripts (and flags in general), -- indicates 'end of flags':
any command line arguments further to the right may be interpreted as an APL
expression:

    $ apl.py -f load_application_workspace -- invoke_application

If there are no such command line arguments and standard input has not been
redirected away from the terminal then the interpreter will enter the
interactive shell.

Summary of the command line flags recognised by the interpreter:
    -f --file           interpret contents of file as APL expressions

    -h --help           print this help text and exit
    -V --Version        print version information and exit

    --script            suppress interactive output
    -s --silent         as for --script
    -v --verbose        resume interactive output

    --                  ends of flags

Note that at present in the interactive interpreter:

    ^D  (end of input)  is equivalent to )OFF
    ^C  (interrupt)     will abort execution and quit the interpreter

This program is still under active development:  any and all features
are 'as is' and subject to change.

Your curiosity is much appreciated. Thank you.
"""

# ------------------------------

def     rep_from_file (prompt,path,inputFile,silent):
    """
    read input lines from a file, evaluate them and print the results
    """
    lineCount = 0
    for line in inputFile:
        lineCount += 1

        if lineCount == 1:
            if line.startswith("#!"):
                continue

        line = line.rstrip()

        if not silent:
            print("{0}{1}".format(prompt,line))

        if not line.lstrip():
            continue

        try:
            if not silent:
                print("□",end="")
            evaluate_and_print_line(line,apl_print(),silent)
        except apl_exception as error:
            if silent:
                print("{0}{1}".format(prompt,line))
            print_error(error,line,prompt,"in {0} on line {1}".format(path,lineCount))
            apl_exit(1)

# ------------------------------

def     rep_from_tty (prompt):
    """
    read input lines from a tty, evaluate them and print the results
    """
    while True:
        line = input(prompt)

        if not line.lstrip():
            continue

        try:
            print("□",end="")
            evaluate_and_print_line(line,apl_print())
        except apl_exception as error:
            print_error(error,line,prompt)

# ------------------------------

if __name__ == '__main__':
    prompt = 6 * ' '

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
                print(_banner)
                apl_quit(0,_helpText)

            elif flag in ("-V", "--Version"):
                print(_banner)
                print(_version)
                print(_milestone)
                apl_quit(0)

            elif flag in ("-s", "--silent", "--script"):
                silent = True

            elif flag in ("-v", "--verbose"):
                silent = False

            elif flag.startswith(("-f ", "--file ")):
                path = flag.split()[1];
                try:
                    inputFile = open(path, "r")
                except:
                    apl_quit(3,"unable to open '{0}' for input".format(path))

                rep_from_file(prompt,path,inputFile,silent)
                inputFile.close()

            else:
                apl_quit(3,"{0} not recognised: perhaps try --help".format(flag))

        if sys.stdin.isatty():
            # enter interactive shell iff there are is no command line expression

            if not len(args):
                print(_banner)

                try:
                    rep_from_tty(prompt)
                except EOFError:
                    apl_exit(0,"^D")
        else:
            # stdin redirected

            rep_from_file(prompt,"<stdin>",sys.stdin,silent)

        if len(args):
            # evaluate command line expression

            line = ' '.join(args)

            try:
                evaluate_and_print_line(line,apl_print())
                apl_exit(0)
            except apl_exception as error:
                print(line)
                print_error(error,line)
                apl_exit(1)

    except KeyboardInterrupt:
        apl_quit(2,"^C")

# EOF
