#!/usr/bin/python3
"""
    a simple implementation of APL in Python 3

    UNDER DEVELOPMENT

    This Python module is the executable command-line intepreter.

    For more information try:

                    apl.py --help
"""

import sys

from functools import reduce

from evaluate import evaluate_and_print

from apl_cio import APL_cio as apl_cio
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

It is possible to log the entire interactive session to file:

    $ apl.py -l log_file

has the same effect as:

    $ apl.py |& tee -i log_file

except the second disables readline editing.

Non-interactive (or scripted) use is supported:

    $ apl.py < script_file
    $ cat script_file | apl-py
    $ apl.py -f script_file

will all interpret script_file as a sequence of APL expressions.  Interactive
output may be suppressed using the --silent flag.  In response to an error,
the interpreter will print the offending line (and line number) and then exit.

To be able to run a script directly from a Linux command line, the file must
be executable and its first line should read something like:

    # !/usr/bin/apl.py --silent -f

Use the path appropriate for your installation.  The -f flag must appear to the
right of any other flags.

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

    -s --silent         suppress interactive output
    -v --verbose        resume interactive output

    --                  ends of flags

Note that at present in the interactive interpreter:

    ^D  (end of input)  is equivalent to )OFF
    ^C  (interrupt)     will abort execution and quit the interpreter

This program is still under active development:  any and all features are
'as is' and subject to change.

Your curiosity is much appreciated. Thank you.
"""

# ------------------------------

def     read_evaluate_print (cio):
    """
    read lines from a tty or a file, evaluate them and print the results
    """
    while True:
        cio.reset()

        try:
            line = cio.read(cio.scriptFile)
        except EOFError:
            return

        try:
            evaluate_and_print(line,cio)
        except apl_exception as error:
            cio.printError(cio.scriptFile,error,line)
            if cio.scriptFile is not None:
                apl_exit(1)

# ------------------------------

if __name__ == '__main__':
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

    try:
        with apl_cio(6 * ' ',"□") as cio:

            for flag in flags:
                if flag in ("-h", "--help"):
                    print(_banner)
                    apl_quit(0,_helpText)

                elif flag in ("-V", "--Version"):
                    print(_banner)
                    print(_version)
                    print(_milestone)
                    apl_quit(0)

            for flag in flags:
                if flag in ("-s", "--silent"):
                    cio.silent = True

                elif flag in ("-v", "--verbose"):
                    cio.silent = False

                elif flag.startswith(("-l ", "--log ")):
                    cio.logFile.setPath(flag.split()[1])

                elif flag.startswith(("-o ", "--output ")):
                    cio.outFile.setPath(flag.split()[1])

                elif flag.startswith(("-i ", "--input ")):
                    cio.inFile.setPath(flag.split()[1])

                elif flag.startswith(("-f ", "--file ")):
                    cio.scriptFile.setPath(flag.split()[1])
                    read_evaluate_print(cio)

                else:
                    apl_quit(3,"{0} not recognised: perhaps try --help".format(flag))

            if not sys.stdin.isatty():
                # stdin redirected

                read_evaluate_print(cio)

            elif not len(args):
                # enter interactive shell as there are is no command line expression

                cio.printThis(_banner)
                read_evaluate_print(cio)
                cio.printThis("^D")
                apl_exit(0)

            if len(args):
                # evaluate command line expression

                cio.prompt=""
                cio.prefix=""
                cio.silent=False
                cio.reset()
                line = ' '.join(args)

                try:
                    evaluate_and_print(line,cio)
                    apl_exit(0)
                except apl_exception as error:
                    cio.printThis(line)
                    cio.printError(None,error,line)
                    apl_exit(1)

    except KeyboardInterrupt:
        apl_quit(2,"^C")

# EOF
